# views.py
import streamlit as st
import time
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- INTRO VIDEO (DÜZELTİLMİŞ) ---
def render_intro_video():
    # Video URL
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-technological-interface-hud-9844-large.mp4"
    
    # KESİN ÇÖZÜM: CSS Parantezlerini {{ }} yaparak kaçış karakteri kullandık
    html_code = f"""
    <style>
        .intro-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: black;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }}
        .intro-video {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.4;
        }}
        .intro-text {{
            z-index: 10;
            position: relative;
            text-align: center;
            color: white;
            padding: 20px;
        }}
        .intro-title {{
            font-family: 'Cinzel', serif;
            font-size: 60px;
            color: #fff;
            margin: 0;
            text-shadow: 0 0 20px rgba(0,0,0,0.8);
        }}
        .intro-subtitle {{
            color: #D4AF37;
            letter-spacing: 5px;
            font-size: 16px;
            text-transform: uppercase;
            margin-top: 10px;
            font-weight: bold;
        }}
    </style>

    <div class="intro-container">
        <video autoplay muted loop playsinline class="intro-video">
            <source src="{video_url}" type="video/mp4">
        </video>
        <div class="intro-text">
            <h1 class="intro-title">ARTIFICIAL STAFF</h1>
            <p class="intro-subtitle">2026 Vision Enterprise</p>
            <hr style="border-color: rgba(255,255,255,0.2); width: 200px; margin: 20px auto;">
            <p style="color: #ccc; font-size: 18px; max-width: 600px; line-height: 1.6;">
                Sıradan olanı terk edin. İşletmenizi Dolar ($) kazanan global bir güce dönüştürün.
            </p>
        </div>
    </div>
    """
    
    # HTML'i Render Et
    st.markdown(html_code, unsafe_allow_html=True)

    # Buton için boşluk bırak ve butonu ekle
    st.markdown("<div style='position: fixed; bottom: 100px; left: 0; width: 100%; text-align: center; z-index: 10000;'>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
         if st.button("SİSTEME GİRİŞ YAP / ENTER SYSTEM", type="primary"):
            st.session_state["intro_watched"] = True
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

# --- LOGIN ---
def render_login():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div class="login-box">
            <h1 style="color:#D4AF37 !important; font-family: 'Cinzel', serif; font-size: 50px; margin: 0;">AS</h1>
            <p style="letter-spacing: 3px; font-size: 10px; margin-bottom: 30px; color: #666;">ARTIFICIAL STAFF | ENTERPRISE ACCESS</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: center; margin-bottom: 10px; color: #888;'>Giriş Yapın</div>", unsafe_allow_html=True)
        username = st.text_input("Kullanıcı Adı", placeholder="admin")
        password = st.text_input("Şifre", type="password", placeholder="1234")
        
        if st.button("GİRİŞ YAP"):
            if username == "admin" and password == "1234": 
                st.session_state["logged_in"] = True
                st.session_state["intro_watched"] = False
                st.success("Erişim İzni Verildi...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Hatalı Kimlik Bilgileri.")

# --- MİNİ PLAYER ---
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
    
    with st.sidebar:
        st.markdown("---")
        if st.button("↺ INTRO TEKRAR İZLE"):
            st.session_state["intro_watched"] = False
            st.rerun()

# --- ANA EKRANLAR ---
def render_welcome():
    render_mini_player()
    st.markdown("""
    <div>
        <span style="color:#D4AF37; letter-spacing:2px; font-size:12px;">01 // DASHBOARD</span>
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

def render_profile():
    st.markdown("## 👤 Marka & Profil Analizi")
    with st.form("kyc_form"):
        st.text_input("Marka Adı")
        st.text_input("Yetkili Ad Soyad")
        if st.form_submit_button("ANALİZİ TAMAMLA"):
            st.session_state["current_page"] = "SERVICE_SELECT"
            st.rerun()

def render_service_selection():
    st.markdown("## 🧭 Paket Seçimi")
    c1, c2 = st.columns(2)
    with c1:
        st.write("### STARTUP PACK")
        if st.button("SEÇ: STARTUP ($1500)"):
            st.session_state["selected_plan"] = "Startup"
            st.session_state["current_page"] = "EXECUTION"
            st.rerun()
    with c2:
        st.write("### ENTERPRISE PACK")
        if st.button("SEÇ: ENTERPRISE ($2500)"):
            st.session_state["selected_plan"] = "Enterprise"
            st.session_state["current_page"] = "EXECUTION"
            st.rerun()

def render_jarvis():
    st.markdown("## 🧠 Jarvis AI")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": COMPANY_DATA}]
        st.session_state.messages.append({"role": "assistant", "content": "Jarvis Online."})
    
    for msg in st.session_state.messages:
        if msg["role"] == "system": continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Sorunuzu yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            response = get_ai_response(st.session_state.messages)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

def render_execution():
    st.markdown("## ⚙️ Kurulum İşlemleri")
    st.write("Operasyon başlatılıyor...")
