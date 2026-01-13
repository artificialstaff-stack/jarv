import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
from google.genai import types
import streamlit as st
import time
import random

# --- 1. GÜVENLİ İSTEMCİ ---
def get_client():
    api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_APT_KEY")
    if not api_key: return None
    return genai.Client(api_key=api_key)

# --- 2. GELİŞMİŞ YEDEK CEVAPLAR (Tekrara Düşmez) ---
MOCK_RESPONSES = {
    # Selamlaşma
    "greetings": [
        "Merhaba! Operasyonel süreçlerinizde size nasıl destek olabilirim?",
        "Selamlar. ARTIS sistemi kullanıma hazır. Rapor ister misiniz?",
        "Hoş geldiniz. Lojistik, stok veya finans verilerini analiz etmemi ister misiniz?"
    ],
    # Konu: Lojistik
    "lojistik": [
        "Şu an 1 aktif sevkiyatınız var: TR-8821 numaralı konteyner Atlantik Okyanusu'nda.",
        "Lojistik ağında gecikme görünmüyor. Tahmini varış süresi: 48 saat.",
        "Kargo takibi: Gümrük belgeleri onaylandı, gemi rotasında ilerliyor."
    ],
    # Konu: Stok
    "stok": [
        "Depo doluluk oranı %64. Ancak 'Deri Çanta' stokları kritik seviyede (Son 50 adet).",
        "Envanter analizi: Tekstil grubu stokları yeterli, aksesuar grubunda azalma var.",
        "Stoklarımızda 8,550 parça ürün bulunuyor. Riskli ürün: Deri Çanta."
    ],
    # Konu: Finans
    "finans": [
        "Bu ayki cironuz $42,500. Geçen aya göre %12 artış var.",
        "Finansal durum pozitif. Kârlılık oranınız %32 seviyesinde.",
        "Reklam harcamaları sabit kalırken gelirleriniz arttı. Verimli bir ay geçiriyoruz."
    ],
    # Bilinmeyen / Saçma Girdi (Random Seçilecek)
    "unknown": [
        "Bu komutu tam anlayamadım. 'Lojistik', 'Stok' veya 'Finans' hakkında soru sorabilirsiniz.",
        "Veri tabanımda bununla ilgili kayıt yok. Kargo durumunu veya ciroyu sormak ister misiniz?",
        "Sadece operasyonel verilere erişimim var. Lütfen geçerli bir talimat verin.",
        "Analiz edebilmem için daha net bir soru sorabilir misiniz? (Örn: Ciro ne kadar?)"
    ]
}

def get_streaming_response(messages_history, user_data):
    client = get_client()
    last_msg = messages_history[-1]["content"].lower() if messages_history else ""
    
    # --- DURUM A: API VARSA VE ÇALIŞIYORSA ---
    if client:
        try:
            sys_prompt = f"Sen ARTIS. {user_data.get('brand')} markasının AI asistanısın. Kısa ve profesyonel Türkçe konuş."
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
            return # Başarılıysa çık
        except Exception:
            pass # Hata olursa aşağıya (Yedek Mod) düş

    # --- DURUM B: YEDEK MOD (SİMÜLASYON) ---
    time.sleep(0.6) # Düşünme efekti
    
    # Akıllı Cevap Seçici
    if any(x in last_msg for x in ["selam", "merhaba", "naber", "günaydın", "hey"]):
        text = random.choice(MOCK_RESPONSES["greetings"])
        
    elif any(x in last_msg for x in ["lojistik", "kargo", "konum", "nerede", "gemi", "takip"]):
        text = random.choice(MOCK_RESPONSES["lojistik"])
        
    elif any(x in last_msg for x in ["stok", "ürün", "envanter", "mal", "depo"]):
        text = random.choice(MOCK_RESPONSES["stok"])
        
    elif any(x in last_msg for x in ["finans", "para", "ciro", "kar", "kazanç", "gelir"]):
        text = random.choice(MOCK_RESPONSES["finans"])
        
    else:
        # Tanımadığı bir şey yazılırsa (ddd, asd, vb.) rastgele bir "Anlamadım" mesajı seçer
        text = random.choice(MOCK_RESPONSES["unknown"])

    # Kelime kelime yazdır
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)

# --- GRAFİK MOTORU (NEON & MODERN) ---

def get_sales_chart():
    df = pd.DataFrame({'Tarih': pd.date_range('2026-01-01', periods=30), 'Gelir': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Tarih'], y=df['Gelir'], fill='tozeroy', mode='lines',
        line=dict(color='#3B82F6', width=4, shape='spline'), name='Ciro'
    ))
    fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=10,b=10,l=10,r=10), height=280,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=True, gridcolor='#27272A', zeroline=False), showlegend=False
    )
    return fig

def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='lines', 
        line=dict(width=3, color='#10B981', dash="dot")
    ))
    fig.add_trace(go.Scattergeo(
        lon=[28.9784, -77.0369], lat=[41.0082, 38.9072], mode='markers', 
        marker=dict(size=10, color='#10B981', line=dict(width=5, color='rgba(16, 185, 129, 0.3)'))
    ))
    fig.update_layout(
        geo=dict(
            projection_type="equirectangular", showland=True, landcolor="#18181B", 
            bgcolor="rgba(0,0,0,0)", showocean=False, showcountries=False, coastlinecolor="#27272A"
        ), margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)", height=280
    )
    return fig

def get_inventory_chart():
    labels = ['Tekstil', 'Kozmetik', 'Aksesuar', 'Diğer']
    values = [45, 25, 20, 10]
    colors = ['#3B82F6', '#8B5CF6', '#10B981', '#64748B']
    fig = go.Figure(data=[go.Pie(
        labels=labels, values=values, hole=.7, 
        marker=dict(colors=colors, line=dict(color='#09090B', width=5)), 
        textinfo='none', hoverinfo='label+percent'
    )])
    fig.add_annotation(text="8.5K", x=0.5, y=0.5, font_size=24, font_color="#FFF", showarrow=False)
    fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=0, b=0, l=0, r=0), height=280, showlegend=True,
        legend=dict(orientation="h", y=-0.1)
    )
    return fig
