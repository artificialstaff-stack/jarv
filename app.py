import streamlit as st
import sys
import os
import textwrap

# --- AYARLAR ---
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

st.set_page_config(
    page_title="ARTIS OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# --- STİL (HEADER VE BUTON DÜZELTMESİ) ---
st.markdown("""
<style>
    /* Header'ı şeffaf yap ama tıklanabilir bırak */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Sidebar Butonunu Zorla Göster (Mavi Kutu) */
    [data-testid="stSidebarCollapsedControl"] {
        display: block !important;
        color: white !important;
        background-color: #2563EB !important;
        border-radius: 8px;
        padding: 4px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Sidebar Arka Plan */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# --- MODÜLLERİ YÜKLE ---
try:
    import styles
    from views import login, dashboard, logistics, inventory, plan, documents, todo, forms
except ImportError as e:
    st.error(f"⚠️ Hata: {e}")
    st.stop()

styles.load_css()

# --- STATE ---
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}
if "nav_selection" not in st.session_state: st.session_state.nav_selection = "Dashboard"

# --- SIDEBAR ---
def render_sidebar():
    with st.sidebar:
        user = st.session_state.user_data
        brand = user.get('brand', 'ARTIS')
        
        st.info(f"🏢 {brand} (Enterprise)")
        
        # Navigasyon
        pages = ["Dashboard", "Lojistik", "Envanter", "Formlar", "Dokümanlar", "Yapılacaklar", "Planlar"]
        selection = st.radio("Menü", pages, label_visibility="collapsed")
        
        # Seçim değişirse güncelle
        if selection != st.session_state.nav_selection:
            st.session_state.nav_selection = selection
            st.rerun()
            
        st.divider()
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()

# --- ANA UYGULAMA ---
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        render_sidebar()
        
        # Hangi sayfadayız?
        page = st.session_state.nav_selection
        
        # === ACİL DURUM MENÜSÜ (Eğer Sidebar Açılmazsa Buradan Tıkla) ===
        if page != "Dashboard": # Dashboard'da gösterme
            with st.expander("🚀 Hızlı Menü (Sidebar Bozulursa Burayı Kullan)", expanded=False):
                c1,c2,c3,c4 = st.columns(4)
                if c1.button("📊 Dashboard"): st.session_state.nav_selection="Dashboard"; st.rerun()
                if c2.button("📦 Lojistik"): st.session_state.nav_selection="Lojistik"; st.rerun()
                if c3.button("📋 Envanter"): st.session_state.nav_selection="Envanter"; st.rerun()
                if c4.button("🚪 Çıkış"): st.session_state.logged_in=False; st.rerun()

        # Sayfayı Yükle
        if page == "Dashboard": dashboard.render_dashboard()
        elif page == "Lojistik": logistics.render_logistics()
        elif page == "Envanter": inventory.render_inventory()
        elif page == "Formlar": forms.render_forms()
        elif page == "Dokümanlar": documents.render_documents()
        elif page == "Yapılacaklar": todo.render_todo()
        elif page == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
