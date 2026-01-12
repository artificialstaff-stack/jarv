import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time

def get_artis_response(query):
    """
    Simulates the AI Operating System logic.
    """
    query = query.lower()
    time.sleep(1) # Simulate processing time
    
    if "tax" in query or "llc" in query:
        return "ARTIS FINANCE KERNEL: For Delaware LLCs exporting to Turkey, you are exempt from US Federal Income Tax if you have no dependent agents in the US. However, you must file Form 5472 and pro-forma 1120 annually. Would you like me to generate a compliance calendar?"
    elif "ship" in query or "logistics" in query:
        return "ARTIS LOGISTICS KERNEL: Current sea freight transit from Ambarli (Istanbul) to Port of NY/NJ is averaging 24 days. Air freight via Turkish Airlines Cargo is 48 hours. I detect a potential 12% saving by consolidating LCL shipments in Week 4."
    elif "ad" in query or "marketing" in query:
        return "ARTIS MARKETING KERNEL: Meta Ads CPM for 'Made in Turkey' home textiles in California is currently $18.50. I recommend shifting 30% of the budget to TikTok Shop ads where ROAS is trending at 4.2x."
    else:
        return "ARTIS CORE: Input received. I am analyzing your business vector relative to US Market entry protocols. Please specify: Logistics, Finance, or Marketing operations."

def get_financial_data():
    """Generates dummy financial data for the dashboard."""
    dates = pd.date_range(start='2025-01-01', periods=30)
    revenue = np.linspace(10000, 50000, 30) + np.random.normal(0, 2000, 30)
    profit = revenue * 0.45
    return pd.DataFrame({'Date': dates, 'Revenue': revenue, 'Profit': profit})

def get_logistics_map():
    """Creates a Cinematic Dark Mode route map."""
    fig = go.Figure()

    # Route: Istanbul to NY
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -74.0060],
        lat = [41.0082, 40.7128],
        mode = 'lines',
        line = dict(width = 2, color = '#D4AF37'), # Gold Line
        opacity = 0.8
    ))
    
    # Points
    fig.add_trace(go.Scattergeo(
        lon = [28.9784, -74.0060, -118.2437],
        lat = [41.0082, 40.7128, 34.0522],
        hoverinfo = 'text',
        text = ['Istanbul HQ', 'New York Hub', 'LA Distribution'],
        mode = 'markers',
        marker = dict(size = 8, color = '#FFFFFF')
    ))

    fig.update_layout(
        geo = dict(
            projection_type="equirectangular",
            showland = True,
            landcolor = "#111111",
            showocean = True,
            oceancolor = "#000000",
            showlakes = False,
            bgcolor= "#000000",
            coastlinecolor = "#333333"
        ),
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor="#000000",
    )
    return fig

def get_sales_chart():
    """Creates a Gold Gradient Area Chart."""
    df = get_financial_data()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Date'], y=df['Revenue'],
        fill='tozeroy',
        mode='lines',
        line=dict(color='#D4AF37', width=2),
        name='Revenue'
    ))
    
    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Share Tech Mono", color="#888"),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#222'),
        margin=dict(l=0, r=0, t=20, b=0),
        height=300
    )
    return fig
