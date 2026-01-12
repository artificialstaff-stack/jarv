import streamlit as st
import styles
import views
import brain

# 1. AYARLAR
st.set_page_config(page_title="Artificial Staff | AI OS", layout="wide", initial_sidebar_state="expanded")
styles.load_css()

# 2. SESSION STATE
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'COMMAND CENTER'

# FORM VERİLERİNİ TUTACAK DEPO
if 'form_data' not in st.session_state:
    st.session_state['form_data'] = {
        'brand_name': '',
        'sector': 'Tekstil',
        'star_product': '',
        'dimensions': '',
        'selected_package': ''
    }

# CHAT GEÇMİŞİ
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [{
        "role": "assistant", 
        "content": "Hoş geldiniz. Sol taraftaki formları doldururken size yardımcı olmak için buradayım. Washington DC operasyon detaylarını sorabilirsiniz."
    }]

# RAPOR DURUMU
if 'submission_complete' not in st.session_state:
    st.session_state['submission_complete'] = False

# 3. ANA AKIŞ
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

    # YÖNLENDİRME
    if st.session_state['current_page'] == "COMMAND CENTER":
        if st.session_state['submission_complete']:
            st.success("BAŞVURUNUZ BAŞARIYLA ALINDI! YÖNETİCİYE İLETİLEN RAPOR AŞAĞIDADIR:")
            st.code(st.session_state['final_report'], language='text')
            if st.button("Yeni Başvuru Yap"):
                st.session_state['submission_complete'] = False
                st.rerun()
        else:
            views.render_command_center()
            
    elif st.session_state['current_page'] == "FINANCE":
        views.render_dashboard()
    elif st.session_state['current_page'] == "ARTIS AI":
        views.render_chat_interface()
    elif st.session_state['current_page'] == "LOGISTICS":
        st.markdown("<h3>GLOBAL LOGISTICS TRACKER</h3>", unsafe_allow_html=True)
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
