import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. DOSYA YOLLARI
# ==============================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

# ==============================================================================
# ⚙️ 2. SAYFA AYARLARI (KRİTİK DÜZELTME: EXPANDED)
# ==============================================================================
st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded", # <-- BURAYI "expanded" YAPTIK, ARTIK AÇIK BAŞLAYACAK
    menu_items={'About': "Powered by Artificial Staff"}
)

# ==============================================================================
# 🛠️ 3. CSS: BUTONU ZORLA GÖRÜNÜR YAPMA
# ==============================================================================
st.markdown("""
<style>
    /* Header'ı Şeffaf Yap ama Tıklamaya İzin Ver */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
    }

    /* SOL ÜSTTEKİ OK İŞARETİNİ (BUTONU) ZORLA, EN ÜSTE KOY */
    button[data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        z-index: 9999999 !important; /* En üst katman */
        
        /* Görünüm: Parlak Mavi Kutu */
        background-color: #2563EB !important;
        color: white !important;
        width: 45px !important;
        height: 45px !important;
        border-radius: 8px !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.8) !important;
        
        /* Etkileşim */
        pointer-events: auto !important; 
        cursor: pointer !important;
    }

    /* İkonu Beyaz Yap */
    button[data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
    }

    /* Hover Efekti */
    button[data-testid="stSidebarCollapsedControl"]:hover {
        background-color: #3B82F6 !important;
        transform: scale(1.1) !important;
    }

    /* Sidebar Arka Planı */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 📦 4. MODÜLLER
# ==============================================================================
try:
    import styles
    from views import login, dashboard, logistics, inventory, plan, documents, todo, forms
except ImportError as e:
    st.error(f"⚠️ Hata: {e}")
    st.stop()

# ==============================================================================
# 🚀 5. UYGULAMA MANTIĞI
# ==============================================================================
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}
if "nav_selection" not in st.session_state: st.session_state.nav_selection = "Dashboard"

def render_sidebar():
    with st.sidebar:
        user = st.session_state.user_data
        st.markdown(textwrap.dedent(f"""
            <div style="padding:15px; margin-bottom:20px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid rgba(255,255,255,0.05); display:flex; gap:10px; align-items:center;">
                <div style="width:32px; height:32px; background:linear-gradient(135deg, #8B5CF6, #3B82F6); border-radius:6px; display:flex; justify-content:center; align-items:center;"><i class='bx bxs-command'></i></div>
                <div><div style="font-weight:bold; font-size:14px;">{user.get('brand', 'ARTIS')}</div><div style="font-size:10px; color:#34D399;">● Enterprise</div></div>
            </div>
        """), unsafe_allow_html=True)

        opts = {
            "Dashboard": "📊 Dashboard", "Lojistik": "📦 Lojistik", 
            "Envanter": "📋 Envanter", "Formlar": "📝 Formlar", 
            "Dokümanlar": "📂 Dokümanlar", "Yapılacaklar": "✅ Yapılacaklar", 
            "Planlar": "💎 Planlar"
        }
        
        selection = st.radio("Menü", list(opts.keys()), format_func=lambda x: opts[x], label_visibility="collapsed", key="sb_radio")
        
        if selection != st.session_state.nav_selection:
            st.session_state.nav_selection = selection
            st.rerun()

        st.markdown("<div style='flex-grow:1; min-height:100px;'></div>", unsafe_allow_html=True)
        if st.button("Çıkış Yap", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        render_sidebar()
        
        sel = st.session_state.nav_selection
        
        # --- ACİL DURUM MENÜSÜ (ARTIK HER SAYFADA GÖRÜNÜR) ---
        # Sidebar bozulsa bile buradan gezebilirsin.
        st.markdown("""
        <style>div.stButton > button {width: 100%; border-radius: 8px;}</style>
        """, unsafe_allow_html=True)
        
        # Sadece Dashboard'da değil, HER YERDE bu butonları göster (Toggle ile)
        with st.expander("🚀 HIZLI GEÇİŞ MENÜSÜ (Yedek)", expanded=False):
            c1,c2,c3,c4,c5,c6,c7 = st.columns(7)
            if c1.button("📊 Dash"): st.session_state.nav_selection="Dashboard"; st.rerun()
            if c2.button("📦 Lojistik"): st.session_state.nav_selection="Lojistik"; st.rerun()
            if c3.button("📋 Envanter"): st.session_state.nav_selection="Envanter"; st.rerun()
            if c4.button("📝 Formlar"): st.session_state.nav_selection="Formlar"; st.rerun()
            if c5.button("📂 Dosyalar"): st.session_state.nav_selection="Dokümanlar"; st.rerun()
            if c6.button("✅ İşler"): st.session_state.nav_selection="Yapılacaklar"; st.rerun()
            if c7.button("💎 Plan"): st.session_state.nav_selection="Planlar"; st.rerun()

        # Sayfaları Render Et
        if sel == "Dashboard": dashboard.render_dashboard()
        elif sel == "Lojistik": logistics.render_logistics()
        elif sel == "Envanter": inventory.render_inventory()
        elif sel == "Formlar": forms.render_forms()
        elif sel == "Dokümanlar": documents.render_documents()
        elif sel == "Yapılacaklar": todo.render_todo()
        elif sel == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
