import streamlit as st
import plotly.graph_objects as go
from brain import get_dashboard_metrics, get_sales_chart, get_map_chart

# --- COMMON HEADER ---
def render_header(title, subtitle):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"""
        <div>
            <span style='font-size: 12px; color: #666; font-family: Inter;'>Ana Sayfa / {title}</span>
            <h2 style='margin-top: -5px; color: white;'>{title}</h2>
            <p style='margin-top: -10px; font-size: 14px; color: #888;'>{subtitle}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='text-align: right; padding-top: 10px;'>
            <span style='color: #D4AF37; font-size: 12px; font-weight:bold;'>● ONLINE</span><br>
            <span style='color: #FFF; font-family: Inter; font-size: 14px;'>Admin User</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin-bottom: 30px;'>", unsafe_allow_html=True)

# --- 1. DASHBOARD PAGE ---
def render_dashboard():
    render_header("Global Operasyon Merkezi", "Anlık Veri Akışı ve Pazar Analizi")
    
    # Metrics Bento Grid
    metrics = get_dashboard_metrics()
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric(metrics["revenue"]["label"], metrics["revenue"]["value"], metrics["revenue"]["delta"])
    with c2: st.metric(metrics["region"]["label"], metrics["region"]["value"], metrics["region"]["delta"])
    with c3: st.metric(metrics["visitors"]["label"], metrics["visitors"]["value"], metrics["visitors"]["delta"])
    with c4: st.metric(metrics["conversion"]["label"], metrics["conversion"]["value"], metrics["conversion"]["delta"])

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    # Chart & Notifications Split
    col_chart, col_notif = st.columns([2, 1])
    
    with col_chart:
        st.markdown("### 📈 Satış Trendi")
        st.markdown("<div style='background: rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:10px;'>", unsafe_allow_html=True)
        # Fix: using theme="streamlit" and letting streamlit handle width if needed, or specific kwargs
        st.plotly_chart(get_sales_chart(), use_container_width=True, config={'displayModeBar': False})
        st.markdown("</div>", unsafe_allow_html=True)

    with col_notif:
        st.markdown("### 🔔 Canlı Bildirimler")
        # Pure HTML implementation that matches styles.py classes
        html_content = """
        <div class="notification-box">
            <div class="notif-item">
                <div class="status-dot" style="background-color: #3b82f6;"></div>
                <div class="notif-content">
                    <h4>NJ Deposuna ürün girişi</h4>
                    <p>SKU-204 New Jersey deposuna ulaştı.<br><span style="color:#555; font-size:10px;">2 dk önce</span></p>
                </div>
            </div>
            <div class="notif-item">
                <div class="status-dot" style="background-color: #22c55e;"></div>
                <div class="notif-content">
                    <h4>Stripe ödemesi alındı</h4>
                    <p>$249.00 başarıyla tahsil edildi.<br><span style="color:#555; font-size:10px;">15 dk önce</span></p>
                </div>
            </div>
            <div class="notif-item">
                <div class="status-dot" style="background-color: #eab308;"></div>
                <div class="notif-content">
                    <h4>Stok Uyarısı</h4>
                    <p>Leather Wallet stoğu kritik seviyede (%5).<br><span style="color:#555; font-size:10px;">1 saat önce</span></p>
                </div>
            </div>
             <div class="notif-item">
                <div class="status-dot" style="background-color: #a855f7;"></div>
                <div class="notif-content">
                    <h4>AI Satış Ajanı</h4>
                    <p>50 yeni potansiyel müşteriye mail atıldı.<br><span style="color:#555; font-size:10px;">2 saat önce</span></p>
                </div>
            </div>
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)

# --- 2. JARVIS AI PAGE ---
def render_ai_manager():
    render_header("JARVIS AI", "Yapay Zeka Operasyon Asistanı")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Merhaba. Operasyon verilerini analiz ettim. Bugün size nasıl yardımcı olabilirim?"}
        ]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            # Coloring logic: Gold for AI, White for User
            color = "#D4AF37" if message["role"] == "assistant" else "#FFF"
            st.markdown(f"<span style='color: {color}'>{message['content']}</span>", unsafe_allow_html=True)

    # Chat Input
    if prompt := st.chat_input("Talimat verin (Örn: İade oranlarını analiz et...)"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(f"<span style='color: #FFF'>{prompt}</span>", unsafe_allow_html=True)
        
        # Simulated Response
        response = "Veriler analiz ediliyor... Geçen ayki iade oranı %2.1. Bu, sektör ortalamasının altında. Özellikle tekstil kategorisinde performans yüksek."
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(f"<span style='color: #D4AF37'>{response}</span>", unsafe_allow_html=True)

# --- 3. LOGISTICS PAGE ---
def render_logistics():
    render_header("Lojistik Ağı", "Canlı Kargo Takibi ve Rota Yönetimi")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.plotly_chart(get_map_chart(), use_container_width=True)

    with col2:
        st.markdown("### 📦 Aktif Sevkiyatlar")
        st.markdown("""
        <div style="background:rgba(255,255,255,0.03); padding:15px; border-radius:10px; border:1px solid #333;">
            <div style="margin-bottom:15px; border-bottom:1px solid #333; padding-bottom:10px;">
                <span style="color:#D4AF37; font-size:12px;">SHIPMENT #TR-8821</span><br>
                <span style="color:white;">Istanbul ➔ New York</span><br>
                <span style="color:#888; font-size:11px;">Durum: Gümrükte</span>
            </div>
            <div style="margin-bottom:15px;">
                <span style="color:#D4AF37; font-size:12px;">SHIPMENT #EU-1029</span><br>
                <span style="color:white;">Istanbul ➔ Berlin</span><br>
                <span style="color:#888; font-size:11px;">Durum: Dağıtımda</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- 4. MARKETING PAGE ---
def render_marketing():
    render_header("Pazarlama 360°", "Kampanya Performansı ve ROAS Analizi")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("### Kampanya Dağılımı")
        labels = ['Google Ads', 'Meta (FB/IG)', 'Email', 'Influencer']
        values = [40, 35, 15, 10]
        
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6)])
        fig.update_traces(marker=dict(colors=['#D4AF37', '#b69246', '#333333', '#555555']))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            showlegend=True,
            height=300,
            margin=dict(t=0, b=0, l=0, r=0)
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with c2:
        st.markdown("### ROAS (Reklam Getirisi)")
        st.metric("Google ROAS", "4.2x", "+0.3x")
        st.metric("Meta ROAS", "3.1x", "-0.1x")
        st.info("💡 Meta reklamlarında kreatif değişikliği öneriliyor.")
