import streamlit as st
import google.generativeai as genai
from instructions import COMPANY_DATA

st.set_page_config(page_title="Jarvis v2.5 | Artificial Staff", page_icon="🏦", layout="wide")

# --- 2026 PRESTIGE INTERFACE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp {
        background: #050505;
        color: #E0E0E0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Başlık: Altın ve Gümüş Geçişi */
    .brand-header {
        font-family: 'Cinzel', serif;
        font-size: 3.5rem;
        text-align: center;
        background: linear-gradient(to bottom, #FFFFFF 0%, #B89B5E 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 12px;
        margin-top: 40px;
        font-weight: 700;
    }
    
    .sub-brand {
        text-align: center;
        color: #666;
        letter-spacing: 5px;
        font-size: 0.7rem;
        text-transform: uppercase;
        margin-bottom: 60px;
    }

    /* Mesaj Balonları: Minimalist ve Lüks */
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.02) !important;
        border: none !important;
        border-left: 1px solid rgba(184, 155, 94, 0.3) !important;
        padding: 20px !important;
        margin-bottom: 25px !important;
    }

    /* Giriş Alanı: Modern ve İnce */
    .stChatInputContainer input {
        border: none !important;
        border-bottom: 1px solid #B89B5E !important;
        background: transparent !important;
        color: #B89B5E !important;
        border-radius: 0px !important;
        font-size: 1.1rem !important;
    }

    /* Scrollbar Gizleme */
    ::-webkit-scrollbar { width: 0px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="brand-header">ARTIFICIAL STAFF</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-brand">Strategic Global Expansion Hub</div>', unsafe_allow_html=True)

# --- AI ENGINE ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# Kotayı korumak için gemini-1.5-flash kullanıyoruz ama 2.5 beyniyle konuşturuyoruz
model = genai.GenerativeModel('models/gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = ("İyi akşamlar. Ben Jarvis. Artificial Staff operasyonel zekasının başındayım.\n\n"
             "Türkiye'deki potansiyelinizi Amerika'nın kalbine taşımak için stratejik hattımız hazır. "
             "Hangi ürün grubuyla global sahneye çıkıyoruz? Vizyonunuzu paylaşın, planı hemen devreye alalım.")
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Chat Akışı
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Vizyonunuzu fısıldayın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Hafızayı sadece son 4 mesajla sınırlı tutarak kota hatasını engelliyoruz
        history_context = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-4:]])
        full_query = f"{COMPANY_DATA}\n\nKonuşma Akışı:\n{history_context}\n\nStratejik Yanıt:"
        
        try:
            with st.spinner(""): # Temiz bir bekleme
                response = model.generate_content(full_query)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            if "429" in str(e):
                st.warning("Stratejik bir mola. Sistem 30 saniye sonra tekrar emrinizde.")
            else:
                st.error("Operasyonel bir kesinti. Jarvis sistemi kontrol ediyor.")

st.markdown("<br><br><br>", unsafe_allow_html=True)
