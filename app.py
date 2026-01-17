import streamlit as st
import sys
import os

# --- 1. SİSTEM YOLLARI ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

# 2. SAYFA AYARLARI
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

# --- NAVİGASYON MANTIĞI ---
def update_page(key):
    st.session_state.current_page = st.session_state[key]
    if key == "nav_main":
        st.session_state["nav_services"] = None
        st.session_state["nav_tools"] = None
    elif key == "nav_services":
        st.session_state["nav_main"] = None
        st.session_state["nav_tools"] = None
    elif key == "nav_tools":
        st.session_state["nav_main"] = None
        st.session_state["nav_services"] = None

# --- GLOBAL HEADER (HER SAYFADA GÖRÜNÜR) ---
def render_global_header():
    """
    Sayfanın en üstünde görünen, navigasyon ve profil butonlarını içeren global bar.
    """
    # Kullanıcı markası (Yoksa ARTIS AI yazar)
    user_brand = "Anatolia Home" # Burayı session_state'den çekebilirsin
    
    # CSS ile Header Konteyneri
    st.markdown("""
        <style>
        .global-header {
            padding: 10px 20px;
            background: linear-gradient(90deg, rgba(20,20,20,0.5) 0%, rgba(20,20,20,0.2) 100%);
            border-bottom: 1px solid rgba(255,255,255,0.05);
            margin-bottom: 20px;
            border-radius: 12px;
        }
        /* Butonları biraz şeffaf yap */
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

    # Kolon Yapısı: [Marka İsmi] --- [Boşluk] --- [Bildirim] [Ayarlar] [Profil]
    col_brand, col_space, col_notif, col_settings, col_profile = st.columns([4, 3, 0.4, 0.4, 0.4])

    with col_brand:
        st.markdown(f"""
        <div style="display:flex; flex-direction:column;">
            <span style="font-size: 24px; font-weight:bold; color:white;">{user_brand}</span>
            <span style="font-size: 10px; color:#34D399; letter-spacing:1px;">● SYSTEM ONLINE</span>
        </div>
        """, unsafe_allow_html=True)

    # --- SAĞ ÜST MENÜLER (POPOVER) ---
    
    # 1. Bildirimler
    with col_notif:
        with st.popover("🔔", use_container_width=True):
            st.markdown("##### 🔔 Bildirimler")
            st.info("📦 **TR-8821** nolu kargo gümrükten geçti.")
            st.warning("⚠️ Stok Uyarısı: 'Deri Çanta' azalıyor.")
            st.success("✅ Aylık rapor hazırlandı.")
            if st.button("Tümünü Temizle"):
                st.toast("Bildirimler temizlendi")

    # 2. Ayarlar
    with col_settings:
        with st.popover("⚙️", use_container_width=True):
            st.markdown("##### ⚙️ Hızlı Ayarlar")
            st.toggle("Karanlık Mod", value=True)
            st.toggle("Bildirim Sesleri", value=False)
            st.selectbox("Dil / Language", ["Türkçe", "English", "Deutsch"])
            if st.button("Tam Ayarlar Sayfası"):
                st.session_state.current_page = "Settings" # Eğer sayfan varsa
                st.rerun()

    # 3. Profil (Çıkış Buraya Taşındı)
    with col_profile:
        with st.popover("👤", use_container_width=True):
            st.markdown("##### 👤 Hesabım")
            st.markdown(f"**Kullanıcı:** Admin")
            st.markdown("**Paket:** Enterprise Plan")
            st.divider()
            if st.button("🚪 Güvenli Çıkış", type="primary", use_container_width=True):
                st.session_state.logged_in = False
                st.rerun()
    
    st.divider() # Header ile sayfa içeriği arasına çizgi

# 5. STRATEJİK SOL MENÜ (LOGO GÜNCELLENDİ)
def render_sidebar():
    with st.sidebar:
        # LOGO ALANI (İSTEDİĞİN GİBİ: A ve I Altın, rts Beyaz)
        st.markdown(f"""
            <div style="padding: 20px 0; text-align: center; margin-bottom: 20px;">
                <div style="font-weight: 900; font-size: 32px; letter-spacing: 1px; font-family: 'Arial', sans-serif;">
                    <span style="color:#d4af37;">A</span><span style="color:#FFF;">RT</span><span style="color:#d4af37;">I</span><span style="color:#FFF;">S</span> <span style="color:#d4af37;">AI</span>
                </div>
                <div style="font-size: 8px; color: #666; letter-spacing: 2px; margin-top: -5px;">GLOBAL OPERATIONS ENGINE</div>
            </div>
        """, unsafe_allow_html=True)

        user_role = st.session_state.user_data.get('role', 'user')
        curr = st.session_state.current_page

        # --- MENÜLER ---
        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-bottom:5px; font-weight:600;">ANA KOMUTA</div>', unsafe_allow_html=True)
        idx_main = 0 if curr == "Dashboard" else None
        st.radio("Main Nav", ["Dashboard"], format_func=lambda x: "📊 Komuta Merkezi", key="nav_main", on_change=update_page, args=("nav_main",), label_visibility="collapsed", index=idx_main)

        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-top:20px; margin-bottom:5px; font-weight:600;">GLOBAL SERVİSLER</div>', unsafe_allow_html=True)
        services_map = {"Website": "🌐 Web Sitesi & UX", "LLC_Legal": "⚖️ LLC & Şirket", "Logistics": "📦 Lojistik & Sevk", "Inventory": "📋 Envanter & Stok", "Marketplace": "🏪 Pazaryeri (Amazon)", "Social": "📱 Sosyal Medya", "Ads": "🎯 Reklam (ROAS)", "Automation": "🤖 Otomasyon", "LeadGen": "🚀 AI Lead Gen"}
        svc_keys = list(services_map.keys())
        idx_svc = svc_keys.index(curr) if curr in svc_keys else None
        st.radio("Service Nav", svc_keys, format_func=lambda x: services_map[x], key="nav_services", on_change=update_page, args=("nav_services",), label_visibility="collapsed", index=idx_svc)

        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-top:20px; margin-bottom:5px; font-weight:600;">ARAÇLAR</div>', unsafe_allow_html=True)
        tools_map = {"Operasyonlar": "🛠️ Operasyon Merkezi", "Planlar": "💎 Stratejik Planlar"}
        tools_keys = list(tools_map.keys())
        idx_tool = tools_keys.index(curr) if curr in tools_keys else None
        st.radio("Tool Nav", tools_keys, format_func=lambda x: tools_map[x], key="nav_tools", on_change=update_page, args=("nav_tools",), label_visibility="collapsed", index=idx_tool)

        if user_role == 'admin':
            st.markdown("---")
            if st.button("🧠 CORTEX (Super AI)", use_container_width=True):
                st.session_state.current_page = "Admin"
                st.rerun()

# 6. ROUTER
def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        render_sidebar()
        
        # GLOBAL HEADER'I BURADA ÇAĞIRIYORUZ (HER SAYFADA GÖRÜNSÜN DİYE)
        render_global_header()
        
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
            st.error(f"Sayfa Yükleme Hatası: {e}")

if __name__ == "__main__":
    main()
