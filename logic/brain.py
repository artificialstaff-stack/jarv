import streamlit as st
from google import genai
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- AI ---
def get_client():
    key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY")
    if key: os.environ["GOOGLE_API_KEY"] = key
    try: return genai.Client()
    except: return None

def get_streaming_response(history, user):
    client = get_client()
    brand = user.get('brand', 'Şirket')
    
    # Basit bir cevap simülasyonu (API yoksa çalışsın diye)
    if not client:
        last_msg = history[-1]["content"].lower()
        if "lojistik" in last_msg: yield "Lojistik haritasını açtım. Şu an 824 aktif gönderim var."
        elif "stok" in last_msg: yield "Depo ekranını getirdim. 3 üründe stok kritik seviyede."
        else: yield f"{brand} verilerini inceliyorum..."
        return

    # API Varsa Gerçek Zeka
    full_prompt = f"System: Sen {brand} asistanısın. Kısa cevap ver.\n\n"
    for m in history: full_prompt += f"{m['role']}: {m['content']}\n"
    
    try:
        resp = client.models.generate_content_stream(model="gemini-1.5-flash", contents=full_prompt)
        for chunk in resp: 
            if chunk.text: yield chunk.text
    except Exception as e: yield str(e)

# --- GRAFİKLER ---
def get_sales_chart():
    # Mavi Çizgi Grafik (Finans)
    df = pd.DataFrame({'Gün': range(30), 'Satış': np.random.randint(50, 150, 30)})
    fig = go.Figure(go.Scatter(y=df['Satış'], mode='lines', fill='tozeroy', line=dict(color='#2563EB')))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0,l=0,r=0), height=300)
    return fig

def get_logistics_map():
    # Dünya Haritası (Lojistik)
    fig = go.Figure(go.Scattergeo(
        lon=[28.9, -74.0, 139.6, -0.1], lat=[41.0, 40.7, 35.6, 51.5],
        mode='markers+lines', marker=dict(color='#F59E0B', size=10), line=dict(width=2, color='#F59E0B')
    ))
    fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)', showland=True, landcolor='#18181B', showcountries=False), margin=dict(t=0,b=0,l=0,r=0), height=300, paper_bgcolor='rgba(0,0,0,0)')
    return fig

def get_inventory_chart():
    # Pasta Grafik (Stok)
    fig = go.Figure(go.Pie(labels=['Gömlek', 'Pantolon', 'Aksesuar'], values=[400, 300, 150], hole=.6))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0
