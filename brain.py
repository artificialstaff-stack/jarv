import plotly.graph_objects as go
import random
import time

# [BRAIN-01] ARTIS AI (CHATBOT LOGIC)
def get_artis_response(user_input):
    msg = user_input.lower()
    
    if any(x in msg for x in ['selam', 'merhaba', 'günaydın', 'kimsin']):
        return "Merhaba. Ben **ARTIS** (Artificial Intelligence Staff). Operasyonel süreçlerinizi yöneten dijital zekayım."

    elif any(x in msg for x in ['kargo', 'lojistik', 'nakliye']):
        return "📦 **Lojistik:** Ürünleriniz Express Kargo ile **2-4 iş gününde**, Deniz yolu ile **20-30 günde** ABD depolarımıza ulaşır."

    elif any(x in msg for x in ['şirket', 'llc', 'vergi', 'ein']):
        return "🏛️ **LLC Kurulumu:** Delaware veya Wyoming'de şirketiniz **3-5 iş günü** içinde kurulur. EIN ve Banka hesabı ile ödeme altyapısı açılır."

    elif any(x in msg for x in ['fiyat', 'maliyet']):
        return "💰 **Yatırım:** Fiyatlandırma işlem hacminize göre değişir. Detaylar için 'Hizmetler' sekmesine bakabilirsiniz."

    elif any(x in msg for x in ['satış', 'reklam', 'pazar']):
        return "📈 **Satış Stratejisi:** B2B tarafında yapay zeka ile toptancı buluyor, B2C tarafında doğrudan alıcıyı hedefliyoruz."

    else:
        return "Bu konuda bilgim yok. Operasyon ekibime iletiyorum."

# [BRAIN-02] DASHBOARD METRICS
def get_dashboard_metrics():
    return {
        "revenue": {"label": "Hedef Ciro", "value": "$124,500", "delta": "Potansiyel"},
        "region": {"label": "Aktif Pazar", "value": "US & CA", "delta": "2 Bölge"},
        "visitors": {"label": "Erişim", "value": "330M+", "delta": "ABD Nüfusu"},
        "conversion": {"label": "Hedef Dönüşüm", "value": "2.5%", "delta": "Retail"}
    }

# [BRAIN-03] SALES CHART (Line Chart)
def get_sales_chart():
    days = list(range(1, 21))
    sales = [10, 12, 15, 14, 18, 20, 22, 21, 25, 27, 26, 30, 32, 35, 34, 38, 40, 39, 42, 45]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days, y=sales, fill='tozeroy', mode='lines',
        line=dict(width=2, color='#D4AF37'),
        fillcolor='rgba(212, 175, 55, 0.1)', name='Tahmin'
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=10, b=0), height=300, showlegend=False,
        xaxis=dict(showgrid=False, showline=False, color='#666'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', color='#666')
    )
    return fig

# [BRAIN-04] MAP CHART (Logistics)
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

# [BRAIN-05] MARKETING CHART (Pie Chart)
def get_marketing_chart():
    labels = ['Google Ads', 'Meta', 'Email', 'Influencer']
    values = [40, 35, 15, 10]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6)])
    fig.update_traces(marker=dict(colors=['#D4AF37', '#b69246', '#333333', '#555555']))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"), showlegend=True, height=300,
        margin=dict(t=0, b=0, l=0, r=0)
    )
    return fig
