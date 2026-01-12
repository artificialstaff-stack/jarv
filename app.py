import streamlit as st
from styles import load_css
from views import (
    render_login_screen, 
    render_welcome_animation, 
    render_main_hub, 
    render_dashboard, 
    render_artis_ai, 
    render_logistics, 
    render_marketing
)

# [APP-01] CONFIGURATION
st.set_page_config(page_title="Artificial Staff", layout="wide", initial_sidebar_state="expanded")

# [APP-02] SESSION STATE
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'show_welcome' not in st.session_state: st.session_state.show_welcome = False

# [APP-03] LOAD STYLES
load_css()

# [APP-04] MAIN LOGIC FLOW
if not st.session_state.authenticated:
    # Durum 1: Giriş Yapılmamış -> Login Ekranı
    render_login_screen()

elif st.session_state.show_welcome:
    # Durum 2: Yeni Giriş Yapılmış -> Animasyon
    render_welcome_animation()

else:
    # Durum 3: Giriş Yapılmış -> Ana Uygulama (Menü Burada)
    with st.sidebar:
        st.markdown("<h1 style='text-align:center; color:#D4AF37; margin-bottom:0;'>AS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#666; letter-spacing:2px; font-size:10px; margin-top:0;'>ENTERPRISE</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        page = st.radio(
            label="Navigasyon",
            options=["ANA MERKEZ", "DASHBOARD", "ARTIS (AI)", "LOJİSTİK", "PAZARLAMA"],
            label_visibility="collapsed"
        )
        st.markdown("---")
        if st.button("ÇIKIŞ YAP"):
            st.session_state.authenticated = False
            st.rerun()

    # Sayfa Yönlendirmeleri
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
