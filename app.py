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
    initial_sidebar_state="expanded", # Başlangıçta menü açık olsun
    menu_items={'About': "Powered by Artificial Staff"}
)

# ==============================================================================
# 🛠️ 2. CSS: MENÜ BUTONUNU ZORLA GERİ GETİRME
# ==============================================================================
st.markdown("""
<style>
    /* 1. Header'ı GİZLEME, Sadece Arka Planını Sil */
    header[data-testid="stHeader"] {
        background: transparent !important;
        /* pointer-events: none;  <-- BU SATIRI KALDIRDIM, TIKLAMAYI ENGELLİYORDU */
    }

    /* 2. Sidebar AÇMA Butonunu (Ok İşareti) Canlandır */
    [data-testid="stSidebarCollapsedControl"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        color: white !important;
        background-color: #2563EB !important; /* Mavi Arka Plan */
        
        /* Butonu Biraz Büyüt ve Konumlandır */
        transform: scale(1.2);
        margin-top: 10px;
        margin-left: 10px;
        border-radius: 8px;
        padding: 5px;
        border: 1px solid rgba(255,255,255,0.2);
        z-index: 9999999 !important; /* En üstte dur */
    }

    /* Butonun içindeki ok işaretini belirginleştir */
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
        stroke-width: 2px !important;
    }
    
    /* 3. Menü Arka Planı */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* 4. Sayfa İçeriğini Biraz Aşağı İt (Header altında kalmasın) */
    .block-container {
        padding-top: 60px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 📦 3. MODÜLLERİ YÜKLE
# ==============================================================================
try:
    import styles
    from views import login, dashboard, logistics, inventory, plan, documents, todo, forms
except ImportError as e:
    st.error(f"⚠️ Modül Hatası: {e}")
    st.stop()

# ==============================================================================
# 🚀 4. UYGULAMA MANTIĞI
# ==============================================================================
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}
if "nav_selection" not in st.session_state: st.session_state.nav_selection = "Dashboard"

def navigate_to(page):
    st.session_state.nav_selection = page
    st.rerun()

def render_fallback_nav():
    """
    Eğer sidebar bozulursa diye sayfanın en üstüne acil durum menüsü koyar.
    """
    st.markdown("#### 🚀 Hızlı Menü (Yedek)")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    if col1.button("📊 Dashboard", use_container_width=True): navigate_to("Dashboard")
    if col2.button("📦 Lojistik", use_container_width=True): navigate_to("Lojistik")
    if col3.button("📋 Envanter", use_container_width=True): navigate_to("Envanter")
    if col4.button("📝 Formlar", use_container_width=True): navigate_to("Formlar")
    if col5.button("💎 Planlar", use_container_width=True): navigate_to("Planlar")
    st.divider()

def render_sidebar():
    with st.sidebar:
        # Marka
        user = st.session_state.user_data
        st.markdown(textwrap.dedent(f"""
            <div style="padding:15px; margin-bottom:20px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid rgba(255,255,255,0.05); display:flex; gap:10px; align-items:center;">
                <div style="width:32px; height:32px; background:linear-gradient(135deg, #8B5CF6, #3B82F6); border-radius:6px; display:flex; justify-content:center; align-items:center;"><i class='bx bxs-command'></i></div>
                <div><div style="font-weight:bold; font-size:14px;">{user.get('brand', 'ARTIS')}</div><div style="font-size:10px; color:#34D399;">● Enterprise</div></div>
            </div>
        """), unsafe_allow_html=True)

        # Menü Butonları (Radio yerine Button kullanarak daha sağlam yapı)
        opts = {
            "Dashboard": "📊 Dashboard", "Lojistik": "📦 Lojistik", 
            "Envanter": "📋 Envanter", "Formlar": "📝 Formlar", 
            "Dokümanlar": "📂 Dokümanlar", "Yapılacaklar": "✅ Yapılacaklar", 
            "Planlar": "💎 Planlar"
        }
        
        selection = st.radio("Menü", list(opts.keys()), format_func=lambda x: opts[x], label_visibility="collapsed", key="sb_radio")
        
        # Eğer sidebar'dan seçim yapılırsa state'i güncelle
        if selection != st.session_state.nav_selection:
            st.session_state.nav_selection = selection
            st.rerun()

        # Profil
        st.markdown("<div style='flex-grow:1; min-height:100px;'></div>", unsafe_allow_html=True)
        if st.button("Çıkış Yap", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        # Sidebar'ı oluştur
        render_sidebar()
        
        # Seçili sayfayı al
        sel = st.session_state.nav_selection
        
        # --- ACİL DURUM MENÜSÜ ---
        # Eğer sidebar görünmüyorsa buradan geçiş yapabilsin diye
        if sel == "Dashboard":
            # Dashboard'un içine yedek navigasyon koymuyorum, temiz kalsın.
            dashboard.render_dashboard()
        else:
            # Diğer sayfalarda en üstte yedek menü dursun
            # render_fallback_nav() 
            pass

        if sel == "Lojistik": logistics.render_logistics()
        elif sel == "Envanter": inventory.render_inventory()
        elif sel == "Formlar": forms.render_forms()
        elif sel == "Dokümanlar": documents.render_documents()
        elif sel == "Yapılacaklar": todo.render_todo()
        elif sel == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
