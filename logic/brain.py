import pandas as pd
import numpy as np
import plotly.graph_objects as go
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

    sys_prompt = f"Sen ARTIS Lojistik AI asistanısın. Muhatap: {user_data.get('name')}. Marka: {user_data.get('brand')}. Kısa ve profesyonel Türkçe cevap ver."
    
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

def get_sales_chart():
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Tarih'], y=df['Gelir'], fill='tozeroy', line=dict(color='#1F6FEB')))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0,l=0,r=0), height=300)
    return fig

def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='lines', line=dict(width=2, color='#238636')))
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='markers+text', text=['İSTANBUL', 'DC'], marker=dict(size=8, color='#fff')))
    fig.update_layout(geo=dict(projection_type="equirectangular", showland=True, landcolor="#0D1117", bgcolor="#000"), margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#000")
    return fig
