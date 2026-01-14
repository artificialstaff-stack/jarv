import streamlit as st
from google import genai
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# MODEL AYARI
MODEL_NAME = "gemini-2.5-flash"  # Veya "gemini-3-flash-preview"

# --- 1. CLIENT ---
def get_client():
    api_key = None
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
    elif "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]

    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
    
    try:
        return genai.Client()
    except Exception:
        return None

# --- 2. AI FONKSİYONU (2 Parametre Garantili) ---
def get_streaming_response(messages_history, user_data):
    client = get_client()
    
    # Kullanıcı markasını al
    brand = user_data.get('brand', 'Şirket') if user_data else 'Şirket'
    
    # Prompt Hazırla
    sys_instruction = f"Sen ARTIS. {brand} için çalışan profesyonel bir operasyon asistanısın."
    full_prompt = f"System: {sys_instruction}\n\n"
    
    for msg in messages_history:
        role = "User" if msg["role"] == "user" else "Model"
        full_prompt += f"{role}: {msg['content']}\n"

    if not client:
        yield "⚠️ API Anahtarı bulunamadı. Simülasyon moduna geçiliyor..."
        yield f"\n\nSimüle Cevap: {brand} için verileri analiz ettim. Her şey yolunda görünüyor."
        return

    try:
        response = client.models.generate_content_stream(
            model=MODEL_NAME,
            contents=full_prompt
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"⚠️ Bağlantı Hatası: {str(e)}"

# --- 3. GRAFİKLER ---
def get_sales_chart():
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Deger': np.random.normal(100, 10, 30)})
    fig = go.Figure(data=go.Scatter(x=df['Tarih'], y=df['Deger'], mode='lines', line=dict(color='#2563EB', width=4), fill='tozeroy'))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0,l=0,r=0), height=300)
    return fig

# Hata almamak için yedek fonksiyonlar
def get_logistics_map(): return get_sales_chart()
def get_inventory_chart(): return get_sales_chart()
