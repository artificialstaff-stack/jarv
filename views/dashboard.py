import streamlit as st
import brain
import time
from datetime import datetime
from typing import Dict, Any

# ==============================================================================
# 🎨 DASHBOARD STİLİ (AYNI KALIYOR)
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

def render_metric(label, value, delta, icon="bx-stats"):
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
def render_dashboard():
    inject_dashboard_css()
    
    # 1. KULLANICI BİLGİSİNİ AL
    user = st.session_state.get('user_data', {'brand': 'Demo Brand', 'name': 'User'})
    
    # 2. HEADER
    render_header(user)
    
    # 3. DURUM YÖNETİMİ (SOL MENÜYLE BAĞLANTI)
    # Eğer session'da bir mod yoksa varsayılanı 'finance' yap
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
                # Başlangıç mesajını mevcut moda göre ayarla
                welcome_msg = "Merhaba! Finans verilerini inceliyorum."
                if current_mode == "logistics": welcome_msg = "Lojistik ve kargo durumunu kontrol ediyorum."
                elif current_mode == "inventory": welcome_msg = "Stok ve depo raporlarını hazırladım."
                st.info(f"👋 {welcome_msg}")
            
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        # Yeni Mesaj Girişi
        if prompt := st.chat_input("Talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # --- ZEKİ MOD DEĞİŞTİRİCİ ---
            # Kullanıcının sorusuna göre sağ tarafı güncelle
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo", "harita"]):
                st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "depo", "ürün"]):
                st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "satış"]):
                st.session_state.dashboard_mode = "finance"
            
            st.rerun() # Mod değiştiği için sayfayı yenile

    # Asistan Cevabını Oluştur (Rerun sonrası çalışır)
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with chat_cont:
            with st.chat_message("assistant"):
                ph = st.empty()
                full_resp = ""
                # Brain'e 'user' verisini de gönderiyoruz (Hata Çözümü)
                for chunk in brain.get_streaming_response(st.session_state.messages, user):
                    full_resp += chunk
                    ph.markdown(full_resp + "▌")
                    time.sleep(0.01)
                ph.markdown(full_resp)
        st.session_state.messages.append({"role": "assistant", "content": full_resp})

    # --- SAĞ: DİNAMİK GÖRSELLER ---
    with col_viz:
        mode = st.session_state.dashboard_mode
        
        if mode == "finance":
            st.markdown("##### 📈 Finansal Performans")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aylık Ciro", "$42,500", "+%12.5")
            with c2: render_metric("Net Kâr", "%32", "+%4.2", "bx-trending-up")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            
        elif mode == "logistics":
            st.markdown("##### 🌍 Lojistik Ağı")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aktif Kargo", "TR-8821", "Yolda", "bx-map-pin")
            with c2: render_metric("Varış", "2 Gün", "Zamanında", "bx-time")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            
        elif mode == "inventory":
            st.markdown("##### 📦 Depo Durumu")
            c1, c2 = st.columns(2)
            with c1: render_metric("Toplam Ürün", "8,500", "Adet", "bx-package")
            with c2: render_metric("Riskli Stok", "Çanta", "Kritik", "bx-error")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
