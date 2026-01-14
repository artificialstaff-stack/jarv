import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. SYSTEM CONFIGURATION & PATH SETUP
# ==============================================================================
# Add module paths relative to the current file to ensure imports work regardless of run directory
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
        'About': "# ARTIS Operating System v4.2\nPowered by Artificial Staff"
    }
)

# ==============================================================================
# 📦 2. MODULE IMPORTS (LAZY LOADING SAFEGUARDS)
# ==============================================================================
# Wrap imports in a try-except block to handle missing modules gracefully (Fail-Safe UI)
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
    st.error(f"""
    ### ⚠️ System Integrity Error
    Required modules could not be loaded. Please ensure the `views` and `logic` directories are correctly configured.
    \n**Error Details:** `{e}`
    """)
    st.stop()

# ==============================================================================
# 🎨 3. UI INJECTION & STATE MANAGEMENT
# ==============================================================================

# Load Enterprise CSS System (Global Styles)
styles.load_css()

# Initialize Session State (Persistence Layer)
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}
if "active_tab" not in st.session_state: st.session_state.active_tab = "Dashboard"

# ==============================================================================
# 🧭 4. SIDEBAR NAVIGATION COMPONENT (DYNAMIC & STYLED)
# ==============================================================================
def render_sidebar():
    with st.sidebar:
        # --- A. DYNAMIC BRAND HEADER ---
        # Get user data from session, fallback to default if missing
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        user_plan = st.session_state.user_data.get('plan', 'Enterprise')
        
        # HTML Block for Brand Header (Using dedent for safety)
        brand_html = textwrap.dedent(f"""
            <div style="margin-bottom: 25px; padding: 10px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 32px; height: 32px; background: linear-gradient(135deg, #8B5CF6 0%, #3B82F6 100%); border-radius: 8px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);">
                        <i class='bx bxs-command' style="color: white; font-size: 18px;"></i>
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 15px; color: #FFF; letter-spacing: -0.3px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 180px;">
                            {user_brand}
                        </div>
                        <div style="font-size: 10px; color: #34D399; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">
                            ● {user_plan} Edition
                        </div>
                    </div>
                </div>
            </div>
        """)
        st.markdown(brand_html, unsafe_allow_html=True)

        # --- B. NAVIGATION MENU ---
        # Custom styled radio button acts as the main navigation
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
        
        # --- C. SPACER & FOOTER ---
        # Push the user profile to the bottom
        st.markdown("<div style='flex-grow: 1; height: 100px;'></div>", unsafe_allow_html=True) 

        # --- D. USER PROFILE CARD (Sticky Bottom Look) ---
        user_name = st.session_state.user_data.get('name', 'Kullanıcı')
        user_initial = user_name[0] if user_name else "U"
        
        profile_html = textwrap.dedent(f"""
            <div style="
                margin-top: auto;
                background: linear-gradient(180deg, rgba(255,255,255,0.02) 0%, rgba(255,255,255,0.05) 100%); 
                border-top: 1px solid rgba(255,255,255,0.08); 
                padding: 15px; 
                border-radius: 12px; 
                display: flex; 
                align-items: center; 
                gap: 12px;
                transition: all 0.3s;">
                <div style="width: 34px; height: 34px; background: #27272A; border: 1px solid #3F3F46; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #E4E4E7; font-size: 14px;">
                    {user_initial}
                </div>
                <div style="flex-grow: 1; overflow: hidden;">
                    <div style="font-size: 13px; font-weight: 600; color: #E4E4E7; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{user_name}</div>
                    <div style="font-size: 10px; color: #A1A1AA;">admin@artis.ai</div>
                </div>
            </div>
        """)
        st.markdown(profile_html, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        if st.button("Çıkış Yap", use_container_width=True):
            with st.spinner("Güvenli çıkış yapılıyor..."):
                time.sleep(0.5)
            st.session_state.logged_in = False
            st.rerun()
            
        return selected

# ==============================================================================
# 🚀 5. MAIN APP ROUTER
# ==============================================================================
def main():
    # 1. Check Login Status
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        # 2. Render Sidebar & Get Page Selection
        selection = render_sidebar()
        
        # 3. Route to the appropriate view
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

# Entry Point
if __name__ == "__main__":
    main()
