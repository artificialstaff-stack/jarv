import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. DOSYA YOLLARI & SİSTEM AYARLARI (CRITICAL FIX)
# ==============================================================================
# Python'un "views" klasörünü görmesi için bulunduğu dizini ekliyoruz
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

# Sayfa Ayarları
st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded", # Varsayılan olarak AÇIK başla
    menu_items={'About': "Powered by Artificial Staff"}
)

# ==============================================================================
# 🛠️ 2. CSS: "ÇOKLU BUTON SİSTEMİ" (MULTI-TRIGGER)
# ==============================================================================
st.markdown("""
<style>
    /* 1. Header'ı Tamamen Pasifize Et (Tıklamalar Alta Geçsin) */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
        height: 0px !important;
        z-index: 0 !important;
    }

    /* ==================================================================
       BÜYÜK BUTON (TRIGGER 1) - Sol Üstte "MENÜ" Yazan Mavi Buton
       ================================================================== */
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        visibility: visible !important;
        opacity: 1 !important;
        
        /* KONUM VE BOYUT */
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        width: 120px !important; /* Geniş buton */
        height: 45px !important;
        z-index: 9999999 !important; /* Her şeyin üstünde */
        
        /* GÖRÜNÜM */
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.6) !important;
        
        /* ETKİLEŞİM */
        pointer-events: auto !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
    }

    /* Butonun Üzerine "MENÜ AÇ" Yazısı Ekliyoruz (CSS Hack) */
    [data-testid="stSidebarCollapsedControl"]::after {
        content: "MENÜ AÇ";
        color: white;
        font-weight: 800;
        font-size: 14px;
        margin-left: 8px;
        letter-spacing: 1px;
    }

    /* Orijinal Oku Beyaz Yap */
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
        width: 20px !important;
        height: 20px !important;
    }

    /* Hover Efekti */
    [data-testid="stSidebarCollapsedControl"]:hover {
        transform: scale(1.05) !important;
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%) !important;
        box-shadow: 0 0 30px rgba(59, 130, 246, 0.8) !important;
    }

    /* ==================================================================
       GİZLİ TETİKLEYİCİ (TRIGGER 2) - Sol Kenar Boyunca Görünmez Şerit
       ================================================================== */
    /* Kullanıcı fareyi sol kenara götürürse de açılsın diye ekstra alan */
    div[data-testid="stSidebarCollapsedControl"]::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 20px; /* Sol kenarda 20px'lik alan */
        height: 100vh; /* Tüm yükseklik */
        z-index: 9999998;
    }

    /* 3. Sağ Üst Menüyü (3 Nokta) Kurtar */
    div[data-testid="stToolbar"] {
        top: 20px !important;
        right: 20px !important;
        pointer-events: auto !important;
        z-index: 999999 !important;
    }

    /* 4. Sidebar Kapalıyken Çıkan Çizgiyi Yok Et */
    div[data-testid="stDecoration"] { display: none !important; }
    div[data-testid="stSidebarNav"] { display: none !important; }
    
    /* 5. Sidebar Tasarımı */
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
    st.error(f"⚠️ Modül Yükleme Hatası: `{e}`. Lütfen dosya yapısını kontrol edin.")
    st.stop()

# ==============================================================================
# 🚀 4. UYGULAMA MANTIĞI
# ==============================================================================
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

def render_sidebar():
    with st.sidebar:
        # A. MARKA
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        user_plan = st.session_state.user_data.get('plan', 'Enterprise')
        
        st.markdown(textwrap.dedent(f"""
            <div style="margin-top:10px; margin-bottom:25px; padding:12px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid rgba(255,255,255,0.05);">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div style="width:36px; height:36px; background:linear-gradient(135deg, #8B5CF6, #3B82F6); border-radius:8px; display:flex; justify-content:center; align-items:center;">
                        <i class='bx bxs-command' style="color:white; font-size:20px;"></i>
                    </div>
                    <div>
                        <div style="font-weight:800; font-size:15px; color:#FFF; white-space:nowrap;">{user_brand}</div>
                        <div style="font-size:10px; color:#34D399; font-weight:600; text-transform:uppercase;">● {user_plan}</div>
                    </div>
                </div>
            </div>
        """), unsafe_allow_html=True)

        # B. MENÜ
        opts = {
            "Dashboard": "📊 Dashboard", "Lojistik": "📦 Lojistik", 
            "Envanter": "📋 Envanter", "Formlar": "📝 Formlar", 
            "Dokümanlar": "📂 Dokümanlar", "Yapılacaklar": "✅ Yapılacaklar", 
            "Planlar": "💎 Planlar"
        }
        sel = st.radio("NAV", list(opts.keys()), format_func=lambda x: opts[x], label_visibility="collapsed")
        
        # C. PROFIL
        st.markdown("<div style='flex-grow:1; min-height:100px;'></div>", unsafe_allow_html=True)
        user_name = st.session_state.user_data.get('name', 'Kullanıcı')
        
        st.markdown(textwrap.dedent(f"""
            <div style="padding:15px; border-top:1px solid rgba(255,255,255,0.08); display:flex; align-items:center; gap:10px; background:rgba(255,255,255,0.02); border-radius:10px;">
                <div style="width:32px; height:32px; background:#27272A; border-radius:50%; display:flex; justify-content:center; align-items:center; color:#FFF; font-weight:bold;">
                    {user_name[0]}
                </div>
                <div>
                    <div style="font-size:13px; font-weight:600; color:#E4E4E7;">{user_name}</div>
                    <div style="font-size:10px; color:#71717A;">Çevrimiçi</div>
                </div>
            </div>
        """), unsafe_allow_html=True)
        
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        
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
