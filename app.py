import streamlit as st
import styles
import views
import brain

# 1. PAGE CONFIG
st.set_page_config(page_title="Artificial Staff | AI OS", layout="wide", initial_sidebar_state="expanded")

# 2. LOAD STYLES
styles.load_css()

# 3. SESSION STATE INIT (BURASI ÇOK ÖNEMLİ)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'COMMAND CENTER'

# --- YENİ EKLENEN STATE DEĞİŞKENLERİ ---
if 'checklist' not in st.session_state:
    st.session_state['checklist'] = {
        'profile': False,
        'legal': False,
        'logistics': False,
        'marketing': False
    }

if 'onboarding_step' not in st.session_state:
    st.session_state['onboarding_step'] = 'intro'

if 'onboarding_history' not in st.session_state:
    # İlk açılış mesajını otomatik ekleyelim
    st.session_state['onboarding_history'] = [{
        "role": "assistant", 
        "content": "Sistem başlatıldı. Ben ARTIS. İşletmenizi analiz etmem için lütfen önce 'Marka Adınızı' yazar mısınız?"
    }]
    # İlk adım isme geçsin
    st.session_state['onboarding_step'] = 'get_name'
# ----------------------------------------

# 4. MAIN CONTROLLER
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
        st.button("TERMINATE SESSION", on_click=lambda: st.session_state.update({'logged_in': False}))

    # Router
    if st.session_state['current_page'] == "COMMAND CENTER":
        # Yeni fonksiyonu çağırıyoruz
        views.render_command_center()
        
    elif st.session_state['current_page'] == "FINANCE":
        views.render_dashboard()
    elif st.session_state['current_page'] == "ARTIS AI":
        views.render_chat_interface() # Bu views.py içinde tanımlı olmalı (eski kodunuzda vardı)
    elif st.session_state['current_page'] == "LOGISTICS":
        st.markdown("<h3>GLOBAL LOGISTICS TRACKER</h3>", unsafe_allow_html=True)
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
