import streamlit as st
from brain import get_dashboard_metrics, get_sales_chart, get_notifications

def render_header():
    """Üst Bar: Breadcrumbs ve Profil"""
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        <div>
            <span style='font-size: 12px; color: #666; font-family: Inter;'>Ana Sayfa / Dashboard</span>
            <h2 style='margin-top: -5px;'>Global Operasyon Merkezi</h2>
            <p style='margin-top: -10px; font-size: 14px;'>Anlık Veri Akışı ve Pazar Analizi</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        # Profil simülasyonu
        st.markdown("""
        <div style='text-align: right; padding-top: 10px;'>
            <span style='color: #D4AF37; font-size: 12px;'>● ONLINE</span><br>
            <span style='color: #FFF; font-family: Inter;'>Admin User</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin-bottom: 30px;'>", unsafe_allow_html=True)

def render_dashboard():
    # 1. Header
    render_header()

    # 2. Verileri Çek
    metrics = get_dashboard_metrics()

    # 3. Metrik Satırı (Bento Grid - Üst)
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.metric(metrics["revenue"]["label"], metrics["revenue"]["value"], metrics["revenue"]["delta"])
    with c2:
        st.metric(metrics["region"]["label"], metrics["region"]["value"], metrics["region"]["delta"])
    with c3:
        st.metric(metrics["visitors"]["label"], metrics["visitors"]["value"], metrics["visitors"]["delta"])
    with c4:
        st.metric(metrics["conversion"]["label"], metrics["conversion"]["value"], metrics["conversion"]["delta"])

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    # 4. Alt Bölüm: Grafik ve Bildirimler (Split Layout)
    # Sol taraf (Grafik) daha geniş (2 birim), Sağ taraf (Bildirimler) daha dar (1 birim)
    col_chart, col_notif = st.columns([2, 1])

    with col_chart:
        st.markdown("### 📈 Satış Trendi")
        st.markdown("<div style='background: rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:20px;'>", unsafe_allow_html=True)
        st.plotly_chart(get_sales_chart(), use_container_width=True, config={'displayModeBar': False})
        st.markdown("</div>", unsafe_allow_html=True)

    with col_notif:
        st.markdown(get_notifications(), unsafe_allow_html=True)

def render_ai_manager():
    render_header()
    st.info("AI Manager (JARVIS) modülü yapım aşamasında. Burası chat arayüzü olacak.")

def render_logistics():
    render_header()
    st.info("Lojistik modülü harita entegrasyonu.")

def render_marketing():
    render_header()
    st.info("Pazarlama 360 modülü.")
