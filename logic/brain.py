import streamlit as st
from google import genai
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ==============================================================================
# ⚙️ AYARLAR
# ==============================================================================
MODEL_NAME = "gemini-1.5-flash"  # Veya erişimin varsa "gemini-1.5-pro"

# ==============================================================================
# 1. GOOGLE API İSTEMCİSİ
# ==============================================================================
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
    except Exception as e:
        return None

# ==============================================================================
# 2. SOHBET FONKSİYONU (DÜZELTİLDİ: 2 PARAMETRE ALIYOR)
# ==============================================================================
def get_streaming_response(messages_history, user_data):
    """
    Bu fonksiyon Dashboard'dan çağrılırken MUTLAKA 2 parametre ile çağrılmalı.
    """
    client = get_client()
    
    # API Anahtarı Yoksa Uyarı Ver
    if not client:
        yield "⚠️ API Anahtarı bulunamadı. Lütfen secrets.toml dosyasını kontrol edin."
        return

    # Kullanıcı bilgilerini al
    brand_name = user_data.get('brand', 'Şirket')
    
    # Sistem Talimatı
    sys_instruction = f"""
    Sen ARTIS, {brand_name} markası için çalışan profesyonel bir operasyon asistanısın.
    Sorulara kısa, net ve yönetici özeti formatında cevap ver.
    """

    # Mesaj Geçmişini Metne Dök (Context)
    full_prompt = f"System: {sys_instruction}\n\n"
    for msg in messages_history:
        role = "User" if msg["role"] == "user" else "Model"
        content = msg.get("content", "")
        if content:
            full_prompt += f"{role}: {content}\n"

    # API Çağrısı
    try:
        response = client.models.generate_content_stream(
            model=MODEL_NAME,
            contents=full_prompt,
            config={"temperature": 0.7}
        )
        
        for chunk in response:
            if chunk.text:
                yield chunk.text

    except Exception as e:
        yield f"⚠️ Bağlantı Hatası: {str(e)}"

# ==============================================================================
# 3. GRAFİK MOTORLARI
# ==============================================================================
def get_sales_chart():
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Tarih'], y=df['Gelir'], fill='tozeroy', mode='lines', line=dict(color='#3B82F6', width=4), name='Ciro'))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=10,b=10,l=10,r=10), height=280, xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='#27272A'))
    return fig

def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(lon=[28.97, -74.00], lat=[41.00, 40.71], mode='lines+markers', line=dict(width=2, color='#10B981'), marker=dict(size=8, color='#10B981')))
    fig.update_layout(geo=dict(showland=True, landcolor="#18181B", bgcolor="rgba(0,0,0,0)", showocean=False, showcountries=False), margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)", height=280)
    return fig

def get_inventory_chart():
    fig = go.Figure(data=[go.Pie(labels=['A', 'B', 'C'], values=[40, 30, 30], hole=.7, marker=dict(colors=['#3B82F6', '#8B5CF6', '#10B981']))])
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0), height=280, showlegend=False)
    return fig
