import streamlit as st
import sys
import os
import time

# --- 1. SİSTEM YOLLARI ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

# 2. SAYFA AYARLARI (Silicon Valley UX Standards)
st.set_page_config(
    page_title="ARTIS | Global Operations Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# 3. PREMIUM SIDEBAR & NAVIGATION CSS
st.markdown("""
<style>
    /* Sidebar Kilitleme ve Modernizasyon */
    [data-testid="stSidebar"] button { display: none !important; }
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    
    [data-testid="stSidebar"] {
        min-width: 320px !important;
        max-width: 320px !important;
        background-color: #000000 !important;
        border-right: 1px solid rgba(197, 160, 89, 0.15); /* Sunumdaki Altın Rengi Dokunuş */
    }

    /* Menü Gruplandırma Yazıları */
    .menu-label {
        font-size: 10px;
        color: #444;
        letter-spacing: 2px;
        font-weight: 700;
        margin: 20px 0 10px 10px;
        text-transform: uppercase;
    }

    /* Header Şeffaflık */
    header[data-testid="stHeader"] { background: transparent !important; }
    
    /* Navigasyon İkon ve Yazı Uyumu */
    .stRadio label p { font-size: 14px !important; font-weight: 500 !important; color: #E4E4E7 !important; }
</style>
""", unsafe_allow_html=True)

# 4. MODÜL YÜKLEME (Fail-Safe)
try:
    import styles, login, dashboard, logistics, inventory, plan, documents, todo, forms
    # Yeni Hizmet View'ları (Bu dosyaları oluşturman gerekecek)
    # import website, legal, marketplace, social, ads, automation, leadgen 
except ImportError as e:
    st.error(f"Sistem Bileşeni Eksik: {e}")

# Global Stilleri Uygula
styles.load_css()

# Session State Yönetimi
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

# 5. STRATEJİK SOL MENÜ (9 Ana Hizmet + Araçlar)
def render_sidebar():
    with st.sidebar:
        user_brand = st.session_state.user_data.get('brand', 'Anatolia Home')
        
        # Marka Kimliği
        st.markdown(f"""
            <div style="padding: 15px; background: rgba(197, 160, 89, 0.03); border-radius: 12px; margin-bottom: 25px; border: 1px solid rgba(197, 160, 89, 0.1);">
                <div style="font-weight: 800; font-size: 18px; color: #FFF; letter-spacing: -0.5px;">⚡ {user_brand}</div>
                <div style="font-size: 10px; color: #C5A059; font-weight: 700;">● GLOBAL INTEGRATION ACTIVE</div>
            </div>
        """, unsafe_allow_html=True)

        # GRUP 1: ANA KOMUTA
        st.markdown('<div class="menu-label">Ana Komuta</div>', unsafe_allow_html=True)
        main_nav = {
            "Dashboard": "📊 Dashboard (Genel Bakış)"
        }
        selected_main = st.radio("MAIN", list(main_nav.keys()), format_func=lambda x: main_nav[x], label_visibility="collapsed")

        # GRUP 2: 9 ANA HİZMET (Sunumdaki Modüller)
        st.markdown('<div class="menu-label">Global Büyüme Servisleri</div>', unsafe_allow_html=True)
        service_nav = {
            "Website": "🌐 Web Sitesi & UX (0.4s)",
            "LLC_Legal": "⚖️ LLC & Şirket Yönetimi",
            "Logistics": "📦 Lojistik & Nakliye",
            "Inventory": "📋 Envanter & Tahminleme",
            "Marketplace": "🏪 Pazaryeri Yönetimi",
            "Social": "📱 Sosyal Medya & İçerik",
            "Ads": "🎯 Reklam (ROAS) Yönetimi",
            "Automation": "🤖 Otomasyon & Ops",
            "LeadGen": "🚀 AI Lead Gen (B2B Satış)"
        }
        selected_service = st.radio("SERVICES", list(service_nav.keys()), format_func=lambda x: service_nav[x], label_visibility="collapsed")

        # GRUP 3: İÇ OPERASYON (Araçlar)
        st.markdown('<div class="menu-label">Operasyonel Araçlar</div>', unsafe_allow_html=True)
        tool_nav = {
            "Docs": "📂 Dijital Arşiv",
            "Tasks": "✅ Yapılacaklar",
            "Forms": "📝 Formlar & Onaylar"
        }
        selected_tool = st.radio("TOOLS", list(tool_nav.keys()), format_func=lambda x: tool_nav[x], label_visibility="collapsed")

        # Sticky Footer: Kullanıcı Bilgisi
        st.markdown("<div style='flex-grow: 1; height: 50px;'></div>", unsafe_allow_html=True)
        user_name = st.session_state.user_data.get('name', 'Ahmet Yılmaz')
        st.markdown(f"""
            <div style="padding: 12px; background: rgba(255,255,255,0.03); border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
                <div style="font-size: 12px; font-weight: 600; color: #FAFAFA;">{user_name}</div>
                <div style="font-size: 9px; color: #34D399;">Enterprise Edition v4.2</div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Sistemden Çıkış", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
        # Hangi grubun en son seçildiğini kontrol etmek için küçük bir mantık
        # Şimdilik sadece basitleştirilmiş bir return kullanıyoruz
        return selected_main, selected_service, selected_tool

# 6. ROUTER (YÖNLENDİRİCİ)
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        # Menüden seçimleri al
        # Not: Streamlit'te radio buttonlar her zaman bir değer döndürür. 
        # Gerçek bir SaaS'da hangi radyo grubunun en son tıklandığını session_state ile takip etmelisin.
        main_sel, svc_sel, tool_sel = render_sidebar()
        
        # Basitleştirilmiş Sayfa Yönlendirme (Örnek Mantık)
        # Kullanıcı Dashboard dışındaki bir servise tıklarsa onu göster
        if svc_sel != "Website": # Website varsayılan ilk eleman olduğu için
             # Burada svc_sel'e göre yönlendirme yapılır
             pass

        # Mevcut yönlendirme yapını bozmadan entegre ediyorum:
        page = main_sel # Varsayılan
        
        # Eğer Dashboard dışında bir servis tıklandıysa (Bu kısmı kendine göre optimize edebilirsin)
        if svc_sel == "Logistics": logistics.render_logistics()
        elif svc_sel == "Inventory": inventory.render_inventory()
        # Yeni servis dosyalarını eklediğinde burayı genişletmelisin
        elif main_sel == "Dashboard": dashboard.render_dashboard()
        
        # Araçlar grubu yönlendirmesi
        # elif tool_sel == "Docs": documents.render_documents()

if __name__ == "__main__":
    main()
