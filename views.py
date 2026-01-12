import streamlit as st
import time
from brain import get_artis_response, get_dashboard_metrics, get_sales_chart

# --- LOGIN EKRANI ---
def render_login_screen():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center; font-family:Cinzel; font-size:60px; color:#D4AF37; margin-bottom:0;'>AS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#666; font-size:12px; letter-spacing:4px;'>ENTERPRISE ACCESS</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.form("login"):
            username = st.text_input("ID", placeholder="admin")
            password = st.text_input("PASS", type="password", placeholder="••••")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.form_submit_button("Sisteme Giriş"):
                if username == "admin" and password == "admin":
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Erişim Reddedildi")

# --- ANA EKRAN (PERPLEXITY TARZI HOME) ---
def render_artis_home():
    # Başlık ve Karşılama
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>ARTIFICIAL STAFF</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Global operasyonlarınız için neyi bilmek istersiniz?</p>", unsafe_allow_html=True)

    # Chat / Arama Alanı (Sayfanın Ortasında)
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        user_input = st.chat_input("Bir soru sorun (Örn: Lojistik süresi nedir?)...")
    
    # Hızlı Erişim Butonları (Öneriler)
    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
    b1, b2, b3, b4 = st.columns(4)
    with b1: 
        if st.button("📦 Lojistik Durumu"): pass
    with b2:
        if st.button("💰 Maliyet Analizi"): pass
    with b3:
        if st.button("🏛️ Şirket Kurulumu"): pass
    with b4:
        if st.button("📈 Pazar Trendleri"): pass

    # Cevap Alanı (Varsa)
    if user_input:
        st.markdown("---")
        with st.chat_message("user"):
            st.write(user_input)
        
        response = get_artis_response(user_input)
        with st.chat_message("assistant"):
            st.markdown(f"<span style='color:#D4AF37'><strong>ARTIS:</strong></span> {response}", unsafe_allow_html=True)

# --- HİZMETLER (KART GÖRÜNÜMÜ) ---
def render_services():
    st.markdown("### Hizmetler & Çözümler")
    st.markdown("---")
    
    services = [
        ("fa-solid fa-code", "Web & Teknoloji", "ABD uyumlu e-ticaret altyapısı."),
        ("fa-solid fa-building-columns", "LLC Kurulumu", "Delaware şirket ve banka hesabı."),
        ("fa-solid fa-plane", "Lojistik", "2-4 günde kapı teslim kargo."),
        ("fa-solid fa-warehouse", "Depolama", "NJ/CA 3PL depolama hizmeti."),
        ("fa-brands fa-amazon", "Pazaryeri", "Amazon & Walmart hesap yönetimi."),
        ("fa-solid fa-bullhorn", "Reklam", "Meta & Google Ads yönetimi.")
    ]
    
    # Grid oluştur
    rows = [services[i:i+3] for i in range(0, len(services), 3)]
    for row in rows:
        cols = st.columns(3)
        for idx, (icon, title, desc) in enumerate(row):
            with cols[idx]:
                st.markdown(f"""
                <div class="info-card">
                    <div class="card-icon"><i class="{icon}"></i></div>
                    <div class="card-title">{title}</div>
                    <div class="card-desc">{desc}</div>
                </div>
                """, unsafe_allow_html=True)
        st.write("")

# --- DASHBOARD ---
def render_dashboard():
    st.markdown("### Finansal Genel Bakış")
    metrics = get_dashboard_metrics()
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric(metrics["revenue"]["label"], metrics["revenue"]["value"], metrics["revenue"]["delta"])
    with c2: st.metric(metrics["region"]["label"], metrics["region"]["value"], metrics["region"]["delta"])
    with c3: st.metric(metrics["visitors"]["label"], metrics["visitors"]["value"], metrics["visitors"]["delta"])
    with c4: st.metric(metrics["conversion"]["label"], metrics["conversion"]["value"], metrics["conversion"]["delta"])
    
    st.markdown("### Satış Trendi")
    st.plotly_chart(get_sales_chart(), use_container_width=True)
