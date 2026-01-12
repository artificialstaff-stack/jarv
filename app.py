import streamlit as st
from styles import load_css
from views import render_dashboard, render_artis_ai, render_logistics, render_marketing, render_services_catalog

# 1. Sayfa Ayarları (En başta olmalı)
st.set_page_config(
    page_title="Artificial Staff - Enterprise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Yükle
load_css()

# 3. Sidebar (Yan Menü)
with st.sidebar:
    st.markdown("<h1 style='text-align:center; color:#D4AF37; margin-bottom:0;'>AS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; letter-spacing:2px; font-size:10px; margin-top:0;'>ENTERPRISE</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Menüde 'Hizmetlerimiz'i başa koyduk ki müşteri ilk girdiğinde ne sattığımızı görsün
    page = st.radio(
        label="Menü",
        options=["HİZMETLERİMİZ", "DASHBOARD", "ARTIS (AI)", "LOJİSTİK", "PAZARLAMA"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("© 2026 Artificial Staff LLC")

# 4. Sayfa Yönlendirmesi
if page == "HİZMETLERİMİZ":
    render_services_catalog()
elif page == "DASHBOARD":
    render_dashboard()
elif page == "ARTIS (AI)":
    render_artis_ai()
elif page == "LOJİSTİK":
    render_logistics()
elif page == "PAZARLAMA":
    render_marketing()
