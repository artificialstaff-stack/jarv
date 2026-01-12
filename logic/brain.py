import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
import streamlit as st
import time

# --- API CLIENT KURULUMU ---
def get_client():
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
        return genai.Client(api_key=api_key)
    except Exception:
        return None

# --- ARTIS PERSONA (Senin İş Modelin) ---
ARTIS_SYS_PROMPT = """
Sen ARTIS. Washington DC merkezli (Beyaz Saray'a 15dk) bir Lojistik & Operasyon Yapay Zekasısın.
GÖREVİN: Müşteriyle sohbet ederek onları analiz etmek ve paket satmak.

DAVRANIŞ KURALLARI:
1. ChatGPT gibi davran: Kısa, net, profesyonel ama samimi.
2. Bilgi Toplama Sırası: İsim > Sektör > Yıldız Ürün > Üretim Maliyeti/Boyut.
3. Satış Aşaması: Veriler tamamsa şu 3 paketi sun:
   - ORTAKLIK (Sadece Kargo Öde).
   - KURUMSAL ($2000 Kurulum + $250/ay).
   - VIP OTOMASYON ($2000 Kurulum + $500/ay).

TONUN: Güven verici, vizyoner. Washington operasyon gücünü hissettir.
"""

# --- STREAMING FONKSİYONU (Daktilo Efekti İçin) ---
def get_streaming_response(messages_history):
    client = get_client()
    
    if not client:
        # API Anahtarı yoksa hata mesajını stream et
        error_msg = "⚠️ HATA: API Anahtarı bulunamadı. Lütfen secrets.toml dosyasını kontrol edin."
        for word in error_msg.split():
            yield word + " "
            time.sleep(0.05)
        return

    # Geçmişi formatla
    formatted_history = f"SİSTEM: {ARTIS_SYS_PROMPT}\n\n"
    for msg in messages_history:
        role = "KULLANICI" if msg["role"] == "user" else "ARTIS"
        formatted_history += f"{role}: {msg['content']}\n"
    
    formatted_history += "ARTIS:"

    try:
        # GEMINI 2.5 FLASH STREAMING
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=formatted_history
        )
        
        for chunk in response:
            if chunk.text:
                yield chunk.text
                
    except Exception as e:
        yield f"Bağlantı hatası: {str(e)}"

# --- CHART DATA ---
def get_sales_chart():
    df = pd.DataFrame({'Date': pd.date_range('2025-01-01', periods=30), 'Revenue': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Revenue'], fill='tozeroy', line=dict(color='#10a37f'), name='Gelir')) # ChatGPT Yeşili
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0,l=0,r=0), height=300)
    return fig

def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='lines', line=dict(width=2, color='#10a37f')))
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='markers+text', text=['IST', 'WAS-DC'], marker=dict(size=8, color='#fff')))
    fig.update_layout(geo=dict(projection_type="equirectangular", showland=True, landcolor="#1e1e1e", bgcolor="#000"), margin={"r":0,"t":0,"l":0,"b":0})
    return fig
