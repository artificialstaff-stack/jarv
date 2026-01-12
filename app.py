import streamlit as st
from styles import load_css
# Artık tüm fonksiyonlar views.py içinde mevcut, hata vermez.
from views import (
    render_login_screen, 
    render_welcome_animation, 
    render_main_hub,          # Bu artık views.py içinde tanımlı!
    render_services_catalog, 
    render_dashboard, 
    render_artis_ai, 
    render_logistics, 
    render_marketing
)

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Artificial Staff - Enterprise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'show_welcome' not in st.session_state:
    st.session_state.show_welcome = False

# 3. CSS Yükle
load_css()

# --- ANA AKIŞ ---

if not st.session_state.authenticated:
    render_login_screen()

elif st.session_state.show_welcome:
    render_welcome_animation()

else:
    # MENÜ (Sadece giriş yapınca görünür)
    with st.sidebar:
        st.markdown("<h1 style='text-align:center; color:#D4AF37; margin-bottom:0;'>AS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#666; letter-spacing:2px; font-size:10px; margin-top:0;'>ENTERPRISE</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        page = st.radio(
            label="Menü",
            options=["ANA MERKEZ", "DASHBOARD", "ARTIS (AI)", "LOJİSTİK", "PAZARLAMA"],
            label_visibility="collapsed"
        )
        st.markdown("---")
        if st.button("ÇIKIŞ YAP"):
            st.session_state.authenticated = False
            st.session_state.show_welcome = False
            st.rerun()

    # SAYFA YÖNLENDİRME
    if page == "ANA MERKEZ":
        render_main_hub()
    elif page == "DASHBOARD":
        render_dashboard()
    elif page == "ARTIS (AI)":
        render_artis_ai()
    elif page == "LOJİSTİK":
        render_logistics()
    elif page == "PAZARLAMA":
        render_marketing()
