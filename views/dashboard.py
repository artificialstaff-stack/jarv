import streamlit as st
import brain
from datetime import datetime
from typing import Dict, Any
import time

# ==============================================================================
# 🎨 DASHBOARD CSS
# ==============================================================================
def inject_dashboard_css():
    st.markdown("""
    <style>
        .dash-header-container {
            padding: 20px;
            background: linear-gradient(90deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            margin-bottom: 20px;
        }
        .metric-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 15px;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 BİLEŞENLER
# ==============================================================================
def render_header(user_data):
    brand = user_data.get('brand', 'Anatolia Home')
    st.markdown(f"""
    <div class="dash-header-container">
        <h1 style="margin:0; font-size: 2rem;">{brand}</h1>
        <div style="color: #34D399; font-size: 0.8rem; margin-top: 5px;">● Sistem Operasyonel</div>
    </div>
    """, unsafe_allow_html=True)

def render_metric(label, value, delta):
    st.markdown(f"""
    <div class="metric-card">
        <div style="color: #A1A1AA; font-size: 0.8rem;">{label}</div>
        <div style="font-size: 1.5rem; font-weight: bold;">{value}</div>
        <div style="color: #34D399; font-size: 0.8rem;">{delta}</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🚀 ANA FONKSİYON (HATAYI ÇÖZEN KISIM BURASI)
# ==============================================================================
def render_dashboard():
    # 1. CSS Yükle
    inject_dashboard_css()
    
    # 2. Kullanıcı Verisini Al
    user = st.session_state.get('user_data', {'brand': 'Demo Brand'})
    
    # 3. Header'ı Çiz
    render_header(user)
    
    # 4. Sayfa Düzeni
    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.subheader("🤖 Asistan")
        st.info("👋 Merhaba! Finans veya Stok durumunu sorabilirsin.")
        
        # Chat Arayüzü
        if "messages" not in st.session_state: st.session_state.messages = []
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
            
        if prompt := st.chat_input("Bir şey sor..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            # Cevap (Mock)
            response = f"'{prompt}' ile ilgili verileri inceliyorum..."
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)

    with c2:
        st.subheader("📊 Özet")
        m1, m2, m3 = st.columns(3)
        with m1: render_metric("Ciro", "$42,500", "+%12")
        with m2: render_metric("Net Kâr", "%32", "+%4")
        with m3: render_metric("Sipariş", "142", "Aktif")
        
        st.markdown("### 📈 Satış Grafiği")
        try:
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
        except:
            st.warning("Grafik yüklenemedi (Brain modülü bekleniyor).")
