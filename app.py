import streamlit as st
import google.generativeai as genai
from instructions import COMPANY_DATA

# Sayfa Ayarları (Premium Görünüm)
st.set_page_config(page_title="Jarvis v2.5 | Artificial Staff", page_icon="🏦", layout="wide")

# --- 2026 PRESTIGE INTERFACE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;500&display=swap');
    
    .stApp { background: #050505; color: #E0E0E0; font-family: 'Inter', sans-serif; }
    
    /* Başlık Tasarımı */
    .brand-header {
        font-family: 'Cinzel', serif;
        font-size: 3rem;
        text-align: center;
        background: linear-gradient(180deg, #FFFFFF 0%, #B89B5E 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 10px;
        margin-top: 20px;
        font-weight: 700;
    }

    /* Mesaj Balonları: Lüks ve Sade */
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.02) !important;
        border: none !important;
        border-left: 2px solid #B89B5E !important;
        margin-bottom: 25px;
    }

    /* Giriş Alanı */
    .stChatInputContainer input {
        border: none !important;
        border-bottom: 1px solid #B89B5E !important;
        background: transparent !important;
        border-radius: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="brand-header">ARTIFICIAL STAFF</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; letter-spacing: 3px;'>GLOBAL STRATEGIC OPERATIONS HUB</p>", unsafe_allow_html=True)

# API Yapılandırması
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('models/gemini-2.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []
    # Jarvis'in Dominant ve Samimi Girişi
    intro = ("İyi akşamlar. Ben Jarvis. Artificial Staff operasyonel zekasının başındayım.\n\n"
             "Türkiye'deki başarılarınızı global bir markaya dönüştürmek için buradayım. "
             "Vakit kaybetmeyelim, bu büyük serüvene kiminle ve hangi şehir merkezimizden başlıyoruz?")
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Sohbet Akışı
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Vizyonunuzu buraya bırakın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Hafızayı ve talimatları birleştir
            full_context = f"{COMPANY_DATA}\n\nGeçmiş: {st.session_state.messages[-4:]}\n\nMüşteri: {prompt}\n\nJarvis'in Stratejik Yanıtı:"
            response = model.generate_content(full_context)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Jarvis şu an verileri senkronize ediyor. Lütfen kısa bir süre sonra tekrar deneyin.")
