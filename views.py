# views.py
import streamlit as st
import time
import pandas as pd
import numpy as np
import random
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- YARDIMCI: STREAMING TEXT EFEKTİ ---
def stream_text(text):
    """Yazıyı daktilo gibi yazar"""
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(full_text + "▌")
        time.sleep(0.01) # Hız ayarı
    placeholder.markdown(full_text)

# --- 1. INTRO (FIXED) ---
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
    
    # Giriş Butonu
    st.markdown("<div style='position: fixed; bottom: 15%; left: 0; width: 100%; text-align: center; z-index: 10000;'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
         if st.button("SİSTEME GİRİŞ YAP", type="primary"):
            st.session_state["intro_watched"] = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. LOGIN (ADVANCED) ---
def render_login():
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #333; padding:40px; text-align:center; border-radius:12px; box-shadow:0 0 50px rgba(0,0,0,0.8);">
            <h1 style="color:#D4AF37 !important; font-family:'Cinzel';">AS</h1>
            <p style="font-size:10px; letter-spacing:4px; margin-bottom:20px;">ENTERPRISE ACCESS</p>
        </div>
        """, unsafe_allow_html=True)
        
        user = st.text_input("Kimlik ID", value="admin")
        pwd = st.text_input("Erişim Anahtarı", type="password", value="1234")
        
        if st.button("CONNECT TO MAINFRAME"):
            with st.spinner("Şifreli bağlantı kuruluyor..."):
                time.sleep(1.5) # Simüle edilmiş gecikme
                if user == "admin" and pwd == "1234":
                    st.session_state["logged_in"] = True
                    st.success("Yetki Doğrulandı.")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Erişim Reddedildi.")

# --- 3. ANA DASHBOARD (GRAFİKLİ) ---
def render_welcome():
    st.markdown("""
    <div class="glass-card">
        <h1 style="margin:0;">Global Operasyon Merkezi</h1>
        <p>Anlık Veri Akışı ve Pazar Analizi</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Üst Metrikler
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Toplam Ciro (Tahmini)", "$124,500", "+12%")
    m2.metric("Aktif Pazar", "US & CA", "2 Bölge")
    m3.metric("Ziyaretçi", "14.2K", "+8%")
    m4.metric("Dönüşüm Oranı", "3.2%", "+0.4%")
    
    st.divider()
    
    col_chart, col_news = st.columns([2, 1])
    
    with col_chart:
        st.subheader("📊 Satış Projeksiyonu (2026)")
        # Rastgele gerçekçi veri üretimi
        chart_data = pd.DataFrame(
            np.random.randn(20, 3) + [10, 15, 8],
            columns=['Amazon', 'Shopify', 'Walmart']
        )
        st.area_chart(chart_data, color=["#D4AF37", "#333333", "#666666"])
    
    with col_news:
        st.subheader("📡 Sistem Bildirimleri")
        st.info("📦 **Lojistik:** NJ deposuna 500 birim ürün giriş yaptı.")
        st.success("💰 **Finans:** Stripe ödemesi ($4,200) hesabınıza geçti.")
        st.warning("⚠️ **Stok:** 'Premium Havlu' stoğu kritik seviyede (%12).")

# --- 4. PROFİL & ANALİZ (DETAYLI) ---
def render_profile():
    st.markdown("## 🧬 Marka DNA Analizi")
    st.write("Yapay zeka, markanızın ABD pazarındaki potansiyelini hesaplayacak.")
    
    with st.form("advanced_kyc"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Marka İsmi")
            st.slider("Yatırım Bütçesi ($)", 1000, 100000, 5000)
            st.multiselect("Hedef Eyaletler", ["New York", "California", "Texas", "Florida", "Delaware"], ["Delaware"])
        with c2:
            st.selectbox("Sektör", ["Ev & Yaşam", "Moda", "Teknoloji", "Kozmetik", "Gıda"])
            st.radio("Lojistik Tercihi", ["Hava Kargo (Hızlı)", "Deniz Kargo (Ekonomik)", "Hibrit"])
            
        if st.form_submit_button("ANALİZİ BAŞLAT"):
            progress_text = "Veriler işleniyor..."
            my_bar = st.progress(0, text=progress_text)
            
            for percent_complete in range(100):
                time.sleep(0.02)
                my_bar.progress(percent_complete + 1, text=f"Rakip analizi yapılıyor... %{percent_complete}")
            
            st.success("Analiz Tamamlandı! Başarı Skoru: 87/100")
            time.sleep(1)
            st.session_state["current_page"] = "SERVICE_SELECT"
            st.rerun()

# --- 5. JARVIS (STREAMING EFFECT) ---
def render_jarvis():
    st.markdown("## 🧠 Jarvis Neural Interface")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Jarvis Online. Stratejik planlama için hazırım."}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Jarvis'e talimat verin..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # Brain.py'den cevap al ama burada animasyonlu yazdır
            response_text = get_ai_response(st.session_state.messages)
            stream_text(response_text)
            
        st.session_state.messages.append({"role": "assistant", "content": response_text})

# --- 6. LOJİSTİK (HARİTALI) ---
def render_logistics():
    st.markdown("## 📦 Global Lojistik Takibi")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Harita Verisi (Simülasyon: İstanbul -> NY rotası)
        map_data = pd.DataFrame({
            'lat': [41.0082, 40.7128, 38.9072],
            'lon': [28.9784, -74.0060, -77.0369],
            'size': [100, 500, 200] # Nokta büyüklüğü
        })
        st.map(map_data, zoom=2, color="#D4AF37")
        
    with col2:
        st.markdown("### Aktif Gönderiler")
        st.markdown("""
        <div class="glass-card">
            <strong>TR-IST-092</strong><br>
            <span style="color:#0f0;">● Yolda (Air Cargo)</span><br>
            <small>Varış: 2 Gün</small>
        </div>
        <div class="glass-card">
            <strong>US-NYC-881</strong><br>
            <span style="color:#D4AF37;">● Gümrükte</span><br>
            <small>Liman: NJ Port</small>
        </div>
        """, unsafe_allow_html=True)

# --- 7. PAZARLAMA (MOCKUP) ---
def render_marketing():
    st.markdown("## 📈 360° Pazarlama Paneli")
    
    tab1, tab2, tab3 = st.tabs(["Google Ads", "Meta (Instagram)", "Influencer"])
    
    with tab1:
        st.metric("ROAS (Reklam Getirisi)", "4.2X", "+0.5")
        st.line_chart([1, 2, 2.5, 3, 4, 3.8, 5, 6], color="#4285F4")
        
    with tab2:
        st.write("Son Gönderi Etkileşimi")
        col_a, col_b = st.columns(2)
        col_a.image("https://images.unsplash.com/photo-1542291026-7eec264c27ff", caption="Viral Kampanya #1")
        col_b.bar_chart({"Beğeni": 1200, "Kaydetme": 450, "Paylaşım": 300}, color="#E1306C")

# --- 8. DİĞER (Servis Seçimi ve Kurulum) ---
def render_service_selection():
    st.markdown("## 🧭 Paket Seçimi")
    c1, c2 = st.columns(2)
    with c1:
        st.info("🚀 STARTUP PACK - $1500")
        if st.button("SEÇ: STARTUP"):
            st.session_state["current_page"] = "EXECUTION"
            st.rerun()
    with c2:
        st.success("💎 ENTERPRISE PACK - $2500")
        if st.button("SEÇ: ENTERPRISE"):
            st.session_state["current_page"] = "EXECUTION"
            st.rerun()

def render_execution():
    st.markdown("## ⚙️ Kurulum İşlemleri")
    st.write("Ödeme altyapısı yükleniyor...")
    with st.expander("Sözleşme"):
        st.write("Madde 1...")
    if st.button("ÖDEMEYİ TAMAMLA"):
        st.balloons()
        st.success("Tebrikler! Artificial Staff ailesine hoş geldiniz.")
