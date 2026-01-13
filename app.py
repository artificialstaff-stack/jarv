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
# 🛠️ 2. CSS FIX (SIDEBAR & HEADER)
# ==============================================================================
st.markdown("""
<style>
    /* Header'ı Şeffaf Yap (Buton Kaybolmasın Diye) */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        z-index: 99 !important;
    }
    
    /* Sidebar Toggle Butonunu Görünür Yap */
    button[kind="header"] {
        background-color: rgba(0,0,0,0.5) !important;
        color: #FFF !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }
    button[kind="header"]:hover {
        background-color: #3B82F6 !important;
        color: white !important;
    }

    /* Üst Çizgiyi Kaldır */
    div[data-testid="stDecoration"] { display: none; }
    
    /* Native Menüyü Gizle */
    div[data-testid="stSidebarNav"] { display: none; }
    
    /* Sidebar Arka Planı */
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
    import login  # Login dosyasının views/login.py olduğundan emin ol
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

# ==============================================================================
# 🚀 4. UYGULAMA MANTIĞI
# ==============================================================================
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

def render_sidebar():
    with st.sidebar:
        # MARKA ALANI
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        user_plan = st.session_state.user_data.get('plan', 'Enterprise')
        
        st.markdown(textwrap.dedent(f"""
            <div style="margin-top:20px; margin-bottom:20px; padding:12px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid rgba(255,255,255,0.05);">
                <div style="display:flex; gap:10px; align-items:center;">
                    <div style="width:32px; height:32px; background:linear-gradient(135deg, #8B5CF6, #3B82F6); border-radius:8px; display:flex; justify-content:center; align-items:center;">
                        <i class='bx bxs-command' style="color:white;"></i>
                    </div>
                    <div>
                        <div style="font-weight:700; font-size:14px; color:#FFF;">{user_brand}</div>
                        <div style="font-size:10px; color:#34D399;">● {user_plan}</div>
                    </div>
                </div>
            </div>
        """), unsafe_allow_html=True)

        # MENÜ
        opts = {
            "Dashboard": "📊 Dashboard",
            "Lojistik": "📦 Lojistik",
            "Envanter": "📋 Envanter",
            "Formlar": "📝 Formlar",
            "Dokümanlar": "📂 Dokümanlar",
            "Yapılacaklar": "✅ Yapılacaklar",
            "Planlar": "💎 Planlar"
        }
        selection = st.radio("NAV", list(opts.keys()), format_func=lambda x: opts[x], label_visibility="collapsed")
        
        # PROFIL ALANI
        st.markdown("<div style='flex-grow:1; min-height:100px;'></div>", unsafe_allow_html=True)
        user_name = st.session_state.user_data.get('name', 'Kullanıcı')
        
        st.markdown(textwrap.dedent(f"""
            <div style="padding:15px; background:rgba(255,255,255,0.03); border-radius:12px; display:flex; gap:10px; align-items:center; border-top:1px solid rgba(255,255,255,0.08);">
                <div style="width:32px; height:32px; background:#27272A; border-radius:50%; display:flex; justify-content:center; align-items:center; color:#FFF; font-weight:bold;">
                    {user_name[0]}
                </div>
                <div>
                    <div style="font-size:13px; font-weight:600; color:#FFF;">{user_name}</div>
                    <div style="font-size:10px; color:#71717A;">Çevrimiçi</div>
                </div>
            </div>
        """), unsafe_allow_html=True)
        
        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
        if st.button("Güvenli Çıkış", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
        return selection

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
