import streamlit as st
import sys
import os
import textwrap

# --- 1. SİSTEM AYARLARI ---
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

# Sidebar'ı AÇIK başlatıyoruz
st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# --- 2. CSS: MENÜ BUTONUNU GERİ GETİRME (KURTARICI KOD) ---
st.markdown("""
<style>
    /* 1. Header'ı Şeffaf Yap */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
    }

    /* 2. MENÜ AÇMA BUTONUNU ZORLA GÖSTER (MAVİ KUTU) */
    /* Tarayıcı menüyü kapalı hatırlasa bile bu butonla açabileceksin */
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        z-index: 9999999 !important;
        
        background-color: #2563EB !important;
        color: white !important;
        width: 44px !important;
        height: 44px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        align-items: center !important;
        justify-content: center !important;
        
        pointer-events: auto !important;
        cursor: pointer !important;
    }
    
    /* İkon Rengi */
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
    }

    /* 3. Sidebar Tasarımı */
    [data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.1);
        min-width: 280px !important;
        max-width: 280px !important;
    }
    
    /* 4. Menü Butonlarını Güzelleştir */
    .st-emotion-cache-6qob1r { font-weight: 600 !important; color: #FAFAFA !important; }
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
    st.error(f"⚠️ Modül Hatası: {e}")
    st.stop()

styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

# --- 4. SOL MENÜ İÇERİĞİ ---
def render_sidebar():
    with st.sidebar:
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        user_name = st.session_state.user_data.get('name', 'Ahmet Yılmaz')
        
        # Marka Logosu
        st.markdown(f"""
            <div style="padding: 15px; background: rgba(255,255,255,0.03); border-radius: 12px; margin-bottom: 25px; border: 1px solid rgba(255,255,255,0.05);">
                <div style="display:flex; align-items:center; gap:10px;">
                    <div style="background:#2563EB; width:8px; height:8px; border-radius:50%;"></div>
                    <div style="font-weight: 800; font-size: 16px; color: #FFF; letter-spacing:1px;">{user_brand}</div>
                </div>
                <div style="font-size: 10px; color: #71717A; margin-left:18px; margin-top:4px;">ENTERPRISE OS v4.2</div>
            </div>
        """, unsafe_allow_html=True)

        # MENÜ SEÇENEKLERİ
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
        
        # Alt Kısım (Boşluk ve Profil)
        st.markdown("<div style='flex-grow: 1; height: 200px;'></div>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="padding: 12px; background: rgba(255,255,255,0.03); border-radius: 10px; border-top: 1px solid rgba(255,255,255,0.1); display:flex; align-items:center; gap:10px;">
                <div style="width:30px; height:30px; background:#27272A; border-radius:50%; display:flex; justify-content:center; align-items:center;">👤</div>
                <div>
                    <div style="font-size: 12px; font-weight: 600; color: #E4E4E7;">{user_name}</div>
                    <div style="font-size: 10px; color: #34D399;">● Çevrimiçi</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Çıkış Yap", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
        return selection

# --- 5. ANA UYGULAMA ---
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        # Menüyü çiz ve seçimi al
        page = render_sidebar()
        
        # Sayfaları Yükle
        if page == "Dashboard": dashboard.render_dashboard()
        elif page == "Lojistik": logistics.render_logistics()
        elif page == "Envanter": inventory.render_inventory()
        elif page == "Formlar": forms.render_forms()
        elif page == "Dokümanlar": documents.render_documents()
        elif page == "Yapılacaklar": todo.render_todo()
        elif page == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
