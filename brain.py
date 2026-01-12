import pandas as pd
import numpy as np
import plotly.graph_objects as go
from google import genai
import streamlit as st

# --- API AYARLARI ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
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

# --- RAPOR OLUŞTURMA FONKSİYONU ---
def generate_final_report(data):
    """
    Tüm form verilerini alır ve yöneticiye gidecek bir mail taslağı oluşturur.
    """
    report = f"""
    ================================================
    📢 YENİ MÜŞTERİ BAŞVURUSU (ARTIS SYSTEM)
    ================================================
    
    1. KİMLİK BİLGİLERİ
    -------------------
    Marka Adı: {data.get('brand_name', 'Girilmedi')}
    Sektör: {data.get('sector', 'Girilmedi')}
    
    2. ÜRÜN & ENVANTER
    ------------------
    Yıldız Ürün: {data.get('star_product', 'Girilmedi')}
    Tahmini Stok Boyutu: {data.get('dimensions', 'Girilmedi')}
    
    3. LOJİSTİK PLANI
    -----------------
    Hedef Depo: Washington DC Hub (US-IAD)
    Lojistik Durumu: Beklemede
    
    4. SEÇİLEN PAKET
    ----------------
    Paket: {data.get('selected_package', 'Seçilmedi')}
    
    ================================================
    🤖 ARTIS AI ONAYI: [DOĞRULANDI]
    Tarih: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}
    ================================================
    """
    return report

# --- CHART FONKSİYONLARI ---
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

# --- AI SOHBET YÖNETİCİSİ ---
class OnboardingBrain:
    def process_message(self, user_input, form_context):
        if client is None:
            return "HATA: API Anahtarı bulunamadı."

        # Asistana o an kullanıcının hangi formu doldurduğunu söylüyoruz
        context_prompt = f"KULLANICI ŞU AN BU FORM ALANINDA: {form_context}. Buna göre kısa bir yorum yap veya sorusunu cevapla."
        
        full_prompt = f"{ARTIS_PERSONA}\n\n{context_prompt}\n\nKULLANICI MESAJI: {user_input}\nARTIS:"

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=full_prompt
            )
            return response.text
        except Exception as e:
            return f"Bağlantı hatası: {str(e)}"
