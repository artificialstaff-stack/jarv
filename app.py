import streamlit as st
import google.generativeai as genai
from instructions import COMPANY_DATA # Yeni dosyadan bilgileri çekiyoruz

st.set_page_config(page_title="Jarvis 2.5 - Artificial Staff", page_icon="🤖")

# API Ayarı
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('models/gemini-2.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = ("Sistem Aktif. Ben Jarvis. Artificial Staff Operasyon merkezine hoş geldiniz.\n\n"
             "Amerika projenizi başlatmadan önce sizi ve firmanızı tanımam gerekiyor. "
             "Lütfen isim, soyisim, firmanızın konumu ve size ulaşabileceğimiz bir iletişim bilgisi paylaşır mısınız?")
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Chat Arayüzü
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Mesajınızı yazın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Jarvis'in hafızası ve patron talimatı birleşiyor
        full_context = f"{COMPANY_DATA}\n\nKonuşma Geçmişi: {st.session_state.messages}\n\nMüşteri: {prompt}"
        
        try:
            response = model.generate_content(full_context)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Hata: {e}")
