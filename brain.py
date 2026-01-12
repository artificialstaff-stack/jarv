import plotly.graph_objects as go
import random
import time

# --- ARTIS AI (SATIŞ ODAKLI AKILLI ASİSTAN) ---
def get_artis_response(user_input):
    """
    Müşteriyi ikna etmeye ve bilgi vermeye yönelik 'Keyword Matching' beyni.
    """
    msg = user_input.lower()
    
    # 1. Selamlaşma
    if any(x in msg for x in ['selam', 'merhaba', 'günaydın', 'kimsin', 'artıs', 'artis']):
        return "Merhaba. Ben **ARTIS** (Artificial Intelligence Staff). Operasyonel süreçlerinizi yöneten ve satışlarınızı artıran dijital zekayım. Size **Lojistik**, **Şirket Kurulumu**, **Yatırım Maliyetleri** veya **Satış Stratejileri** hakkında bilgi verebilirim."

    # 2. Lojistik & Kargo
    elif any(x in msg for x in ['kargo', 'lojistik', 'nakliye', 'teslimat', 'gönderim', 'gümrük']):
        return "📦 **Lojistik Hattı:** Türkiye'den çıkan ürünleriniz Express Kargo (FedEx/UPS) ile **2-4 iş gününde**, Deniz yolu ile **20-30 günde** ABD depolarımıza (NJ & CA) ulaşır. Gümrükleme tarafımızca yönetilir, siz sadece etiketi basarsınız."

    # 3. Şirket Kurulumu (LLC)
    elif any(x in msg for x in ['şirket', 'llc', 'vergi', 'ein', 'banka', 'stripe', 'paypal']):
        return "🏛️ **LLC & Finans:** Delaware veya Wyoming eyaletlerinde şirketiniz **3-5 iş günü** içinde kurulur. EIN numaranız alındıktan sonra Mercury Bank hesabınız açılır ve **Stripe/PayPal** entegrasyonu ile tahsilat engeliniz tamamen kalkar."

    # 4. Fiyat & Maliyet
    elif any(x in msg for x in ['fiyat', 'kaç para', 'ücret', 'maliyet', 'paket']):
        return "💰 **Yatırım Planı:** Biz bir 'gider kalemi' değil, dolar kazandıran bir yatırım ortağıyız. Fiyatlandırma işlem hacminize ve seçtiğiniz modüllere göre değişir. Detaylı paketleri **'HİZMETLERİMİZ'** sekmesinden inceleyebilirsiniz."

    # 5. Satış & Pazarlama
    elif any(x in msg for x in ['satış', 'reklam', 'müşteri', 'pazar', 'marketing', 'b2b']):
        return "📈 **Satış Stratejisi:** B2B tarafında yapay zeka ile nokta atışı toptancı buluyoruz (Cold Outreach). B2C tarafında ise Meta/Google reklamları ile doğrudan 'satın alma niyeti' yüksek kitleyi hedefliyoruz."

    # Varsayılan Cevap
    else:
        return "Bu spesifik konuda veri tabanımda hazır bir yanıt yok. Ancak operasyon ekibime not ilettim. Şunları sormak ister misiniz: **'Lojistik süresi ne kadar?', 'LLC avantajları neler?', 'Reklam bütçesi ne olmalı?'**"

# --- GRAFİK MOTORU (DASHBOARD İÇİN) ---
def get_dashboard_metrics():
    return {
        "revenue": {"label": "Hedef Ciro", "value": "$124,500", "delta": "Potansiyel"},
        "region": {"label": "Aktif Pazar", "value": "US & CA", "delta": "2 Bölge"},
        "visitors": {"label": "Erişim", "value": "330M+", "delta": "ABD Nüfusu"},
        "conversion": {"label": "Hedef Dönüşüm", "value": "2.5%", "delta": "Retail"}
    }

def get_sales_chart():
    days = list(range(1, 21))
    sales = [12, 14, 13, 16, 15, 18, 22, 20, 24, 23, 27, 26, 30, 28, 32, 35, 33, 38, 40, 42]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days, y=sales, fill='tozeroy', mode='lines',
        line=dict(width=2, color='#D4AF37'),
        fillcolor='rgba(212, 175, 55, 0.1)', name='Projeksiyon'
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=10, b=0), height=300, showlegend=False,
        xaxis=dict(showgrid=False, showline=False, color='#666'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', color='#666')
    )
    return fig

def get_map_chart():
    fig = go.Figure()
    # Rota
    fig.add_trace(go.Scattergeo(
        lon = [28.97, -74.00], lat = [41.00, 40.71], mode = 'lines',
        line = dict(width = 2, color = '#D4AF37'), opacity = 0.8
    ))
    # Noktalar
    fig.add_trace(go.Scattergeo(
        lon = [28.97, -74.00, 13.40, -118.24],
        lat = [41.00, 40.71, 52.52, 34.05], mode = 'markers',
        marker = dict(size=6, color='#D4AF37'),
        text = ["Istanbul", "NY", "Berlin", "LA"]
    ))
    fig.update_layout(
        geo=dict(
            scope='world', projection_type='equirectangular',
            showland=True, landcolor="#111", showocean=True, oceancolor="#050505",
            showcountries=True, countrycolor="#333", bgcolor="rgba(0,0,0,0)"
        ),
        margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="rgba(0,0,0,0)", height=400
    )
    return fig

def get_marketing_chart():
    labels = ['Google Ads', 'Meta (FB/IG)', 'Email', 'Influencer']
    values = [40, 35, 15, 10]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6)])
    fig.update_traces(marker=dict(colors=['#D4AF37', '#b69246', '#333333', '#555555']))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"), showlegend=True, height=300,
        margin=dict(t=0, b=0, l=0, r=0)
    )
    return fig
