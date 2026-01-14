import streamlit as st
import sys
import os

# Yolları Tanıt
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

# 1. AYARLAR: Menü AÇIK başlasın (expanded)
st.set_page_config(
    page_title="ARTIS OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# 2. CSS FIX: KAYBOLAN BUTONU GERİ GETİR
st.markdown("""
<style>
    /* Header'ı tamamen gizleme, sadece şeffaf yap */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
    }
    
    /* MENÜ BUTONUNU ZORLA GÖSTER (Mavi Kutu) */
    [data-testid="stSidebarCollapsedControl"] {
        display: block !important;
        visibility: visible !important;
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        z-index: 9999999 !important; /* En üst katman */
        
        background-color: #2563EB !important;
        color: white !important;
        width: 40px !important;
        height: 40px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        
        pointer-events: auto !important;
        cursor: pointer !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# Modülleri Yükle
try:
    import styles
    from views import login, dashboard, logistics, inventory, plan, documents, todo, forms
except ImportError as e:
    st.error(f"⚠️ Hata: {e}")
    st.stop()

# Stilleri Yükle
styles.load_css()

# State Başlat
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "nav_selection" not in st.session_state: st.session_state.nav_selection = "Dashboard"
if "user_data" not in st.session_state: st.session_state.user_data = {}

# Yan Menü
def render_sidebar():
    with st.sidebar:
        st.title("⚡ ARTIS")
        
        pages = ["Dashboard", "Lojistik", "Envanter", "Formlar", "Dokümanlar", "Planlar"]
        selection = st.radio("Menü", pages, label_visibility="collapsed")
        
        if selection != st.session_state.nav_selection:
            st.session_state.nav_selection = selection
            st.rerun()
            
        st.divider()
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()

# Ana Uygulama
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        render_sidebar()
        
        sel = st.session_state.nav_selection
        
        if sel == "Dashboard": dashboard.render_dashboard()
        elif sel == "Lojistik": logistics.render_logistics()
        elif sel == "Envanter": inventory.render_inventory()
        elif sel == "Formlar": forms.render_forms()
        elif sel == "Dokümanlar": documents.render_documents()
        elif sel == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
