import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time

def get_artis_response(query):
    """
    Simulates the AI Operating System logic.
    """
    query = query.lower()
    time.sleep(1) # Simulate processing time
    
    if "tax" in query or "llc" in query:
        return "ARTIS FINANCE KERNEL: For Delaware LLCs exporting to Turkey, you are exempt from US Federal Income Tax if you have no dependent agents in the US. However, you must file Form 5472 and pro-forma 1120 annually. Would you like me to generate a compliance calendar?"
    elif "ship" in query or "logistics" in query:
        return "ARTIS LOGISTICS KERNEL: Current sea freight transit from Ambarli (Istanbul) to Port of NY/NJ is averaging 24 days. Air freight via Turkish Airlines Cargo is 48 hours. I detect a potential 12% saving by consolidating LCL shipments in Week 4."
    elif "ad" in query or "marketing" in query:
        return "ARTIS MARKETING KERNEL: Meta Ads CPM for 'Made in Turkey' home textiles in California is currently $18.50. I recommend shifting 30% of the budget to TikTok Shop ads where ROAS is trending at 4.2x."
    else:
        return "ARTIS CORE: Input received. I am analyzing your business vector relative to US Market entry protocols. Please specify: Logistics, Finance, or Marketing operations."

# --- YENİ ONBOARDING MANTIĞI ---

class OnboardingBrain:
    def __init__(self):
        # Sohbet Adımları
        self.steps = [
            "intro",
            "get_name",
            "get_llc",
            "get_logistics",
            "get_marketing",
            "complete"
        ]

    def process_message(self, user_input, current_step, checklist_state):
        """
        Kullanıcı mesajını alır, bir sonraki soruyu ve güncellenmiş checklist durumunu döndürür.
        """
        response_text = ""
        next_step = current_step
        
        user_input = user_input.lower()
        
        # ADIM 0: GİRİŞ -> İSİM SORMA
        if current_step == "intro":
            response_text = "Ben ARTIS. Operasyon yöneticinizim. ABD operasyonunuzu başlatmak için sistem taraması yapacağım. Öncelikle, markanızın veya şirketinizin adı nedir?"
            next_step = "get_name"

        # ADIM 1: İSİM ALINDI -> LLC SORMA
        elif current_step == "get_name":
            checklist_state['profile'] = True # İsim verildi, tik atıldı
            response_text = f"Memnun oldum. Sisteme kaydettim. Şimdi yasal zemini kontrol edelim. ABD'de kurulu bir şirketiniz (LLC/Corp) ve EIN numaranız var mı? (Var/Yok)"
            next_step = "get_llc"

        # ADIM 2: LLC DURUMU -> LOJİSTİK SORMA
        elif current_step == "get_llc":
            if "var" in user_input or "evet" in user_input or "yes" in user_input:
                checklist_state['legal'] = True # Hazır
                response_text = "Mükemmel. Yasal altyapı hazır görünüyor. Peki ürünlerinizi şu an nasıl gönderiyorsunuz? (Amazon FBA, Depo, veya Türkiye'den tek tek?)"
            else:
                checklist_state['legal'] = False # Hazır Değil
                response_text = "Anlaşıldı. Yasal kurulum protokolünü listeye ekledim (Eksik). Biz hallederiz. Peki lojistik durumunuz nedir? Ürünler nasıl gidiyor?"
            next_step = "get_logistics"

        # ADIM 3: LOJİSTİK -> PAZARLAMA SORMA
        elif current_step == "get_logistics":
            if "fba" in user_input or "depo" in user_input or "3pl" in user_input:
                checklist_state['logistics'] = True
                response_text = "Harika, toplu gönderim yapıyorsunuz. Bu maliyetleri düşürür. Son olarak: ABD pazarı için aylık reklam bütçesi ayırdınız mı?"
            else:
                checklist_state['logistics'] = False
                response_text = "Tek tek gönderim kârlılığı düşürür. Bunu optimize etmemiz gerekecek (Not alındı). Son soru: Reklam/Pazarlama bütçeniz hazır mı?"
            next_step = "get_marketing"

        # ADIM 4: PAZARLAMA -> BİTİŞ
        elif current_step == "get_marketing":
            if "evet" in user_input or "var" in user_input or "hazır" in user_input:
                checklist_state['marketing'] = True
                response_text = "Bütçe onayı alındı. Sistem analizini tamamladım. Sol taraftaki panelden durumunuzu kontrol edebilirsiniz. Operasyonu başlatmak için hazırım."
            else:
                checklist_state['marketing'] = False
                response_text = "Bütçesiz ilerlemek zor. Bunu da yapılacaklar listesine ekledim. Analiz tamamlandı."
            next_step = "complete"

        elif current_step == "complete":
            response_text = "Analiz tamamlandı. Lütfen sol menüden eksik modülleri inceleyin veya 'ARTIS AI' sekmesine geçerek detaylı soru sorun."

        return response_text, next_step, checklist_state
        
def get_financial_data():
    """Generates dummy financial data for the dashboard."""
    dates = pd.date_range(start='2025-01-01', periods=30)
    revenue = np.linspace(10000, 50000, 30) + np.random.normal(0, 2000, 30)
    profit = revenue * 0.45
    return pd.DataFrame({'Date': dates, 'Revenue': revenue, 'Profit': profit})

def get_logistics_map():
    """Creates a Cinematic Dark Mode route map."""
    fig = go.Figure()

    # Route: Istanbul to NY
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -74.0060],
        lat = [41.0082, 40.7128],
        mode = 'lines',
        line = dict(width = 2, color = '#D4AF37'), # Gold Line
        opacity = 0.8
    ))
    
    # Points
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -74.0060, -118.2437],
        lat = [41.0082, 40.7128, 34.0522],
        hoverinfo = 'text',
        text = ['Istanbul HQ', 'New York Hub', 'LA Distribution'],
        mode = 'markers',
        marker = dict(size = 8, color = '#FFFFFF')
    ))

    fig.update_layout(
        geo = dict(
            projection_type="equirectangular",
            showland = True,
            landcolor = "#111111",
            showocean = True,
            oceancolor = "#000000",
            showlakes = False,
            bgcolor= "#000000",
            coastlinecolor = "#333333"
        ),
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor="#000000",
    )
    return fig

def get_sales_chart():
    """Creates a Gold Gradient Area Chart."""
    df = get_financial_data()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Date'], y=df['Revenue'],
        fill='tozeroy',
        mode='lines',
        line=dict(color='#D4AF37', width=2),
        name='Revenue'
    ))
    
    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Share Tech Mono", color="#888"),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#222'),
        margin=dict(l=0, r=0, t=20, b=0),
        height=300
    )
    return fig
    
# --- YENİ EKLENEN FONKSİYON: ŞİRKET ANALİZİ ---
def analyze_client_business(data):
    """
    Müşteri formundan gelen verileri işler ve yapılması gerekenleri listeler.
    """
    audit_report = []
    score = 100
    
    # 1. Şirket Yapısı Kontrolü
    if data['us_entity'] == "Yok (Sadece TR Şirketi)":
        audit_report.append({
            "criticality": "HIGH",
            "module": "LEGAL",
            "action": "ABD LLC KURULUMU GEREKLİ",
            "detail": "Amerikan bankacılık sistemine ve Stripe/PayPal altyapısına erişim için Wyoming veya Delaware LLC kurulumu başlatılmalı."
        })
        score -= 40
    elif data['ein_status'] == "Yok":
        audit_report.append({
            "criticality": "HIGH",
            "module": "LEGAL",
            "action": "EIN (VERGİ NO) BAŞVURUSU",
            "detail": "Şirketiniz var ancak IRS veritabanında aktif değilsiniz. Gümrük işlemleri için EIN şart."
        })
        score -= 20

    # 2. Lojistik Kontrolü
    if data['fulfillment'] == "Kendi Depomdan (Türkiye)":
        audit_report.append({
            "criticality": "MEDIUM",
            "module": "LOGISTICS",
            "action": "3PL / FBA GEÇİŞİ ÖNERİLİYOR",
            "detail": "Tek tek kargo gönderimi kârlılığı %60 düşürüyor. Ürünleri toplu olarak ABD deposuna çekmeliyiz."
        })
        score -= 15

    # 3. Pazarlama Kontrolü
    if data['marketing_budget'] < 1000:
        audit_report.append({
            "criticality": "LOW",
            "module": "ADS",
            "action": "BÜTÇE REVİZYONU",
            "detail": "ABD pazarında test verisi toplamak için minimum $1500/ay başlangıç bütçesi önerilir."
        })
        score -= 10
        
    return score, audit_report
