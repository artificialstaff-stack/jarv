import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. SİSTEM AYARLARI
# ==============================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': "Powered by Artificial Staff"}
)

# ==============================================================================
# 🛠️ 2. CSS YAMASI (BUTON KURTARMA OPERASYONU)
# ==============================================================================
st.markdown("""
<style>
    /* 1. Header'ı YOK ETME, Sadece Şeffaf Yap (Butonun yaşaması için şart!) */
    header[data-testid="stHeader"] {
        background: transparent !important;
        /* height: 0px !important;  <-- BU SATIRI SİLDİK, SORUN BUYDU */
    }

    /* 2. Sidebar Açma Butonunu (Ok İşareti) Özelleştir */
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        visibility: visible !important;
        
        /* Butonu Sayfaya Çivile (Fixed) */
        position: fixed !important;
        top: 24px !important;
        left: 24px !important;
        z-index: 9999999 !important; /* En üstte dur */
        
        /* Tasarım (Mavi Kutu) */
        background-color: #2563EB !important;
        color: white !important;
        width: 44px !important;
        height: 44px !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
        
        /* Tıklanabilirlik */
        pointer-events: auto !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
    }

    /* İkon Rengi */
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
        width: 24px !important;
        height: 24px !important;
    }

    /* Hover Efekti */
    [data-testid="stSidebarCollapsedControl"]:hover {
        background-color: #3B82F6 !important;
        transform: scale(1.1) !important;
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.8) !important;
    }

    /* 3. İKİNCİ GARANTİ: Sol Kenara Görünmez Bir Tıklama Alanı Koy */
    /* Sol kenara fare gelirse veya tıklanırsa butonun orada olduğunu hissettirir */
    div[data-testid="stSidebarCollapsedControl"]::before {
        content: "";
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        width: 10px; /* Sol kenarda 10px'lik şerit */
        z-index: 9999998;
    }

    /* 4. Diğer Gereksizleri Gizle */
    div[data-testid="stDecoration"] { display: none !important; }
    div[data-testid="stSidebarNav"] { display: none !important; }
    .stDeployButton { display: none !important; }

    /* 5. Sağ Üst Menü Ayarı */
    div[data-testid="stToolbar"] {
        top: 15px !important;
        right: 15px !important;
    }
    
    /* 6. Sidebar Arka Planı */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 📦 3. MODÜLLERİ YÜKLE
# ==============================================================================
try:
    import styles
    from views import login
    from views import dashboard
    from views import logistics
    from views import inventory
    from views import plan
    from views import documents
    from views import todo
    from views import forms
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
        user = st.session_state.user_data
        
        # Marka Header
        st.markdown(textwrap.dedent(f"""
            <div style="margin-top:20px; margin-bottom:25px; padding:12px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid rgba(255,255,255,0.05);">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div style="width:36px; height:36px; background:linear-gradient(135deg, #8B5CF6, #3B82F6); border-radius:8px; display:flex; justify-content:center; align-items:center; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.25);">
                        <i class='bx bxs-command' style="color:white; font-size:20px;"></i>
                    </div>
                    <div>
                        <div style="font-weight:800; font-size:15px; color:#FFF;">{user.get('brand', 'ARTIS')}</div>
                        <div style="font-size:10px; color:#34D399; font-weight:600;">● {user.get('plan', 'Pro')}</div>
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
        st.markdown("<div style='flex-grow:1; min-height:100px;'></div>", unsafe_allow_html=True)
        st.markdown(textwrap.dedent(f"""
            <div style="padding:12px; background:rgba(255,255,255,0.02); border-radius:10px; border-top:1px solid rgba(255,255,255,0.08); display:flex; align-items:center; gap:10px;">
                <div style="width:32px; height:32px; background:#27272A; border-radius:50%; display:flex; justify-content:center; align-items:center; color:#FFF; font-weight:bold;">
                    {user.get('name', 'U')[0]}
                </div>
                <div>
                    <div style="font-size:13px; font-weight:600; color:#E4E4E7;">{user.get('name', 'User')}</div>
                    <div style="font-size:10px; color:#71717A;">Çevrimiçi</div>
                </div>
            </div>
        """), unsafe_allow_html=True)
        
        if st.button("Güvenli Çıkış", use_container_width=True):
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
