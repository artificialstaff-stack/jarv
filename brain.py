import google.generativeai as genai
import streamlit as st
from instructions import COMPANY_DATA

def get_jarvis_response(messages):
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    # Hafızayı ve talimatı birleştir
    history = "\n".join([f"{m['role']}: {m['content']}" for m in messages[-3:]])
    prompt = f"{COMPANY_DATA}\n\nGeçmiş:\n{history}\n\nJarvis:"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except:
        return "💎 Jarvis: Sistemde bir kalibrasyon yapıyorum, 10 saniye sonra tekrar deneyelim."
