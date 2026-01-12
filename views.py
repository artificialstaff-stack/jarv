# views.py
import streamlit as st
import time
import pandas as pd
import numpy as np
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- YARDIMCI: HARF HARF YAZMA EFEKTİ ---
def stream_text(text):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(full_text + "▌")
        time.sleep(0.01) 
    placeholder.markdown(full_text)

# --- 1. INTRO VIDEO (KESİN ÇÖZÜM) ---
def render_intro_video():
    video_url = "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-technological-interface-hud-9844-large.mp4"
    
    # 1. Arka Planı ve Yazıları Oluştur (Z-Index: 0)
    st.markdown(f"""
    <style>
        /* Kenar çubuğunu ve üst barı gizle */
        section[data-testid="stSidebar"] {{ display: none !important; }}
        header {{ display: none !important; }}
        
        /* Video Konteyneri */
        .intro-container {{
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: #000;
            z-index: 0; /* En altta */
            display: flex; flex-direction: column; align-items: center; justify-content: center;
        }}
        .intro-video {{
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            object-fit: cover; opacity: 0.4;
        }}
        .intro-content {{
            z-index: 1; position: relative; text-align: center; margin-bottom: 100px;
        }}
        
        /* BUTONU ZORLA EN ÜSTE TAŞIYAN CSS */
        .stButton {{
            position: fixed !important;
            bottom: 20% !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            z-index: 99999 !important; /* En üstte */
            width: auto !important;
        }}
        .stButton > button {{
            background: rgba(0,0,0,0.7) !important;
            border: 2px solid #D4AF37 !important;
            color: #D4AF37 !important;
            font-size: 20px !important;
            padding: 15px 50px !important;
            font-family: 'Cinzel', serif !important;
            text-transform: uppercase !important;
            letter-spacing: 3px !important;
            transition: all 0.3s ease !important;
        }}
        .stButton > button:hover {{
            background: #D4AF37 !important;
            color: #000 !important;
            box-shadow: 0 0 40px #D4AF37 !important;
        }}
    </style>
    
    <div class="intro-container">
        <video autoplay muted loop playsinline class="intro-video">
            <source src="{video_url}" type="video/mp4">
        </video>
        <div class="intro-content">
            <h1 style="font-family: 'Cinzel', serif; font-size: 70px; color: white; text-shadow: 0 0 30px rgba(212,175,55,0.6); margin:0;">ARTIFICIAL STAFF</h1>
            <p style="color:#D4AF37; letter-spacing:8px; font-size:14px; margin-top:10px;">BEYOND BORDERS</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Butonu Normal Olarak Ekle (CSS bunu yakalayıp yukarı taşıyacak)
    if st.button("SİSTEME GİRİŞ YAP"):
        st.session_state["intro_watched"] = True
        st.rerun()

# --- 2. LOGIN ---
def render_login():
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background:#050505; border:1px solid #222; padding:40px; text-align:center; border-radius:12px; border-top: 4px solid #D4AF37;">
            <h1 style="color:#D4AF37 !important; font-family:'Cinzel'; font-size: 50px; margin:0;">AS</h1>
            <p style="font-size:10px; letter-spacing:4px; margin-bottom:20px; color:#666;">ENTERPRISE ACCESS</p>
        </div>
        """, unsafe_allow_html=True)
        
        user = st.text_input("Kullanıcı Adı", value="admin")
        pwd = st.text_input("Şifre", type="password", value="1234")
        
        if st.button("BAĞLAN"):
            if user == "admin" and pwd == "1234":
                st.session_state["logged_in"] = True
                st.success("Doğrulandı.")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Hatalı Giriş.")

# --- 3. DASHBOARD ---
def render_welcome():
    st.markdown("""
    <div class="glass-card">
        <h1 style="margin:0;">Global Operasyon Merkezi</h1>
        <p>Anlık Veri Akışı ve Pazar Analizi</p>
    </div>
    """, unsafe_allow_html=True)
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Ciro", "$124,500", "+12%")
    m2.metric("Bölge", "US & CA", "2")
    m3.metric("Ziyaretçi", "14.2K", "+8%")
    m4.metric("Dönüşüm", "3.2%", "+0.4%")
    
    st.divider()
    
    c_chart, c_news = st.columns([2, 1])
    with c_chart:
        st.subheader("📊 Satış Trendi")
        data = pd.DataFrame(np.random.randn(20, 3) + [10, 15, 8], columns=['AMZ', 'Shopify', 'Walmart'])
        st.area_chart(data, color=["#D4AF37", "#333", "#666"])
    
    with c_news:
        st.subheader("📡 Bildirimler")
        st.info("📦 NJ Deposuna ürün girişi.")
        st.success("💰 Stripe ödemesi alındı.")
        st.warning("⚠️ Stok uyarısı.")

# --- 4. PROFİL ---
def render_profile():
    st.markdown("## 🧬 Marka Analizi")
    with st.form("kyc"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Marka Adı")
            st.slider("Bütçe", 1000, 100000, 5000)
        with c2:
            st.selectbox("Sektör", ["Ev", "Moda", "Teknoloji"])
            st.multiselect("Hedef", ["Amazon", "Etsy"])
            
        if st.form_submit_button("ANALİZ ET"):
            bar = st.progress(0, "İşleniyor...")
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i+1)
            st.success("Tamamlandı: Skor 87/100")

# --- 5. JARVIS ---
def render_jarvis():
    st.markdown("## 🧠 Jarvis AI")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": COMPANY_DATA}]
        st.session_state.messages.append({"role": "assistant", "content": "Jarvis Online."})

    for msg in st.session_state.messages:
        if msg["role"] == "system": continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Mesaj yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            resp = get_ai_response(st.session_state.messages)
            stream_text(resp)
        st.session_state.messages.append({"role": "assistant", "content": resp})

# --- 6. LOJİSTİK ---
def render_logistics():
    st.markdown("## 📦 Lojistik Takip")
    c1, c2 = st.columns([3, 1])
    with c1:
        df = pd.DataFrame({'lat': [41.0082, 40.7128], 'lon': [28.9784, -74.0060]})
        st.map(df, zoom=1, color="#D4AF37")
    with c2:
        st.success("TR->US: Yolda ✈️")

# --- 7. PAZARLAMA ---
def render_marketing():
    st.markdown("## 📈 Pazarlama")
    st.bar_chart({"IG": 1200, "TikTok": 2500}, color="#D4AF37")

# --- 8. KURULUM ---
def render_service_selection():
    st.markdown("## 🧭 Paket Seçimi")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("STARTUP - $1500"):
            st.session_state["current_page"] = "EXECUTION"
            st.rerun()
    with c2:
        if st.button("ENTERPRISE - $2500"):
            st.session_state["current_page"] = "EXECUTION"
            st.rerun()

def render_execution():
    st.markdown("## ⚙️ Kurulum")
    if st.button("ÖDEMEYİ TAMAMLA"):
        st.balloons()
        st.success("Hoş Geldiniz!")
