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
    
    # MOD YÖNETİMİ
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
                st.info("👋 Merhaba! Finans, stok veya lojistik durumunu sorabilirsin.")
            
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        if prompt := st.chat_input("Talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # ZEKİ MOD DEĞİŞTİRİCİ
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo"]): st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "depo", "ürün"]): st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "satış"]): st.session_state.dashboard_mode = "finance"
            elif any(x in p_low for x in ["belge", "doküman"]): st.session_state.dashboard_mode = "documents"
            elif any(x in p_low for x in ["görev", "todo"]): st.session_state.dashboard_mode = "todo"
            elif any(x in p_low for x in ["form", "talep"]): st.session_state.dashboard_mode = "forms"
            elif any(x in p_low for x in ["plan", "hedef"]): st.session_state.dashboard_mode = "plans"
            
            st.rerun()

    # ASİSTAN CEVABI (Stream)
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with chat_cont:
            with st.chat_message("assistant"):
                ph = st.empty()
                full_resp = ""
                # Brain'den stream cevap al (logic/brain.py dosyasının var olduğundan emin olun)
                try:
                    for chunk in brain.get_streaming_response(st.session_state.messages, user):
                        full_resp += chunk
                        ph.markdown(full_resp + "▌")
                        time.sleep(0.01)
                    ph.markdown(full_resp)
                    st.session_state.messages.append({"role": "assistant", "content": full_resp})
                except Exception as e:
                    st.error(f"AI Yanıt Hatası: {e}")

    # --- SAĞ: DİNAMİK GÖRSELLER ---
    with col_viz:
        mode = st.session_state.dashboard_mode
        
        def metric_card(lbl, val, delta, col="#34D399"):
            st.markdown(f"""<div class='metric-card'><div style='color:#AAA; font-size:12px'>{lbl}</div><div style='font-size:24px; font-weight:bold'>{val}</div><div style='color:{col}; font-size:12px'>{delta}</div></div>""", unsafe_allow_html=True)

        if mode == "finance":
            st.markdown("##### 📈 Finansal Performans")
            c1, c2 = st.columns(2)
            with c1: metric_card("Aylık Ciro", "$42,500", "+%12.5")
            with c2: metric_card("Net Kâr", "%32", "+%4.2")
            st.markdown("<br>", unsafe_allow_html=True)
            try: st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            except: st.warning("Grafik yüklenemedi.")
            
        elif mode == "logistics":
            st.markdown("##### 🌍 Lojistik Ağı")
            c1, c2 = st.columns(2)
            with c1: metric_card("Aktif Kargo", "TR-8821", "Yolda", "#3B82F6")
            with c2: metric_card("Varış", "2 Gün", "Zamanında")
            st.markdown("<br>", unsafe_allow_html=True)
            try: st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            except: st.warning("Harita yüklenemedi.")
            
        elif mode == "inventory":
            st.markdown("##### 📦 Depo Durumu")
            c1, c2 = st.columns(2)
            with c1: metric_card("Toplam Ürün", "8,500", "Adet")
            with c2: metric_card("Riskli Stok", "Çanta", "Kritik", "#F87171")
            st.markdown("<br>", unsafe_allow_html=True)
            try: st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
            except: st.warning("Grafik yüklenemedi.")

        elif mode == "documents":
            st.markdown("##### 📂 Dijital Arşiv")
            st.info("Son yüklenen belgeler burada görüntülenir.")
            metric_card("Toplam Belge", "1,240", "+5 Bugün", "#3B82F6")

        elif mode == "todo":
            st.markdown("##### ✅ Görevler")
            st.checkbox("Gümrük Müşaviri ile Görüş", value=True)
            st.checkbox("Sevkiyat Onayı", value=False)

        elif mode == "forms":
            st.markdown("##### 📝 Formlar")
            st.info("Bekleyen onaylarınız var.")

        elif mode == "plans":
            st.markdown("##### 💎 Stratejik Planlar")
            st.success("Q1 Hedefi: %15 Büyüme")
