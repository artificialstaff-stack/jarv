import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. SİSTEM AYARLARI
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
# 🛠️ 2. CSS "KURTARMA OPERASYONU" (SIDEBAR BUTONU FIX)
# ==============================================================================
# Bu CSS bloğu, sidebar kapandığında açma butonunu zorla görünür kılar.
# Butonu sayfanın sol üstüne 'fixed' olarak çivileriz.
st.markdown("""
<style>
    /* 1. Header'ı Gizle (Renkli çizgi vs. gitsin) */
    header[data-testid="stHeader"] {
        background: transparent !important;
        height: 0px !important; /* Yüksekliği sıfırla */
    }

    /* 2. Sidebar Açma Butonunu (Ok İşareti) Zorla Konumlandır */
    [data-testid="stSidebarCollapsedControl"] {
        display: block !important;
        visibility: visible !important;
        position: fixed !important; /* Sayfaya çivile */
        top: 20px !important;
        left: 20px !important;
        z-index: 1000001 !important; /* Her şeyin üstünde */
        
        /* Görünürlük Stili */
        background-color: #18181B !important;
        color: #FFFFFF !important;
        border: 1px solid #3F3F46 !important;
        padding: 8px !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }

    /* Hover Efekti */
    [data-testid="stSidebarCollapsedControl"]:hover {
        background-color: #3B82F6 !important; /* Mavi Yanar */
        border-color: #3B82F6 !important;
        transform: scale(1.1);
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
    }
    
    /* 3. Sağ Üstteki Menüyü (3 Nokta) Ayarla */
    div[data-testid="stToolbar"] {
        right: 2rem;
        top: 1rem;
        visibility: visible !important;
        z-index: 1000000 !important;
    }

    /* 4. Native Sidebar Navigasyonunu Gizle */
    div[data-testid="stSidebarNav"] { display: none; }
    
    /* 5. Sidebar Arka Plan Rengi */
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
    st.error(f"⚠️ Kritik Hata: Modüller yüklenemedi.\nDetay: {e}")
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
            <div style="margin-top: 10px; margin-bottom: 25px; padding: 12px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #8B5CF6 0%, #3B82F6 100%); border-radius: 8px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.25);">
                        <i class='bx bxs-command' style="color: white; font-size: 20px;"></i>
                    </div>
                    <div>
                        <div style="font-weight: 800; font-size: 15px; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 170px;">
                            {user_brand}
                        </div>
                        <div style="font-size: 10px; color: #34D399; font-weight: 600; text-transform: uppercase;">
                            ● {user_plan} Edition
                        </div>
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
        st.markdown("<div style='flex-grow: 1; min-height: 200px;'></div>", unsafe_allow_html=True)
        user_name = st.session_state.user_data.get('name', 'Kullanıcı')
        
        st.markdown(textwrap.dedent(f"""
            <div style="padding: 15px; background: rgba(255,255,255,0.03); border-radius: 12px; display: flex; align-items: center; gap: 12px; border-top: 1px solid rgba(255,255,255,0.08);">
                <div style="width: 34px; height: 34px; background: #27272A; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #FFF; font-weight: 700;">
                    {user_name[0]}
                </div>
                <div>
                    <div style="font-size: 13px; font-weight: 600; color: #E4E4E7;">{user_name}</div>
                    <div style="font-size: 10px; color: #71717A;">Çevrimiçi</div>
                </div>
            </div>
        """), unsafe_allow_html=True)
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
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
