import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

# --- LOGISTICS & SALES CHARTS ---
def get_logistics_map():
    """Washington DC ve İstanbul arasındaki rotayı çizer."""
    fig = go.Figure()
    
    # Rota: İstanbul -> Washington DC
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -77.0369], 
        lat = [41.0082, 38.9072],
        mode = 'lines', 
        line = dict(width = 2, color = '#D4AF37'),
        opacity = 0.8
    ))
    
    # Noktalar
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -77.0369],
        lat = [41.0082, 38.9072],
        hoverinfo = 'text',
        text = ['Istanbul HQ', 'Washington DC Hub (15min to White House)'],
        mode = 'markers', 
        marker = dict(size = 8, color = '#FFFFFF')
    ))

    fig.update_layout(
        geo = dict(
            projection_type="equirectangular", 
            showland=True, 
            landcolor="#111111", 
            bgcolor="#000000", 
            coastlinecolor="#333333",
            showocean=True,
            oceancolor="#000000"
        ),
        margin={"r":0,"t":0,"l":0,"b":0}, 
        paper_bgcolor="#000000",
    )
    return fig

def get_sales_chart():
    """Dummy finansal veri oluşturur."""
    df = pd.DataFrame({'Date': pd.date_range('2025-01-01', periods=30), 'Revenue': np.random.normal(30000, 5000, 30)})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Revenue'], fill='tozeroy', line=dict(color='#D4AF37')))
    fig.update_layout(
        template='plotly_dark', 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Share Tech Mono", color="#888"),
        margin=dict(t=0, b=0, l=0, r=0), 
        height=300
    )
    return fig

def get_artis_response(query):
    # Bu fonksiyon "ARTIS AI" genel sohbet sekmesi içindir.
    return "ARTIS CORE: Paket seçimi yapıldıktan sonra detaylı analiz raporu ve strateji sunulacaktır. Lütfen önce 'Command Center' üzerinden kurulumu tamamlayın."

# --- ONBOARDING & SATIŞ MANTIĞI ---

class OnboardingBrain:
    def __init__(self):
        # Sohbet Adımları
        self.steps = [
            "intro",           # İsim Alma
            "get_sector",      # Sektör Öğrenme (Genel)
            "get_products",    # Ürün Detayı (Özel)
            "get_details",     # Gizli Veri (Maliyet/Boyut/Depo)
            "present_offer",   # Paket Sunumu
            "finalize"         # Kapanış
        ]

    def process_message(self, user_input, current_step, checklist_state):
        """
        Kullanıcı mesajını işler, bir sonraki adımı belirler ve cevabı döndürür.
        """
        response_text = ""
        next_step = current_step
        user_input = user_input.lower()
        
        # 1. ADIM: TANIŞMA -> SEKTÖR
        if current_step == "intro":
            # Kullanıcı ismini/markasını girdi varsayıyoruz
            response_text = "Merhaba. Ben ARTIS, Washington DC operasyonunuzu yönetecek yapay zekayım. Sizi dünyaya açmadan önce biraz tanıyalım. Markanızın adı nedir?"
            next_step = "get_sector"

        # 2. ADIM: SEKTÖR (GENEL)
        elif current_step == "get_sector":
            checklist_state['brand'] = True # Marka bilgisi tik atıldı
            response_text = "Memnun oldum. Sisteme kaydettim. Peki genel olarak hangi sektörde faaliyet gösteriyorsunuz? (Tekstil, Gıda, Kozmetik, Ev Dekorasyon vb.)"
            next_step = "get_products"

        # 3. ADIM: ÜRÜNLER (ÖZEL)
        elif current_step == "get_products":
            response_text = "Harika bir sektör. Peki bu sektörde spesifik olarak ne üretiyorsunuz? Elinizde satışa hazır 'Yıldız Ürün' dediğiniz bir parça var mı?"
            next_step = "get_details"

        # 4. ADIM: DETAYLAR (GİZLİ VERİ TOPLAMA)
        elif current_step == "get_details":
            checklist_state['product'] = True # Ürün bilgisi tik atıldı
            response_text = "Çok ilgi çekici. Bu ürünlerin Amerika pazarında potansiyeli yüksek.\n\nWashington DC'de, Beyaz Saray'a sadece 15 dk mesafedeki fiziksel depomuzda bunlara hemen yer açabilirim. 😉\n\nLojistik partnerimizle maliyet çalışabilmem için; ürünlerin kabaca boyutları veya tahmini üretim maliyetleri hakkında aklınızda bir rakam var mı?"
            next_step = "present_offer"

        # 5. ADIM: PAKET SUNUMU
        elif current_step == "present_offer":
            checklist_state['data'] = True # Kritik veriler alındı
            response_text = """
            Verileri işledim. Sizin için Washington Hub operasyonlu 3 farklı çalışma modeli hazırladım:
            
            1️⃣ **ORTAKLIK MODELİ:** Siz ürünleri yollarsınız, kargo masrafını ödersiniz. Biz mağazalarımızda satarız, kârdan pay alırız.
            
            2️⃣ **KURUMSAL KURULUM ($2000):** Size ait LLC şirket ve Pazaryeri mağazalarını kurarız. Ürünleri kendi markanızla satarsınız. Biz yönetiriz ($250/ay).
            
            3️⃣ **TAM OTOMASYON ($2000 + $500/ay):** Şirket, Mağaza, Reklam, Sosyal Medya ve Vergi süreçlerinin tamamını biz yönetiriz.
            
            *(Not: Bütçeniz kısıtlıysa $500'a basit bir web sitesi ile de başlayabiliriz.)*
            
            Hangi model size daha yakın geliyor?
            """
            next_step = "finalize"

        # 6. ADIM: FİNAL
        elif current_step == "finalize":
            if "1" in user_input or "ortak" in user_input:
                selected = "ORTAKLIK MODELİ"
            elif "2" in user_input or "kurumsal" in user_input:
                selected = "KURUMSAL MODEL"
            elif "3" in user_input or "tam" in user_input or "full" in user_input:
                selected = "VIP TAM PAKET"
            elif "500" in user_input or "web" in user_input:
                selected = "WEB BAŞLANGIÇ PAKETİ"
            else:
                selected = "ÖZEL TEKLİF"
            
            checklist_state['offer'] = True # Paket seçildi
            response_text = f"**{selected}** harika bir seçim. Anlaşmalı lojistik firmamıza bilgilerinizi iletiyorum. Ürünlerinizi evinizden alıp DC depomuza getirmek için operasyonu başlatıyorum. Aramıza hoş geldiniz."
            next_step = "completed"

        elif current_step == "completed":
            response_text = "Kayıtlar tamamlandı. Sol menüden 'Finans' sekmesine geçerek tahmini gelir simülasyonunu inceleyebilirsiniz."

        return response_text, next_step, checklist_state
