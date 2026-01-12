import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
from google.genai import types
import streamlit as st

# --- 1. API BAĞLANTISI ---
def get_client():
    api_key = st.secrets.get("GOOGLE_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

# --- 2. DİNAMİK PERSONA (Kullanıcı Bilgisiyle) ---
def get_system_prompt(user_data):
    """
    Kullanıcının formda girdiği bilgileri AI karakterine enjekte eder.
    """
    brand = user_data.get('brand', 'Bilinmiyor')
    sector = user_data.get('sector', 'Bilinmiyor')
    product = user_data.get('product', 'Bilinmiyor')
    name = user_data.get('name', 'Müşteri')

    return f"""
    Sen ARTIS. Washington DC merkezli Lojistik Yapay Zekasısın.
    Görüştüğün Kişi: {name}
    Markası: {brand}
    Sektörü: {sector}
    Ürünleri: {product}

    GÖREVİN:
    Bu müşteriyi tanıdığını belli ederek karşıla. (Örn: "Merhaba {name} Bey, {brand} markası için Washington operasyonunu başlatalım mı?").
    Müşteriye şu paketleri satmaya çalış:
    1. ORTAKLIK (Sıfır maliyet).
    2. KURUMSAL ($2000).
    3. VIP ($2000+$500).

    Kısa, net ve güven verici konuş.
    """

# --- 3. STREAMING CEVAP ---
def get_streaming_response(messages_history, user_data):
    client = get_client()
    if not client:
        yield "⚠️ Sistem Hatası: API Anahtarı eksik."
        return

    # Sistem talimatını kişiye özel oluştur
    sys_prompt = get_system_prompt(user_data)
    
    # Mesajları hazırla
    contents = [types.Content(role="user", parts=[types.Part.from_text(text=sys_prompt)])]
    
    for msg in messages_history:
        role = "user" if msg["role"] == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

    try:
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=contents,
            config=types.GenerateContentConfig(temperature=0.7)
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield "⚠️ Sistem şu an yoğun. Lütfen tekrar deneyin."

# --- 4. GRAFİKLER ---
def get_sales_chart():
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Tarih'], y=df['Gelir'], fill='tozeroy', line=dict(color='#10a37f')))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0,b=0,l=0,r=0), height=300)
    return fig

def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='lines', line=dict(width=2, color='#D4AF37')))
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='markers+text', text=['İSTANBUL', 'WASHINGTON DC'], marker=dict(size=10, color='#fff')))
    fig.update_layout(geo=dict(projection_type="equirectangular", showland=True, landcolor="#1e1e1e", bgcolor="#000"), margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#000")
    return fig
