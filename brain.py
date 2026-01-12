import plotly.graph_objects as go

def get_dashboard_metrics():
    return {
        "revenue": {"label": "Toplam Ciro", "value": "$124,500", "delta": "+12%"},
        "region": {"label": "Aktif Bölge", "value": "US & CA", "delta": "2 Bölge"},
        "visitors": {"label": "Ziyaretçi", "value": "14.2K", "delta": "+8%"},
        "conversion": {"label": "Dönüşüm", "value": "3.2%", "delta": "+0.4%"}
    }

def get_sales_chart():
    days = list(range(1, 21))
    sales = [12, 14, 13, 16, 15, 18, 22, 20, 24, 23, 27, 26, 30, 28, 32, 35, 33, 38, 40, 42]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days, y=sales, fill='tozeroy', mode='lines',
        line=dict(width=2, color='#D4AF37'),
        fillcolor='rgba(212, 175, 55, 0.1)',
        name='Satış Trendi'
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=10, b=0),
        height=350,
        showlegend=False,
        xaxis=dict(showgrid=False, showline=False, color='#666'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', color='#666')
    )
    return fig
