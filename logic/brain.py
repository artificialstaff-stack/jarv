import streamlit as st
from google import genai
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. MODEL YAPILANDIRMASI (GÜNCEL: GEMINI 3 FLASH) ---
# En yeni ve hızlı model: gemini-3-flash-preview
MODEL_NAME = "gemini-3-flash-preview" 

def get_client():
    """
    Google GenAI istemcisini güvenli bir şekilde başlatır.
    Önce Streamlit secrets, sonra ortam değişkenlerini kontrol eder.
    """
    api_key = None
    # Streamlit Cloud'da secrets.toml dosyasından okur
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
    elif "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
    # Lokal ortam değişkenlerinden okur
    elif "GOOGLE_API_KEY" in os.environ:
        api_key = os.environ["GOOGLE_API_KEY"]

    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key # SDK bazen env'den okumayı tercih eder
        try:
            # Google GenAI v0.1+ Client Başlatma
            return genai.Client(api_key=api_key)
        except Exception as e:
            print(f"Client Init Error: {e}")
            return None
    return None

# --- 2. AI MOTORU (Çift Parametre Garantili) ---
def get_streaming_response(messages_history, user_data):
    """
    Dashboard'dan gelen mesajları ve kullanıcı verisini alıp
    Gemini 3 Flash modeline iletir ve cevabı stream eder.
    """
    client = get_client()
    
    # Kullanıcı markasını güvenli çek
    brand = user_data.get('brand', 'Şirket') if user_data else 'Şirket'
    user_name = user_data.get('name', 'Yönetici') if user_data else 'Yönetici'
    
    # Sistem Talimatı (Persona)
    sys_instruction = (
        f"Sen ARTIS. {brand} markası için çalışan, üst düzey bir Global Operasyon Asistanısın. "
        f"Kullanıcı adı: {user_name}. "
        "Cevapların kısa, net, profesyonel ve çözüm odaklı olsun. "
        "Veri analizi yapıyormuş gibi davran. Türkçe konuş."
    )
    
    full_prompt = f"System: {sys_instruction}\n\n"
    
    # Mesaj Geçmişini Ekle
    for msg in messages_history:
        role = "User" if msg["role"] == "user" else "Model"
        full_prompt += f"{role}: {msg['content']}\n"

    # API Kontrolü
    if not client:
        yield "⚠️ API Anahtarı bulunamadı. Lütfen .streamlit/secrets.toml dosyasına GOOGLE_API_KEY ekleyin."
        # Demo modunda olduğumuz belli olsun diye sahte bir cevap da dönebiliriz:
        yield f"\n\n[SİMÜLASYON]: {brand} verilerini analiz ediyorum... (API Key eksik olduğu için bu bir simülasyondur)."
        return

    # Canlı Cevap Üretimi (Gemini 3 Flash)
    try:
        # v0.1 SDK'sında generate_content methodu kullanılır
        response = client.models.generate_content_stream(
            model=MODEL_NAME, # gemini-3-flash-preview
            contents=full_prompt
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"❌ Bağlantı Hatası ({MODEL_NAME}): {str(e)}"

# --- 3. GÖRSELLEŞTİRME FABRİKASI (Silicon Valley Style) ---

def get_sales_chart():
    """Finans Sayfası İçin: Altın Rengi Alan Grafiği"""
    dates = pd.date_range(end=pd.Timestamp.now(), periods=30)
    values = np.random.normal(1200, 150, 30).cumsum() # Kümülatif artış efekti
    values = values + 10000 # Baz değer
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates, y=values, 
        mode='lines', 
        fill='tozeroy',
        line=dict(color='#C5A059', width=3), # Kurumsal Altın Rengi
        name='Ciro'
    ))
    
    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=20, l=20, r=20),
        height=320,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    )
    return fig

def get_logistics_map():
    """Lojistik Sayfası İçin: Dünya Haritası ve Rota"""
    fig = go.Figure()

    # Rota: İstanbul -> New York
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -74.0060],
        lat = [41.0082, 40.7128],
        mode = 'lines+markers',
        line = dict(width=2, color='#3B82F6', dash="dashdot"), # Mavi Rota
        marker = dict(size=8, color='#C5A059'), # Altın Noktalar
        name = 'TR-8821 Hattı'
    ))

    # Rota: İstanbul -> Berlin
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, 13.4050],
        lat = [41.0082, 52.5200],
        mode = 'lines+markers',
        line = dict(width=2, color='#10B981', dash="solid"), 
        marker = dict(size=6, color='#10B981'),
        name = 'EU-Express'
    ))

    fig.update_layout(
        template='plotly_dark',
        geo=dict(
            showland=True,
            landcolor="rgba(30, 30, 30, 1)",
            oceancolor="rgba(0, 0, 0, 0)",
            showocean=False,
            bgcolor='rgba(0,0,0,0)',
            projection_type="equirectangular"
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=0, b=0, l=0, r=0),
        height=320
    )
    return fig

def get_inventory_chart():
    """Envanter Sayfası İçin: Donut Grafik"""
    labels = ['Tekstil', 'Ev Dekoru', 'Aksesuar', 'Kozmetik']
    values = [4500, 2500, 1050, 500]
    colors = ['#C5A059', '#3B82F6', '#10B981', '#EF4444'] # Altın, Mavi, Yeşil, Kırmızı

    fig = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values, 
        hole=.6, # Donut Efekti
        marker=dict(colors=colors)
    )])

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=20, l=20, r=20),
        height=320,
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="right", x=1)
    )
    return fig
