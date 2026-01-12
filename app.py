import streamlit as st
from styles import load_css
from views import render_login_screen, render_jarvis_core, render_global_hub, render_finances, render_logistics_view

# [APP-01] AYARLAR
st.set_page_config(
    page_title="Artificial Staff",
    layout="wide",
    initial_sidebar_state="expanded" # Başlangıçta açık olsun
)

if 'authenticated' not in st.session_state: st.session_state.authenticated = False

load_css()

# [APP-02] ANA AKIŞ
if not st.session_state.authenticated:
    render_login_screen()
else:
    # --- COMMAND CENTER SIDEBAR ---
    with st.sidebar:
        # Logo ve Alt Başlık
        st.markdown("<div class='sidebar-logo'>ARTIFICIAL<br>STAFF</div>", unsafe_allow_html=True)
        st.markdown("<div class='sidebar-sub'>COMMAND CENTER</div>", unsafe_allow_html=True)
        
        # Ekran Görüntüsündeki Birebir Menü Yapısı
        page = st.radio(
            "MODULES",
            [
                "🔴 JARVIS CORE",  # Ana Ekran
                "📦 INVENTORY",    # Hizmetler/Envanter
                "✈️ LOGISTICS",    # Lojistik
                "💰 FINANCES",     # Dashboard
                "📈 STRATEGY"      # Pazarlama/Strateji
            ],
            label_visibility="collapsed"
        )
        
        # Alt Bilgi (Status)
        st.markdown("""
        <div class='sidebar-status'>
            <div><span class='status-dot'></span> SİSTEM: AKTİF</div>
            <div style='margin-top:5px;'><i class="fa-solid fa-lock"></i> GÜVENLİK: SSL-V3</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("LOGOUT", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()

    # --- SAYFA YÖNLENDİRME ---
    # Seçilen menü ismine göre ilgili sayfayı çağırıyoruz
    if "JARVIS CORE" in page:
        render_jarvis_core() # Ana Ekran
    elif "INVENTORY" in page:
        render_global_hub() # Hizmet Kataloğu
    elif "FINANCES" in page:
        render_finances() # Dashboard
    elif "LOGISTICS" in page:
        render_logistics_view() # Harita
    elif "STRATEGY" in page:
        st.info("Strateji modülü yapım aşamasında.")
