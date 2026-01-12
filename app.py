import streamlit as st
import styles
import views
import brain

# 1. PAGE CONFIG
st.set_page_config(
    page_title="Artificial Staff | AI OS",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. LOAD STYLES
styles.load_css()

# 3. SESSION STATE INIT
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'COMMAND CENTER'

# --- GÜNCELLENMİŞ CHECKLIST & ONBOARDING STATE ---
if 'checklist' not in st.session_state:
    st.session_state['checklist'] = {
        'brand': False,   # Marka/Sektör girildi mi?
        'product': False, # Ürün detayları alındı mı?
        'data': False,    # Gizli veriler (maliyet/boyut) alındı mı?
        'offer': False    # Paket seçildi mi?
    }

if 'onboarding_step' not in st.session_state:
    st.session_state['onboarding_step'] = 'intro'

if 'onboarding_history' not in st.session_state:
    # İlk mesaj: Sistem otomatik başlatılır.
    st.session_state['onboarding_history'] = [{
        "role": "assistant", 
        "content": "Sistem başlatıldı. Washington merkezli operasyon ofisinize hoş geldiniz. Ben ARTIS. İşletmenizi analiz etmek için hazırım. Öncelikle, markanızın adı nedir?"
    }]
    # İlk adımda markayı soruyoruz, cevap gelince sector adımına geçecek.
    st.session_state['onboarding_step'] = 'get_sector'

# 4. MAIN CONTROLLER
if not st.session_state['logged_in']:
    views.render_login()
else:
    # Navbar
    views.render_navbar()
    
    # Sidebar
    with st.sidebar:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("### NAVIGATION")
        
        page = st.radio(
            "MODULES", 
            ["COMMAND CENTER", "ARTIS AI", "FINANCE", "LOGISTICS"],
            label_visibility="collapsed"
        )
        st.session_state['current_page'] = page
        
        st.markdown("---")
        st.markdown("""
            <div style="font-family: 'Share Tech Mono'; font-size: 0.7rem; color: #666;">
                SYSTEM ID: 44-X-99<br>
                SERVER: US-EAST-1<br>
                LATENCY: 12ms
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("TERMINATE SESSION"):
            st.session_state['logged_in'] = False
            st.rerun()

    # Router
    if st.session_state['current_page'] == "COMMAND CENTER":
        views.render_command_center()
        
    elif st.session_state['current_page'] == "FINANCE":
        views.render_dashboard()
        
    elif st.session_state['current_page'] == "ARTIS AI":
        views.render_chat_interface()
        
    elif st.session_state['current_page'] == "LOGISTICS":
        st.markdown("<h3>GLOBAL LOGISTICS TRACKER</h3>", unsafe_allow_html=True)
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
        st.markdown("""
            <div class='hub-card' style='height:100px; flex-direction:row; justify-content:space-around;'>
                <div><b>TR-IST</b><br><span style='color:#D4AF37'>DEPARTED</span></div>
                <div>>></div>
                <div><b>US-DC</b><br><span style='color:#888'>WASH. HUB</span></div>
            </div>
        """, unsafe_allow_html=True)
