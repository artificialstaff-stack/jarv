import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. SİSTEM KONFİGÜRASYONU
# ==============================================================================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': "# ARTIS OS v4.2\nPowered by Artificial Staff"}
)

# ==============================================================================
# 🛠️ 2. CSS "ZORLA GÖRÜNÜR YAPMA" YAMASI
# ==============================================================================
st.markdown("""
<style>
    /* 1. Header'ı Tamamen Tıklanamaz Yap (Arka plana düşsün) */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
        height: 0 !important; /* Yüksekliği sıfırla ki yer kaplamasın */
    }

    /* 2. Sidebar AÇMA Butonunu (Ok İşareti) Zorla Yakala ve En Üste Çivile */
    button[data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        
        /* KONUMLANDIRMA: Sayfanın Sol Üstüne Çiviliyoruz */
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        z-index: 9999999 !important; /* Diğer her şeyin en üstünde olsun */
        
        /* GÖRÜNÜM: Parlak Mavi Kutu */
        background-color: #3B82F6 !important; 
        width: 45px !important;
        height: 45px !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
        
        /* ETKİLEŞİM */
        pointer-events: auto !important; /* Tıklanabilir olsun */
        cursor: pointer !important;
        transition: transform 0.2s ease !important;
    }

    /* İkon Rengini Beyaz Yap */
    button[data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
        width: 24px !important;
        height: 24px !important;
    }

    /* Hover (Üzerine Gelince) */
    button[data-testid="stSidebarCollapsedControl"]:hover {
        transform: scale(1.1) !important;
        background-color: #2563EB !important;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.8) !important;
    }

    /* 3. Streamlit Toolbar (Sağ Üstteki 3 Nokta) */
    div[data-testid="stToolbar"] {
        top: 20px !important;
        right: 20px !important;
        pointer-events: auto !important;
        z-index: 9999998 !important;
    }

    /* 4. Sidebar Kapalıyken Çıkan Çizgiyi Yok Et */
    div[data-testid="stDecoration"] { display: none !important; }
    
    /* 5. Sidebar Görünümü */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 📦 3. MODÜL YÜKLEME
# ==============================================================================
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

# ==============================================================================
# 🚀 4. UYGULAMA MANTIĞI
# ==============================================================================
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

def render_sidebar():
    with st.sidebar:
        # MARKA HEADER
        user = st.session_state.user_data
        
        st.markdown(textwrap.dedent(f"""
            <div style="margin-top:20px; margin-bottom:20px; padding:12px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid rgba(255,255,255,0.05);">
                <div style="display:flex; gap:10px; align-items:center;">
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

        # NAVIGASYON
        opts = {
            "Dashboard": "📊 Dashboard", "Lojistik": "📦 Lojistik", 
            "Envanter": "📋 Envanter", "Formlar": "📝 Formlar", 
            "Dokümanlar": "📂 Dokümanlar", "Yapılacaklar": "✅ Yapılacaklar", 
            "Planlar": "💎 Planlar"
        }
        sel = st.radio("NAV", list(opts.keys()), format_func=lambda x: opts[x], label_visibility="collapsed")
        
        # PROFIL
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
        sel = render_sidebar()
        if sel == "Dashboard": dashboard.render_dashboard()
        elif sel == "Lojistik": logistics.render_logistics()
        elif sel == "Envanter": inventory.render_inventory()
        elif sel == "Formlar": forms.render_forms()
        elif sel == "Dokümanlar": documents.render_documents()
        elif sel == "Yapılacaklar": todo.render_todo()
        elif sel == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
