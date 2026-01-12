# views.py
import streamlit as st
import time
import pandas as pd
import numpy as np
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- YARDIMCI: STREAMING TEXT EFEKTİ ---
def stream_text(text):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(full_text + "▌")
        time.sleep(0.015) 
    placeholder.markdown(full_text)

# --- 1. INTRO VIDEO ---
def render_intro_video():
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-technological-interface-hud-9844-large.mp4"
    
    html_code = f"""
    <style>
        .intro-container {{ position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: black; z-index: 9999; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
        .intro-video {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.4; }}
        .intro-content {{ z-index: 10; text-align: center; color: white; }}
        .intro-title {{ font-family: 'Cinzel', serif; font-size: 70px; margin: 0; text-shadow: 0 0 30px rgba(212,175,55,0.5); }}
    </style>
    <div class="intro-container">
        <video autoplay muted loop playsinline class="intro-video"><source src="{video_url}" type="video/mp4"></video>
        <div class="intro-content">
            <h1 class="intro-title">ARTIFICIAL STAFF</h1>
            <p style="color:#D4AF37; letter-spacing:8px; font-size:14px; margin-top:10px;">BEYOND BORDERS</p>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    
    st.markdown("<div style='position: fixed; bottom: 15%; left: 0; width: 100%; text-align: center; z-index: 10000;'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,1,1])
    with c2:
         if st.button("SİSTEME GİRİŞ YAP", type="primary"):
            st.session_state["intro_watched"] = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. LOGIN ---
def render_login():
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #333; padding:40px; text-align:center; border-radius:12px; border-top: 4px solid #D4AF37;">
            <h1 style="color:#D4AF37 !important; font-family:'Cinzel'; font-size: 50px; margin:0;">AS</h1>
            <p style="font-size:10px; letter-spacing:4px; margin-bottom:20px; color:#888;">ENTERPRISE ACCESS</p>
        </div>
        """, unsafe_allow_html=True)
        
        user = st.text_input("Kimlik ID", value="admin")
        pwd = st.text_input("Erişim Anahtarı", type="password", value="1234")
        
        if st.button("BAĞLANTI KUR"):
            if user == "admin" and pwd == "1234":
                st.session_state["logged_in"] = True
                st.success("Yetki Doğrulandı.")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Erişim Reddedildi.")

# --- 3. ANA DASHBOARD ---
def render_welcome():
    st.markdown("""
    <div class="glass-card">
        <h1 style="margin:0;">Global Operasyon Merkezi</h1>
        <p>Anlık Veri Akışı ve Pazar Analizi</p>
    </div>
    """, unsafe_allow_html=True)
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Toplam Ciro (Tahmini)", "$124,500", "+12%")
    m2.metric("Aktif Pazar", "US & CA", "2 Bölge")
    m3.metric("Ziyaretçi", "14.2K", "+8%")
    m4.metric("Dönüşüm", "3.2%", "+0.4%")
    
    st.divider()
    
    col_chart, col_news = st.columns([2, 1])
    with col_chart:
        st.subheader("📊 Satış Projeksiyonu")
        data = pd.DataFrame(np.random.randn(20, 3) + [10, 15, 8], columns=['Amazon', 'Shopify', 'Walmart'])
        st.area_chart(data, color=["#D4AF37", "#333333", "#666666"])
    
    with col_news:
        st.subheader("📡 Bildirimler")
        st.info("📦 **Lojistik:** NJ deposuna giriş yapıldı.")
        st.success("💰 **Finans:** $4,200 transfer tamamlandı.")
        st.warning("⚠️ **Stok:** Havlu stoğu %12.")

# --- 4. PROFİL & ANALİZ ---
def render_profile():
    st.markdown("## 🧬 Marka Analizi")
    with st.form("kyc"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Marka İsmi")
            st.slider("Bütçe ($)", 1000, 100000, 5000)
        with c2:
            st.selectbox("Sektör", ["Ev & Yaşam", "Moda", "Teknoloji"])
            st.multiselect("Hedef", ["Amazon", "Etsy", "Walmart"])
            
        if st.form_submit_button("ANALİZİ BAŞLAT"):
            bar = st.progress(0, "Veriler işleniyor...")
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i+1)
            st.success("Analiz Tamamlandı! Skor: 87/100")

# --- 5. JARVIS (AI) ---
def render_jarvis():
    st.markdown("## 🧠 Jarvis Neural Interface")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": COMPANY_DATA}]
        st.session_state.messages.append({"role": "assistant", "content": "Jarvis Online."})

    for msg in st.session_state.messages:
        if msg["role"] == "system": continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Talimat verin..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response_text = get_ai_response(st.session_state.messages)
            stream_text(response_text)
            
        st.session_state.messages.append({"role": "assistant", "content": response_text})

# --- 6. LOJİSTİK (HARİTA) ---
def render_logistics():
    st.markdown("## 📦 Global Lojistik")
    c1, c2 = st.columns([3, 1])
    with c1:
        # Örnek Rota: İstanbul -> New York -> Washington
        df = pd.DataFrame({'lat': [41.0082, 40.7128, 38.9072], 'lon': [28.9784, -74.0060, -77.0369]})
        st.map(df, zoom=1, color="#D4AF37")
    with c2:
        st.success("TR-IST-92: Yolda ✈️")
        st.warning("US-NY-81: Gümrükte ⚓")

# --- 7. PAZARLAMA ---
def render_marketing():
    st.markdown("## 📈 360° Pazarlama")
    tab1, tab2 = st.tabs(["Performans", "Sosyal Medya"])
    with tab1:
        st.line_chart([1, 3, 2, 4, 5, 4, 6, 7], color="#D4AF37")
    with tab2:
        st.bar_chart({"Instagram": 1200, "TikTok": 2500}, color="#E1306C")

# --- 8. KURULUM ---
def render_service_selection():
    st.markdown("## 🧭 Paket Seçimi")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("STARTUP ($1500)"):
            st.session_state["current_page"] = "EXECUTION"
            st.rerun()
    with c2:
        if st.button("ENTERPRISE ($2500)"):
            st.session_state["current_page"] = "EXECUTION"
            st.rerun()

def render_execution():
    st.markdown("## ⚙️ Kurulum")
    st.write("Ödeme Sayfası...")
    if st.button("ÖDEMEYİ TAMAMLA"):
        st.balloons()
        st.success("Tebrikler!")
