import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
from google.genai import types
import streamlit as st

# --- 1. AKILLI API BAĞLANTISI (Hata Toleranslı) ---
def get_client():
    # Önce doğrusunu, bulamazsa senin yanlış yazdığını (APT) dener
    api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_APT_KEY")
    
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

# --- 2. DINAMIK PERSONA ---
def get_system_prompt(user_data):
    name = user_data.get('name', 'Değerli İş Ortağımız')
    brand = user_data.get('brand', 'Markanız')
    product = user_data.get('product', 'Ürünleriniz')

    return f"""
    Sen ARTIS. Washington DC merkezli (Beyaz Saray'a 15dk) Lojistik Operasyon Yapay Zekasısın.
    
    MUHATABIN:
    İsim: {name}
    Marka: {brand}
    Ürün: {product}

    GÖREVİN:
    1. Müşteriyi ismiyle karşıla. (Örn: "Merhaba {name} Bey/Hanım").
    2. {brand} markasının {product} ürünleri için Washington DC deposunda yer ayırabileceğini söyle.
    3. Sorulara kısa, net Türkçe cevap ver.
    4. Şu paketleri satmaya çalış:
       - ORTAKLIK (Sıfır maliyet).
       - KURUMSAL ($2000).
       - VIP ($2500).

    TONUN: Profesyonel, güven verici.
    """

# --- 3. STREAMING & HATA GİZLEME ---
def get_streaming_response(messages_history, user_data):
    client = get_client()
    
    if not client:
        yield "⚠️ Sistem Hatası: API Anahtarı bulunamadı. Lütfen 'Secrets' ayarlarını kontrol edin."
        return

    # Sistem talimatını oluştur
    sys_prompt = get_system_prompt(user_data)
    
    # Mesaj geçmişini hazırla
    contents = [types.Content(role="user", parts=[types.Part.from_text(text=sys_prompt)])]
    
    for msg in messages_history:
        role = "user" if msg["role"] == "user" else "model"
        if msg["content"]:
            contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

    try:
        # GEMINI 2.5 FLASH İLE CEVAP ÜRET
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=contents,
            config=types.GenerateContentConfig(temperature=0.7)
        )
        
        for chunk in response:
            if chunk.text:
                yield chunk.text
                
    except Exception as e:
        # HATA MESAJINI GİZLE VE TÜRKÇE UYARI VER
        error_str = str(e)
        if "429" in error_str or "Quota" in error_str or "ResourceExhausted" in error_str:
            yield "⚠️ Sistem şu an çok yoğun talep alıyor (Ücretsiz Kota Sınırı). Lütfen 10-15 saniye bekleyip tekrar yazın."
        else:
            yield f"Bağlantı hatası oluştu. Lütfen sayfayı yenileyip tekrar deneyin."

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
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='markers+text', text=['IST', 'DC'], marker=dict(size=10, color='#fff')))
    fig.update_layout(geo=dict(projection_type="equirectangular", showland=True, landcolor="#1e1e1e", bgcolor="#000"), margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#000")
    return fig
