import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
from google.genai import types
import streamlit as st
import time

# --- 1. GÜÇLENDİRİLMİŞ API BAĞLANTISI ---
def get_client():
    # Hem API hem APT ihtimalini dener (Hata toleransı)
    api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_APT_KEY")
    
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

# --- 2. ARTIS PERSONA ---
ARTIS_SYS_PROMPT = """
Sen ARTIS. Washington DC merkezli (Beyaz Saray'a 15dk) Türk ihracatçılar için çalışan Lojistik & Operasyon Yapay Zekasısın.
GÖREVİN: Müşteriyle sohbet ederek güven kazanmak, veri toplamak ve paket satışı yapmak.

DAVRANIŞ KURALLARI:
1. Kısa, net ve samimi Türkçe konuş.
2. Bilgi Toplama Sırası: İsim > Sektör > Ürün Detayı > Koli Boyutları.
3. Asla kod veya teknik terim kullanma.
4. Veriler tamamsa şu 3 paketi sun:
   - ORTAKLIK (Sıfır maliyet, kârdan pay).
   - KURUMSAL ($2000 Kurulum + $250/ay).
   - VIP OTOMASYON ($2000 Kurulum + $500/ay).

TONUN: Güven verici, profesyonel. "Merkezimiz DC'de, hemen raf ayırabilirim" gibi ifadeler kullan.
"""

# --- 3. STREAMING & HATA YÖNETİMİ ---
def get_streaming_response(messages_history):
    client = get_client()
    
    if not client:
        yield "⚠️ Sistem Hatası: API Anahtarı bulunamadı. Lütfen panelden 'Secrets' ayarlarını kontrol edin."
        return

    # Geçmişi Gemini formatına çevir
    contents = [types.Content(role="user", parts=[types.Part.from_text(text=ARTIS_SYS_PROMPT)])]
    
    for msg in messages_history:
        role = "user" if msg["role"] == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

    try:
        # GEMINI 2.5 FLASH STREAMING
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=contents,
            config=types.GenerateContentConfig(temperature=0.7)
        )
        
        for chunk in response:
            if chunk.text:
                yield chunk.text
                
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "Quota" in error_msg or "ResourceExhausted" in error_msg:
            yield "⚠️ Sistem şu an çok yoğun talep alıyor (Hız Sınırı). Lütfen 20 saniye bekleyip tekrar deneyin."
        else:
            yield f"Bağlantı hatası oluştu. Lütfen tekrar deneyin. (Hata Kodu: 500)"

# --- 4. GRAFİK VERİLERİ ---
def get_sales_chart():
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Tarih'], y=df['Gelir'], fill='tozeroy', line=dict(color='#10a37f'), name='Tahmini Gelir'))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0,l=0,r=0), height=300)
    return fig

def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='lines', line=dict(width=2, color='#D4AF37')))
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='markers+text', text=['İSTANBUL', 'WASHINGTON DC'], marker=dict(size=10, color='#fff'), textposition="top center"))
    fig.update_layout(geo=dict(projection_type="equirectangular", showland=True, landcolor="#1e1e1e", bgcolor="#000", coastlinecolor="#333"), margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#000")
    return fig
