import streamlit as st
import sys
import os
import textwrap

# --- SISTEM YOLLARI ---
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

# 1. SIDEBAR'I VARSAYILAN OLARAK AÇIK BAŞLAT
st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# 2. RADİKAL CSS: TÜM AÇMA/KAPAMA BUTONLARINI GİZLE
st.markdown("""
<style>
    /* Sidebar içindeki 'X' (kapatma) butonunu gizle */
    [data-testid="stSidebar"] button {
        display: none !important;
    }
    
    /* Ana sayfadaki '>' (açma) butonunu gizle */
    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    
    /* Sidebar genişliğini sabitle ve kullanıcı tarafından daraltılmasını engelle */
    [data-testid="stSidebar"] {
        min-width: 260px !important;
        max-width: 260px !important;
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* Header alanındaki boşlukları temizle */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

import styles
import login
import dashboard

# Uygulama Stillerini Yükle
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

def render_sidebar():
    with st.sidebar:
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        
        # Marka Başlığı
        st.markdown(f"### ⚡ {user_brand}")
        st.markdown("---")
        
        # Menü (Radio button her zaman görünür olacak)
        pages = ["Dashboard", "Lojistik", "Envanter", "Formlar", "Dokümanlar", "Planlar"]
        selection = st.radio("MENÜ", pages, label_visibility="collapsed")
        
        st.markdown("<div style='flex-grow: 1; height: 300px;'></div>", unsafe_allow_html=True)
        
        if st.button("Güvenli Çıkış", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
        return selection

def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        selection = render_sidebar()
        if selection == "Dashboard":
            dashboard.render_dashboard()
        # Diğer sayfalar buraya eklenebilir

if __name__ == "__main__":
    main()
