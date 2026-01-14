import streamlit as st
import brain
import time
import pandas as pd # Tablo göstermek için gerekli
from datetime import datetime
from typing import Dict, Any

# ==============================================================================
# 🎨 DASHBOARD STİLİ (Aynı Kalıyor)
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
        
        /* Tablo Stilleri */
        [data-testid="stDataFrame"] { background: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 YARDIMCI BİLEŞENLER
# ==============================================================================
def render_header(user_data):
    brand = user_data.get('brand', 'Anatolia Home')
    st.markdown(f"""
    <div class="dash-header-container">
        <h1 style="margin:0; font-size: 2.5rem; color:white;">{brand}</h1>
        <div style="color: #34D399; font-size: 0.8rem; margin-top: 5px;">● SYSTEM ONLINE | Istanbul HQ</div>
    </div>
    """, unsafe_allow_html=True)

def render_metric(label, value, delta, icon="bx-stats", color_override=None):
    if color_override:
        color = color_override
    else:
        color = "#34D399" if "+" in delta else "#F87171"
        
    st.markdown(f"""
    <div class="metric-card">
        <div style="color:#A1A1AA; font-size:0.8rem; text-transform:uppercase;">{label}</div>
        <div style="font-size:2rem; font-weight:bold; color:white; margin:5px 0;">{value}</div>
        <div style="color:{color}; font-size:0.8rem;"><i class='bx {icon}'></i> {delta}</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🚀 ANA DASHBOARD FONKSİYONU
# ==============================================================================
# views/dashboard.py içindeki render_dashboard fonksiyonunun başlangıcı
def render_dashboard():
    # Session State kontrollerini garantiye al
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {'brand': 'Anatolia Home', 'name': 'Ahmet Yılmaz'}
    
    # Değişkeni güvenli şekilde çek
    user = st.session_state.user_data
    
    # 2. HEADER
    render_header(user)
    
    # 3. MOD YÖNETİMİ
    if "dashboard_mode" not in st.session_state: 
        st.session_state.dashboard_mode = "finance"
    
    current_mode = st.session_state.dashboard_mode

    # 4. İKİ KOLONLU YAPI
    col_chat, col_viz = st.columns([1.2, 2], gap="medium")

    # --- SOL: AI ASİSTAN ---
    with col_chat:
        st.markdown("##### 🧠 Operasyon Asistanı")
        chat_cont = st.container(height=480)
        
        # Mesaj Geçmişi
        if "messages" not in st.session_state: st.session_state.messages = []
        
        with chat_cont:
            if not st.session_state.messages:
                st.info("👋 Merhaba! Tüm departman verilerini (Dokümanlar, Formlar, Planlar dahil) analiz edebilirim.")
            
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        # Yeni Mesaj Girişi
        if prompt := st.chat_input("Talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # --- ZEKİ MOD DEĞİŞTİRİCİ (TÜM SAYFALAR İÇİN) ---
            p_low = prompt.lower()
            
            # 1. Mevcut Modlar
            if any(x in p_low for x in ["lojistik", "kargo", "harita"]):
                st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "depo", "ürün", "envanter"]):
                st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "satış", "para"]):
                st.session_state.dashboard_mode = "finance"
                
            # 2. EKLENEN YENİ MODLAR (Doküman, Form, Plan, Todo)
            elif any(x in p_low for x in ["belge", "doküman", "dosya", "pdf"]):
                st.session_state.dashboard_mode = "documents"
            elif any(x in p_low for x in ["form", "başvuru", "talep"]):
                st.session_state.dashboard_mode = "forms"
            elif any(x in p_low for x in ["yapılacak", "görev", "todo", "işler"]):
                st.session_state.dashboard_mode = "todo"
            elif any(x in p_low for x in ["plan", "proje", "hedef", "strateji"]):
                st.session_state.dashboard_mode = "plans"
            
            st.rerun()

    # Asistan Cevabı
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with chat_cont:
            with st.chat_message("assistant"):
                ph = st.empty()
                full_resp = ""
                # Brain'e gönder
                for chunk in brain.get_streaming_response(st.session_state.messages, user):
                    full_resp += chunk
                    ph.markdown(full_resp + "▌")
                    time.sleep(0.01)
                ph.markdown(full_resp)
        st.session_state.messages.append({"role": "assistant", "content": full_resp})

    # --- SAĞ: DİNAMİK GÖRSELLER (ARTIK HEPSİ VAR) ---
    with col_viz:
        mode = st.session_state.dashboard_mode
        
        # 1. FİNANS
        if mode == "finance":
            st.markdown("##### 📈 Finansal Performans")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aylık Ciro", "$42,500", "+%12.5")
            with c2: render_metric("Net Kâr", "%32", "+%4.2", "bx-trending-up")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            
        # 2. LOJİSTİK
        elif mode == "logistics":
            st.markdown("##### 🌍 Lojistik Ağı")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aktif Kargo", "TR-8821", "Yolda", "bx-map-pin")
            with c2: render_metric("Varış", "2 Gün", "Zamanında", "bx-time")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            
        # 3. ENVANTER
        elif mode == "inventory":
            st.markdown("##### 📦 Depo Durumu")
            c1, c2 = st.columns(2)
            with c1: render_metric("Toplam Ürün", "8,500", "Adet", "bx-package")
            with c2: render_metric("Riskli Stok", "Çanta", "Kritik", "bx-error")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)

        # --- YENİ EKLENEN SAYFALAR ---
        
        # 4. DOKÜMANLAR (Tablo Görünümü)
        elif mode == "documents":
            st.markdown("##### 📂 Dijital Arşiv")
            c1, c2 = st.columns(2)
            with c1: render_metric("Toplam Dosya", "1,240", "+5 Yeni", "bx-folder", "#3B82F6")
            with c2: render_metric("Son Yükleme", "Bugün", "İrsaliye", "bx-cloud-upload", "#A1A1AA")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("**📁 Son Yüklenen Evraklar**")
            
            # Sahte Veri Tablosu
            data = {
                "Dosya Adı": ["Fatura_Ocak_2026.pdf", "Gümrük_Beyan_TR88.pdf", "Stok_Raporu_V2.xlsx", "İade_Prosedürü.docx"],
                "Tarih": ["14.01.2026", "13.01.2026", "12.01.2026", "10.01.2026"],
                "Boyut": ["1.2 MB", "450 KB", "2.1 MB", "800 KB"],
                "Durum": ["Onaylandı", "İşleniyor", "Hazır", "Taslak"]
            }
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

        # 5. FORMLAR (Liste Görünümü)
        elif mode == "forms":
            st.markdown("##### 📝 Aktif Formlar")
            c1, c2 = st.columns(2)
            with c1: render_metric("Bekleyen", "3", "Acil", "bx-edit", "#F59E0B")
            with c2: render_metric("Onaylanan", "12", "Bu Hafta", "bx-check-circle", "#10B981")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.info("ℹ️ Aşağıdaki formların onayı bekleniyor.")
            
            with st.expander("📌 Personel İzin Formu - Ahmet Y.", expanded=True):
                st.write("**Departman:** Lojistik")
                st.write("**Tarih:** 15-20 Ocak")
                st.button("Onayla", key="f1")
                
            with st.expander("📌 Satın Alma Talebi - #9921", expanded=False):
                st.write("**Ürün:** Ambalaj Malzemesi")
                st.write("**Tutar:** 5.000 TL")
                st.button("Onayla", key="f2")

        # 6. YAPILACAKLAR (Checklist)
        elif mode == "todo":
            st.markdown("##### ✅ Görev Yöneticisi")
            st.markdown("Bugünün öncelikli görevleri:")
            
            st.checkbox("Gümrük müşaviri ile görüş", value=True)
            st.checkbox("Ocak ayı finans raporunu onayla", value=False)
            st.checkbox("Depo sayım farklarını incele", value=False)
            st.checkbox("Yeni tedarikçi sözleşmesini hazırla", value=False)
            
            st.markdown("<br>", unsafe_allow_html=True)
            render_metric("Tamamlanan", "%25", "Devam Ediyor", "bx-task", "#8B5CF6")

        # 7. PLANLAR (Kart Görünümü)
        elif mode == "plans":
            st.markdown("##### 💎 Stratejik Planlar")
            
            st.success("🎯 **Q1 Hedefi:** Lojistik maliyetlerini %10 düşür.")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("""
                <div class="metric-card">
                    <h4>🇪🇺 Avrupa Genişlemesi</h4>
                    <p style="color:#A1A1AA; font-size:12px;">Berlin deposu açılış süreci.</p>
                    <div style="background:#333; height:5px; width:100%; margin-top:10px;"><div style="background:#3B82F6; height:5px; width:70%;"></div></div>
                    <p style="text-align:right; font-size:10px;">%70</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_b:
                st.markdown("""
                <div class="metric-card">
                    <h4>🤖 AI Entegrasyonu</h4>
                    <p style="color:#A1A1AA; font-size:12px;">Otomatik sipariş botu.</p>
                    <div style="background:#333; height:5px; width:100%; margin-top:10px;"><div style="background:#10B981; height:5px; width:40%;"></div></div>
                    <p style="text-align:right; font-size:10px;">%40</p>
                </div>
                """, unsafe_allow_html=True)
