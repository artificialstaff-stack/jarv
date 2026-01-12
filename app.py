import streamlit as st
import google.generativeai as genai
from instructions import COMPANY_DATA

st.set_page_config(page_title="Jarvis v2.5 | Artificial Staff", page_icon="🏦", layout="wide")

# --- 2026 ELITE INTERFACE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;600&family=Playfair+Display:wght@700&display=swap');
    
    .stApp {
        background: #050505;
        color: #f0f0f0;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Premium Mesaj Alanları */
    [data-testid="stChatMessage"] {
        border-radius: 2px !important;
        border: none !important;
        background: transparent !important;
        border-left: 1px solid #b89b5e !important;
        margin-bottom: 30px;
    }

    /* Başlık Tasarımı */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        text-align: center;
        letter-spacing: 8px;
        background: linear-gradient(180deg, #ffffff 0%, #b89b5e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 50px;
    }

    .sub-title {
        text-align: center;
        letter-spacing: 4px;
        color: #666;
        text-transform: uppercase;
        font-size: 0.8rem;
        margin-bottom: 50px;
    }

    /* Chat Input */
    .stChatInputContainer input {
        border: none !important;
        border-bottom: 1px solid #b89b5e !important;
        background: transparent !important;
        border-radius: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">ARTIFICIAL STAFF</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Global Expansion Management by Jarvis v2.5</p>', unsafe_allow_html=True)

# --- AI CORE ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('models/gemini-2.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []
    # Jarvis'in Dominant ve Vizyoner Girişi
    intro = ("Hoş geldiniz. Ben Jarvis. Artificial Staff çatısı altında, markanızı Türkiye sınırlarından çıkarıp "
             "Amerika'nın merkezine yerleştirecek operasyonun başındayım. \n\n"
             "Vakit kaybetmeyelim. Hangi ürün veya kategoriyle küresel pazarı domine etmeyi hedefliyorsunuz? "
             "Bilgileri verin, stratejinizi hemen çizelim.")
    st.session_state.messages.append({"role": "assistant", "content": intro})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Vizyonunuzu buraya bırakın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Jarvis'in geçmişi ve dominant karakteri
        full_context = f"{COMPANY_DATA}\n\nGeçmiş: {st.session_state.messages[-4:]}\n\nMüşteri Girişi: {prompt}\n\nJarvis'in Stratejik Yanıtı:"
        
        try:
            response = model.generate_content(full_context)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Sistem yoğunluğu. Jarvis strateji üzerinde çalışıyor.")
