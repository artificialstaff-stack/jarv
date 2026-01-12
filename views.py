# views.py
import streamlit as st
import time
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- INTRO VIDEO OYNATICI ---
def render_intro_video():
    # Video URL (Arka plan için kaliteli abstract video)
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-technological-interface-hud-9844-large.mp4"
    
    # HTML KODUNU DÜZGÜN BİR ŞEKİLDE RENDER ET
    st.markdown(f"""
    <div class="intro-overlay">
        <video autoplay muted loop playsinline class="intro-bg-video">
            <source src="{video_url}" type="video/mp4">
        </video>
        
        <div class="intro-text-wrapper">
            <h1 style="font-family: 'Cinzel', serif; font-size: 60px; color: #fff; margin: 0;">ARTIFICIAL STAFF</h1>
            <p style="color: #D4AF37; letter-spacing: 5px; font-size: 14px; text-transform: uppercase; margin-top: 10px;">
                2026 Vision Enterprise
            </p>
            <hr style="border-color: rgba(255,255,255,0.2); width: 50%; margin: 20px auto;">
            <p style="color: #ccc; font-size: 18px; max-width: 600px; line-height: 1.6;">
                Sıradan olanı terk edin. İşletmenizi Dolar ($) kazanan global bir güce dönüştürün.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Butonu HTML'in üzerine bindirmek için Streamlit kolonu kullanıyoruz
    # CSS ile bu butonu ekranın ortasına/altına itiyoruz
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        # Butonu videonun üstüne çıkarmak için boşluk bırakıyoruz
        st.markdown("<div style='height: 70vh;'></div>", unsafe_allow_html=True)
        if st.button("SİSTEME GİRİŞ YAP [ENTER SYSTEM]", type="primary"):
            st.session_state["intro_watched"] = True
            st.rerun()

# --- LOGIN EKRANI ---
def render_login():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div class="login-box">
            <h1 style="color:#D4AF37 !important; font-family: 'Cinzel', serif; font-size: 50px; margin:0;">AS</h1>
            <p style="color:#666; font-size: 10px; letter-spacing: 3px; margin-bottom: 30px;">ENTERPRISE ACCESS</p>
        </div>
        """, unsafe_allow_html=True)
        
        username = st.text_input("Kullanıcı Adı", placeholder="admin")
        password = st.text_input("Şifre", type="password", placeholder="1234")
        
        if st.button("GİRİŞ YAP"):
            if username == "admin" and password == "1234":
                st.session_state["logged_in"] = True
                st.session_state["intro_watched"] = False
                st.success("Giriş Başarılı.")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Hatalı Şifre.")

# --- MİNİ PLAYER (SAĞ ALT) ---
def render_mini_player():
    st.markdown("""
    <div style="position: fixed; bottom: 20px; right: 20px; width: 180px; z-index: 9990; 
                background: #000; border: 1px solid #333; border-radius: 8px; padding: 5px; opacity: 0.8;">
        <p style="color: #D4AF37; font-size: 9px; text-align: center; margin: 0 0 5px 0;">● REPLAY INTRO</p>
        <video autoplay muted loop style="width: 100%; border-radius: 4px;">
            <source src="https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-technological-interface-hud-9844-large.mp4" type="video/mp4">
        </video>
    </div>
    """, unsafe_allow_html=True)

# --- ANA DASHBOARD ---
def render_welcome():
    render_mini_player() # Mini player'ı göster
    
    st.markdown("""
    <div>
        <span style="color:#D4AF37; font-size:12px; letter-spacing:2px;">01 // DASHBOARD</span>
        <h1 style="font-size: 48px; margin-top:0;">Global Entegrasyon</h1>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("Misyon: 'TL Gider, Dolar Gelir' modelini şirketinize entegre etmek.")
    with c2:
        if st.button("PROFİL KURULUMUNA BAŞLA ->"):
            st.session_state["current_page"] = "PROFILE"
            st.rerun()

# --- DİĞER FONKSİYONLAR (Eski kodlarınızla aynı kalabilir) ---
def render_profile():
    st.markdown("## 👤 Profil")
    st.write("Marka bilgilerinizi giriniz.")
    if st.button("Kaydet ve İlerle"):
        st.session_state["current_page"] = "SERVICE_SELECT"
        st.rerun()

def render_service_selection():
    st.markdown("## 🧭 Paket Seçimi")
    st.write("Paketinizi seçin.")
    if st.button("Startup Paketi"):
        st.session_state["selected_plan"] = "Startup"
        st.session_state["current_page"] = "EXECUTION"
        st.rerun()

def render_execution():
    st.markdown("## 🚀 Kurulum")
    st.write("İşlemler başlatılıyor...")

def render_jarvis():
    st.markdown("## 🧠 Jarvis AI")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    prompt = st.chat_input("Sorunuzu yazın...")
    if prompt:
        st.write(f"User: {prompt}")
        st.write("Jarvis: Anlaşıldı.")
