import plotly.graph_objects as go
import pandas as pd
import random

def get_artis_response(user_input):
    """
    ARTIS'in (Artificial Intelligence Staff) kural tabanlı beyni.
    Müşteriyi ikna etmeye ve bilgi vermeye yönelik cevaplar üretir.
    """
    msg = user_input.lower()
    
    # 1. Selamlaşma ve Tanışma
    if any(x in msg for x in ['selam', 'merhaba', 'günaydın', 'kimsin', 'nedir']):
        return "Merhaba. Ben **ARTIS** (Artificial Intelligence Staff). Operasyonel süreçlerinizi yöneten dijital zekayım. Size **Lojistik**, **LLC Kurulumu**, **Satış Stratejileri** veya **Maliyetler** hakkında bilgi verebilirim."

    # 2. Lojistik ve Kargo Süreleri
    elif any(x in msg for x in ['kargo', 'lojistik', 'nakliye', 'teslimat', 'gönderim', 'depo']):
        return "📦 **Lojistik Altyapısı:** Türkiye'den çıkan ürünleriniz Express Kargo (FedEx/UPS) ile **2-4 iş gününde**, Deniz yolu ile **20-30 günde** ABD depolarımıza (NJ & CA) ulaşır. Şu an gümrükleme süreçleri %100 sorunsuz işlemektedir."

    # 3. Şirket Kurulumu (LLC)
    elif any(x in msg for x in ['şirket', 'llc', 'vergi', 'ein', 'banka', 'stripe', 'paypal']):
        return "🏛️ **LLC ve Bankacılık:** Delaware veya Wyoming eyaletlerinde şirketiniz **3-5 iş günü** içinde kurulur. Ardından EIN numaranız alınır, Mercury Bank hesabınız açılır ve Türkiye'deki en büyük engel olan **Stripe/PayPal** tahsilat altyapısı aktif hale getirilir."

    # 4. Fiyatlandırma ve Maliyet
    elif any(x in msg for x in ['fiyat', 'kaç para', 'ücret', 'maliyet', 'komisyon']):
        return "💰 **Yatırım Planlaması:** Fiyatlarımız işletmenizin hacmine ve ihtiyaç duyduğu modüllere göre değişir. Biz bir 'gider kalemi' değil, dolar kazandıran bir **yatırım** ortağıyız. Detaylı teklif için 'HİZMETLERİMİZ' sekmesindeki paketleri inceleyebilir veya satış ekibimizle görüşebilirsiniz."

    # 5. Satış ve Pazarlama
    elif any(x in msg for x in ['satış', 'reklam', 'müşteri', 'pazar', 'marketing', 'b2b']):
        return "📈 **Satış Stratejisi:** Yapay zeka destekli B2B müşteri bulma (Cold Outreach) ve Meta/Google reklamları ile doğrudan 'satın alma niyeti' yüksek kitleyi hedefleriz. Hedefimiz minimum **3x ROAS** (Reklam Getirisi) sağlamaktır."

    # 6. Web ve Teknoloji
    elif any(x in msg for x in ['web', 'site', 'tasarım', 'altyapı', 'shopify']):
        return "💻 **Global Vitrin:** ABD tüketici algısına uygun, Google Core Web Vitals uyumlu ve yüksek dönüşüm odaklı e-ticaret siteleri kuruyoruz. Siteniz sadece bir kartvizit değil, 7/24 çalışan bir satış makinesidir."

    # Varsayılan Cevap
    else:
        return "Bu spesifik konu hakkında veri tabanımda şu an hazır bir yanıt yok. Ancak operasyon ekibime notunuzu ilettim. Şunlardan birini sormak ister misiniz: **'Kargo süreleri nedir?', 'LLC nasıl kurulur?', 'Reklam stratejiniz ne?'**"

def get_dashboard_metrics():
    """Dashboard için örnek/hedef veriler."""
    return {
        "revenue": {"label": "Hedeflenen Ciro", "value": "$124,500", "delta": "Potansiyel"},
        "region": {"label": "Hedef Pazar", "value": "US & CA", "delta": "Aktif"},
        "visitors": {"label": "Erişilebilir Kitle", "value": "330M+", "delta": "ABD Nüfusu"},
        "conversion": {"label": "Sektör Ortalaması", "value": "2.5%", "delta": "Retail"}
    }

def get_sales_chart():
    """Satış trendi grafiği (Gold Gradient)."""
    days = list(range(1, 21))
    sales = [12, 14, 13, 16, 15, 18, 22, 20, 24, 23, 27, 26, 30, 28, 32, 35, 33, 38, 40, 42]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days, 
        y=sales, 
        fill='tozeroy',
        mode='lines',
        line=dict(width=2, color='#D4AF37'),
        fillcolor='rgba(212, 175, 55, 0.1)',
        name='Projeksiyon',
        hovertemplate='<b>Gün %{x}</b><br>Tahmin: $%{y}k<extra></extra>'
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=20, b=0),
        height=350,
        showlegend=False,
        hovermode="x unified",
        xaxis=dict(showgrid=False, showline=False, color='#666'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', showline=False, color='#666')
    )
    return fig

def get_map_chart():
    """Lojistik haritası."""
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon = [28.97, -74.00], lat = [41.00, 40.71],
        mode = 'lines',
        line = dict(width = 2, color = '#D4AF37'),
        opacity = 0.8,
        name="Lojistik Hattı"
    ))
    fig.add_trace(go.Scattergeo(
        lon = [28.97, -74.00, 13.40, -118.24],
        lat = [41.00, 40.71, 52.52, 34.05],
        mode = 'markers',
        marker = dict(size = 8, color = '#D4AF37', line=dict(width=1, color='white')),
        text = ["Istanbul", "New York", "Berlin", "Los Angeles"],
        name="Hublar"
    ))
    fig.update_layout(
        geo = dict(
            scope = 'world',
            projection_type = 'equirectangular',
            showland = True, landcolor = "#111",
            showocean = True, oceancolor = "#050505",
            showcountries = True, countrycolor = "#333",
            bgcolor = "rgba(0,0,0,0)"
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        height=500
    )
    return fig
