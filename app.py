import streamlit as st
from styles import load_css
from views import render_login_screen, render_jarvis_core, render_global_hub, render_finances, render_logistics_view

# [APP-01] AYARLAR
st.set_page_config(page_title="Artificial Staff", layout="wide", initial_sidebar_state="expanded")

if 'authenticated' not in st.session_state: st.session_state.authenticated = False

load_css()

# [APP-02] ANA AKIŞ
if not st.session_state.authenticated:
    render_login_screen()
else:
    # --- COMMAND CENTER SIDEBAR ---
    with st.sidebar:
        # Logo ve Alt Başlık (Resimdeki Gibi)
        st.markdown("<div class='sidebar-logo'>ARTIFICIAL<br>STAFF</div>", unsafe_allow_html=True)
        st.markdown("<div class='sidebar-sub'>COMMAND CENTER</div>", unsafe_allow_html=True)
        
        # Menü (İngilizce/Teknik Terimler - Resimdeki gibi)
        page = st.radio(
            "MODULES",
            ["JARVIS CORE", "GLOBAL HUB", "FINANCES", "LOGISTICS", "STRATEGY"],
            label_visibility="collapsed"
        )
        
        # Alt Bilgi (Status)
        st.markdown("""
        <div class='sidebar-status'>
            <div><span class='status-dot'></span> SYSTEM: ACTIVE</div>
            <div style='margin-top:5px;'><i class="fa-solid fa-lock"></i> SECURITY: SSL-V3</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("LOGOUT", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()

    # --- SAYFA YÖNLENDİRME ---
    if page == "JARVIS CORE":
        render_jarvis_core() # Ana Ekran (Perplexity Tarzı)
    elif page == "GLOBAL HUB":
        render_global_hub() # Hizmetler (Kartlar)
    elif page == "FINANCES":
        render_finances() # Dashboard
    elif page == "LOGISTICS":
        render_logistics_view() # Harita
    elif page == "STRATEGY":
        st.info("Strateji modülü yapım aşamasında.")
