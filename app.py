import streamlit as st
import sys
import os

# --- 1. SİSTEM YOLLARI ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

# 2. SAYFA AYARLARI
# Not: Eğer login.py içinde set_page_config kullanıyorsanız, buradaki hata verebilir. 
# Streamlit'te set_page_config sadece bir kez çağrılmalıdır. 
# En güvenli yol, bunu sadece app.py'nin en başında tutmaktır.
try:
    st.set_page_config(
        page_title="ARTIS | Global Operations Engine",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded" 
    )
except:
    pass

# 3. MODÜLLERİ YÜKLE
try:
    import styles, login, dashboard
    # Operasyonel Araçlar
    import operations, logistics, inventory, plan
    # Servisler
    import website, llc, seller, social, ads, automation, leadgen
    # Admin
    import admin
except ImportError as e:
    st.error(f"⚠️ Kritik Modül Eksik: {e}. Lütfen 'views' klasörünü kontrol edin.")

# 4. GLOBAL CSS VE STATE
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {} 
if "current_page" not in st.session_state: st.session_state.current_page = "Dashboard"

# CORTEX AI Global Veritabanı
if "users_db" not in st.session_state:
    st.session_state.users_db = [
        {"id": 101, "name": "Ahmet Yılmaz", "role": "editor", "status": "Active", "mrr": 1200},
        {"id": 104, "name": "John Doe", "role": "admin", "status": "Active", "mrr": 5000},
    ]

# --- NAVİGASYON MANTIĞI ---
def update_page(key):
    """
    Bir menü grubuna tıklandığında diğerlerini sıfırlar.
    Bu, menüler arası geçişte takılmayı önler.
    """
    st.session_state.current_page = st.session_state[key]
    
    # Mutual Exclusivity (Biri seçilince diğerlerini temizle)
    if key == "nav_main":
        st.session_state["nav_services"] = None
        st.session_state["nav_tools"] = None
    elif key == "nav_services":
        st.session_state["nav_main"] = None
        st.session_state["nav_tools"] = None
    elif key == "nav_tools":
        st.session_state["nav_main"] = None
        st.session_state["nav_services"] = None

# 5. STRATEJİK SOL MENÜ (GÜNCELLENDİ)
def render_sidebar():
    with st.sidebar:
        # LOGO ALANI (SADELEŞTİRİLDİ)
        # Kullanıcı bilgileri artık Dashboard Header'da olduğu için burası marka alanı oldu.
        st.markdown(f"""
            <div style="padding: 20px 0; text-align: center; margin-bottom: 20px;">
                <div style="font-weight: 900; font-size: 24px; color: #FFF; letter-spacing: 2px;">ARTIS<span style="color:#d4af37;">AI</span></div>
                <div style="font-size: 9px; color: #666; letter-spacing: 1px; margin-top: 5px;">GLOBAL OPERATIONS ENGINE</div>
            </div>
        """, unsafe_allow_html=True)

        user_role = st.session_state.user_data.get('role', 'user')
        curr = st.session_state.current_page

        # --- GRUP 1: ANA KOMUTA ---
        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-bottom:5px; font-weight:600;">ANA KOMUTA</div>', unsafe_allow_html=True)
        
        idx_main = 0 if curr == "Dashboard" else None
        
        st.radio(
            "Main Nav", 
            ["Dashboard"], 
            format_func=lambda x: "📊 Komuta Merkezi",
            key="nav_main",
            on_change=update_page, args=("nav_main",),
            label_visibility="collapsed",
            index=idx_main
        )

        # --- GRUP 2: SERVİSLER ---
        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-top:20px; margin-bottom:5px; font-weight:600;">GLOBAL SERVİSLER</div>', unsafe_allow_html=True)
        
        services_map = {
            "Website": "🌐 Web Sitesi & UX",
            "LLC_Legal": "⚖️ LLC & Şirket",
            "Logistics": "📦 Lojistik & Sevk",
            "Inventory": "📋 Envanter & Stok",
            "Marketplace": "🏪 Pazaryeri (Amazon)",
            "Social": "📱 Sosyal Medya",
            "Ads": "🎯 Reklam (ROAS)",
            "Automation": "🤖 Otomasyon",
            "LeadGen": "🚀 AI Lead Gen"
        }
        
        svc_keys = list(services_map.keys())
        idx_svc = svc_keys.index(curr) if curr in svc_keys else None
        
        st.radio(
            "Service Nav",
            svc_keys,
            format_func=lambda x: services_map[x],
            key="nav_services", 
            on_change=update_page, args=("nav_services",),
            label_visibility="collapsed",
            index=idx_svc 
        )

        # --- GRUP 3: ARAÇLAR ---
        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-top:20px; margin-bottom:5px; font-weight:600;">ARAÇLAR</div>', unsafe_allow_html=True)
        
        tools_map = {
            "Operasyonlar": "🛠️ Operasyon Merkezi",
            "Planlar": "💎 Stratejik Planlar"
        }
        
        tools_keys = list(tools_map.keys())
        idx_tool = tools_keys.index(curr) if curr in tools_keys else None
        
        st.radio(
            "Tool Nav",
            tools_keys,
            format_func=lambda x: tools_map[x],
            key="nav_tools",
            on_change=update_page, args=("nav_tools",),
            label_visibility="collapsed",
            index=idx_tool
        )

        # --- CORTEX (ADMIN) ---
        if user_role == 'admin':
            st.markdown("---")
            if st.button("🧠 CORTEX (Super AI)", use_container_width=True):
                st.session_state.current_page = "Admin"
                st.rerun()

        # ÇIKIŞ BUTONU KALDIRILDI (Artık Dashboard Header'da)

# 6. ROUTER
def main():
    # Login Kontrolü
    if not st.session_state.logged_in:
        # Login sayfası kendi içinde set_page_config çağırıyor olabilir, bu yüzden app.py başındaki try-except önemli.
        login.render_login_page()
    else:
        render_sidebar()
        page = st.session_state.current_page
        
        try:
            if page == "Dashboard": dashboard.render_dashboard()
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
            elif page == "Operasyonlar": operations.render_operations()
            elif page == "Planlar": plan.render_plans()
            else:
                dashboard.render_dashboard() 
        except Exception as e:
            st.error(f"Sayfa Yükleme Hatası: {e}")

if __name__ == "__main__":
    main()
