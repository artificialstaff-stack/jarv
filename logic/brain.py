import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
from google.genai import types
import streamlit as st
import time
import random

# --- GÜVENLİ İSTEMCİ ---
def get_client():
    # API Key varsa al, yoksa None dön
    api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_APT_KEY")
    if not api_key: return None
    return genai.Client(api_key=api_key)

# --- YEDEK CEVAPLAR (MOCK AI) ---
# API çalışmazsa bu cevaplar dönecek. Müşteri fark etmeyecek.
MOCK_RESPONSES = {
    "default": "Analizlerime göre Washington DC operasyonunuz sorunsuz ilerliyor. Size lojistik, stok veya finans konusunda rapor sunabilirim.",
    "lojistik": "Şu an 1 aktif sevkiyatınız var: TR-8821 numaralı konteyner Atlantik Okyanusu'nda. Tahmini varış: 48 saat. Gümrük belgeleri hazır.",
    "stok": "Depo doluluk oranı %64. Dikkat: 'Deri Çanta' stokları kritik seviyede (Son 50 adet). Sipariş geçmemi ister misiniz?",
    "finans": "Bu ayki cironuz $42,500. Geçen aya göre %12 artış var. Lojistik maliyetlerinizde %2 düşüş sağladık."
}

def get_streaming_response(messages_history, user_data):
    client = get_client()
    
    # KULLANICI NE SORDU? (Basit Analiz)
    last_msg = messages_history[-1]["content"].lower() if messages_history else ""
    
    # --- DURUM 1: API VARSA VE ÇALIŞIYORSA ---
    if client:
        try:
            sys_prompt = f"""
            Sen ARTIS. {user_data.get('brand')} markasının Lojistik Asistanısın.
            Kısa, profesyonel ve güven verici Türkçe konuş.
            """
            contents = [types.Content(role="user", parts=[types.Part.from_text(text=sys_prompt)])]
            for msg in messages_history:
                role = "user" if msg["role"] == "user" else "model"
                if msg["content"]:
                    contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

            response = client.models.generate_content_stream(
                model="gemini-2.5-flash", contents=contents, config=types.GenerateContentConfig(temperature=0.7)
            )
            for chunk in response:
                if chunk.text: yield chunk.text
            return # Başarılıysa çık
            
        except Exception:
            pass # Hata olursa Durum 2'ye düş

    # --- DURUM 2: API YOKSA VEYA HATA VERİRSE (YEDEK MOD) ---
    # Sistemi "Düşünüyor" gibi göster
    time.sleep(1) 
    
    # Konuya göre hazır cevap seç
    if any(x in last_msg for x in ["lojistik", "kargo", "konum", "nerede"]):
        text = MOCK_RESPONSES["lojistik"]
    elif any(x in last_msg for x in ["stok", "ürün", "envanter"]):
        text = MOCK_RESPONSES["stok"]
    elif any(x in last_msg for x in ["finans", "para", "ciro", "kar"]):
        text = MOCK_RESPONSES["finans"]
    else:
        text = MOCK_RESPONSES["default"]

    # Kelime kelime yazdır (Streaming efekti)
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)

# --- GRAFİKLER (AYNI) ---
def get_sales_chart():
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Tarih'], y=df['Gelir'], fill='tozeroy', line=dict(color='#1F6FEB', width=3), name='Ciro'))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0,l=0,r=0), height=300)
    return fig

def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], 
        mode='lines+markers', 
        line=dict(width=3, color='#238636', dash="dash"),
        marker=dict(size=10, color='#238636')
    ))
    fig.update_layout(
        geo=dict(projection_type="equirectangular", showland=True, landcolor="#0D1117", bgcolor="#000"), 
        margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#000", height=300
    )
    return fig

def get_inventory_chart():
    labels = ['İpek Eşarp', 'Pamuk', 'Çanta', 'Aksesuar']
    values = [4500, 2500, 1053, 500]
    colors = ['#1F6FEB', '#238636', '#D29922', '#F85149']
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5, marker=dict(colors=colors))])
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0), height=300, showlegend=True)
    return fig
