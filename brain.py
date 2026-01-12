import pandas as pd
import numpy as np
import plotly.graph_objects as go

def get_dashboard_metrics():
    """Dashboard üst kısım verilerini döndürür"""
    return {
        "revenue": {"label": "Toplam Ciro", "value": "$124,500", "delta": "+12%"},
        "region": {"label": "Aktif Bölge", "value": "US & CA", "delta": "2 Bölge"},
        "visitors": {"label": "Ziyaretçi", "value": "14.2K", "delta": "+8%"},
        "conversion": {"label": "Dönüşüm", "value": "3.2%", "delta": "+0.4%"}
    }

def get_sales_chart():
    """Modern Altın Gradient Area Chart oluşturur"""
    # Örnek Veri
    days = list(range(1, 21))
    sales = [12, 14, 13, 16, 15, 18, 22, 20, 24, 23, 27, 26, 30, 28, 32, 35, 33, 38, 40, 42]
    
    fig = go.Figure()
    
    # Gradient Area Chart
    fig.add_trace(go.Scatter(
        x=days, 
        y=sales, 
        fill='tozeroy',
        mode='lines',
        line=dict(width=2, color='#D4AF37'), # Gold Line
        fillcolor='rgba(212, 175, 55, 0.1)', # Transparent Gold Fill
        name='Satış Trendi',
        hovertemplate='<b>Gün %{x}</b><br>Satış: $%{y}k<extra></extra>'
    ))

    # Layout Ayarları (Dark Mode & Minimalist)
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=10, b=0),
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

def get_notifications():
    """Bildirim listesi HTML'ini döndürür"""
    return """
        <div class="notification-box">
            <div class="notif-header">
                <i class="fa-regular fa-bell"></i> Canlı Bildirimler
            </div>
            
            <div class="notif-item">
                <div class="status-dot" style="background-color: #3b82f6;"></div>
                <div class="notif-content">
                    <h4>NJ Deposuna ürün girişi</h4>
                    <p>SKU-204 New Jersey deposuna ulaştı. • 2 dk önce</p>
                </div>
            </div>
            
            <div class="notif-item">
                <div class="status-dot" style="background-color: #22c55e;"></div>
                <div class="notif-content">
                    <h4>Stripe ödemesi alındı</h4>
                    <p>$249.00 başarıyla tahsil edildi. • 15 dk önce</p>
                </div>
            </div>
            
            <div class="notif-item">
                <div class="status-dot" style="background-color: #eab308;"></div>
                <div class="notif-content">
                    <h4>Stok Uyarısı</h4>
                    <p>Leather Wallet stoğu kritik seviyede (%5). • 1 saat önce</p>
                </div>
            </div>

            <div class="notif-item">
                <div class="status-dot" style="background-color: #a855f7;"></div>
                <div class="notif-content">
                    <h4>AI Satış Ajanı</h4>
                    <p>50 yeni potansiyel müşteriye mail atıldı. • 2 saat önce</p>
                </div>
            </div>
        </div>
    """
