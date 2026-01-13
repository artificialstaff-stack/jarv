import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. SİSTEM KONFİGÜRASYONU (EN ÜSTTE OLMALI)
# ==============================================================================
# Modül yollarını dinamik olarak ekle (Her ortamda çalışması için)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

# Sayfa Ayarları
st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.artificialstaff.com',
        'Report a bug': "mailto:support@artificialstaff.com",
        'About': "# ARTIS OS v4.2\nPowered by Artificial Staff"
    }
)

# ==============================================================================
# 🛠️ 2. KRİTİK UI YAMALARI (SIDEBAR TOGGLE FIX)
# ==============================================================================
# Bu kısım, Sidebar kapatıldığında geri açma tuşunun kaybolmasını engeller.
# Ayrıca üstteki renkli çizgiyi ve varsayılan Streamlit menüsünü gizler.
st.markdown("""
<style>
    /* 1. Header'ı Şeffaf Yap ama Gizleme (Toggle Butonu İçin) */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        z-index: 1 !important;
    }
    
    /* 2. Sidebar Açma/Kapama Tuşunu Zorla Görünür Yap ve Rengini Aç */
    button[kind="header"] {
        background-color: transparent !important;
        color: #A1A1AA !important; /* Gri ton */
        border: 1px solid rgba(255,255,255,0.1) !important;
        transition: all 0.3s ease;
    }
    button[kind="header"]:hover {
        color: #FFFFFF !important;
        background-color: rgba(255,255,255,0.05) !important;
        transform: scale(1.1);
    }

    /* 3. Üstteki Renkli Çizgiyi (Decoration) Kaldır */
    div[data-testid="stDecoration"] {
        display: none;
    }

    /* 4. Varsayılan Navigasyonu Gizle (Kendi Sidebarımızı Kullanıyoruz) */
    div[data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* 5. Sidebar Arka Planı (Derinlikli) */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 📦 3. MODÜL YÜKLEME (FAIL-SAFE SİSTEM)
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
    # Hata durumunda şık bir uyarı ekranı
    st.error(f"""
    ### ⚠️ Sistem Başlatılamadı
    Gerekli modüller yüklenirken bir sorun oluştu.
    \n**Hata Kodu:** `{e}`
    """)
    st.stop()

# ==============================================================================
# 🎨 4. STİL VE OTURUM YÖNETİMİ
# ==============================================================================

# Global CSS Yükle
styles.load_css()

# Session State Başlatma (Oturumun kalıcılığı için)
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}
if "active_tab" not in st.session_state: st.session_state.active_tab = "Dashboard"

# ==============================================================================
# 🧭 5. SIDEBAR BİLEŞENİ (PROFESYONEL NAVİGASYON)
# ==============================================================================
def render_sidebar():
    with st.sidebar:
        # --- A. DİNAMİK MARKA BAŞLIĞI (HEADER) ---
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        user_plan = st.session_state.user_data.get('plan', 'Enterprise')
        
        # HTML Header (Dedent ile temizlenmiş)
        brand_html = textwrap.dedent(f"""
            <div style="margin-top: 20px; margin-bottom: 25px; padding: 12px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #8B5CF6 0%, #3B82F6 100%); border-radius: 8px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.25);">
                        <i class='bx bxs-command' style="color: white; font-size: 20px;"></i>
                    </div>
                    <div style="overflow: hidden;">
                        <div style="font-weight: 800; font-size: 15px; color: #FFF; letter-spacing: -0.3px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 170px;">
                            {user_brand}
                        </div>
                        <div style="font-size: 10px; color: #34D399; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; display:flex; align-items:center; gap:4px;">
                            <span style="width:6px; height:6px; background:#34D399; border-radius:50%; display:inline-block;"></span> {user_plan}
                        </div>
                    </div>
                </div>
            </div>
        """)
        st.markdown(brand_html, unsafe_allow_html=True)

        # --- B. NAVİGASYON MENÜSÜ ---
        menu_options = {
            "Dashboard": "📊  Dashboard",
            "Lojistik": "📦  Lojistik",
            "Envanter": "📋  Envanter",
            "Formlar": "📝  Formlar",
            "Dokümanlar": "📂  Dokümanlar",
            "Yapılacaklar": "✅  Yapılacaklar",
            "Planlar": "💎  Planlar"
        }
        
        # CSS ile özelleştirilmiş Radio Button
        selected = st.radio(
            "MENÜ",
            list(menu_options.keys()),
            format_func=lambda x: menu_options[x],
            label_visibility="collapsed",
            key="nav_radio"
        )
        
        # --- C. BOŞLUK (SPACER) ---
        # Profil kartını en alta itmek için
        st.markdown("<div style='flex-grow: 1; min-height: 200px;'></div>", unsafe_allow_html=True)

        # --- D. KULLANICI PROFİLİ (STICKY BOTTOM) ---
        user_name = st.session_state.user_data.get('name', 'Kullanıcı')
        user_avatar = st.session_state.user_data.get('avatar', user_name[0])
        
        profile_html = textwrap.dedent(f"""
            <div style="
                margin-top: auto;
                background: linear-gradient(180deg, rgba(255,255,255,0.02) 0%, rgba(255,255,255,0.04) 100%); 
                border-top: 1px solid rgba(255,255,255,0.08); 
                padding: 15px; 
                border-radius: 12px; 
                display: flex; 
                align-items: center; 
                gap: 12px;
                transition: all 0.3s;
                cursor: default;">
                <div style="width: 36px; height: 36px; background: #18181B; border: 1px solid #27272A; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; color: #E4E4E7; font-size: 13px;">
                    {user_avatar}
                </div>
                <div style="flex-grow: 1; overflow: hidden;">
                    <div style="font-size: 13px; font-weight: 600; color: #E4E4E7; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{user_name}</div>
                    <div style="font-size: 10px; color: #71717A; display:flex; align-items:center; gap:4px;">
                        <span style="width:6px; height:6px; background:#10B981; border-radius:50%;"></span> Çevrimiçi
                    </div>
                </div>
            </div>
        """)
        st.markdown(profile_html, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        # Çıkış Butonu
        if st.button("Güvenli Çıkış", use_container_width=True):
            with st.spinner("Oturum kapatılıyor..."):
                time.sleep(0.5)
            st.session_state.logged_in = False
            st.rerun()
            
        return selected

# ==============================================================================
# 🚀 6. ANA YÖNLENDİRİCİ (MAIN ROUTER)
# ==============================================================================
def main():
    # 1. Login Kontrolü
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        # 2. Sidebar'ı Render Et
        selection = render_sidebar()
        
        # 3. Sayfa Yönlendirmesi
        if selection == "Dashboard":
            dashboard.render_dashboard()
        elif selection == "Lojistik":
            logistics.render_logistics()
        elif selection == "Envanter":
            inventory.render_inventory()
        elif selection == "Formlar":
            forms.render_forms()
        elif selection == "Dokümanlar":
            documents.render_documents()
        elif selection == "Yapılacaklar":
            todo.render_todo()
        elif selection == "Planlar":
            plan.render_plans()

# Uygulama Başlatma Noktası
if __name__ == "__main__":
    main()
