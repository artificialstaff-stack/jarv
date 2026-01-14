import streamlit as st
import sys
import os
import textwrap

# --- 1. AYARLAR ---
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

st.set_page_config(
    page_title="ARTIS | Kurtarma Modu",
    page_icon="🚑",
    layout="wide",
    initial_sidebar_state="expanded" # Bunu 'expanded' yaptık ama tarayıcı inat ederse alttaki CSS butonu getirecek
)

# --- 2. CSS: KAYIP BUTONU GERİ GETİR ---
st.markdown("""
<style>
    /* 1. Header'ı Şeffaf Yap (Yok etme!) */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
    }

    /* 2. MENÜ AÇMA BUTONUNU ZORLA GÖSTER (EN ÖNEMLİ KISIM) */
    /* Tarayıcı menüyü kapalı tutsa bile, bu kod açma butonunu görünür kılar */
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        z-index: 9999999 !important; /* Her şeyin üstüne çıkar */
        
        background-color: #2563EB !important; /* Mavi Renk */
        color: white !important;
        width: 50px !important;
        height: 50px !important;
        border-radius: 10px !important;
        border: 2px solid white !important;
        box-shadow: 0 0 20px rgba(37, 99, 235, 0.8) !important;
        
        align-items: center !important;
        justify-content: center !important;
        pointer-events: auto !important;
        cursor: pointer !important;
    }
    
    /* İkonun Rengi */
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
        width: 30px !important;
        height: 30px !important;
    }

    /* 3. Sidebar Görünümü */
    [data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.1);
        min-width: 280px !important;
    }
    
    /* 4. Sayfa İçeriğini Biraz Aşağı İt */
    .block-container {
        padding-top: 80px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. MODÜLLERİ YÜKLE ---
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
    st.error(f"Modül Hatası: {e}")
    st.stop()

styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

# --- 4. SOL MENÜ ---
def render_sidebar():
    with st.sidebar:
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        
        st.markdown(f"### ⚡ {user_brand}")
        st.info("👈 Menü kapandığında sol üstteki MAVİ BUTONA basarak geri açabilirsin.")
        
        menu_options = {
            "Dashboard": "📊 Dashboard",
            "Lojistik": "📦 Lojistik",
            "Envanter": "📋 Envanter",
            "Formlar": "📝 Formlar",
            "Dokümanlar": "📂 Dokümanlar",
            "Yapılacaklar": "✅ Yapılacaklar",
            "Planlar": "💎 Planlar"
        }
        
        selection = st.radio(
            "MENÜ",
            list(menu_options.keys()),
            format_func=lambda x: menu_options[x],
            label_visibility="collapsed"
        )
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()
            
        return selection

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
        elif page == "Yapılacaklar": todo.render_todo()
        elif page == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
