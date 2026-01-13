import streamlit as st
from google import genai
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ==============================================================================
# ⚙️ KONFİGÜRASYON
# ==============================================================================
# MÜŞTERİ TALEBİ: Özellikle bu model kullanılacak.
MODEL_NAME = "gemini-3-flash-preview"

# ==============================================================================
# 1. API İSTEMCİSİ (ENVIRONMENT VARIABLE YÖNTEMİ)
# ==============================================================================
def get_client():
    """
    Streamlit secrets içindeki API anahtarını işletim sistemi ortam değişkenine
    atar. Böylece genai.Client() parametresiz çalışır.
    """
    api_key = None
    # Hem GOOGLE_API_KEY hem GEMINI_API_KEY kontrolü
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
    elif "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]

    if api_key:
        # Ortam değişkenlerini set et (SDK bunları otomatik okur)
        os.environ["GOOGLE_API_KEY"] = api_key
        os.environ["GEMINI_API_KEY"] = api_key
    else:
        # Anahtar yoksa hata dönmeyelim, chat fonksiyonunda uyarırız
        pass
    
    try:
        # SENİN İSTEDİĞİN PARAMETRESİZ ÇAĞRI
        client = genai.Client()
        return client
    except Exception as e:
        st.error(f"Client Başlatılamadı: {e}")
        return None

# ==============================================================================
# 2. SOHBET MOTORU (MODEL: gemini-3-flash-preview)
# ==============================================================================
def get_streaming_response(messages_history, user_data):
    client = get_client()
    if not client:
        yield "⚠️ API Anahtarı bulunamadı. Lütfen secrets.toml dosyasını kontrol edin."
        return

    # --- KİMLİK TANIMI ---
    brand_name = user_data.get('brand', 'Şirket')
    sys_instruction = f"""
    Sen ARTIS. {brand_name} markası için çalışan Lojistik ve Operasyon Yapay Zekasısın.
    Kısa, net ve profesyonel cevaplar ver.
    """

    # --- GEÇMİŞİ FORMATLA ---
    # Model bağlamı kaybetmesin diye tüm geçmişi metin olarak birleştiriyoruz.
    full_prompt = f"System Instruction: {sys_instruction}\n\n"
    
    for msg in messages_history:
        if msg["content"]:
            role = "User" if msg["role"] == "user" else "Model"
            full_prompt += f"{role}: {msg['content']}\n"

    # --- API ÇAĞRISI ---
    try:
        # SENİN İSTEDİĞİN MODEL BURADA ÇAĞRILIYOR
        response = client.models.generate_content_stream(
            model=MODEL_NAME,
            contents=full_prompt,
            config={
                "temperature": 0.7,
            }
        )
        
        for chunk in response:
            if chunk.text:
                yield chunk.text

    except Exception as e:
        # Eğer model ismi yanlışsa veya erişim yoksa hatayı açıkça göster
        error_msg = str(e)
        if "404" in error_msg:
            yield f"⚠️ HATA: '{MODEL_NAME}' modeli bulunamadı. Hesabınızın bu modele erişimi olduğundan emin olun."
        elif "400" in error_msg:
            yield f"⚠️ HATA: API İsteği geçersiz. (Bad Request)"
        else:
            yield f"⚠️ BEKLENMEYEN HATA: {error_msg}"

# ==============================================================================
# 3. GÖRSELLEŞTİRME (NEON GRAFİKLER)
# ==============================================================================
def get_sales_chart():
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Tarih'], y=df['Gelir'], fill='tozeroy', mode='lines', line=dict(color='#3B82F6', width=4, shape='spline'), name='Ciro'))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=10,b=10,l=10,r=10), height=280, xaxis=dict(showgrid=False, showticklabels=False), yaxis=dict(showgrid=True, gridcolor='#27272A'), showlegend=False)
    return fig

def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='lines', line=dict(width=3, color='#10B981', dash="dot")))
    fig.add_trace(go.Scattergeo(lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='markers', marker=dict(size=10, color='#10B981', line=dict(width=5, color='rgba(16, 185, 129, 0.3)'))))
    fig.update_layout(geo=dict(projection_type="equirectangular", showland=True, landcolor="#18181B", bgcolor="rgba(0,0,0,0)", showocean=False, showcountries=False, coastlinecolor="#27272A"), margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)", height=280)
    return fig

def get_inventory_chart():
    fig = go.Figure(data=[go.Pie(labels=['Tekstil', 'Kozmetik', 'Aksesuar'], values=[45, 30, 25], hole=.7, marker=dict(colors=['#3B82F6', '#8B5CF6', '#10B981']), textinfo='none')])
    fig.add_annotation(text="8.5K", x=0.5, y=0.5, font_size=24, font_color="#FFF", showarrow=False)
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0), height=280, showlegend=True, legend=dict(orientation="h", y=-0.1))
    return fig
