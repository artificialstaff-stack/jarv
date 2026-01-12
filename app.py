# app.py
import streamlit as st
from styles import apply_custom_styles
from views import (
    render_login, render_welcome, render_profile, 
    render_service_selection, render_jarvis, render_execution
)

# 1. Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff Enterprise", layout="wide", page_icon="AS")
apply_custom_styles()

# 2. Session State Kontrolü (Giriş Yapıldı mı?)
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "WELCOME" # Girişten sonra ilk bura açılır

# 3. GİRİŞ EKRANI (Eğer giriş yapılmadıysa sadece bunu göster)
if not st.session_state["logged_in"]:
    render_login()

# 4. ANA UYGULAMA (Giriş yapıldıysa burası çalışır)
else:
    # --- YENİ GENİŞLETİLMİŞ SIDEBAR ---
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="font-family: 'Cormorant Garamond'; font-size: 40px; margin:0; color:#C5A059;">AS</h1>
            <span style="font-size: 10px; letter-spacing: 2px; color: #666;">ARTIFICIAL STAFF v5.0</span>
        </div>
        """, unsafe_allow_html=True)
        
        # MENÜ SEÇENEKLERİ
        selected_menu = st.radio("NAVİGASYON", 
            [
                "🏠 ANA MERKEZ (Vision)", 
                "👤 PROFİL & KYC",
                "🚀 YENİ KURULUM", 
                "🧠 JARVIS AI", 
                "📦 LOJİSTİK & DEPO", 
                "💳 FİNANS & BANKA", 
                "📈 PAZARLAMA"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        if st.button("ÇIKIŞ YAP"):
            st.session_state["logged_in"] = False
            st.rerun()

    # --- SAYFA YÖNLENDİRME MANTIĞI ---
    
    # A. Menüden Tıklananlar
    if selected_menu == "🏠 ANA MERKEZ (Vision)":
        render_welcome()
        
    elif selected_menu == "👤 PROFİL & KYC":
        render_profile()
        
    elif selected_menu == "🚀 YENİ KURULUM":
        # Akıllı Yönlendirme: Eğer zaten bir işlemdeyse oraya git
        if st.session_state.get("current_page") == "SERVICE_SELECT":
            render_service_selection()
        elif st.session_state.get("current_page") == "EXECUTION":
            render_execution()
        else:
            render_service_selection() 
            
    elif selected_menu == "🧠 JARVIS AI":
        render_jarvis()
        
    elif selected_menu == "📦 LOJİSTİK & DEPO":
        st.title("📦 Lojistik Paneli")
        st.info("Bu modül 'Enterprise' paketine özeldir. Entegrasyon bekleniyor...")
        
    elif selected_menu == "💳 FİNANS & BANKA":
        st.title("💳 Finansal Yönetim")
        st.info("Mercury Bank API bağlantısı bekleniyor...")
        
    elif selected_menu == "📈 PAZARLAMA":
        st.title("📈 Growth & Marketing")
        st.info("Google Ads & Meta verileri yükleniyor...")
