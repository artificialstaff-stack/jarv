import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
from google.genai import types
import streamlit as st
import time
import random

# ==============================================================================
# 🧠 ARTIS INTELLIGENCE CORE (BACKEND LOGIC)
# ==============================================================================

# --- 1. GÜVENLİ İSTEMCİ & API YÖNETİMİ ---
def get_client():
    # API Key varsa al, yoksa None dön (Hata patlatma)
    api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_APT_KEY")
    if not api_key: return None
    return genai.Client(api_key=api_key)

# --- 2. YEDEK CEVAPLAR (FALLBACK MECHANISM) ---
# API kotası dolarsa veya anahtar yoksa devreye giren "Hayalet Mod"
MOCK_RESPONSES = {
    "default": "Sistem analizlerime göre Washington DC operasyon akışınız %98 verimlilikle devam ediyor. Lojistik, envanter veya finansal raporlarınızı sunabilirim.",
    "lojistik": "Lojistik ağında 1 aktif sevkiyat tespit edildi. TR-8821 numaralı konteyner şu an Atlantik rotasında ve plana uygun ilerliyor. Tahmini varış: 48 saat.",
    "stok": "Depo doluluk oranınız %64 seviyesinde. Kritik Uyarı: 'Deri Çanta' stokları güvenlik sınırının altına indi (Son 50 adet). Otomatik sipariş öneriyorum.",
    "finans": "Finansal özet: Bu ayki cironuz $42,500 seviyesine ulaştı. Geçen aya göre %12'lik bir büyüme trendi var. Operasyonel maliyetler optimize edildi."
}

def get_streaming_response(messages_history, user_data):
    """
    Kullanıcı mesajına göre API'den veya Yedek Veritabanından cevap üretir.
    Asla hata vermez (Fail-Safe).
    """
    client = get_client()
    
    # Kullanıcının son mesajını analiz et (Basit NLP)
    last_msg = messages_history[-1]["content"].lower() if messages_history else ""
    
    # --- DURUM A: API BAĞLANTISI VAR ---
    if client:
        try:
            sys_prompt = f"""
            Sen ARTIS. {user_data.get('brand')} markasının Lojistik ve Operasyon Yapay Zekasısın.
            Tonun: Profesyonel, fütüristik, güven verici ve net.
            Görevin: Kullanıcıya verilerle destek olmak. Asla hayali bilgi uydurma.
            """
            contents = [types.Content(role="user", parts=[types.Part.from_text(text=sys_prompt)])]
            for msg in messages_history:
                role = "user" if msg["role"] == "user" else "model"
                if msg["content"]:
                    contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

            response = client.models.generate_content_stream(
                model="gemini-2.5-flash", contents=contents, config=types.GenerateContentConfig(temperature=0.7)
            )
            for chunk in response:
                if chunk.text: yield chunk.text
            return # Başarılıysa fonksiyondan çık
            
        except Exception:
            pass # API hatası olursa sessizce Durum B'ye geç

    # --- DURUM B: YEDEK MOD (SİMÜLASYON) ---
    time.sleep(0.8) # "Düşünüyor" efekti
    
    # Konuya uygun cevabı seç
    if any(x in last_msg for x in ["lojistik", "kargo", "konum", "nerede", "gemi"]):
        text = MOCK_RESPONSES["lojistik"]
    elif any(x in last_msg for x in ["stok", "ürün", "envanter", "mal"]):
        text = MOCK_RESPONSES["stok"]
    elif any(x in last_msg for x in ["finans", "para", "ciro", "kar", "kazanç"]):
        text = MOCK_RESPONSES["finans"]
    else:
        text = MOCK_RESPONSES["default"]

    # Kelime kelime yazdır (Streaming simülasyonu)
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.04)

# ==============================================================================
# 📊 NEXT-GEN VISUALIZATION ENGINE (GRAFİK MOTORU)
# ==============================================================================

def get_sales_chart():
    """Modern, yumuşak geçişli (Spline) Alan Grafiği"""
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Tarih'], y=df['Gelir'], 
        fill='tozeroy', # Altını doldur
        mode='lines',
        line=dict(color='#3B82F6', width=3, shape='spline'), # Spline = Yumuşak kıvrımlar
        name='Ciro'
    ))
    
    fig.update_layout(
        template='plotly_dark', 
        paper_bgcolor='rgba(0,0,0,0)', # Şeffaf arka plan
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=10,b=10,l=10,r=10), 
        height=280,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False), # X eksenini temizle
        yaxis=dict(showgrid=True, gridcolor='#27272A', zeroline=False), # Izgarayı çok silik yap
        showlegend=False
    )
    return fig

def get_logistics_map():
    """Minimalist, Holografik Dünya Haritası"""
    fig = go.Figure()
    
    # Rota Çizgisi (Kesik Çizgi - Animasyon hissi verir)
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], 
        mode='lines', 
        line=dict(width=2, color='#10B981', dash="dot")
    ))
    
    # Noktalar (Parlayan Efektli)
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], 
        mode='markers', 
        marker=dict(size=8, color='#10B981', line=dict(width=4, color='rgba(16, 185, 129, 0.2)'))
    ))

    fig.update_layout(
        geo=dict(
            projection_type="equirectangular", 
            showland=True, 
            landcolor="#18181B", # Koyu gri kara parçaları
            bgcolor="rgba(0,0,0,0)", # Şeffaf okyanus
            showocean=False,
            showcountries=False,
            coastlinecolor="#27272A"
        ), 
        margin={"r":0,"t":0,"l":0,"b":0}, 
        paper_bgcolor="rgba(0,0,0,0)",
        height=280
    )
    return fig

def get_inventory_chart():
    """Modern Donut (Halka) Grafiği - Ortası boş"""
    labels = ['Tekstil', 'Kozmetik', 'Aksesuar', 'Diğer']
    values = [45, 25, 20, 10]
    # Modern renk paleti
    colors = ['#3B82F6', '#8B5CF6', '#10B981', '#64748B']

    fig = go.Figure(data=[go.Pie(
        labels=labels, values=values, hole=.7, # %70 boşluk
        marker=dict(colors=colors, line=dict(color='#09090B', width=4)), # Dilimler arası boşluk
        textinfo='none', # Üzerindeki yazıları kaldır (Temiz görünüm)
        hoverinfo='label+percent'
    )])
    
    # Ortaya Toplam Yazısı Ekleme
    fig.add_annotation(text="8.5K", x=0.5, y=0.5, font_size=24, font_color="#FFF", showarrow=False)
    
    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=0, b=0, l=0, r=0),
        height=280,
        showlegend=True,
        legend=dict(orientation="h", y=-0.1) # Legendi alta al
    )
    return fig
