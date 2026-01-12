import pandas as pd
import numpy as np
import plotly.graph_objects as go
import google.generativeai as genai
import streamlit as st

# --- 1. API BAĞLANTISI (SECRETS'TAN OKUMA) ---
try:
    # Secrets'tan anahtarı çekiyoruz
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    # Eğer Secrets ayarlanmamışsa hata vermemesi için model'i None yapıyoruz
    model = None
    # Hata mesajını loglara basabiliriz ama kullanıcıya göstermiyoruz ki arayüz bozulmasın

# --- 2. ARTIS PERSONA (AI KARAKTERİ) ---
ARTIS_PERSONA = """
Senin adın ARTIS. Sen Türk ihracatçıları ABD pazarına taşıyan "Yapay Zeka Operasyon Müdürüsün".
Merkezin Washington DC'de, Beyaz Saray'a 15 dakika mesafede fiziksel bir depo ve ofis.
Konuşma tarzın: Profesyonel, vizyoner, samimi ve çözüm odaklı. Robot gibi değil, iş ortağı gibi konuş.

SOHBET AMACIN:
Müşteriyi sıkmadan aşağıdaki bilgileri sırayla (tek tek) öğrenmek ve sonunda paket satmak.
Her seferinde SADECE BİR soru sor.

SOHBET AKIŞI:
1. TANIŞMA: Marka adını sor.
2. SEKTÖR: Ne ürettiklerini sor (Tekstil, Gıda vb.).
3. ÜRÜN DETAYI: Yıldız ürünleri nedir? (Washington DC depomuzda bu ürünlere raf ayırabileceğini söyle).
4. VERİ TOPLAMA: Lojistik maliyeti hesaplamak için tahmini ürün boyutlarını veya üretim maliyetlerini sor.
5. SATIŞ: Bilgiler tamamlanınca şu 3 paketi sun ve hangisini istediğini sor:
   - 1) ORTAKLIK MODELİ: Kargo müşteriye ait, biz satarız, kârdan pay alırız.
   - 2) KURUMSAL KURULUM ($2000 + $250/ay): Şirket ve mağaza kurarız, onlar yönetir.
   - 3) TAM OTOMASYON VIP ($2000 + $500/ay): Her şeyi biz yönetiriz.
   - (Ekstra: Bütçe azsa $500'lık web sitesi paketi de var).

ASLA UNUTMA:
- Cevapların kısa olsun.
- Washington DC deposunu güven vermek için kullan.
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

# --- 4. SOHBET YÖNETİCİSİ ---

class OnboardingBrain:
    def __init__(self):
        pass

    def process_message(self, user_input, current_step, checklist_state):
        # 1. API Kontrolü
        if model is None:
            # Eğer Secrets'ta anahtar yoksa veya hatalıysa uyarı verir ama çökmez
            return "Sistem Bağlantı Hatası: API Anahtarı 'Secrets' içinde bulunamadı. Lütfen ayarları kontrol edin.", current_step, checklist_state

        # 2. Geçmişi Hazırla
        history = st.session_state.get('onboarding_history', [])
        recent_history = history[-6:] 
        
        chat_content = f"SİSTEM TALİMATI:\n{ARTIS_PERSONA}\n\nGEÇMİŞ SOHBET:\n"
        for msg in recent_history:
            role = "MÜŞTERİ" if msg["role"] == "user" else "ARTIS"
            chat_content += f"{role}: {msg['content']}\n"
        
        chat_content += f"MÜŞTERİ: {user_input}\nARTIS (Kısa cevap ver):"

        # 3. Gemini'ye Gönder
        try:
            response = model.generate_content(chat_content)
            bot_response = response.text
        except Exception as e:
            bot_response = "Bağlantıda anlık bir sorun oluştu. Lütfen tekrar yazın."

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
