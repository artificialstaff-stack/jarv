import streamlit as st
import brain  # logic/brain.py dosyasını kullanır
import time
import pandas as pd 
from datetime import datetime

# ==============================================================================
# 🎨 DASHBOARD STİLİ
# ==============================================================================
def inject_dashboard_css():
    st.markdown("""
    <style>
        .dash-header-container {
            padding: 20px 25px;
            background: linear-gradient(90deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            margin-bottom: 25px;
            backdrop-filter: blur(10px);
        }
        .metric-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 20px;
            transition: transform 0.2s;
        }
        .metric-card:hover { transform: translateY(-3px); border-color: rgba(255,255,255,0.1); }
        
        [data-testid="stDataFrame"] { background: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🚀 ANA DASHBOARD FONKSİYONU
# ==============================================================================
def render_dashboard():
    inject_dashboard_css()
    
    # KULLANICI BİLGİSİ
    user = st.session_state.get('user_data', {'brand': 'Demo Brand', 'name': 'User'})
    brand = user.get('brand', 'Anatolia Home')

    # HEADER
    st.markdown(f"""
    <div class="dash-header-container">
        <h1 style="margin:0; font-size: 2.5rem; color:white;">{brand}</h1>
        <div style="color: #34D399; font-size: 0.8rem; margin-top: 5px;">● SYSTEM ONLINE | Istanbul HQ</div>
    </div>
    """, unsafe_allow_html=True)
    
    # MOD YÖNETİMİ (Varsayılan Finans)
    if "dashboard_mode" not in st.session_state: st.session_state.dashboard_mode = "finance"
    
    # İKİ KOLONLU YAPI
    col_chat, col_viz = st.columns([1.2, 2], gap="medium")

    # --- SOL: AI ASİSTAN ---
    with col_chat:
        st.markdown("##### 🧠 Operasyon Asistanı")
        chat_cont = st.container(height=480)
        
        if "messages" not in st.session_state: st.session_state.messages = []
        
        with chat_cont:
            if not st.session_state.messages:
                st.info("👋 Merhaba! 'Finans raporu', 'Stok durumu' veya 'Lojistik haritası' diyerek sağ tarafı değiştirebilirsin.")
            
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        # CHAT INPUT
        if prompt := st.chat_input("Talimat verin..."):
            # 1. Kullanıcı mesajını ekle
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # 2. NİYET ANALİZİ VE EKRAN DEĞİŞTİRME (AKILLI ANAHTARLAMA)
            p_low = prompt.lower()
            
            # Kelimeye göre sağ ekranı değiştir
            if any(x in p_low for x in ["lojistik", "kargo", "harita", "yol", "sevkiyat"]):
                st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "depo", "ürün", "envanter", "sayım"]):
                st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "satış", "para", "gelir", "gider"]):
                st.session_state.dashboard_mode = "finance"
            elif any(x in p_low for x in ["belge", "doküman", "dosya", "pdf"]):
                st.session_state.dashboard_mode = "documents"
            elif any(x in p_low for x in ["form", "başvuru", "talep"]):
                st.session_state.dashboard_mode = "forms"
            elif any(x in p_low for x in ["yapılacak", "görev", "todo", "işler"]):
                st.session_state.dashboard_mode = "todo"
            elif any(x in p_low for x in ["plan", "proje", "hedef", "strateji"]):
                st.session_state.dashboard_mode = "plans"
            
            # 3. Sayfayı yenile ki sağ taraf güncellensin
            st.rerun()

    # ASİSTAN CEVABI (Sayfa yenilendikten sonra çalışır)
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with chat_cont:
            with st.chat_message("assistant"):
                ph = st.empty()
                full_resp = ""
                # Brain'den stream cevap al
                for chunk in brain.get_streaming_response(st.session_state.messages, user):
                    full_resp += chunk
                    ph.markdown(full_resp + "▌")
                    time.sleep(0.01)
                ph.markdown(full_resp)
        st.session_state.messages.append({"role": "assistant", "content": full_resp})

    # --- SAĞ: DİNAMİK GÖRSELLER (AI NEYİ AÇARSA O GELİR) ---
    with col_viz:
        mode = st.session_state.dashboard_mode
        
        def metric_card(lbl, val, delta, col="#34D399"):
            st.markdown(f"""<div class='metric-card'><div style='color:#AAA; font-size:12px'>{lbl}</div><div style='font-size:24px; font-weight:bold'>{val}</div><div style='color:{col}; font-size:12px'>{delta}</div></div>""", unsafe_allow_html=True)

        # 1. FİNANS EKRANI
        if mode == "finance":
            st.markdown("##### 📈 Finansal Performans")
            c1, c2 = st.columns(2)
            with c1: metric_card("Aylık Ciro", "$42,500", "+%12.5")
            with c2: metric_card("Net Kâr", "%32", "+%4.2")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            
        # 2. LOJİSTİK EKRANI
        elif mode == "logistics":
            st.markdown("##### 🌍 Lojistik Ağı")
            c1, c2 = st.columns(2)
            with c1: metric_card("Aktif Kargo", "TR-8821", "Yolda", "#3B82F6")
            with c2: metric_card("Varış", "2 Gün", "Zamanında")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            
        # 3. ENVANTER EKRANI
        elif mode == "inventory":
            st.markdown("##### 📦 Depo Durumu")
            c1, c2 = st.columns(2)
            with c1: metric_card("Toplam Ürün", "8,500", "Adet")
            with c2: metric_card("Riskli Stok", "Çanta", "Kritik", "#F87171")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)

        # 4. DOKÜMANLAR
        elif mode == "documents":
            st.markdown("##### 📂 Dijital Arşiv")
            c1, c2 = st.columns(2)
            with c1: metric_card("Toplam Dosya", "1,240", "+5 Yeni", "#3B82F6")
            with c2: metric_card("Son Yükleme", "Bugün", "İrsaliye", "#A1A1AA")
            st.markdown("<br>", unsafe_allow_html=True)
            st.info("💡 Tam liste için 'Operasyon Merkezi'ne gidin.")

        # 5. GÖREVLER
        elif mode == "todo":
            st.markdown("##### ✅ Hızlı Görevler")
            st.checkbox("Gümrük müşaviri ile görüş", value=True)
            st.checkbox("Ocak ayı finans raporunu onayla", value=False)
            metric_card("Tamamlanan", "%25", "Devam Ediyor", "#8B5CF6")

        # 6. FORMLAR
        elif mode == "forms":
            st.markdown("##### 📝 Onay Bekleyenler")
            with st.expander("📌 Personel İzin Formu - Ahmet Y.", expanded=True):
                st.write("**Tarih:** 15-20 Ocak")
                st.button("Onayla", key="f1_dash")

        # 7. PLANLAR
        elif mode == "plans":
            st.markdown("##### 💎 Stratejik Hedefler")
            st.success("🎯 **Q1 Hedefi:** Lojistik maliyetlerini %10 düşür.")
            metric_card("Hedef Tamamlanma", "%70", "İyi Gidiyor", "#3B82F6")
