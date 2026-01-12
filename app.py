import streamlit as st
import google.generativeai as genai
from instructions import COMPANY_DATA

# Sayfa Yapılandırması
st.set_page_config(page_title="Jarvis 2.5 | Artificial Staff", page_icon="🤖", layout="centered")

# --- PREMIUM TEMA (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #E0E0E0;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
    }
    /* Kullanıcı mesaj balonu */
    [data-testid="stChatMessageUser"] {
        background-color: #1E2633 !important;
        border: 1px solid #30363D;
    }
    /* Jarvis mesaj balonu */
    [data-testid="stChatMessageAssistant"] {
        background-color: #0B0E14 !important;
        border-left: 5px solid #00D4FF;
    }
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    h1 {
        color: #00D4FF;
        font-family: 'Inter', sans-serif;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("ARTIFICIAL STAFF")
st.markdown("<p style='text-align: center; color: #888;'>Operasyonel Zeka - Jarvis v2.5</p>", unsafe_allow_html=True)

# API Ayarı
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('models/gemini-2.5-flash')

# Hafıza Yönetimi
if "messages" not in st.session_state:
    st.session_state.messages = []
    # İlk karşılama
    intro = "Selam! Ben Jarvis. Artificial Staff'e hoş geldin. Türkiye'deki gücümüzü Amerika'ya taşımak için buradayım. Hikayenizi merak ediyorum, isminiz nedir?"
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Sohbeti Görüntüle
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Giriş Alanı
if prompt := st.chat_input("Jarvis ile konuşun..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Jarvis'in daha önceki cevaplarını ve kimliğini hatırlaması için
        full_context = f"{COMPANY_DATA}\n\nSohbet Geçmişi:\n{st.session_state.messages}\n\nMüşterinin Son Yanıtı: {prompt}\n\nJarvis'in Vereceği Tek Soru:"
        
        try:
            response = model.generate_content(full_context)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Sistem hatası: {e}")

# Alt Bilgi
st.markdown("---")
st.caption("© 2026 Artificial Staff Global Operations. Tüm hakları saklıdır.")
