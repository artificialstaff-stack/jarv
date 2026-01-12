import streamlit as st
from styles import load_css
from views import render_dashboard, render_artis_ai, render_logistics, render_marketing, render_services_catalog

# 1. Ayarlar
st.set_page_config(
    page_title="Artificial Staff - Enterprise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS
load_css()

# 3. Sidebar
with st.sidebar:
    st.markdown("<h1 style='text-align:center; color:#D4AF37;'>AS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; letter-spacing:2px; font-size:10px;'>ENTERPRISE</p>", unsafe_allow_html=True)
    
    page = st.radio(
        "Menü",
        ["HİZMETLERİMİZ", "DASHBOARD", "ARTIS (AI)", "LOJİSTİK", "PAZARLAMA"],
        label_visibility="collapsed"
    )

# 4. Yönlendirme
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
