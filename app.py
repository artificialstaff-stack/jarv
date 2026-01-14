import streamlit as st
import sys
import os
import time

# ==============================================================================
# 🔧 1. SYSTEM CONFIGURATION & PATH SETUP
# ==============================================================================
# Add module paths relative to the current file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

# Page Configuration (Must be the very first Streamlit command)
st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.anatoliacapital.com',
        'Report a bug': "mailto:support@anatolia.com",
        'About': "# ARTIS Operating System v4.2"
    }
)

# ==============================================================================
# 📦 2. MODULE IMPORTS (LAZY LOADING SAFEGUARDS)
# ==============================================================================
try:
    import styles
    import login
    import dashboard
    import logistics
    import inventory
    import plan
    import documents
    import todo
    import forms
except ImportError as e:
    st.error(f"⚠️ System Module Error: {e}")
    st.stop()

# ==============================================================================
# 🎨 3. UI INJECTION & STATE MANAGEMENT
# ==============================================================================

# Load Enterprise CSS System
styles.load_css()

# Initialize Session State
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}
if "active_tab" not in st.session_state: st.session_state.active_tab = "Dashboard"

# ==============================================================================
# 🧭 4. SIDEBAR NAVIGATION COMPONENT
# ==============================================================================
def render_sidebar():
    with st.sidebar:
        # A. Brand Header
        st.markdown("""
        <div style="margin-bottom: 30px; padding-left: 10px;">
            <div style="font-weight: 800; font-size: 20px; color: #FFF; letter-spacing: -0.5px; display: flex; align-items: center; gap: 10px;">
                <span style="background: linear-gradient(135deg, #8B5CF6 0%, #3B82F6 100%); width: 24px; height: 24px; border-radius: 6px; display: inline-block;"></span>
                Anatolia Home
            </div>
            <div style="font-size: 11px; color: #71717A; font-weight: 500; margin-left: 34px;">Enterprise Edition</div>
        </div>
        """, unsafe_allow_html=True)

        # B. Navigation Menu (Custom Styled Radio)
        # İkonları label'ın içine gömüyoruz çünkü st.radio native ikon desteklemez
        menu_options = {
            "Dashboard": "📊  Dashboard",
            "Lojistik": "📦  Lojistik",
            "Envanter": "📋  Envanter",
            "Formlar": "📝  Formlar",
            "Dokümanlar": "📂  Dokümanlar",
            "Yapılacaklar": "✅  Yapılacaklar",
            "Planlar": "💎  Planlar"
        }
        
        selected = st.radio(
            "NAVİGASYON",
            list(menu_options.keys()),
            format_func=lambda x: menu_options[x],
            label_visibility="collapsed",
            key="nav_radio"
        )
        
        # C. Spacer
        st.markdown("<div style='flex-grow: 1;'></div>", unsafe_allow_html=True)
        st.markdown("<br>" * 5, unsafe_allow_html=True) # Bottom spacer

        # D. User Profile Card (Bottom Sticky)
        user_name = st.session_state.user_data.get('brand', 'Kullanıcı')
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.03); 
            border: 1px solid rgba(255,255,255,0.05); 
            padding: 12px; 
            border-radius: 12px; 
            display: flex; 
            align-items: center; 
            gap: 12px;
            margin-top: auto;">
            <div style="width: 36px; height: 36px; background: linear-gradient(45deg, #3B82F6, #8B5CF6); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: white;">
                {user_name[0]}
            </div>
            <div style="flex-grow: 1;">
                <div style="font-size: 13px; font-weight: 600; color: #E4E4E7;">{user_name}</div>
                <div style="font-size: 11px; color: #34D399;">● Çevrimiçi</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Çıkış Yap", use_container_width=True):
            with st.spinner("Oturum kapatılıyor..."):
                time.sleep(0.5)
            st.session_state.logged_in = False
            st.rerun()
            
        return selected

# ==============================================================================
# 🚀 5. MAIN APP ROUTER
# ==============================================================================
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        # Render Sidebar & Get Selection
        selection = render_sidebar()
        
        # Route Logic
        if selection == "Dashboard":
            dashboard.render_dashboard()
        elif selection == "Lojistik":
            logistics.render_logistics()
        elif selection == "Envanter":
            inventory.render_inventory()
        elif selection == "Formlar":
            forms.render_forms()
        elif selection == "Dokümanlar":
            documents.render_documents()
        elif selection == "Yapılacaklar":
            todo.render_todo()
        elif selection == "Planlar":
            plan.render_plans()

if __name__ == "__main__":
    main()
