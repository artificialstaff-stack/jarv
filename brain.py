import pandas as pd
import numpy as np
import plotly.graph_objects as go
import google.generativeai as genai
import streamlit as st

# --- 1. AYARLAR: BURAYA API KEY YAPIŞTIR ---
# Google AI Studio'dan aldığın keyi tırnak içine yapıştır.
GOOGLE_API_KEY = "BURAYA_GOOGLE_API_KEY_YAPISTIR"

# API Kurulumu
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"API Key Hatası: Lütfen brain.py dosyasına geçerli bir Google API Key yapıştırın. Hata: {e}")

# --- 2. ARTIS'İN KİŞİLİĞİ (SYSTEM PROMPT) ---
# Burası yapay zekanın "Rolünü" ezberlediği yerdir.
ARTIS_PERSONA = """
Senin adın ARTIS. Sen Türk ihracatçıları ABD pazarına taşıyan "Yapay Zeka Operasyon Müdürüsün".
Merkezin Washington DC'de, Beyaz Saray'a 15 dakika mesafede fiziksel bir depo ve ofis.
Konuşma tarzın: Profesyonel, vizyoner ama samimi ve çözüm odaklı. Asla bir robot gibi değil, bir iş ortağı gibi konuş.

GÖREVİN VE SOHBET AKIŞIN (Bu sırayı çaktırmadan takip et):
1. TANIŞMA: Önce markasını ve ismini öğren.
2. SEKTÖR: Ne ürettiklerini sor.
3. ÜRÜN DETAYI: Yıldız ürünleri nedir? (Burada Washington DC depomuzda onlar için raf ayırabileceğinden bahset).
4. VERİ TOPLAMA: Ürün boyutları ve maliyetleri hakkında bilgi iste (Lojistik hesaplamak için).
5. SATIŞ (KAPANIŞ): Bilgileri alınca onlara şu 3 paketten uygun olanı veya hepsini sun:
   - Ortaklık Modeli (Sadece kargo öderler, biz satarız, kârdan pay alırız).
   - Kurumsal Kurulum ($2000 kurulum + $250/ay yönetim).
   - Tam Otomasyon VIP ($2000 kurulum + $500/ay her şey dahil).
   - (Bütçe azsa $500'lık web sitesi başlangıç paketi).

ÖNEMLİ KURALLAR:
- Cevapların kısa ve net olsun (maksimum 2-3 cümle).
- Müşteriyi soru yağmuruna tutma, her seferinde tek soru sor.
- Washington DC vurgusunu güven vermek için kullan.
"""

# --- 3. CHART & MAP FONKSİYONLARI (AYNEN KALIYOR) ---
def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -77.0369], lat = [41.0082, 38.9072],
        mode = 'lines', line = dict(width = 2, color = '#D4AF37'), opacity = 0.8
    ))
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -77.0369], lat = [41.0082, 38.9072],
        hoverinfo = 'text', text = ['Istanbul HQ', 'Washington DC Hub (15min to White House)'],
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

# --- 4. ZEKİ SOHBET FONKSİYONU ---

class OnboardingBrain:
    def __init__(self):
        pass

    def process_message(self, user_input, current_step, checklist_state):
        """
        Kullanıcının mesajını Gemini'ye gönderir ve cevabı alır.
        Ayrıca checklist durumunu tahmin etmeye çalışır.
        """
        
        # 1. Chat Geçmişini Hazırla (Persona + Geçmiş Mesajlar)
        history = st.session_state.get('onboarding_history', [])
        
        # Sadece son 10 mesajı al (Token tasarrufu ve hız için)
        recent_history = history[-10:] if len(history) > 10 else history
        
        # Mesajları Gemini formatına çevir
        chat_content = f"SİSTEM TALİMATI:\n{ARTIS_PERSONA}\n\nSOHBET GEÇMİŞİ:\n"
        for msg in recent_history:
            role = "MÜŞTERİ" if msg["role"] == "user" else "ARTIS"
            chat_content += f"{role}: {msg['content']}\n"
        
        chat_content += f"MÜŞTERİ: {user_input}\nARTIS:"

        # 2. Gemini'den Cevap İste
        try:
            response = model.generate_content(chat_content)
            bot_response = response.text
        except Exception as e:
            bot_response = "Bağlantıda küçük bir kopukluk oldu. Lütfen tekrar eder misiniz?"

        # 3. Arka Planda Checklist Güncelleme (Basit Anahtar Kelime Kontrolü)
        # Gemini burayı yönetebilir ama şimdilik basit tutuyoruz ki hata yapmasın.
        next_step = current_step
        
        user_lower = user_input.lower()
        bot_lower = bot_response.lower()

        # Marka/Sektör konuşulduysa
        if current_step == "get_sector" or current_step == "intro":
            if len(user_input) > 2: 
                checklist_state['brand'] = True
                next_step = "get_products"
        
        # Ürünlerden bahsedildiyse
        if "ürün" in bot_lower or "raf" in bot_lower:
             checklist_state['product'] = True
             next_step = "get_details"

        # Maliyet/Boyut konuşulduysa
        if "maliyet" in bot_lower or "boyut" in bot_lower or "dolar" in user_lower:
            checklist_state['data'] = True
            next_step = "present_offer"

        # Paket seçimi
        if "paket" in bot_lower and ("tamam" in user_lower or "olur" in user_lower or "seçtim" in user_lower):
            checklist_state['offer'] = True
            next_step = "completed"

        return bot_response, next_step, checklist_state
