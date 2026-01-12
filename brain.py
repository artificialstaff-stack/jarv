import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai  # İstediğin yeni kütüphane
import streamlit as st

# --- 1. API BAĞLANTISI (YENİ SDK & SECRETS) ---
try:
    # Secrets panelindeki "GOOGLE_API_KEY"i okur. 
    # (Panelde APT yazdıysan API olarak düzeltmelisin)
    api_key = st.secrets["GOOGLE_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    client = None

# --- 2. ARTIS PERSONA ---
ARTIS_PERSONA = """
Senin adın ARTIS. Sen Türk ihracatçıları ABD pazarına taşıyan "Yapay Zeka Operasyon Müdürüsün".
Merkezin Washington DC'de, Beyaz Saray'a 15 dakika mesafede fiziksel bir depo ve ofis.
Konuşma tarzın: Profesyonel, vizyoner, samimi ve çözüm odaklı.

SOHBET AKIŞI:
1. TANIŞMA: Marka adını sor.
2. SEKTÖR: Ne ürettiklerini sor.
3. ÜRÜN DETAYI: Yıldız ürünleri nedir? (DC depomuzda raf ayırabileceğini söyle).
4. VERİ TOPLAMA: Lojistik için ürün boyutlarını veya maliyetlerini sor.
5. SATIŞ: Bilgiler tamamlanınca şu 3 paketi sun:
   - ORTAKLIK MODELİ (Sadece kargo öderler).
   - KURUMSAL KURULUM ($2000 + $250/ay).
   - TAM OTOMASYON VIP ($2000 + $500/ay).

ASLA UNUTMA:
- Kısa cevap ver.
- Washington DC deposunu vurgula.
"""

# --- 3. CHART & MAP FONKSİYONLARI ---
def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -77.0369], lat = [41.0082, 38.9072],
        mode = 'lines', line = dict(width = 2, color = '#D4AF37'), opacity = 0.8
    ))
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -77.0369], lat = [41.0082, 38.9072],
        hoverinfo = 'text', text = ['Istanbul HQ', 'Washington DC Hub'],
        mode = 'markers', marker = dict(size = 8, color = '#FFFFFF')
    ))
    fig.update_layout(
        geo = dict(projection_type="equirectangular", showland=True, landcolor="#111111", bgcolor="#000000", coastlinecolor="#333"),
        margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#000000",
    )
    return fig

def get_sales_chart():
    df = pd.DataFrame({'Date': pd.date_range('2025-01-01', periods=30), 'Revenue': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Revenue'], fill='tozeroy', line=dict(color='#D4AF37')))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0), height=300)
    return fig

# --- 4. SOHBET YÖNETİCİSİ (GEMINI 2.5 FLASH) ---
class OnboardingBrain:
    def process_message(self, user_input, current_step, checklist_state):
        # 1. Client Kontrolü
        if client is None:
            return "HATA: API Anahtarı bulunamadı. Lütfen Secrets panelinde anahtar adının 'GOOGLE_API_KEY' (P değil I ile) olduğundan emin olun.", current_step, checklist_state

        # 2. Geçmişi Hazırla
        history = st.session_state.get('onboarding_history', [])
        recent_history = history[-6:] 
        
        chat_content = f"SİSTEM TALİMATI:\n{ARTIS_PERSONA}\n\nGEÇMİŞ SOHBET:\n"
        for msg in recent_history:
            role = "MÜŞTERİ" if msg["role"] == "user" else "ARTIS"
            chat_content += f"{role}: {msg['content']}\n"
        
        chat_content += f"MÜŞTERİ: {user_input}\nARTIS (Kısa cevap ver):"

        # 3. Gemini 2.5 Flash'a Gönder
        try:
            # İSTEDİĞİN YENİ MODEL VE KOD YAPISI BURADA:
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=chat_content
            )
            bot_response = response.text
        except Exception as e:
            bot_response = f"Bağlantı hatası: {str(e)}. (Model adını veya API Key'i kontrol edin)."

        # 4. Durum Güncelleme
        next_step = current_step
        user_len = len(user_input)

        if current_step == "intro" and user_len > 2:
            checklist_state['brand'] = True
            next_step = "get_sector"
        elif current_step == "get_sector" and user_len > 2:
            checklist_state['brand'] = True
            next_step = "get_products" 
        elif current_step == "get_products" and user_len > 2:
            checklist_state['product'] = True
            next_step = "get_details"
        elif current_step == "get_details" and user_len > 1:
            checklist_state['data'] = True
            next_step = "present_offer"
        elif current_step == "present_offer" and user_len > 1:
            checklist_state['offer'] = True
            next_step = "completed"

        return bot_response, next_step, checklist_state
