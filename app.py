import streamlit as st
from styles import load_css
# views.py içindeki tüm render fonksiyonlarını import ediyoruz
from views import (
    render_login_screen, 
    render_welcome_animation, 
    render_main_hub, 
    render_services_catalog, # Bu fonksiyonun views.py'da olduğundan emin olun
    render_dashboard, 
    render_artis_ai, 
    render_logistics, 
    render_marketing
)

# 1. Sayfa Ayarları (En başta olmalı)
st.set_page_config(
    page_title="Artificial Staff - Enterprise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State Başlatma (Hata almamak için varsayılan değerler)
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'show_welcome' not in st.session_state:
    st.session_state.show_welcome = False

# 3. CSS Yükle
load_css()

# --- ANA AKIŞ MANTIĞI ---

# DURUM 1: Giriş Yapılmamışsa -> Sadece Login Ekranı Göster
if not st.session_state.authenticated:
    render_login_screen()

# DURUM 2: Giriş Yapılmışsa -> Menüyü ve İçeriği Göster
else:
    # --- KARŞILAMA ANİMASYONU ---
    # Eğer 'show_welcome' True ise animasyonu göster ve sonra kapat
    if st.session_state.show_welcome:
        render_welcome_animation()
        # Animasyon fonksiyonu içinde st.rerun() olduğu için burası tekrar çalışacak
        # ve show_welcome False olduğu için aşağıdaki bloğa geçecek.
    
    else:
        # --- SIDEBAR (YAN MENÜ) ---
        # Artık giriş yapıldığı için menüyü burada oluşturuyoruz.
        with st.sidebar:
            st.markdown("<h1 style='text-align:center; color:#D4AF37; margin-bottom:0;'>AS</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; color:#666; letter-spacing:2px; font-size:10px; margin-top:0;'>ENTERPRISE</p>", unsafe_allow_html=True)
            st.markdown("---")
            
            # Menü Seçenekleri
            page = st.radio(
                label="Navigasyon",
                options=["ANA MERKEZ", "HİZMETLERİMİZ", "DASHBOARD", "ARTIS (AI)", "LOJİSTİK", "PAZARLAMA"],
                label_visibility="collapsed"
            )
            
            st.markdown("---")
            
            # Çıkış Butonu
            if st.button("ÇIKIŞ YAP"):
                st.session_state.authenticated = False
                st.session_state.show_welcome = False
                st.rerun()
            
            st.caption("© 2026 Artificial Staff LLC")

        # --- SAYFA YÖNLENDİRME ---
        # Menüden seçilen sayfayı ana ekrana bas
        if page == "ANA MERKEZ":
            render_main_hub() # Hub ekranı (Kartlı menü)
        elif page == "HİZMETLERİMİZ":
            render_services_catalog() # Detaylı Hizmet Kataloğu
        elif page == "DASHBOARD":
            render_dashboard()
        elif page == "ARTIS (AI)":
            render_artis_ai()
        elif page == "LOJİSTİK":
            render_logistics()
        elif page == "PAZARLAMA":
            render_marketing()
