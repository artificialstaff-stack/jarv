import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
from google.genai import types
import streamlit as st
import time
import random

# --- 1. GÜVENLİ İSTEMCİ ---
def get_client():
    api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_APT_KEY")
    if not api_key: return None
    return genai.Client(api_key=api_key)

# --- 2. YEDEK CEVAPLAR (Gelismis Mock Data) ---
MOCK_RESPONSES = {
    "default": "Sistem analizlerime göre Washington DC operasyon akışınız %98 verimlilikle devam ediyor. Hangi konuda rapor istersiniz?",
    "lojistik": "Lojistik ağında 1 aktif sevkiyat tespit edildi. TR-8821 numaralı konteyner şu an Atlantik rotasında ve plana uygun ilerliyor. Tahmini varış: 48 saat.",
    "stok": "Depo doluluk oranınız %64 seviyesinde. Kritik Uyarı: 'Deri Çanta' stokları güvenlik sınırının altına indi (Son 50 adet).",
    "finans": "Finansal özet: Bu ayki cironuz $42,500 seviyesine ulaştı. Geçen aya göre %12'lik bir büyüme trendi var."
}

def get_streaming_response(messages_history, user_data):
    client = get_client()
    last_msg = messages_history[-1]["content"].lower() if messages_history else ""
    
    # API VARSA
    if client:
        try:
            sys_prompt = f"Sen ARTIS. {user_data.get('brand')} markasının AI asistanısın. Kısa ve profesyonel Türkçe konuş."
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
            return
        except Exception:
            pass 

    # API YOKSA (SİMÜLASYON)
    time.sleep(0.8) # Yapay zeka düşünüyor efekti
    
    if any(x in last_msg for x in ["lojistik", "kargo", "konum", "nerede"]): text = MOCK_RESPONSES["lojistik"]
    elif any(x in last_msg for x in ["stok", "ürün", "envanter"]): text = MOCK_RESPONSES["stok"]
    elif any(x in last_msg for x in ["finans", "para", "ciro", "kar"]): text = MOCK_RESPONSES["finans"]
    else: text = MOCK_RESPONSES["default"]

    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)

# --- 3. NEXT-GEN GRAFİKLER (NEON STYLE) ---

def get_sales_chart():
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Tarih'], y=df['Gelir'], 
        fill='tozeroy', 
        mode='lines',
        line=dict(color='#3B82F6', width=4, shape='spline'), # Neon Mavi Kalın Çizgi
        name='Ciro'
    ))
    fig.update_layout(
        template='plotly_dark', 
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=10,b=10,l=10,r=10), height=280,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=True, gridcolor='#27272A', zeroline=False),
        showlegend=False
    )
    return fig

def get_logistics_map():
    fig = go.Figure()
    # Rota (Neon Yeşil)
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], 
        mode='lines', 
        line=dict(width=3, color='#10B981', dash="dot")
    ))
    # Noktalar (Parlayan Efekt)
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], 
        mode='markers', 
        marker=dict(size=10, color='#10B981', line=dict(width=5, color='rgba(16, 185, 129, 0.3)'))
    ))
    fig.update_layout(
        geo=dict(
            projection_type="equirectangular", showland=True, landcolor="#18181B", 
            bgcolor="rgba(0,0,0,0)", showocean=False, showcountries=False, coastlinecolor="#27272A"
        ), 
        margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)", height=280
    )
    return fig

def get_inventory_chart():
    labels = ['Tekstil', 'Kozmetik', 'Aksesuar', 'Diğer']
    values = [45, 25, 20, 10]
    colors = ['#3B82F6', '#8B5CF6', '#10B981', '#64748B']

    fig = go.Figure(data=[go.Pie(
        labels=labels, values=values, hole=.7, 
        marker=dict(colors=colors, line=dict(color='#09090B', width=5)), 
        textinfo='none', hoverinfo='label+percent'
    )])
    # Ortaya Rakam
    fig.add_annotation(text="8.5K", x=0.5, y=0.5, font_size=24, font_color="#FFF", showarrow=False)
    fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=0, b=0, l=0, r=0), height=280, showlegend=True,
        legend=dict(orientation="h", y=-0.1)
    )
    return fig
