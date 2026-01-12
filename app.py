import streamlit as st
import google.generativeai as genai
from instructions import COMPANY_DATA

# 1. API YAPILANDIRMASI
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key bulunamadı! Lütfen Secrets kısmını kontrol edin.")

# 2. MODEL SEÇİMİ (2026'nın en stabil versiyonu)
# Eğer hala hata alırsan bu satırı 'models/gemini-1.5-flash' olarak değiştirebilirsin.
SELECTED_MODEL = 'models/gemini-1.5-flash' 

# 3. SAYFA TASARIMI (PREMIUM 2026)
st.set_page_config(page_title="Jarvis v2.5 | Artificial Staff", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #050505; color: #E0E0E0; font-family: 'Inter', sans-serif; }
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.02) !important;
        border-left: 1px solid #B89B5E !important;
        margin-bottom: 20px;
    }
    .stChatInputContainer input { border-bottom: 1px solid #B89B5E !important; background: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#B89B5E; letter-spacing:8px;">ARTIFICIAL STAFF</h1>', unsafe_allow_html=True)

# 4. SOHBET YÖNETİMİ
if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = "Sistem yenilendi. Ben Jarvis. Türkiye'den Amerika'ya uzanan bu prestijli yolculukta operasyon merkeziniz hazır. Vizyonunuzu dünya pazarıyla nasıl buluşturalım?"
    st.session_state.messages.append({"role": "assistant", "content": intro})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. AKILLI YANIT SİSTEMİ
if prompt := st.chat_input("Planınızı buraya fısıldayın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Sadece son 3 mesajı alarak sistemi yormuyoruz
            history = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-3:]])
            
            model = genai.GenerativeModel(SELECTED_MODEL)
            # Jarvis'e Patron Talimatlarını ve Mevcut Durumu Veriyoruz
            full_prompt = f"{COMPANY_DATA}\n\nGeçmiş:\n{history}\n\nMüşteri: {prompt}\n\nJarvis'in Stratejik Yanıtı:"
            
            response = model.generate_content(full_prompt)
            
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.warning("Jarvis şu an strateji üzerinde derinlemesine düşünüyor. Lütfen kısa bir mesaj daha gönderin.")
                
        except Exception as e:
            st.info("💎 **Operasyonel Güncelleme:** Jarvis şu an verileri senkronize ediyor. Lütfen 15 saniye bekleyip tekrar deneyin.")
            # Hatayı teknik olarak görmek istersen: st.write(e)
