import plotly.graph_objects as go
import time

# [BRAIN-01] ARTIS AI CEVAPLARI
def get_artis_response(user_input):
    msg = user_input.lower()
    
    if any(x in msg for x in ['selam', 'merhaba', 'günaydın']):
        return "Merhaba. Ben ARTIS. Global operasyonlarınız için size nasıl yardımcı olabilirim?"
    elif any(x in msg for x in ['kargo', 'lojistik', 'süre']):
        return "📦 **Lojistik:** Express kargo ile 2-4 gün, deniz yoluyla 20-30 günde ABD depolarımıza teslimat sağlıyoruz."
    elif any(x in msg for x in ['fiyat', 'maliyet', 'ücret']):
        return "💰 **Maliyet:** Hizmet paketlerimiz işlem hacminize göre değişir. Detaylı bilgi için 'Hizmetler' sekmesine bakabilirsiniz."
    elif any(x in msg for x in ['şirket', 'llc']):
        return "🏛️ **LLC:** Delaware/Wyoming şirket kurulumu ve EIN numarası temini 3-5 iş günü sürmektedir."
    else:
        return "Bu konuda henüz yeterli veriye sahip değilim. Operasyon ekibine bildirim gönderdim."

# [BRAIN-02] DASHBOARD VERİLERİ
def get_dashboard_metrics():
    return {
        "revenue": {"label": "Ciro (Aylık)", "value": "$124,500", "delta": "+12%"},
        "region": {"label": "Bölge", "value": "US & CA", "delta": "Aktif"},
        "visitors": {"label": "Trafik", "value": "14.2K", "delta": "+8%"},
        "conversion": {"label": "Dönüşüm", "value": "3.2%", "delta": "+0.4%"}
    }

# [BRAIN-03] SATIŞ GRAFİĞİ
def get_sales_chart():
    days = list(range(1, 21))
    sales = [10, 12, 15, 14, 18, 20, 22, 21, 25, 27, 26, 30, 32, 35, 34, 38, 40, 39, 42, 45]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days, y=sales, fill='tozeroy', mode='lines',
        line=dict(width=3, color='#D4AF37'), # Altın
        fillcolor='rgba(212, 175, 55, 0.1)',
        name='Satış'
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0), height=300, showlegend=False,
        xaxis=dict(showgrid=False, showline=False, color='#666'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', color='#666')
    )
    return fig
