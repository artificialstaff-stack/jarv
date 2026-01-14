import streamlit as st
import sys
import os
import textwrap

# --- 1. SİSTEM YOLLARI ---
# Views ve Logic klasörlerini Python'a tanıtıyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

# 2. SAYFA AYARLARI (Sidebar her zaman açık başlasın)
st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# 3. KESİN ÇÖZÜM CSS: SIDEBAR'I KİLİTLE VE MENÜYÜ GÜZELLEŞTİR
st.markdown("""
<style>
    /* Sidebar içindeki kapatma 'X' butonunu ve üstteki '>' butonunu tamamen yok et */
    [data-testid="stSidebar"] button { display: none !important; }
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    
    /* Sidebar genişliğini sabitle (Kapanmasını engelle) */
    [data-testid="stSidebar"] {
        min-width: 280px !important;
        max-width: 280px !important;
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }

    /* Menü butonlarını (st.radio) özelleştir */
    .st-emotion-cache-6qob1r { font-weight: 600 !important; color: #FAFAFA !important; }
    
    header[data-testid="stHeader"] { background: transparent !important; }
</style>
""", unsafe_allow_html=True)

# 4. MODÜLLERİ YÜKLE
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

# Stilleri Yükle
styles.load_css()

# Session State Başlat
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

# 5. SOL MENÜ BİLEŞENİ (SAYFALAR BURADA)
def render_sidebar():
    with st.sidebar:
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        user_name = st.session_state.user_data.get('name', 'Ahmet Yılmaz')
        
        # Marka Logosu ve Başlık
        st.markdown(f"""
            <div style="padding: 10px; background: rgba(255,255,255,0.03); border-radius: 12px; margin-bottom: 20px;">
                <div style="font-weight: 800; font-size: 18px; color: #FFF;">⚡ {user_brand}</div>
                <div style="font-size: 10px; color: #34D399; font-weight: 600;">● ENTERPRISE EDITION</div>
            </div>
        """, unsafe_allow_html=True)

        # SAYFA GEÇİŞ BUTONLARI
        # Burası senin sayfalar arasında gezmeni sağlayacak ana menü
        menu_options = {
            "Dashboard": "📊 Dashboard",
            "Lojistik": "📦 Lojistik",
            "Envanter": "📋 Envanter",
            "Formlar": "📝 Formlar",
            "Dokümanlar": "📂 Dokümanlar",
            "Yapılacaklar": "✅ Yapılacaklar",
            "Planlar": "💎 Planlar"
        }
        
        selected_page = st.radio(
            "NAVİGASYON",
            list(menu_options.keys()),
            format_func=lambda x: menu_options[x],
            label_visibility="collapsed"
        )
        
        st.markdown("<div style='flex-grow: 1; height: 150px;'></div>", unsafe_allow_html=True)
        
        # Kullanıcı Kartı
        st.markdown(f"""
            <div style="padding: 15px; background: rgba(255,255,255,0.03); border-radius: 12px; border-top: 1px solid rgba(255,255,255,0.1);">
                <div style="font-size: 13px; font-weight: 600; color: #E4E4E7;">{user_name}</div>
                <div style="font-size: 10px; color: #71717A;">Çevrimiçi</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Çıkış Yap", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
        return selected_page

# 6. ANA YÖNLENDİRİCİ (ROUTING)
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        # Sidebar'ı çiz ve seçilen sayfayı al
        page = render_sidebar()
        
        # Seçilen sayfaya göre ilgili dosyayı çalıştır
        if page == "Dashboard":
            dashboard.render_dashboard()
        elif page == "Lojistik":
            logistics.render_logistics()
        elif page == "Envanter":
            inventory.render_inventory()
        elif page == "Formlar":
            forms.render_forms()
        elif page == "Dokümanlar":
            documents.render_documents()
        elif page == "Yapılacaklar":
            todo.render_todo()
        elif page == "Planlar":
            plan.render_plans()

if __name__ == "__main__":
    main()
