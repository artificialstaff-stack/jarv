import streamlit as st
from styles import load_css
from views import render_login_screen, render_artis_home, render_services, render_dashboard

# Ayarlar
st.set_page_config(page_title="Artificial Staff", layout="wide", initial_sidebar_state="expanded")

# Durumlar
if 'authenticated' not in st.session_state: st.session_state.authenticated = False

load_css()

# AKIŞ
if not st.session_state.authenticated:
    render_login_screen()
else:
    # Sidebar (Sadece Giriş Yapınca)
    with st.sidebar:
        st.markdown("<div style='text-align:center; color:#D4AF37; font-family:Cinzel; font-size:32px; margin-bottom:20px;'>AS</div>", unsafe_allow_html=True)
        
        page = st.radio(
            "MENÜ",
            ["ARTIS AI", "HİZMETLER", "DASHBOARD"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        if st.button("ÇIKIŞ"):
            st.session_state.authenticated = False
            st.rerun()

    # Sayfalar
    if page == "ARTIS AI":
        render_artis_home()
    elif page == "HİZMETLER":
        render_services()
    elif page == "DASHBOARD":
        render_dashboard()
