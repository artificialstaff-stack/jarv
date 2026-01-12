import plotly.graph_objects as go
import random
import time

# --- ARTIS AI BEYNİ ---
def get_artis_response(user_input):
    """Müşteri sorularına satış odaklı cevaplar veren Artis AI."""
    msg = user_input.lower()
    
    if any(x in msg for x in ['selam', 'merhaba', 'günaydın', 'kimsin']):
        return "Merhaba. Ben **ARTIS** (Artificial Intelligence Staff). Operasyonel süreçlerinizi yöneten ve satışlarınızı artıran dijital zekayım. Size **Lojistik**, **Şirket Kurulumu** veya **Maliyetler** hakkında bilgi verebilirim."

    elif any(x in msg for x in ['kargo', 'lojistik', 'nakliye', 'gönderim']):
        return "📦 **Lojistik Hattı:** Türkiye'den çıkan ürünleriniz Express Kargo (FedEx/UPS) ile **2-4 iş gününde**, Deniz yolu ile **20-30 günde** ABD depolarımıza (NJ & CA) ulaşır. Gümrükleme tarafımızca yapılır."

    elif any(x in msg for x in ['şirket', 'llc', 'vergi', 'ein', 'banka']):
        return "🏛️ **LLC & Bankacılık:** Delaware veya Wyoming'de şirketiniz **3-5 iş günü** içinde kurulur. EIN numaranız alındıktan sonra Mercury Bank hesabınız açılır ve **Stripe/PayPal** ile ödeme almaya başlarsınız."

    elif any(x in msg for x in ['fiyat', 'kaç para', 'ücret', 'maliyet']):
        return "💰 **Yatırım:** Biz bir gider kalemi değil, dolar kazandıran bir yatırım ortağıyız. Fiyatlandırma işlem hacminize göre değişir. Detaylı paketlerimizi 'Hizmetlerimiz' sekmesinden inceleyebilirsiniz."

    elif any(x in msg for x in ['satış', 'reklam', 'marketing', 'pazar']):
        return "📈 **Satış Stratejisi:** B2B tarafında yapay zeka ile nokta atışı toptancı buluyoruz. B2C tarafında ise Meta ve Google reklamları ile doğrudan 'satın alma niyeti' olan ABD'li müşteriyi hedefliyoruz."

    else:
        return "Bu konuda veri tabanımda hazır bir yanıt yok, ancak operasyon ekibime not ilettim. Şunları sormak ister misiniz: **'Kargo süresi nedir?', 'LLC nasıl kurulur?'**"

# --- GRAFİK FONKSİYONLARI ---
def get_dashboard_metrics():
    return {
        "revenue": {"label": "Hedef Ciro", "value": "$124,500", "delta": "Potansiyel"},
        "region": {"label": "Pazar", "value": "US & CA", "delta": "Aktif"},
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
    fig.add_trace(go.Scattergeo(
        lon = [28.97, -74.00], lat = [41.00, 40.71], mode = 'lines',
        line = dict(width = 2, color = '#D4AF37'), opacity = 0.8
    ))
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
