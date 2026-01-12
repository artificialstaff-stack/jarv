import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
from google.genai import types
import streamlit as st
import time

# --- 1. GÜÇLENDİRİLMİŞ API BAĞLANTISI ---
def get_client():
    # Hem API hem APT ihtimalini dener (Senin Secrets hatanı tolere eder)
    api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_APT_KEY")
    
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

# --- 2. DİNAMİK PERSONA ---
def get_system_prompt(user_data):
    # Veri yoksa varsayılan değerler ata (Hata önleyici)
    name = user_data.get('name', 'Değerli Girişimci')
    brand = user_data.get('brand', 'Markanız')
    product = user_data.get('product', 'Ürünleriniz')

    return f"""
    Sen ARTIS. Washington DC merkezli (Beyaz Saray'a 15dk) Lojistik Operasyon Yapay Zekasısın.
    
    MUHATABIN:
    İsim: {name}
    Marka: {brand}
    Ürün: {product}

    GÖREVİN:
    1. Müşteriyi ismiyle ve markasıyla karşıla. Güven ver.
    2. Washington DC operasyon merkezinin gücünden bahset.
    3. Müşterinin sorularını yanıtla ve şu paketlere yönlendir:
       - ORTAKLIK (Sıfır maliyet, kârdan pay).
       - KURUMSAL ($2000 Kurulum).
       - VIP OTOMASYON ($2000 + $500/ay).

    TONUN: Profesyonel, Türkçe, Kısa ve Samimi.
    """

# --- 3. STREAMING & HATA GİZLEME ---
def get_streaming_response(messages_history, user_data):
    client = get_client()
    
    if not client:
        yield "⚠️ Sistem Hatası: API Anahtarı bulunamadı. Lütfen panelden 'Secrets' ayarlarını kontrol edin."
        return

    # Sistem talimatını oluştur
    sys_prompt = get_system_prompt(user_data)
    
    # Mesaj geçmişini Gemini formatına çevir
    # (İlk mesaj her zaman sistem talimatı olsun)
    contents = [types.Content(role="user", parts=[types.Part.from_text(text=sys_prompt)])]
    
    for msg in messages_history:
        role = "user" if msg["role"] == "user" else "model"
        # Boş mesaj kontrolü
        if msg["content"]:
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
        # KORKUNÇ HATA KODLARI YERİNE TÜRKÇE UYARI
        error_msg = str(e)
        if "429" in error_msg or "Quota" in error_msg or "ResourceExhausted" in error_msg:
            yield "⚠️ Sistem şu an çok yoğun talep alıyor. Lütfen 10 saniye bekleyip tekrar deneyin (Ücretsiz Plan Limiti)."
        else:
            yield f"Bağlantı hatası oluştu. Lütfen tekrar deneyin."

# --- 4. GRAFİKLER ---
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
