# app.py
import streamlit as st
from styles import apply_custom_styles
# Views dosyasındaki tüm yeni fonksiyonları içeri alıyoruz
from views import (
    render_intro_video, render_login, render_welcome, render_profile, 
    render_service_selection, render_jarvis, render_execution,
    render_logistics, render_marketing
)

# 1. Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff Enterprise", layout="wide", page_icon="AS")

# 2. Tasarımı Yükle
apply_custom_styles()

# 3. Session State Kontrolü
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "intro_watched" not in st.session_state:
    st.session_state["intro_watched"] = False
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "WELCOME"

# --- AKIŞ KONTROLÜ ---

# A. GİRİŞ YAPILMADIYSA -> LOGIN EKRANI
if not st.session_state["logged_in"]:
    render_login()

# B. GİRİŞ YAPILDI AMA INTRO İZLENMEDİ -> VİDEO
elif not st.session_state["intro_watched"]:
    render_intro_video()

# C. GİRİŞ YAPILDI VE VİDEO İZLENDİ -> ANA DASHBOARD
else:
    # --- GELİŞMİŞ SIDEBAR ---
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="font-family: 'Cinzel'; font-size: 40px; margin:0; color:#D4AF37;">AS</h1>
            <span style="font-size: 9px; letter-spacing: 3px; color: #888;">ENTERPRISE SYSTEM v5.2</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Menü Seçenekleri
        menu = st.radio("OPERASYON MERKEZİ", 
            [
                "🏠 DASHBOARD (Ana Ekran)", 
                "👤 PROFİL & ANALİZ", 
                "🧠 JARVIS (AI Manager)", 
                "📦 LOJİSTİK (Canlı Takip)", 
                "📈 PAZARLAMA (360°)",
                "🚀 HİZMET KURULUMU"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Alt Butonlar
        c1, c2 = st.columns(2)
        with c1:
            if st.button("↺ INTRO"):
                st.session_state["intro_watched"] = False
                st.rerun()
        with c2:
            if st.button("ÇIKIŞ"):
                st.session_state["logged_in"] = False
                st.rerun()

    # --- SAYFA YÖNLENDİRMELERİ ---
    if menu == "🏠 DASHBOARD (Ana Ekran)":
        render_welcome()
        
    elif menu == "👤 PROFİL & ANALİZ":
        render_profile()
        
    elif menu == "🧠 JARVIS (AI Manager)":
        render_jarvis()
        
    elif menu == "📦 LOJİSTİK (Canlı Takip)":
        render_logistics()
        
    elif menu == "📈 PAZARLAMA (360°)":
        render_marketing()
        
    elif menu == "🚀 HİZMET KURULUMU":
        # Alt sayfa kontrolü (Seçim mi Ödeme mi?)
        if st.session_state.get("current_page") == "EXECUTION":
            render_execution()
        else:
            render_service_selection()
