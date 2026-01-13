import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px  # YENİ EKLENDİ
from google import genai
from google.genai import types
import streamlit as st

def get_client():
    api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_APT_KEY")
    if not api_key: return None
    return genai.Client(api_key=api_key)

def get_streaming_response(messages_history, user_data):
    client = get_client()
    if not client:
        yield "⚠️ API Anahtarı eksik."
        return

    # Prompt biraz daha zeki hale getirildi
    sys_prompt = f"""
    Sen ARTIS Lojistik AI asistanısın. Muhatap: {user_data.get('name')}. Marka: {user_data.get('brand')}.
    Görevin: Lojistik, stok ve finans konularında yardımcı olmak.
    Kural: Kısa, net ve veriye dayalı konuş.
    """
    
    contents = [types.Content(role="user", parts=[types.Part.from_text(text=sys_prompt)])]
    for msg in messages_history:
        role = "user" if msg["role"] == "user" else "model"
        if msg["content"]:
            contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

    try:
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash", contents=contents, config=types.GenerateContentConfig(temperature=0.7)
        )
        for chunk in response:
            if chunk.text: yield chunk.text
    except Exception:
        yield "⚠️ Sistem şu an yoğun. Lütfen bekleyin."

# --- GRAFİKLER ---

def get_sales_chart():
    # Finans Grafiği (Alan Grafiği)
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Tarih'], y=df['Gelir'], fill='tozeroy', line=dict(color='#1F6FEB', width=3), name='Gelir'))
    fig.update_layout(
        template='plotly_dark', 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20,b=20,l=20,r=20), 
        height=350,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#333')
    )
    return fig

def get_logistics_map():
    # Lojistik Haritası (Animasyonlu Rota)
    fig = go.Figure()
    # Rota Çizgisi
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], 
        mode='lines', 
        line=dict(width=2, color='#238636', dash="dot")
    ))
    # Noktalar
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], 
        mode='markers+text', 
        text=['İSTANBUL (HQ)', 'WASHINGTON DC (HUB)'], 
        textposition="top center",
        marker=dict(size=12, color='#1F6FEB', line=dict(width=2, color='white'))
    ))
    fig.update_layout(
        geo=dict(
            projection_type="equirectangular", 
            showland=True, 
            landcolor="#161B22", 
            bgcolor="#0E1117",
            coastlinecolor="#30363D",
            showocean=True,
            oceancolor="#0E1117"
        ), 
        margin={"r":0,"t":0,"l":0,"b":0}, 
        paper_bgcolor="#0E1117",
        height=350
    )
    return fig

def get_inventory_chart():
    # Envanter Grafiği (Donut Chart)
    labels = ['İpek Eşarp', 'Organik Pamuk', 'Deri Çanta', 'Aksesuar']
    values = [4500, 2500, 1053, 500]
    colors = ['#1F6FEB', '#238636', '#D29922', '#F85149']

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6, marker=dict(colors=colors))])
    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=20, l=20, r=20),
        height=350,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
    )
    return fig
