# brain.py
import streamlit as st
import time

def get_ai_response(messages):
    """
    OpenAI API çağrısını yönetir.
    Eğer API Key yoksa simülasyon yapar.
    """
    
    # --- API VARSA BURAYI AKTİF EDİN ---
    # import openai
    # client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    # try:
    #     response = client.chat.completions.create(
    #         model="gpt-4",
    #         messages=messages
    #     )
    #     return response.choices[0].message.content
    # except Exception as e:
    #     return f"Hata: {str(e)}"
    
    # --- SİMÜLASYON MODU (API YOKSA BU ÇALIŞIR) ---
    time.sleep(1) # Düşünme efekti
    return "Analiz tamamlandı. Amazon FBA için Delaware eyaleti vergi avantajı sağlar. Ancak depo kullanımı için Wyoming daha uygun olabilir. 2. Aşamadan şirketinizi hemen kurabiliriz."
