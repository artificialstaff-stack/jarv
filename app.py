import streamlit as st
import sys
import os

# --- 1. SİSTEM YOLLARI ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

# 2. SAYFA AYARLARI
st.set_page_config(
    page_title="ARTIS | Global Operations Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# 3. MODÜLLERİ YÜKLE
try:
    import styles, login, dashboard
    # Operasyonel Araçlar
    import logistics, inventory, plan, documents, todo, forms
    # Yeni 9 Global Hizmet
    import website, llc, seller, social, ads, automation, leadgen
    # [YENİ] Admin Modülü (SaaS Yönetimi İçin)
    import admin
except ImportError as e:
    st.error(f"⚠️ Kritik Modül Eksik: {e}. Lütfen 'views' klasöründeki tüm dosyaları oluşturduğundan emin ol.")

# 4. GLOBAL CSS VE STATE YÖNETİMİ
styles.load_css()

# Session State Başlatma
if "logged_in" not in st.session_state: st.session_state.logged_in = False

# [ÖNEMLİ] Admin Panelini görebilmen için varsayılan yetkiyi 'admin' yaptım.
if "user_data" not in st.session_state: 
    st.session_state.user_data = {
        'brand': 'Anatolia Home', 
        'name': 'Ahmet Yılmaz',
        'role': 'admin' # <-- Bu yetki sayesinde Admin paneline girebilirsin
    }

if "current_page" not in st.session_state: st.session_state.current_page = "Dashboard"

# --- NAVİGASYON FONKSİYONU ---
def update_page(key):
    st.session_state.current_page = st.session_state[key]

# 5. STRATEJİK SOL MENÜ
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

        # --- GRUP 1: ANA KOMUTA ---
        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; letter-spacing:1px; margin-bottom:5px;">ANA KOMUTA</div>', unsafe_allow_html=True)
        st.radio("Main Nav", ["Dashboard"], format_func=lambda x: "📊 Komuta Merkezi", key="nav_main", on_change=update_page, args=("nav_main",), label_visibility="collapsed")

        # --- GRUP 2: 9 ANA HİZMET ---
        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; letter-spacing:1px; margin-top:20px; margin-bottom:5px;">GLOBAL SERVİSLER</div>', unsafe_allow_html=True)
        services_map = {
            "Website": "🌐 Web Sitesi & UX", "LLC_Legal": "⚖️ LLC & Şirket",
            "Logistics": "📦 Lojistik & Sevk", "Inventory": "📋 Envanter & Stok",
            "Marketplace": "🏪 Pazaryeri (Amazon)", "Social": "📱 Sosyal Medya",
            "Ads": "🎯 Reklam (ROAS)", "Automation": "🤖 Otomasyon", "LeadGen": "🚀 AI Lead Gen"
        }
        st.radio("Service Nav", list(services_map.keys()), format_func=lambda x: services_map[x], key="nav_services", on_change=update_page, args=("nav_services",), label_visibility="collapsed", index=None)

        # --- GRUP 3: ARAÇLAR ---
        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; letter-spacing:1px; margin-top:20px; margin-bottom:5px;">ARAÇLAR</div>', unsafe_allow_html=True)
        tools_map = {
            "Dokümanlar": "📂 Dijital Arşiv", "Yapılacaklar": "✅ Görevler",
            "Formlar": "📝 Formlar", "Planlar": "💎 Stratejik Planlar"
        }
        st.radio("Tool Nav", list(tools_map.keys()), format_func=lambda x: tools_map[x], key="nav_tools", on_change=update_page, args=("nav_tools",), label_visibility="collapsed", index=None)

        # --- [EKLENDİ] YÖNETİM ---
        st.markdown("---")
        if st.button("🛡️ Admin Paneli", use_container_width=True):
            st.session_state.current_page = "Admin"
            st.rerun()

        # Footer
        st.markdown("<div style='flex-grow: 1; height: 30px;'></div>", unsafe_allow_html=True)
        if st.button("Çıkış Yap", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

# 6. ROUTER (ANA YÖNLENDİRİCİ)
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        render_sidebar()
        page = st.session_state.current_page
        
        try:
            if page == "Dashboard": dashboard.render_dashboard()
            # [EKLENDİ] Admin Yönlendirmesi
            elif page == "Admin": admin.render()
            
            # Servisler
            elif page == "Website": website.render()
            elif page == "LLC_Legal": llc.render()
            elif page == "Logistics": logistics.render_logistics()
            elif page == "Inventory": inventory.render_inventory()
            elif page == "Marketplace": seller.render()
            elif page == "Social": social.render()
            elif page == "Ads": ads.render()
            elif page == "Automation": automation.render()
            elif page == "LeadGen": leadgen.render()
            
            # Araçlar
            elif page == "Dokümanlar": documents.render_documents()
            elif page == "Yapılacaklar": todo.render_todo()
            elif page == "Formlar": forms.render_forms()
            elif page == "Planlar": plan.render_plans()
            else:
                dashboard.render_dashboard()
        except Exception as e:
            st.error(f"Sayfa Yükleme Hatası: {e}")
            st.info("Lütfen 'views/admin.py' dosyasını oluşturduğunuzdan emin olun.")

if __name__ == "__main__":
    main()
