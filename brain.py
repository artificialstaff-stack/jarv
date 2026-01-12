import plotly.graph_objects as go
import random
import time

# --- ARTIS AI (AKILLI ASİSTAN) ---
def get_artis_response(user_input):
    """Müşteriyi ikna eden ve bilgi veren yapay zeka cevapları."""
    msg = user_input.lower()
    
    if any(x in msg for x in ['selam', 'merhaba', 'günaydın', 'kimsin']):
        return "Merhaba. Ben **ARTIS**. Artificial Staff operasyonlarını yöneten dijital zekayım. Size **Lojistik**, **Şirket Kurulumu** veya **Maliyetler** hakkında bilgi verebilirim."

    elif any(x in msg for x in ['kargo', 'lojistik', 'nakliye', 'teslimat']):
        return "📦 **Lojistik:** Ürünleriniz Express Kargo (FedEx/UPS) ile **2-4 iş gününde**, Deniz yolu ile **20-30 günde** ABD depolarımıza ulaşır. Gümrük işlemleri tarafımızca yapılır."

    elif any(x in msg for x in ['şirket', 'llc', 'vergi', 'ein', 'banka']):
        return "🏛️ **LLC Kurulumu:** Delaware veya Wyoming eyaletlerinde şirketiniz **3-5 iş günü** içinde kurulur. EIN (Vergi) numarası ve Mercury Bank hesabı açılarak Stripe/PayPal engeli kaldırılır."

    elif any(x in msg for x in ['fiyat', 'kaç para', 'ücret', 'maliyet']):
        return "💰 **Yatırım:** Biz bir gider kalemi değil, dolar kazandıran bir yatırım ortağıyız. Fiyatlandırma hacminize göre değişir. Detaylar için 'HİZMETLERİMİZ' sekmesine bakabilirsiniz."

    elif any(x in msg for x in ['satış', 'reklam', 'marketing', 'pazar']):
        return "📈 **Satış:** B2B için yapay zeka ile toptancı buluyoruz. B2C için Meta/Google reklamları ile doğrudan alıcı kitleyi hedefliyoruz."

    else:
        return "Bu konuda veri tabanımda hazır bir yanıt yok. Operasyon ekibime iletiyorum. Şunları sormak ister misiniz: **'Lojistik süresi nedir?', 'LLC avantajları neler?'**"

# --- GRAFİK MOTORU ---
def get_dashboard_metrics():
    return {
        "revenue": {"label": "Hedef Ciro", "value": "$124,500", "delta": "Potansiyel"},
        "region": {"label": "Pazar", "value": "US & CA", "delta": "Aktif"},
        "visitors": {"label": "Erişim", "value": "330M+", "delta": "ABD Nüfusu"},
        "conversion": {"label": "Hedef Dönüşüm", "value": "2.5%", "delta": "Retail"}
    }

def get_sales_chart():
    # Basit ve hatasız grafik
    days = list(range(1, 21))
    sales = [10, 12, 11, 14, 13, 16, 18, 20, 19, 22, 24, 23, 26, 28, 30, 29, 32, 35, 34, 38]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days, y=sales, fill='tozeroy', mode='lines',
        line=dict(width=2, color='#D4AF37'),
        fillcolor='rgba(212, 175, 55, 0.1)', name='Tahmin'
    ))
    # Layout parantezi düzeltildi
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=20, b=0),
        height=300,
        showlegend=False,
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
