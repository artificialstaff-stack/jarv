import streamlit as st
import sys
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

# Brain modülünü (logic klasöründeyse veya aynı dizindeyse) çağır
try:
    import brain
except ImportError:
    # Eğer klasör yapısı farklıysa logic klasörünü ekle
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))
    import brain

# 1. SAYFA AYARLARI
st.set_page_config(
    page_title="ARTIS | AI OS",
    page_icon="🤖",
    layout="wide", # Geniş ekran
    initial_sidebar_state="expanded"
)

# 2. CSS (ChatGPT Tarzı Menü ve Dark Mode)
st.markdown("""
<style>
    /* Ana Arkaplan */
    .stApp {
        background-color: #343541; /* ChatGPT Koyu Gri */
        color: #ECECF1;
    }
    
    /* Sidebar (Sol Menü) */
    section[data-testid="stSidebar"] {
        background-color: #202123; /* Daha koyu gri */
    }
    
    /* Menüdeki Radio Butonlarını Buton gibi göster */
    .stRadio > div {
        background-color: transparent;
    }
    .stRadio label {
        color: #ECECF1 !important;
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
        transition: 0.3s;
    }
    .stRadio label:hover {
        background-color: #2A2B32;
    }
    
    /* Chat Input */
    .stChatInput {
        position: fixed;
        bottom: 20px;
        width: 70% !important;
        left: 50%;
        transform: translateX(-50%);
    }

    /* Başlık Gizle */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. OTURUM VE HAFIZA (SESSION STATE)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Merhaba. Ben ARTIS. Washington DC operasyon merkezine hoş geldiniz. Markanızın adı nedir?"}
    ]

# 4. SOL MENÜ (NAVIGASYON)
with st.sidebar:
    st.markdown("<h2 style='color:#fff; text-align:center;'>ARTIS v2.5</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # SAYFA SEÇİCİ (MENÜ BURADA)
    selected_page = st.radio(
        "MENÜ",
        ["💬 SOHBET (AI)", "📊 FİNANS", "✈️ LOJİSTİK"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Sohbeti Temizle Butonu (Sadece sohbetteyken göster)
    if selected_page == "💬 SOHBET (AI)":
        if st.button("🗑️ Yeni Sohbet", type="primary"):
            st.session_state.messages = []
            st.rerun()

    st.markdown("<div style='position:fixed; bottom:20px; color:#666; font-size:12px;'>Washington DC Hub: 🟢 ONLINE</div>", unsafe_allow_html=True)


# 5. SAYFA YÖNLENDİRİCİSİ (ROUTER)

# --- SAYFA 1: SOHBET (CHAT) ---
if selected_page == "💬 SOHBET (AI)":
    # Başlık
    st.markdown("<h1 style='text-align: center; color: #ECECF1;'>ARTIS AI</h1>", unsafe_allow_html=True)
    
    # Mesajları Göster
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Yeni Mesaj Girişi
    if prompt := st.chat_input("Operasyon hakkında danışın..."):
        # Kullanıcı mesajını ekle
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Asistan Cevabı (Streaming)
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            
            # Brain modülünden cevap al (Eğer brain.py yoksa hata vermesin)
            try:
                # Burada streaming simülasyonu yapıyoruz (Brain'deki generator fonksiyonu)
                stream_generator = brain.get_streaming_response(st.session_state.messages)
                for chunk in stream_generator:
                    full_response += chunk
                    response_placeholder.markdown(full_response + "▌")
                response_placeholder.markdown(full_response)
            except Exception as e:
                full_response = "Bağlantı hatası veya Brain modülü eksik. Lütfen API ayarlarını kontrol edin."
                response_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})


# --- SAYFA 2: FİNANS ---
elif selected_page == "📊 FİNANS":
    st.title("📊 Finansal Öngörü")
    st.markdown("---")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Tahmini Ciro", "$45,000", "+24%")
    c2.metric("Net Kâr", "%32", "+4%")
    c3.metric("Reklam Gideri", "$4,200", "-12%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    try:
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
    except:
        st.warning("Grafik yüklenemedi. brain.py dosyasını kontrol edin.")


# --- SAYFA 3: LOJİSTİK ---
elif selected_page == "✈️ LOJİSTİK":
    st.title("✈️ Global Lojistik Ağı")
    st.info("Rota: İstanbul (IST) ➔ Washington DC (IAD)")
    
    try:
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
        st.success("Washington DC Depo: Kapasite Uygun (%12 Dolu)")
    except:
        st.warning("Harita yüklenemedi. brain.py dosyasını kontrol edin.")
