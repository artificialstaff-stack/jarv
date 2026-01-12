# views.py
import streamlit as st
import time
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- INTRO VIDEO OYNATICI (Tam Ekran) ---
def render_intro_video():
    # Bu fonksiyon çağrıldığında arayüzü gizler ve sadece videoyu gösterir
    
    # 1. Video URL (Örnek: Yüksek kaliteli abstract tech background)
    # Kendi sunucunuzdaki mp4 linkini buraya koyabilirsiniz.
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-technological-interface-hud-9844-large.mp4"
    
    st.markdown(f"""
    <div class="intro-overlay">
        <video autoplay muted loop class="intro-bg-video">
            <source src="{video_url}" type="video/mp4">
        </video>
        
        <div class="intro-content">
            <h1 style="font-size: 80px; margin-bottom: 10px; font-family: 'Cinzel', serif;">ARTIFICIAL STAFF</h1>
            <p style="font-size: 24px; letter-spacing: 5px; color: #D4AF37; text-transform: uppercase;">2026 Vision Enterprise</p>
            <br>
            <p style="max-width: 600px; margin: 0 auto; color: #ccc; font-size: 16px; line-height: 1.6;">
                Sıradan olanı terk edin. İşletmenizi Dolar ($) kazanan global bir güce dönüştürün.
                Yapay zeka, hukuk ve lojistik tek bir merkezde.
            </p>
            <br><br><br>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Butonu Streamlit native yapıyoruz ki Python state değişebilsin
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.markdown("<br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True) # Boşluk
        if st.button("OPERASYONU BAŞLAT [ENTER SYSTEM]", type="primary"):
            st.session_state["intro_watched"] = True
            st.rerun()

# --- MİNİ PLAYER WIDGET (Sağ Alt Köşe) ---
def render_mini_player():
    # Sadece dashboard'da görünür
    st.markdown("""
    <div class="mini-player-widget" onclick="window.parent.location.reload();">
        <span class="mini-label">● 2026 VISION REPLAY</span>
        <div style="width: 100%; height: 100px; background: #000; overflow: hidden; position: relative;">
            <video autoplay muted loop style="width: 100%; opacity: 0.6;">
                <source src="https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-technological-interface-hud-9844-large.mp4" type="video/mp4">
            </video>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #fff; font-size: 20px;">
                ▶
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Not: Widget'a tıklama olayını yakalamak için sidebar'a bir buton koymak daha sağlıklıdır.
    # HTML click eventi Streamlit'i tetiklemez. O yüzden aşağıya bir buton ekliyoruz:
    with st.sidebar:
        st.markdown("---")
        if st.button("🔄 INTRO TEKRAR İZLE"):
            st.session_state["intro_watched"] = False
            st.rerun()

# --- LOGIN ---
def render_login():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div class="login-container">
            <h1 style="color:#D4AF37 !important; font-size: 50px; margin: 0; font-family: 'Cinzel', serif;">AS</h1>
            <p style="letter-spacing: 3px; font-size: 10px; margin-bottom: 30px; color: #666;">ARTIFICIAL STAFF | ENTERPRISE ACCESS</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: center; margin-bottom: 10px; color: #888;'>Giriş Yapın</div>", unsafe_allow_html=True)
        username = st.text_input("Kullanıcı Adı", placeholder="admin")
        password = st.text_input("Şifre", type="password", placeholder="1234")
        
        if st.button("SİSTEME GİRİŞ YAP"):
            if username == "admin" and password == "1234": 
                st.session_state["logged_in"] = True
                st.session_state["intro_watched"] = False # Giriş yapınca Intro başlasın
                st.success("Erişim İzni Verildi...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Hatalı Kimlik Bilgileri.")

# --- DİĞER EKRANLAR (Aynı kalabilir, sadece intro kontrolü eklenecek) ---

def render_welcome():
    # Burası artık Dashboard'un ana sayfası.
    # Mini player'ı burada çağırıyoruz.
    render_mini_player() 

    st.markdown("""
    <div>
        <span style="color:#D4AF37; letter-spacing:2px; font-size:12px;">01 // DASHBOARD</span>
        <h1 style="font-size: 48px; margin-top:0;">Global Entegrasyon</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Misyonumuz")
        st.info("Tek merkezden 9 farklı hizmet ile 'TL Gider, Dolar Gelir' modelini şirketinize entegre etmek.")
    with col2:
        st.markdown("### Sonraki Adım")
        st.write("Sizi ve markanızı tanımamız için lütfen profil kurulumunu tamamlayın.")
        if st.button("PROFİL KURULUMUNA BAŞLA ->"):
            st.session_state["current_page"] = "PROFILE"
            st.rerun()

# (render_profile, render_service_selection, render_jarvis, render_execution FONKSİYONLARI AYNEN KALSIN)
# Sadece import hataları olmaması için buraya kısaca ekliyorum, siz eskilerini koruyun:

def render_profile():
    st.markdown("## 👤 Marka & Profil Analizi")
    with st.form("kyc_form"):
        st.text_input("Marka Adı")
        if st.form_submit_button("ANALİZİ TAMAMLA"):
            st.session_state["current_page"] = "SERVICE_SELECT"
            st.rerun()

def render_service_selection():
    st.markdown("## 🧭 Paket Seçimi")
    if st.button("SEÇ: STARTUP"):
        st.session_state["selected_plan"] = "Startup"
        st.session_state["current_page"] = "EXECUTION"
        st.rerun()

def render_jarvis():
    st.markdown("## 🧠 Jarvis")
    # ... (Eski kodlar)

def render_execution():
    st.markdown("## ⚙️ Kurulum")
    # ... (Eski kodlar)
