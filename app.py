import streamlit as st
import google.generativeai as genai
from instructions import COMPANY_DATA

# --- PRESTİJ TASARIMI ---
st.set_page_config(page_title="Jarvis v2.5 | Artificial Staff", page_icon="🏦", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Inter:wght@400;600&display=swap');
    .stApp { background: #050505; color: #f0f0f0; font-family: 'Inter', sans-serif; }
    .brand { font-family: 'Cinzel', serif; font-size: 3rem; text-align: center; color: #B89B5E; letter-spacing: 8px; margin-top: 30px; }
    [data-testid="stChatMessage"] { border-left: 2px solid #B89B5E !important; background: rgba(255,255,255,0.01) !important; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="brand">ARTIFICIAL STAFF</div>', unsafe_allow_html=True)

# --- AI ENGINE ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('models/gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []
    # Dükkana giren müşteriye ilk karşılama
    intro = "Hoş geldiniz. Ben Jarvis. Artificial Staff operasyon merkezine adım attınız. Sizinle ve vizyonunuzla tanışmak isterim. Kayıtlarımıza isminizi ve markanızı nasıl geçelim?"
    st.session_state.messages.append({"role": "assistant", "content": intro})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Mesajınızı yazın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Jarvis'in sadece son 2-3 mesajı ve ana talimatı görmesini sağlıyoruz
        # Bu, onun 'felsefeye' dalmasını engeller ve dükkan akışında kalmasını sağlar.
        relevant_history = st.session_state.messages[-3:]
        full_query = f"{COMPANY_DATA}\n\nŞu anki Durum:\n{relevant_history}\n\nMüşterinin Son Cevabı: {prompt}\n\nJarvis'in Vereceği Tek Soru/Cevap:"
        
        try:
            response = model.generate_content(full_query)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("💎 Jarvis: Kısa bir bağlantı kalibrasyonu yapıyorum, hemen döneceğim.")
