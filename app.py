import streamlit as st
import google.generativeai as genai
from instructions import COMPANY_DATA

st.set_page_config(page_title="Jarvis v2.5 | Artificial Staff", page_icon="💎", layout="wide")

# --- 2026 PRESTIGE UI (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;1,700&family=Inter:wght@300;500&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top right, #1a1c23, #08090a);
        color: #d1d1d1;
        font-family: 'Inter', sans-serif;
    }
    
    /* Premium Cam Efekti Mesajlar */
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border-radius: 20px !important;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }

    /* Jarvis'in Özel İmzası (Mavi/Altın Işıltı) */
    [data-testid="stChatMessageAssistant"] {
        border-right: 2px solid #b89b5e !important; /* Altın Detay */
    }

    h1 {
        font-family: 'Playfair Display', serif;
        letter-spacing: 4px;
        background: linear-gradient(90deg, #d1d1d1, #b89b5e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        text-align: center;
    }
    
    .stChatInputContainer input {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid #b89b5e !important;
        border-radius: 30px !important;
        color: #fff !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("ARTIFICIAL STAFF")
st.markdown("<p style='text-align: center; font-style: italic; color: #b89b5e;'>Exclusive Global Operations Hub</p>", unsafe_allow_html=True)

# --- ENGINE ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('models/gemini-2.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []
    # Jarvis'in Prestijli Açılışı
    intro = "İyi akşamlar. Ben Jarvis. Artificial Staff'in küresel operasyon ağına hoş geldiniz. Vizyonunuzu dünya pazarına taşımak için tüm sistemlerimiz hazır. Bugün hangi büyük adımı atıyoruz?"
    st.session_state.messages.append({"role": "assistant", "content": intro})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Planınızı buraya fısıldayın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        context = f"{COMPANY_DATA}\n\nGeçmiş: {st.session_state.messages[-3:]}\n\nLiderden Gelen Mesaj: {prompt}"
        try:
            response = model.generate_content(context)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Operasyonel bir duraksama yaşandı. Lütfen tekrar deneyin.")
