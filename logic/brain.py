import streamlit as st
from google import genai
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ==============================================================================
# ⚙️ KONFİGÜRASYON (AYARLAR)
# ==============================================================================
# Eğer Google'dan özel erişimin varsa burayı "gemini-3-flash-preview" yapabilirsin.
# Şu an genel erişime açık en güçlü model: "gemini-2.0-flash-exp"
MODEL_NAME = "gemini-2.0-flash-exp" 

# ==============================================================================
# 1. API İSTEMCİSİ (ENVIRONMENT VARIABLE YÖNTEMİ)
# ==============================================================================
def get_client():
    """
    Streamlit secrets içindeki API anahtarını işletim sistemi ortam değişkenine
    (os.environ) atar. Bu sayede genai.Client() parametresiz çağrılabilir.
    """
    # 1. Anahtarı Secrets'tan al
    api_key = None
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
    elif "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]

    # 2. Ortam Değişkenine Ata (SDK bunu otomatik okur)
    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key
        os.environ["GOOGLE_API_KEY"] = api_key # Her ihtimale karşı ikisini de set et
    else:
        st.error("❌ HATA: API Key bulunamadı! .streamlit/secrets.toml dosyasını kontrol edin.")
        return None
    
    try:
        # Parametresiz çağrı (Senin istediğin yapı)
        client = genai.Client()
        return client
    except Exception as e:
        st.error(f"❌ Client Başlatma Hatası: {str(e)}")
        return None

# ==============================================================================
# 2. SOHBET MOTORU (SAF ZEKA)
# ==============================================================================
def get_streaming_response(messages_history, user_data):
    """
    Kullanıcı mesajlarını tek bir prompt metni haline getirir ve
    Gemini modeline gönderir. Cevabı parça parça (stream) döner.
    """
    client = get_client()
    if not client:
        yield "⚠️ Sistem Bağlantı Hatası: API Anahtarı doğrulanamadı."
        return

    # --- A. SİSTEM TALİMATI ---
    brand_name = user_data.get('brand', 'Şirket')
    sys_instruction = f"""
    Sen ARTIS. {brand_name} markası için çalışan, profesyonel ve veriye dayalı bir Lojistik AI Asistanısın.
    Görevin: Kullanıcının lojistik, stok ve finans sorularını net, kısa ve profesyonelce yanıtlamak.
    Kural: Asla rolünden çıkma. Kullanıcı samimi konuşursa samimi, resmi konuşursa resmi cevap ver.
    """

    # --- B. GEÇMİŞİ FORMATLA ---
    # Chat geçmişini tek bir metin bloğuna dönüştürüyoruz.
    # Bu yöntem, modelin bağlamı kaybetmemesini garanti eder.
    conversation_text = [f"System Instruction: {sys_instruction}"]
    
    for msg in messages_history:
        if msg["content"]:
            role_prefix = "User" if msg["role"] == "user" else "Model"
            conversation_text.append(f"{role_prefix}: {msg['content']}")
            
    # Sonuna Model'in cevap vereceğini belirten bir işaret ekleyebiliriz (Opsiyonel)
    full_prompt = "\n\n".join(conversation_text)

    # --- C. API ÇAĞRISI ---
    try:
        response = client.models.generate_content_stream(
            model=MODEL_NAME, 
            contents=full_prompt,
            config={
                "temperature": 0.7, # Yaratıcılık seviyesi
                "max_output_tokens": 800, # Cevap uzunluğu
            }
        )
        
        for chunk in response:
            if chunk.text:
                yield chunk.text

    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg:
            yield f"⚠️ MODEL HATASI: '{MODEL_NAME}' modeli bulunamadı. Lütfen 'MODEL_NAME' değişkenini 'gemini-1.5-flash' olarak değiştirip deneyin."
        elif "400" in error_msg or "API key" in error_msg:
            yield f"⚠️ YETKİ HATASI: API Anahtarı geçersiz. Lütfen secrets.toml dosyasını kontrol edin."
        else:
            yield f"⚠️ BEKLENMEYEN HATA: {error_msg}"

# ==============================================================================
# 3. VERİ GÖRSELLEŞTİRME (PLOTLY)
# ==============================================================================
def get_sales_chart():
    # Modern Alan Grafiği (Spline - Yumuşak Geçişli)
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Tarih'], y=df['Gelir'], 
        fill='tozeroy', mode='lines', 
        line=dict(color='#3B82F6', width=4, shape='spline'), 
        name='Ciro'
    ))
    fig.update_layout(
        template='plotly_dark', 
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
        margin=dict(t=10,b=10,l=10,r=10), height=280, 
        xaxis=dict(showgrid=False, showticklabels=False), 
        yaxis=dict(showgrid=True, gridcolor='#27272A'), 
        showlegend=False
    )
    return fig

def get_logistics_map():
    # Neon Stil Dünya Haritası
    fig = go.Figure()
    # Rota Çizgisi
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], 
        mode='lines', line=dict(width=3, color='#10B981', dash="dot")
    ))
    # Konum Noktaları
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], 
        mode='markers', 
        marker=dict(size=10, color='#10B981', line=dict(width=5, color='rgba(16, 185, 129, 0.3)'))
    ))
    fig.update_layout(
        geo=dict(
            projection_type="equirectangular", showland=True, 
            landcolor="#18181B", bgcolor="rgba(0,0,0,0)", 
            showocean=False, showcountries=False, coastlinecolor="#27272A"
        ), 
        margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)", height=280
    )
    return fig

def get_inventory_chart():
    # Modern Halka (Donut) Grafik
    fig = go.Figure(data=[go.Pie(
        labels=['Tekstil', 'Kozmetik', 'Aksesuar'], 
        values=[45, 30, 25], hole=.7, 
        marker=dict(colors=['#3B82F6', '#8B5CF6', '#10B981']), 
        textinfo='none'
    )])
    # Ortaya Dinamik Rakam
    fig.add_annotation(text="8.5K", x=0.5, y=0.5, font_size=24, font_color="#FFF", showarrow=False)
    fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', 
        margin=dict(t=0, b=0, l=0, r=0), height=280, 
        showlegend=True, legend=dict(orientation="h", y=-0.1)
    )
    return fig
