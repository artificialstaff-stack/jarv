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
    # API Key varsa al
    api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_APT_KEY")
    if not api_key: return None
    return genai.Client(api_key=api_key)

# --- 2. GELİŞMİŞ YEDEK CEVAPLAR (General Chat Özellikli) ---
# API çalışmazsa devreye giren "Offline Zeka" artık sohbet edebiliyor.
MOCK_RESPONSES = {
    # Genel Sohbet (Naber, nasılsın vb.)
    "sohbet": [
        "Teşekkürler, gayet iyiyim. Sistemlerimiz %100 performansla çalışıyor. Sizin için ne analiz edebilirim?",
        "Ben bir yapay zeka olduğum için hislerim yok ama işlemcilerim harika çalışıyor! Operasyonlar nasıl gidiyor?",
        "Her şey yolunda. Washington DC hattındaki verileri izliyorum. Bir isteğiniz var mı?",
        "Selamlar! Enerjim yerinde, analiz için hazırım."
    ],
    # Kimlik (Sen kimsin?)
    "kimlik": [
        "Ben ARTIS. Lojistik operasyonlarınızı yönetmek ve optimize etmek için tasarlanmış yeni nesil bir yapay zekayım.",
        "Adım ARTIS. Size lojistik, stok yönetimi ve finansal planlama konularında asistanlık yapıyorum.",
        "Sizin dijital operasyon müdürünüzüm diyebiliriz. 7/24 verilerinizi takip ediyorum."
    ],
    # İş Konuları
    "lojistik": [
        "Lojistik ağını tarıyorum... Şu an 1 aktif sevkiyatınız var: TR-8821 numaralı konteyner Atlantik Okyanusu'nda.",
        "Kargo takibi: Gümrük belgeleri onaylandı, gemi rotasında sorunsuz ilerliyor. Tahmini varış 48 saat.",
    ],
    "stok": [
        "Depo verilerine baktığımda doluluk oranı %64. Ancak 'Deri Çanta' stokları kritik seviyede (Son 50 adet).",
        "Envanter raporu: Tekstil grubu iyi durumda, aksesuar grubunda azalma var. Sipariş geçmemi ister misiniz?",
    ],
    "finans": [
        "Finansal özet: Bu ayki cironuz $42,500. Geçen aya göre %12 artış var. Kârlılık oranınız %32.",
        "Maliyet analizi: Reklam giderleri sabit kalırken ciro arttı. Bu ay oldukça verimli geçiyor.",
    ],
    # Anlamadığı durumlar için daha zeki kaçamak cevaplar
    "fallback": [
        "Bu konuda veri tabanımda yeterli bilgi yok ama operasyonel süreçlerinizle ilgili her şeyi sorabilirsiniz.",
        "Bunu tam olarak simüle edemiyorum ama lojistik veya finansal bir sorun varsa hemen çözebilirim.",
        "İlginç bir konu. Şimdilik odak noktam operasyonel verileriniz. Kargo durumuna bakmamı ister misiniz?"
    ]
}

def get_streaming_response(messages_history, user_data):
    client = get_client()
    last_msg = messages_history[-1]["content"].lower() if messages_history else ""
    
    # --- DURUM A: GERÇEK GEMINI API ---
    # Eğer API anahtarı doğruysa ve kota varsa burası çalışır (Sınırsız zeka)
    if client:
        try:
            # Yapay Zeka Kimliği
            sys_prompt = f"""
            Sen ARTIS. {user_data.get('brand')} markasının profesyonel Lojistik Operasyon AI asistanısın.
            
            Kişiliğin:
            - Profesyonel ama samimi.
            - Kısa ve net cevaplar veren.
            - Lojistik, finans ve stok uzmanı.
            
            Kullanıcı ne sorarsa sorsun (havadan sudan bile olsa) kibarca cevap ver ve konuyu işe/operasyona bağla.
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
            return # Başarılıysa çık, değilse aşağıya düş
            
        except Exception as e:
            # API Hatası durumunda loga yazılabilir ama kullanıcıya çaktırmıyoruz
            pass 

    # --- DURUM B: OFFLINE MOD (SİMÜLASYON) ---
    # API çalışmadığında devreye giren "Akıllı Taklit" modu
    time.sleep(0.6) 
    
    # Kelime Analizi (Basit NLP)
    if any(x in last_msg for x in ["naber", "nasılsın", "nasıl gidiyor", "selam", "merhaba", "hey"]):
        text = random.choice(MOCK_RESPONSES["sohbet"])
        
    elif any(x in last_msg for x in ["kimsin", "nesin", "adın ne", "görevin ne"]):
        text = random.choice(MOCK_RESPONSES["kimlik"])
        
    elif any(x in last_msg for x in ["lojistik", "kargo", "gemi", "nerede", "takip"]):
        text = random.choice(MOCK_RESPONSES["lojistik"])
        
    elif any(x in last_msg for x in ["stok", "ürün", "envanter", "mal", "depo"]):
        text = random.choice(MOCK_RESPONSES["stok"])
        
    elif any(x in last_msg for x in ["finans", "para", "ciro", "kar", "kazanç"]):
        text = random.choice(MOCK_RESPONSES["finans"])
        
    else:
        # Hiçbir şeye uymuyorsa "Anlamadım" demek yerine daha politik cevap ver
        text = random.choice(MOCK_RESPONSES["fallback"])

    # Kelime kelime yazdır
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)

# --- GRAFİKLER (MODERN GÖRÜNÜM) ---

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
