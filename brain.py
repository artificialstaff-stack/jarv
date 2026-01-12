import plotly.graph_objects as go
import time

# [BRAIN-01] ARTIS AI (Perplexity Mantığı)
def get_artis_response(user_input):
    msg = user_input.lower()
    
    if any(x in msg for x in ['selam', 'merhaba']):
        return "ARTIS Core Online. Komuta merkezine hoş geldiniz. Operasyonel veriler hazır."
    elif any(x in msg for x in ['kargo', 'lojistik', 'süre']):
        return "📦 **Lojistik Durumu:** Express hatlar açık. NY ve CA depolarına ortalama varış süresi 3.2 gün."
    elif any(x in msg for x in ['ciro', 'finans', 'para']):
        return "💰 **Finansal Özet:** Bu ayki ciro hedefinin %12 üzerindeyiz. Nakit akışı pozitif."
    elif any(x in msg for x in ['strateji', 'reklam']):
        return "📈 **Strateji:** Meta reklamlarında ROAS 3.1x seviyesinde. Google Ads bütçe artırımı öneriliyor."
    else:
        return "Veri işleniyor... Bu sorgu için veritabanında yeterli kayıt bulunamadı. Lütfen 'Lojistik' veya 'Finans' gibi anahtar kelimeler kullanın."

# [BRAIN-02] CHART GENERATORS
def get_sales_chart():
    # Basit ve hatasız Line Chart
    days = list(range(1, 15))
    sales = [10, 12, 15, 14, 18, 22, 20, 25, 28, 30, 35, 34, 40, 42]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days, y=sales, fill='tozeroy', mode='lines',
        line=dict(width=2, color='#D4AF37'),
        fillcolor='rgba(212, 175, 55, 0.1)'
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0), height=250, showlegend=False,
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
    fig.update_layout(
        geo=dict(
            scope='world', projection_type='equirectangular',
            showland=True, landcolor="#111", showocean=True, oceancolor="#050505",
            bgcolor="rgba(0,0,0,0)"
        ),
        margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="rgba(0,0,0,0)", height=300
    )
    return fig
