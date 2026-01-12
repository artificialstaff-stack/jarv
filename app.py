import streamlit as st
import google.generativeai as genai
from instructions import COMPANY_DATA
import time

st.set_page_config(page_title="Jarvis v2.5 | Artificial Staff", page_icon="💎", layout="wide")

# --- 2026 PRESTIGE INTERFACE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    .stApp { background: #050505; color: #E0E0E0; font-family: 'Inter', sans-serif; }
    .brand-header {
        font-family: 'Cinzel', serif; font-size: 3.5rem; text-align: center;
        background: linear-gradient(to bottom, #FFFFFF 0%, #B89B5E 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        letter-spacing: 12px; margin-top: 40px; font-weight: 700;
    }
    .sub-brand { text-align: center; color: #666; letter-spacing: 5px; font-size: 0.7rem; text-transform: uppercase; margin-bottom: 60px; }
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.02) !important; border: none !important;
        border-left: 1px solid rgba(184, 155, 94, 0.3) !important; padding: 20px !important; margin-bottom: 25px !important;
    }
    .stChatInputContainer input {
        border: none !important; border-bottom: 1px solid #B89B5E !important;
        background: transparent !important; color: #B89B5E !important; border-radius: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="brand-header">ARTIFICIAL STAFF</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-brand">Strategic Global Expansion Hub</div>', unsafe_allow_html=True)

# --- AI ENGINE ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# Kotayı en iyi yöneten model: gemini-1.5-flash
model = genai.GenerativeModel('models/gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = "İyi akşamlar. Ben Jarvis. Artificial Staff'in küresel operasyon stratejilerini yönetiyorum. Vizyonunuzu dünya pazarına taşımak için sabırsızlanıyorum. Hangi ürün grubuyla global sahneye çıkıyoruz?"
    st.session_state.messages.append({"role": "assistant", "content": intro})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Stratejik düşüncenizi buraya bırakın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Kota dostu kısa hafıza
        history_summary = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-3:]])
        full_query = f"{COMPANY_DATA}\n\nGeçmiş:\n{history_summary}\n\nMüşteri: {prompt}\n\nJarvis'in Cevabı:"
        
        try:
            with st.spinner(""):
                # Kota koruma: İstekler arasına kısa bir bekleme (Opsiyonel)
                response = model.generate_content(full_query)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            if "429" in str(e):
                st.info("💎 **Jarvis Notu:** Operasyonel verimliliği en üst düzeye çıkarmak için sistem kısa bir kalibrasyon sürecinde. Lütfen 20 saniye sonra vizyonunuzu paylaşmaya devam edin.")
            else:
                st.error("Sistemde küçük bir senkronizasyon hatası. Jarvis durumu kontrol ediyor.")

st.markdown("<br><br><br>", unsafe_allow_html=True)
