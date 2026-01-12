import streamlit as st
import plotly.graph_objects as go
from brain import get_dashboard_metrics, get_sales_chart, get_map_chart, get_artis_response

# --- ORTAK HEADER ---
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

# --- 1. HİZMET KATALOĞU (YENİ MODÜL) ---
def render_services_catalog():
    render_header("Hizmetler & Çözümler", "Artificial Staff Enterprise Ekosistemi")
    
    st.markdown("""
    <p style='color:#ccc; font-size:16px; margin-bottom:30px;'>
        İşletmenizi global bir markaya dönüştürmek için ihtiyacınız olan 9 temel yapı taşı. 
        Tek merkezden yönetim, tam entegrasyon.
    </p>
    """, unsafe_allow_html=True)

    # Hizmet verileri (Sunumdan alındı)
    services = [
        {"icon": "fa-solid fa-laptop-code", "title": "Web & Teknoloji", "desc": "ABD tüketici algısına uygun, yüksek dönüşüm odaklı e-ticaret altyapısı."},
        {"icon": "fa-solid fa-building-columns", "title": "LLC Şirket Kurulumu", "desc": "Delaware/Wyoming kurulumu, EIN, Banka hesabı ve Stripe/PayPal çözümü."},
        {"icon": "fa-solid fa-plane-departure", "title": "Lojistik & Gümrük", "desc": "Depodan kapıya uçtan uca nakliye. Express kargo ile 2-4 günde teslimat."},
        {"icon": "fa-solid fa-boxes-stacked", "title": "3PL Depolama", "desc": "NJ ve CA eyaletlerinde stratejik depolar. 24 saatte sipariş işleme."},
        {"icon": "fa-brands fa-amazon", "title": "Pazaryeri Yönetimi", "desc": "Amazon, Etsy, Walmart hesap açılışı, A9 algoritmasına uygun SEO."},
        {"icon": "fa-solid fa-hashtag", "title": "Sosyal Medya", "desc": "Markayı 'Yaşam Tarzı'na dönüştüren içerik üretimi ve Influencer pazarlaması."},
        {"icon": "fa-solid fa-bullhorn", "title": "Reklam (Ads)", "desc": "Meta ve Google reklamlarında yüksek ROAS (Yatırım Getirisi) hedefli yönetim."},
        {"icon": "fa-solid fa-robot", "title": "Otomasyon (CRM)", "desc": "Sipariş, fatura ve müşteri iletişiminde insan hatasını sıfıra indiren sistemler."},
        {"icon": "fa-solid fa-handshake", "title": "B2B AI Satış", "desc": "Yapay zeka ile ABD'li toptancıları bulup otomatik iletişime geçen satış ordusu."}
    ]

    # 3x3 Grid oluşturma
    rows = [services[i:i+3] for i in range(0, len(services), 3)]
    
    for row in rows:
        cols = st.columns(3)
        for idx, service in enumerate(row):
            with cols[idx]:
                # Styles.py'daki 'metric-container' sınıfını kullanarak kart görünümü veriyoruz
                st.markdown(f"""
                <div class="metric-container" style="height: 220px; position: relative;">
                    <div style="color: #D4AF37; font-size: 24px; margin-bottom: 15px;">
                        <i class="{service['icon']}"></i>
                    </div>
                    <h3 style="color: white; font-family: 'Cinzel', serif; font-size: 18px; margin-bottom: 10px;">{service['title']}</h3>
                    <p style="color: #888; font-size: 13px; line-height: 1.5;">{service['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-top: 40px; padding: 20px; border: 1px solid #333; border-radius: 10px;">
        <p style="color: #D4AF37; font-family: 'Cinzel', serif; font-size: 20px;">"Ürünler Türkiye'den, Kazanç Amerika'dan."</p>
        <p style="color: #666; font-size: 12px;">Hangi paketin size uygun olduğunu öğrenmek için ARTIS AI ile konuşun.</p>
    </div>
    """, unsafe_allow_html=True)


# --- 2. DASHBOARD ---
def render_dashboard():
    render_header("Global Operasyon Merkezi", "Anlık Veri Akışı ve Pazar Analizi")
    
    metrics = get_dashboard_metrics()
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric(metrics["revenue"]["label"], metrics["revenue"]["value"], metrics["revenue"]["delta"])
    with c2: st.metric(metrics["region"]["label"], metrics["region"]["value"], metrics["region"]["delta"])
    with c3: st.metric(metrics["visitors"]["label"], metrics["visitors"]["value"], metrics["visitors"]["delta"])
    with c4: st.metric(metrics["conversion"]["label"], metrics["conversion"]["value"], metrics["conversion"]["delta"])

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    col_chart, col_notif = st.columns([2, 1])
    
    with col_chart:
        st.markdown("### 📈 Büyüme Projeksiyonu")
        st.markdown("<div style='background: rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:10px;'>", unsafe_allow_html=True)
        st.plotly_chart(get_sales_chart(), use_container_width=True, config={'displayModeBar': False})
        st.markdown("</div>", unsafe_allow_html=True)

    with col_notif:
        st.markdown("### 🔔 Canlı Bildirimler (Demo)")
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
                <div class="status-dot" style="background-color: #a855f7;"></div>
                <div class="notif-content">
                    <h4>ARTIS Satış Ajanı</h4>
                    <p>50 yeni potansiyel müşteriye mail atıldı.<br><span style="color:#555; font-size:10px;">2 saat önce</span></p>
                </div>
            </div>
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)

# --- 3. ARTIS AI (AKILLI ASİSTAN) ---
def render_artis_ai():
    render_header("ARTIS AI", "Artificial Intelligence Staff - Operasyon Asistanı")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Merhaba! Ben ARTIS. İşletmenizi globalleştirmek için buradayım. Lojistik, LLC kurulumu veya Maliyetler hakkında sorunuz var mı?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            color = "#D4AF37" if message["role"] == "assistant" else "#FFF"
            st.markdown(f"<span style='color: {color}'>{message['content']}</span>", unsafe_allow_html=True)

    if prompt := st.chat_input("Sorunuzu yazın (Örn: Kargo kaç günde gider?)..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(f"<span style='color: #FFF'>{prompt}</span>", unsafe_allow_html=True)
        
        # Brain dosyasındaki akıllı fonksiyonu çağırıyoruz
        response = get_artis_response(prompt)
        
        # Hafif bir gecikme efekti (gerçekçilik için)
        import time
        time.sleep(0.5)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(f"<span style='color: #D4AF37'>{response}</span>", unsafe_allow_html=True)

# --- 4. LOJİSTİK ---
def render_logistics():
    render_header("Lojistik Ağı", "Canlı Kargo Takibi ve Rota Yönetimi")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.plotly_chart(get_map_chart(), use_container_width=True)
    with col2:
        st.markdown("### 📦 Örnek Sevkiyatlar")
        st.markdown("""
        <div class="metric-container">
            <div style="margin-bottom:15px; border-bottom:1px solid #333; padding-bottom:10px;">
                <span style="color:#D4AF37; font-size:12px;">SHIPMENT #TR-8821</span><br>
                <span style="color:white;">Istanbul ➔ New York</span><br>
                <span style="color:#888; font-size:11px;">Durum: Gümrükte</span>
            </div>
            <div>
                <span style="color:#D4AF37; font-size:12px;">SHIPMENT #EU-1029</span><br>
                <span style="color:white;">Istanbul ➔ Berlin</span><br>
                <span style="color:#888; font-size:11px;">Durum: Dağıtımda</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- 5. PAZARLAMA ---
def render_marketing():
    render_header("Pazarlama 360°", "Kampanya Performansı ve ROAS Analizi")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Kanal Dağılımı")
        labels = ['Google Ads', 'Meta (FB/IG)', 'Email', 'Influencer']
        values = [40, 35, 15, 10]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6)])
        fig.update_traces(marker=dict(colors=['#D4AF37', '#b69246', '#333333', '#555555']))
        fig.update_layout(
