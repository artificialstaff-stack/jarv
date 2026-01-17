import streamlit as st
import sys
import os

# --- 1. SİSTEM YOLLARI VE AYARLAR ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

try:
    st.set_page_config(
        page_title="ARTIS | Global Operations Engine",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="collapsed" 
    )
except:
    pass

# --- 2. GLOBAL STATE TANIMLARI ---
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "page" not in st.session_state: st.session_state.page = "Landing" # Varsayılan: Landing
if "pending_prompt" not in st.session_state: st.session_state.pending_prompt = None
if "user_data" not in st.session_state: st.session_state.user_data = {} 
if "current_page" not in st.session_state: st.session_state.current_page = "Dashboard"

# --- 3. MODÜLLERİ GÜVENLİ YÜKLE ---
try:
    import login, dashboard, landing
    # Operasyonel Araçlar
    import operations, logistics, inventory, plan
    # Servisler
    import website, llc, seller, social, ads, automation, leadgen
    # Admin
    import admin
    import styles
except ImportError as e:
    # Eğer dosya yoksa hata verme, placeholder ile geç (Development aşaması için)
    pass

# --- 4. YARDIMCI FONKSİYONLAR ---

# Sidebar Render (Sadece Dashboard'da aktif)
def render_sidebar():
    with st.sidebar:
        st.markdown(f"""
            <div style="padding: 20px 0; text-align: center; margin-bottom: 20px;">
                <div style="font-weight: 900; font-size: 28px; letter-spacing: 1px; color:white;">
                    ARTIS<span style="color:#d4af37;">AI</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

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

        curr = st.session_state.current_page
        
        # Basitleştirilmiş Menü
        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-bottom:5px;">ANA KOMUTA</div>', unsafe_allow_html=True)
        st.radio("Main", ["Dashboard"], key="nav_main", on_change=update_page, args=("nav_main",), label_visibility="collapsed", index=0 if curr=="Dashboard" else None)

        st.markdown('<div class="menu-label" style="font-size:10px; color:#666; margin-top:20px; margin-bottom:5px;">SERVİSLER</div>', unsafe_allow_html=True)
        services = {"Website": "🌐 Web Sitesi", "Logistics": "📦 Lojistik", "Inventory": "📋 Stok"}
        s_keys = list(services.keys())
        s_idx = s_keys.index(curr) if curr in s_keys else None
        st.radio("Services", s_keys, format_func=lambda x: services[x], key="nav_services", on_change=update_page, args=("nav_services",), label_visibility="collapsed", index=s_idx)


# Global Header (Sadece Dashboard'da aktif)
def render_global_header():
    st.markdown("""
        <style>
        .global-header { padding: 10px 0; border-bottom: 1px solid #333; margin-bottom: 20px; }
        </style>
    """, unsafe_allow_html=True)
    c1, c2 = st.columns([8, 1])
    with c1:
        st.markdown("**Anatolia Home** <span style='color:#34D399; font-size:10px'>● ONLINE</span>", unsafe_allow_html=True)
    with c2:
        if st.button("Çıkış", key="logout_btn"):
            st.session_state.logged_in = False
            st.session_state.page = "Landing"
            st.rerun()
    st.divider()

# --- 5. ANA ROUTING MANTIĞI ---
def main():
    
    # A. LANDING PAGE
    if st.session_state.page == "Landing":
        landing.render_landing()

    # B. LOGIN PAGE
    elif st.session_state.page == "Login":
        # Eğer zaten giriş yapmışsa direkt Dashboard'a at
        if st.session_state.logged_in:
            st.session_state.page = "Dashboard"
            st.rerun()
        else:
            login.render_login_page()

    # C. DASHBOARD & UYGULAMA
    elif st.session_state.page == "Dashboard":
        # Güvenlik Kontrolü
        if not st.session_state.logged_in:
            st.session_state.page = "Login"
            st.rerun()
        
        # İçeriği Yükle
        styles.load_css() # Global CSS'i sadece burada yükle
        render_sidebar()
        render_global_header()
        
        # Landing'den gelen prompt var mı?
        if st.session_state.pending_prompt:
            if "messages" not in st.session_state: st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": st.session_state.pending_prompt})
            st.session_state.pending_prompt = None # Temizle ve işle
        
        # Sayfayı Göster
        page = st.session_state.current_page
        try:
            if page == "Dashboard": dashboard.render_dashboard()
            elif page == "Website": website.render()
            elif page == "Logistics": logistics.render_logistics()
            elif page == "Inventory": inventory.render_inventory()
            else: dashboard.render_dashboard()
        except Exception as e:
            st.error(f"Sayfa modülü bulunamadı: {e}")

if __name__ == "__main__":
    main()
