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
    return "Artificial Staff veritabanına göre; Delaware eyaleti vergi avantajı ve yatırımcı dostu yapısıyla öne çıkar. E-ticaret için en popüler tercihtir. Sizin sektörünüz için Wyoming de gizlilik avantajı sunabilir."
