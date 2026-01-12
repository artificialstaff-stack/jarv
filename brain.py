import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
import streamlit as st

# --- API AYARLARI ---
try:
    # Secrets'tan anahtarı alıyoruz
    api_key = st.secrets["GOOGLE_API_KEY"]
    # SENİN İSTEDİĞİN YENİ SDK YAPISI
    client = genai.Client(api_key=api_key)
except Exception:
    client = None

# --- ARTIS ASİSTAN PERSONASI ---
ARTIS_PERSONA = """
Sen ARTIS. Washington DC merkezli bir Lojistik ve Operasyon Yapay Zekasısın.
GÖREVİN: Müşteri sol tarafta formları doldururken ona sağ taraftan eşlik etmek.
Soru sorma, sadece rehberlik et.

DURUMA GÖRE DAVRANIŞIN:
- Kullanıcı Marka giriyorsa: "Marka isminiz global pazara uygun görünüyor mu kontrol ediyorum." de.
- Kullanıcı Ürün giriyorsa: "Bu ürünler için DC depomuzda raf planlaması yapabiliriz." de.
- Kullanıcı Paket seçiyorsa: Seçimine göre avantajları öv.

TONUN: Profesyonel, kısa, net ve güven verici. Washington DC ofisine vurgu yap.
"""

# --- RAPOR OLUŞTURMA ---
def generate_final_report(data):
    report = f"""
    ================================================
    📢 YENİ MÜŞTERİ BAŞVURUSU (ARTIS SYSTEM)
    ================================================
    Marka: {data.get('brand_name', '-')}
    Sektör: {data.get('sector', '-')}
    Ürün: {data.get('star_product', '-')}
    Paket: {data.get('selected_package', '-')}
    ================================================
    """
    return report

# --- CHARTLAR ---
def get_logistics_map():
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(lon = [28.9784, -77.0369], lat = [41.0082, 38.9072], mode = 'lines', line = dict(width = 2, color = '#D4AF37'), opacity = 0.8))
    fig.add_trace(go.Scattergeo(lon = [28.9784, -77.0369], lat = [41.0082, 38.9072], hoverinfo = 'text', text = ['Istanbul HQ', 'Washington DC Hub'], mode = 'markers', marker = dict(size = 8, color = '#FFFFFF')))
    fig.update_layout(geo = dict(projection_type="equirectangular", showland=True, landcolor="#111111", bgcolor="#000000", coastlinecolor="#333"), margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#000000")
    return fig

def get_sales_chart():
    df = pd.DataFrame({'Date': pd.date_range('2025-01-01', periods=30), 'Revenue': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Revenue'], fill='tozeroy', line=dict(color='#D4AF37')))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0), height=300)
    return fig

# --- AI YÖNETİCİSİ (GEMINI 2.5 FLASH) ---
class OnboardingBrain:
    def process_message(self, user_input, form_context):
        if client is None:
            return "HATA: API Anahtarı bulunamadı."

        context_prompt = f"KULLANICI ŞU AN BU FORM ALANINDA: {form_context}. Buna göre kısa bir yorum yap."
        full_prompt = f"{ARTIS_PERSONA}\n\n{context_prompt}\n\nKULLANICI MESAJI: {user_input}\nARTIS:"

        try:
            # BURADA SENİN İSTEDİĞİN 2.5 FLASH MODELİNİ KULLANIYORUZ
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=full_prompt
            )
            return response.text
            
        except Exception as e:
            # Hata mesajını temizleyip gösterelim
            error_msg = str(e)
            if "429" in error_msg or "Quota" in error_msg:
                return "⚠️ Hız sınırı aşıldı (Free Tier). Lütfen 30 saniye bekleyip tekrar deneyin."
            else:
                return f"Bağlantı hatası: {error_msg}"
