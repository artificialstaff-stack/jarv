import streamlit as st
import sys
import os
import time
import textwrap

# 1. AYARLAR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

st.set_page_config(
    page_title="ARTIS OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded" # Sidebar varsayılan olarak açık başlar
)

# 2. KRİTİK CSS YAMASI (BUTON İÇİN)
st.markdown("""
<style>
    /* 1. Header'ı GİZLEME, Sadece Şeffaf Yap (Butonun yaşaması için) */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        pointer-events: none !important; /* Tıklamaları alta geçir */
    }

    /* 2. Sidebar Açma Butonunu ( > ) Yakala ve Yeniden Tasarla */
    [data-testid="stSidebarCollapsedControl"] {
        display: block !important;
        position: fixed !important; /* Ekrana Sabitle */
        top: 20px !important;
        left: 20px !important;
        z-index: 999999 !important;
        
        /* Görünürlük */
        background-color: #3B82F6 !important; /* Parlak Mavi */
        color: white !important;
        border-radius: 8px !important;
        padding: 8px !important;
        width: 40px !important;
        height: 40px !important;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.5) !important;
        
        /* Etkileşim */
        pointer-events: auto !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
    }

    /* Buton Hover Efekti */
    [data-testid="stSidebarCollapsedControl"]:hover {
        transform: scale(1.1) !important;
        background-color: #2563EB !important;
        box-shadow: 0 0 30px rgba(59, 130, 246, 0.8) !important;
    }

    /* 3. İkon Rengini Beyaz Yap */
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
    }

    /* 4. Sidebar Açıkken Kapatma Butonu (X) */
    button[kind="header"] {
        color: white !important; 
        pointer-events: auto !important;
    }

    /* 5. Dekorasyon Çizgisini Kaldır */
    div[data-testid="stDecoration"] { display: none; }
    
    /* 6. Sidebar Stili */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 3. MODÜLLERİ YÜKLE
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
    st.error(f"Sistem Hatası: {e}")
    st.stop()

# 4. APP MANTIĞI
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

def render_sidebar():
    with st.sidebar:
        user = st.session_state.user_data
        
        # Marka Header
        st.markdown(textwrap.dedent(f"""
            <div style="padding:15px; margin-bottom:20px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid rgba(255,255,255,0.05);">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div style="width:36px; height:36px; background:linear-gradient(135deg, #8B5CF6, #3B82F6); border-radius:8px; display:flex; justify-content:center; align-items:center;">
                        <i class='bx bxs-command' style="color:white; font-size:20px;"></i>
                    </div>
                    <div>
                        <div style="font-weight:800; font-size:15px; color:#FFF;">{user.get('brand', 'ARTIS')}</div>
                        <div style="font-size:10px; color:#34D399;">● {user.get('plan', 'Pro')}</div>
                    </div>
                </div>
            </div>
        """), unsafe_allow_html=True)

        # Navigasyon
        opts = {
            "Dashboard": "📊 Dashboard", "Lojistik": "📦 Lojistik", 
            "Envanter": "📋 Envanter", "Formlar": "📝 Formlar", 
            "Dokümanlar": "📂 Dokümanlar", "Yapılacaklar": "✅ Yapılacaklar", 
            "Planlar": "💎 Planlar"
        }
        sel = st.radio("NAV", list(opts.keys()), format_func=lambda x: opts[x], label_visibility="collapsed")
        
        # Profil
        st.markdown("<div style='flex-grow:1; min-height:150px;'></div>", unsafe_allow_html=True)
        st.markdown(textwrap.dedent(f"""
            <div style="padding:15px; border-top:1px solid rgba(255,255,255,0.1); display:flex; align-items:center; gap:10px;">
                <div style="width:32px; height:32px; background:#27272A; border-radius:50%; display:flex; justify-content:center; align-items:center; color:#FFF; font-weight:bold;">
                    {user.get('name', 'U')[0]}
                </div>
                <div style="font-size:13px; color:#E4E4E7;">{user.get('name', 'User')}</div>
            </div>
        """), unsafe_allow_html=True)
        
        if st.button("Çıkış Yap", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
        return sel

def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        selection = render_sidebar()
        if selection == "Dashboard": dashboard.render_dashboard()
        elif selection == "Lojistik": logistics.render_logistics()
        elif selection == "Envanter": inventory.render_inventory()
        elif selection == "Formlar": forms.render_forms()
        elif selection == "Dokümanlar": documents.render_documents()
        elif selection == "Yapılacaklar": todo.render_todo()
        elif selection == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
