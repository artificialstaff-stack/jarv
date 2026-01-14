import streamlit as st
import sys
import os
import textwrap

# --- 1. AYARLAR ---
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

st.set_page_config(
    page_title="ARTIS OS",
    layout="wide",
    # Başlangıçta KAPALI (collapsed) yapıyorum ki o özel butonu hemen gör.
    initial_sidebar_state="collapsed" 
)

# --- 2. CSS: BUTONU SAĞA ALMA VE YAZI EKLEME ---
st.markdown("""
<style>
    /* Header'ı şeffaf yap */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
    }

    /* --- ÖZEL BUTON TASARIMI --- */
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        align-items: center !important;
        
        /* KONUMU: Soldan 50px boşluk bıraktık (Biraz sağa kaydı) */
        position: fixed !important;
        top: 25px !important;
        left: 50px !important; 
        z-index: 9999999 !important;
        
        /* GÖRÜNÜM: Geniş Mavi Buton */
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        
        /* Boyut ayarları - Yazı sığsın diye genişlettim */
        width: auto !important; 
        height: 45px !important;
        padding-left: 10px !important;
        padding-right: 20px !important;
        
        pointer-events: auto !important;
        cursor: pointer !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5) !important;
        transition: transform 0.2s !important;
    }

    /* --- YAZI EKLEME BÖLÜMÜ --- */
    /* Butonun içine sanal bir yazı ekliyoruz */
    [data-testid="stSidebarCollapsedControl"]::after {
        content: "Sayfaları Görüntüle" !important; /* İSTEDİĞİN YAZI BURADA */
        font-size: 14px !important;
        font-weight: 700 !important;
        margin-left: 8px !important; /* Ok işareti ile yazı arası boşluk */
        color: white !important;
        white-space: nowrap !important;
    }

    /* İkon Rengi (Ok İşareti) */
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
    }
    
    /* Hover Efekti */
    [data-testid="stSidebarCollapsedControl"]:hover {
        background-color: #1D4ED8 !important;
        transform: scale(1.02) !important;
    }

    /* Sidebar Arka Planı */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. MODÜLLER ---
try:
    import styles, login, dashboard, logistics, inventory, plan, documents, todo, forms
except ImportError:
    st.error("Modüller bulunamadı.")
    st.stop()

styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

# --- 4. SOL MENÜ ---
def render_sidebar():
    with st.sidebar:
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        
        st.markdown(f"### ⚡ {user_brand}")
        st.markdown("---")
        
        # Sayfalar
        menu = {
            "Dashboard": "📊 Dashboard",
            "Lojistik": "📦 Lojistik",
            "Envanter": "📋 Envanter",
            "Formlar": "📝 Formlar",
            "Dokümanlar": "📂 Dokümanlar",
            "Planlar": "💎 Planlar"
        }
        
        sel = st.radio("MENÜ", list(menu.keys()), format_func=lambda x: menu[x], label_visibility="collapsed")
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()
            
        return sel

# --- 5. ANA UYGULAMA ---
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        page = render_sidebar()
        
        if page == "Dashboard": dashboard.render_dashboard()
        elif page == "Lojistik": logistics.render_logistics()
        elif page == "Envanter": inventory.render_inventory()
        elif page == "Formlar": forms.render_forms()
        elif page == "Dokümanlar": documents.render_documents()
        elif page == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
