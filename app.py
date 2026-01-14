import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. DOSYA YOLLARI (HATA ALMAMAN İÇİN)
# ==============================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'views'))
sys.path.append(os.path.join(current_dir, 'logic'))

# Sayfa Ayarları
st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed", # Başlangıçta KAPALI olsun ki butonu test edebil
    menu_items={'About': "Powered by Artificial Staff"}
)

# ==============================================================================
# 🛠️ 2. CSS: "KAMUFLAJ STRATEJİSİ"
# ==============================================================================
st.markdown("""
<style>
    /* 1. Header'ı YOK ETME, Sadece Arka Planını Siyah Yap (Kamuflaj) */
    header[data-testid="stHeader"] {
        background-color: #000000 !important; /* Arka planla aynı renk */
        height: 60px !important; /* Butonun sığacağı kadar alan bırak */
        z-index: 999 !important;
    }

    /* 2. Renkli Çizgiyi Kaldır (Header'ın üstündeki çizgi) */
    div[data-testid="stDecoration"] {
        display: none !important;
    }

    /* 3. SIDEBAR AÇMA BUTONUNU (OK İŞARETİ) ÖZELLEŞTİR */
    button[data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        
        /* Rengi ve Görünümü */
        color: #FFFFFF !important;
        background-color: #2563EB !important; /* Mavi Buton */
        border: 1px solid rgba(255,255,255,0.3) !important;
        border-radius: 8px !important;
        
        /* Boyut */
        width: 40px !important;
        height: 40px !important;
        margin-top: 5px !important;
        
        /* Efektler */
        box-shadow: 0 0 10px rgba(37, 99, 235, 0.8) !important;
        transition: transform 0.2s !important;
    }

    /* Butonun üzerine gelince büyüteç etkisi */
    button[data-testid="stSidebarCollapsedControl"]:hover {
        transform: scale(1.15) !important;
        background-color: #3B82F6 !important;
    }

    /* 4. EKSTRA GÜVENLİK: Sol Kenara Görünmez Tetikleyici */
    /* Sol kenardaki 20 piksellik alana fare gelirse buton parlasın */
    div[data-testid="stSidebarCollapsedControl"]::before {
        content: "";
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        width: 15px; 
        z-index: 998;
    }

    /* 5. Sidebar Görünümü */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* 6. Ana İçeriği Biraz Aşağı İt (Header altında kalmasın) */
    .block-container {
        padding-top: 80px !important;
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
    st.error(f"⚠️ HATA: Dosyalar bulunamadı ({e}). Lütfen dosya yapısını kontrol et.")
    st.stop()

# ==============================================================================
# 🚀 4. UYGULAMA MANTIĞI
# ==============================================================================
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}
if "nav_selection" not in st.session_state: st.session_state.nav_selection = "Dashboard"

def render_sidebar():
    with st.sidebar:
        # MARKA
        user = st.session_state.user_data
        st.markdown(textwrap.dedent(f"""
            <div style="padding:15px; margin-bottom:20px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid rgba(255,255,255,0.05); display:flex; gap:10px; align-items:center;">
                <div style="width:32px; height:32px; background:linear-gradient(135deg, #8B5CF6, #3B82F6); border-radius:6px; display:flex; justify-content:center; align-items:center;"><i class='bx bxs-command'></i></div>
                <div><div style="font-weight:bold; font-size:14px;">{user.get('brand', 'ARTIS')}</div><div style="font-size:10px; color:#34D399;">● Enterprise</div></div>
            </div>
        """), unsafe_allow_html=True)

        # MENÜ
        opts = {
            "Dashboard": "📊 Dashboard", "Lojistik": "📦 Lojistik", 
            "Envanter": "📋 Envanter", "Formlar": "📝 Formlar", 
            "Dokümanlar": "📂 Dokümanlar", "Yapılacaklar": "✅ Yapılacaklar", 
            "Planlar": "💎 Planlar"
        }
        
        # Radio button state ile senkronize çalışır
        selection = st.radio("Menü", list(opts.keys()), format_func=lambda x: opts[x], label_visibility="collapsed", key="sb_radio")
        
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
        render_sidebar()
        
        # Seçili sayfayı al
        sel = st.session_state.nav_selection
        
        # --- YEDEK NAVİGASYON (ÜST BAR) ---
        # Eğer sidebar yine açılmazsa, kullanıcı buradan gezebilsin diye
        if sel != "Dashboard": # Dashboard'da gösterme, temiz kalsın
            with st.expander("Gezinti Menüsü (Yedek)", expanded=False):
                c1,c2,c3,c4,c5,c6,c7 = st.columns(7)
                if c1.button("📊", help="Dashboard"): st.session_state.nav_selection="Dashboard"; st.rerun()
                if c2.button("📦", help="Lojistik"): st.session_state.nav_selection="Lojistik"; st.rerun()
                if c3.button("📋", help="Envanter"): st.session_state.nav_selection="Envanter"; st.rerun()
                if c4.button("📝", help="Formlar"): st.session_state.nav_selection="Formlar"; st.rerun()
                if c5.button("📂", help="Dokümanlar"): st.session_state.nav_selection="Dokümanlar"; st.rerun()
                if c6.button("✅", help="Yapılacaklar"): st.session_state.nav_selection="Yapılacaklar"; st.rerun()
                if c7.button("💎", help="Planlar"): st.session_state.nav_selection="Planlar"; st.rerun()

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
