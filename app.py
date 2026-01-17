import streamlit as st
import sys
import os

# --- 1. SİSTEM YOLLARI ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

# 2. SAYFA AYARLARI
# Bu konfigürasyon her şeyden önce gelmeli
try:
    st.set_page_config(
        page_title="ARTIS | Global Operations Engine",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="collapsed" 
    )
except:
    pass

# 3. GLOBAL STATE TANIMLARI
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "page" not in st.session_state: st.session_state.page = "Landing" # Varsayılan açılış sayfası
if "pending_prompt" not in st.session_state: st.session_state.pending_prompt = None
if "user_data" not in st.session_state: st.session_state.user_data = {} 
if "current_page" not in st.session_state: st.session_state.current_page = "Dashboard"

# 4. MODÜLLERİ YÜKLE
try:
    import login, dashboard, landing
    # Operasyonel Araçlar
    import operations, logistics, inventory, plan
    # Servisler
    import website, llc, seller, social, ads, automation, leadgen
    # Admin
    import admin
    import styles # CSS yükleyici
except ImportError as e:
    st.error(f"⚠️ Kritik Modül Eksik: {e}")

# 5. GLOBAL HEADER (DASHBOARD İÇİN)
def render_global_header():
    user_brand = "Anatolia Home"
    st.markdown("""
        <style>
        .global-header {
            padding: 10px 20px;
            background: linear-gradient(90deg, rgba(20,20,20,0.5) 0%, rgba(20,20,20,0.2) 100%);
            border-bottom: 1px solid rgba(255,255,255,0.05);
            margin-bottom: 20px;
            border-radius: 12px;
        }
        div.stPopover button {
            background-color: transparent !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            color: #ccc !important;
        }
        div.stPopover button:hover {
            border-color: #d4af37 !important;
            color: #d4af37 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    col_brand, col_space, col_notif, col_settings, col_profile = st.columns([4, 3, 0.4, 0.4, 0.4])

    with col_brand:
        st.markdown(f"""
        <div style="display:flex; flex-direction:column;">
            <span style="font-size: 24px; font-weight:bold; color:white;">{user_brand}</span>
            <span style="font-size: 10px; color:#34D399; letter-spacing:1px;">● SYSTEM ONLINE</span>
        </div>
        """, unsafe_allow_html=True)

    with col_notif:
        with st.popover("🔔", use_container_width=True):
            st.markdown("##### 🔔 Bildirimler")
            st.info("📦 **TR-8821** nolu kargo gümrükten geçti.")
            st.warning("⚠️ Stok Uyarısı: 'Deri Çanta' azalıyor.")
            if st.button("Tümünü Temizle"): st.toast("Temizlendi")

    with col_settings:
        with st.popover("⚙️", use_container_width=True):
            st.markdown("##### ⚙️ Ayarlar")
            st.toggle("Karanlık Mod", value=True)
            st.selectbox("Dil", ["Türkçe", "English"])

    with col_profile:
        with st.popover("👤", use_container_width=True):
            st.markdown("##### 👤 Hesabım")
            st.markdown("**Paket:** Enterprise")
            st.divider()
            if st.button("🚪 Çıkış", type="primary", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.page = "Landing" # Çıkış yapınca Landing'e dön
                st.rerun()
    st.divider()

# 6. SIDEBAR NAVİGASYON (Sadece Giriş Yapınca Görünür)
def render_sidebar():
    with st.sidebar:
        st.markdown(f"""
            <div style="padding: 20px 0; text-align: center; margin-bottom: 20px;">
                <div style="font-weight: 900; font-size: 32px; letter-spacing: 1px; font-family: 'Arial', sans-serif;">
                    <span style="color:#d4af37;">A</span><span style="color:#FFF;">RT</span><span style="color:#d4af37;">I</span><span style="color:#FFF;">S</span> <span style="color:#d4af37;">AI</span>
                </div>
                <div style="font-size: 8px; color: #666; letter-spacing: 2px; margin-top: -5px;">GLOBAL OPERATIONS ENGINE</div>
            </div>
        """, unsafe_allow_html=True)

        def update_page(key):
            st.session_state.current_page = st.session_state[key]
            # Mutual Exclusivity Logic
            if key == "nav_main":
                st.session_state["nav_services"] = None
                st.session_state["nav_tools"] = None
            elif key == "nav_services":
                st.session_state["nav_main"] = None
                st.session_state["nav_tools"] = None
            elif key == "nav_tools":
                st.session_state["nav_main"] = None
                st.session_state["nav_services"] = None

        curr = st.session_state.current_page
        
        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-bottom:5px; font-weight:600;">ANA KOMUTA</div>', unsafe_allow_html=True)
        st.radio("Main Nav", ["Dashboard"], format_func=lambda x: "📊 Komuta Merkezi", key="nav_main", on_change=update_page, args=("nav_main",), label_visibility="collapsed", index=0 if curr=="Dashboard" else None)

        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-top:20px; margin-bottom:5px; font-weight:600;">GLOBAL SERVİSLER</div>', unsafe_allow_html=True)
        services = {"Website": "🌐 Web Sitesi & UX", "LLC_Legal": "⚖️ LLC & Şirket", "Logistics": "📦 Lojistik & Sevk", "Inventory": "📋 Envanter & Stok", "Marketplace": "🏪 Pazaryeri", "Social": "📱 Sosyal Medya", "Ads": "🎯 Reklam (ROAS)", "Automation": "🤖 Otomasyon", "LeadGen": "🚀 AI Lead Gen"}
        s_keys = list(services.keys())
        s_idx = s_keys.index(curr) if curr in s_keys else None
        st.radio("Service Nav", s_keys, format_func=lambda x: services[x], key="nav_services", on_change=update_page, args=("nav_services",), label_visibility="collapsed", index=s_idx)

        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-top:20px; margin-bottom:5px; font-weight:600;">ARAÇLAR</div>', unsafe_allow_html=True)
        tools = {"Operasyonlar": "🛠️ Operasyon Merkezi", "Planlar": "💎 Stratejik Planlar"}
        t_keys = list(tools.keys())
        t_idx = t_keys.index(curr) if curr in t_keys else None
        st.radio("Tool Nav", t_keys, format_func=lambda x: tools[x], key="nav_tools", on_change=update_page, args=("nav_tools",), label_visibility="collapsed", index=t_idx)

# 7. ROUTER (ANA YÖNLENDİRİCİ)
def main():
    
    # --- ROUTING LOGIC ---
    
    # 1. LANDING PAGE
    if st.session_state.page == "Landing":
        landing.render_landing()
        
    # 2. LOGIN PAGE
    elif st.session_state.page == "Login":
        if st.session_state.logged_in:
            st.session_state.page = "Dashboard"
            st.rerun()
        else:
            login.render_login_page()
            
    # 3. DASHBOARD & UYGULAMA
    elif st.session_state.page == "Dashboard":
        if not st.session_state.logged_in:
            st.session_state.page = "Login"
            st.rerun()
        
        # Kullanıcı Giriş Yapmışsa:
        styles.load_css() # Global stilleri sadece burada yükle
        render_sidebar()
        render_global_header()
        
        # Pending Prompt Kontrolü (Landing'den gelen)
        if st.session_state.pending_prompt:
            if "messages" not in st.session_state: st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": st.session_state.pending_prompt})
            st.session_state.pending_prompt = None # Temizle
        
        # Sayfa İçeriğini Yükle
        page = st.session_state.current_page
        try:
            if page == "Dashboard": dashboard.render_dashboard()
            elif page == "Admin": admin.render()
            elif page == "Website": website.render()
            elif page == "LLC_Legal": llc.render()
            elif page == "Logistics": logistics.render_logistics()
            elif page == "Inventory": inventory.render_inventory()
            elif page == "Marketplace": seller.render()
            elif page == "Social": social.render()
            elif page == "Ads": ads.render()
            elif page == "Automation": automation.render()
            elif page == "LeadGen": leadgen.render()
            elif page == "Operasyonlar": operations.render_operations()
            elif page == "Planlar": plan.render_plans()
            else: dashboard.render_dashboard()
        except Exception as e:
            st.error(f"Sayfa hatası: {e}")

if __name__ == "__main__":
    main()
