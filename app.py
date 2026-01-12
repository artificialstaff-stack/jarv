# app.py
import streamlit as st
from styles import apply_custom_styles
# Views dosyasından ilgili fonksiyonları çekiyoruz
from views import (
    render_login, render_intro_video, render_welcome, render_profile, 
    render_service_selection, render_jarvis, render_execution,
    render_mini_player
)

# 1. Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff Enterprise", layout="wide", page_icon="AS")
apply_custom_styles()

# 2. State Başlangıçları
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "intro_watched" not in st.session_state:
    st.session_state["intro_watched"] = False # Başlangıçta izlenmedi
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "WELCOME"

# --- AKIŞ KONTROLÜ ---

# A. GİRİŞ YAPILMADIYSA -> LOGIN
if not st.session_state["logged_in"]:
    render_login()

# B. GİRİŞ YAPILDI AMA INTRO İZLENMEDİ -> VIDEO
elif not st.session_state["intro_watched"]:
    render_intro_video()

# C. GİRİŞ YAPILDI VE INTRO İZLENDİ -> DASHBOARD
else:
    # --- SIDEBAR ---
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="font-family: 'Cinzel'; font-size: 36px; margin:0; color:#D4AF37;">AS</h1>
            <span style="font-size: 10px; letter-spacing: 2px; color: #666;">ENTERPRISE v5.0</span>
        </div>
        """, unsafe_allow_html=True)
        
        selected_menu = st.radio("NAVİGASYON", 
            ["🏠 ANA MERKEZ", "👤 PROFİL", "🚀 KURULUM", "🧠 JARVIS", "📦 LOJİSTİK", "📈 PAZARLAMA"],
            label_visibility="collapsed"
        )
        
        # Sidebar'da "Intro Tekrar İzle" butonu (Views içindeki render_mini_player içinde de var)
        st.markdown("---")
        if st.button("↺ INTRO REPLAY"):
            st.session_state["intro_watched"] = False
            st.rerun()
            
        if st.button("ÇIKIŞ YAP"):
            st.session_state["logged_in"] = False
            st.rerun()

    # --- ANA EKRAN ---
    # Her sayfada sağ altta mini player görünsün
    render_mini_player()

    if selected_menu == "🏠 ANA MERKEZ":
        render_welcome()
    elif selected_menu == "👤 PROFİL":
        render_profile()
    elif selected_menu == "🚀 KURULUM":
        if st.session_state.get("current_page") == "SERVICE_SELECT":
            render_service_selection()
        elif st.session_state.get("current_page") == "EXECUTION":
            render_execution()
        else:
            render_service_selection()
    elif selected_menu == "🧠 JARVIS":
        render_jarvis()
    elif selected_menu == "📦 LOJİSTİK":
        st.title("📦 Lojistik")
        st.info("Modül yükleniyor...")
    elif selected_menu == "📈 PAZARLAMA":
        st.title("📈 Pazarlama")
        st.info("Veriler analiz ediliyor...")
