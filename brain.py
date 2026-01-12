import plotly.graph_objects as go
import pandas as pd
import random

def get_dashboard_metrics():
    """Returns static metrics for the dashboard."""
    return {
        "revenue": {"label": "Toplam Ciro", "value": "$124,500", "delta": "+12%"},
        "region": {"label": "Aktif Bölge", "value": "US & CA", "delta": "2 Bölge"},
        "visitors": {"label": "Ziyaretçi", "value": "14.2K", "delta": "+8%"},
        "conversion": {"label": "Dönüşüm", "value": "3.2%", "delta": "+0.4%"}
    }

def get_sales_chart():
    """Generates a Gold Gradient Area Chart."""
    days = list(range(1, 21))
    # Simulated sales data
    sales = [12, 14, 13, 16, 15, 18, 22, 20, 24, 23, 27, 26, 30, 28, 32, 35, 33, 38, 40, 42]
    
    fig = go.Figure()
    
    # Gradient Area Trace
    fig.add_trace(go.Scatter(
        x=days, 
        y=sales, 
        fill='tozeroy',
        mode='lines',
        line=dict(width=2, color='#D4AF37'), # Gold
        fillcolor='rgba(212, 175, 55, 0.1)', # Translucent Gold
        name='Satış Trendi',
        hovertemplate='<b>Gün %{x}</b><br>Satış: $%{y}k<extra></extra>'
    ))

    # Layout Configuration
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=20, b=0),
        height=350,
        showlegend=False,
        hovermode="x unified",
        xaxis=dict(
            showgrid=False, 
            showline=False,
            color='#666',
            tickfont=dict(family='Inter', size=11)
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor='rgba(255,255,255,0.05)', 
            showline=False,
            color='#666',
            tickprefix="$",
            ticksuffix="k",
            tickfont=dict(family='Inter', size=11)
        )
    )
    return fig

def get_map_chart():
    """Generates a dark-themed world map with gold routes."""
    fig = go.Figure()

    # Route Lines (Istanbul -> NY)
    fig.add_trace(go.Scattergeo(
        lon = [28.97, -74.00], lat = [41.00, 40.71],
        mode = 'lines',
        line = dict(width = 2, color = '#D4AF37'),
        opacity = 0.8,
        name="Express Hattı (USA)"
    ))
    
    # Warehouse Markers
    fig.add_trace(go.Scattergeo(
        lon = [28.97, -74.00, 13.40, -118.24],
        lat = [41.00, 40.71, 52.52, 34.05],
        mode = 'markers',
        marker = dict(size = 8, color = '#D4AF37', line=dict(width=1, color='white')),
        text = ["Istanbul (HQ)", "New York (Hub)", "Berlin", "Los Angeles"],
        name="Depolar"
    ))

    fig.update_layout(
        geo = dict(
            scope = 'world',
            projection_type = 'equirectangular',
            showland = True,
            landcolor = "#111",
            showocean = True,
            oceancolor = "#050505",
            showcountries = True,
            countrycolor = "#333",
            bgcolor = "rgba(0,0,0,0)"
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        height=500
    )
    return fig
