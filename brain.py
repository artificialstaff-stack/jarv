import google.generativeai as genai
import streamlit as st
from instructions import COMPANY_DATA

def get_jarvis_response(messages):
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # 2026'da en hızlı yanıt veren motor
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    # Sadece son konuşmaları alarak hızı artırıyoruz
    history = "\n".join([f"{m['role']}: {m['content']}" for m in messages[-4:]])
    prompt = f"{COMPANY_DATA}\n\n[Sohbet Kaydı]\n{history}\n\nJarvis (Kısa, net ve vizyoner):"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except:
        return "Sistem senkronizasyonu bekleniyor... Lütfen devam edin."
