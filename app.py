import streamlit as st
import styles
import views
import brain

# 1. AYARLAR
st.set_page_config(page_title="Artificial Staff | AI OS", layout="wide", initial_sidebar_state="expanded")
styles.load_css()

# 2. SESSION STATE (HAFIZA)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'COMMAND CENTER'

# Checklist Durumları
if 'checklist' not in st.session_state:
    st.session_state['checklist'] = {
        'brand': False, 'product': False, 'data': False, 'offer': False
    }

# Sohbet Adımı ve Geçmişi
if 'onboarding_step' not in st.session_state:
    st.session_state['onboarding_step'] = 'intro'
if 'onboarding_history' not in st.session_state:
    st.session_state['onboarding_history'] = [{
        "role": "assistant", 
        "content": "Sistem başlatıldı. Washington DC operasyon merkezine hoş geldiniz. Ben ARTIS. Markanızın adı nedir?"
    }]

# 3. YÖNLENDİRME
if not st.session_state['logged_in']:
    views.render_login()
else:
    views.render_navbar()
    
    with st.sidebar:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("### NAVIGATION")
        page = st.radio("MODULES", ["COMMAND CENTER", "ARTIS AI", "FINANCE", "LOGISTICS"], label_visibility="collapsed")
        st.session_state['current_page'] = page
        st.markdown("---")
        if st.button("TERMINATE SESSION"):
            st.session_state['logged_in'] = False
            st.rerun()

    # YÖNLENDİRİCİ (ROUTER)
    if st.session_state['current_page'] == "COMMAND CENTER":
        views.render_command_center()
    elif st.session_state['current_page'] == "FINANCE":
        views.render_dashboard()
    elif st.session_state['current_page'] == "ARTIS AI":
        views.render_chat_interface()
    elif st.session_state['current_page'] == "LOGISTICS":
        st.markdown("<h3>GLOBAL LOGISTICS TRACKER</h3>", unsafe_allow_html=True)
        # Hata aldığın satır burasıydı, şimdi brain.py düzgün yüklendiği için çalışacak
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
