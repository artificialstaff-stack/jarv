import streamlit as st
import sys
import os
import textwrap

# 1. AYARLAR
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

st.set_page_config(
    page_title="ARTIS OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded" # <-- MENÜYÜ AÇIK BAŞLATIYORUZ
)

# 2. CSS FIX
st.markdown("""
<style>
    /* Header Şeffaf */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
    }
    
    /* Butonu Zorla Göster ve Mavi Yap */
    [data-testid="stSidebarCollapsedControl"] {
        display: block !important;
        visibility: visible !important;
        color: white !important;
        background-color: #2563EB !important;
        width: 40px !important;
        height: 40px !important;
        padding: 5px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        z-index: 9999999 !important;
        pointer-events: auto !important;
    }
    
    /* Yan Menü Arka Planı */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 3. YÜKLEME
try:
    import styles
    from views import login, dashboard, logistics, inventory, plan, documents, todo, forms
except ImportError as e:
    st.error(f"Sistem Hatası: {e}")
    st.stop()

styles.load_css()

# 4. DURUM YÖNETİMİ
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}
if "nav_selection" not in st.session_state: st.session_state.nav_selection = "Dashboard"

# 5. SIDEBAR
def render_sidebar():
    with st.sidebar:
        user = st.session_state.user_data
        st.markdown(f"### ⚡ {user.get('brand', 'ARTIS')}")
        
        pages = {
            "Dashboard": "📊 Dashboard", "Lojistik": "📦 Lojistik",
            "Envanter": "📋 Envanter", "Formlar": "📝 Formlar",
            "Dokümanlar": "📂 Dokümanlar", "Yapılacaklar": "✅ Yapılacaklar",
            "Planlar": "💎 Planlar"
        }
        
        selection = st.radio("Menü", list(pages.keys()), format_func=lambda x: pages[x], label_visibility="collapsed")
        
        if selection != st.session_state.nav_selection:
            st.session_state.nav_selection = selection
            st.rerun()
            
        st.divider()
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()

# 6. ANA AKIŞ
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        render_sidebar()
        page = st.session_state.nav_selection
        
        # ACİL DURUM MENÜSÜ (Eğer sidebar kaybolursa buradan geçiş yap)
        if page != "Dashboard":
            with st.expander("🚀 Hızlı Menü", expanded=False):
                c1,c2,c3,c4 = st.columns(4)
                if c1.button("📊 Dash"): st.session_state.nav_selection="Dashboard"; st.rerun()
                if c2.button("📦 Lojistik"): st.session_state.nav_selection="Lojistik"; st.rerun()
                if c3.button("📋 Envanter"): st.session_state.nav_selection="Envanter"; st.rerun()
                if c4.button("🚪 Çıkış"): st.session_state.logged_in=False; st.rerun()

        # Sayfa Render
        if page == "Dashboard": dashboard.render_dashboard()
        elif page == "Lojistik": logistics.render_logistics()
        elif page == "Envanter": inventory.render_inventory()
        elif page == "Formlar": forms.render_forms()
        elif page == "Dokümanlar": documents.render_documents()
        elif page == "Yapılacaklar": todo.render_todo()
        elif page == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
