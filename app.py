import streamlit as st
from styles import load_css
from views import render_dashboard, render_ai_manager, render_logistics, render_marketing

# 1. Sayfa Konfigürasyonu (En başta olmalı)
st.set_page_config(
    page_title="Artificial Staff - Enterprise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Yükle
load_css()

# 3. Sidebar (Yan Menü) Tasarımı
with st.sidebar:
    # Logo Alanı
    st.markdown("""
        <div style='text-align: center; margin-bottom: 30px;'>
            <h1 style='color: #D4AF37 !important; font-size: 40px; margin:0;'>AS</h1>
            <span style='font-size: 10px; letter-spacing: 3px; color: #888;'>ENTERPRISE</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigasyon
    page = st.radio(
        "Menü",
        ["DASHBOARD (Ana Ekran)", "JARVIS (AI Manager)", "LOJİSTİK (Canlı Takip)", "PAZARLAMA (360°)", "HİZMET KURULUMU"],
        label_visibility="collapsed"
    )
    
    # Alt Bilgi
    st.markdown("""
        <div style='position: fixed; bottom: 20px; width: 200px; text-align: center; color: #444; font-size: 10px;'>
            © 2026 Artificial Staff LLC<br>System Operational
        </div>
    """, unsafe_allow_html=True)

# 4. Sayfa Yönlendirmesi
if page == "DASHBOARD (Ana Ekran)":
    render_dashboard()
elif page == "JARVIS (AI Manager)":
    render_ai_manager()
elif page == "LOJİSTİK (Canlı Takip)":
    render_logistics()
elif page == "PAZARLAMA (360°)":
    render_marketing()
else:
    st.warning("Bu modül geliştirme aşamasındadır.")
