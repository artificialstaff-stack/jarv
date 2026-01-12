import streamlit as st
import time
from brain import get_dashboard_metrics, get_sales_chart, get_map_chart, get_marketing_chart, get_artis_response

# --- HEADER ---
def render_header(title, subtitle):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**{title}**")
        st.caption(subtitle)
    with col2:
        st.markdown("<div style='text-align:right; color:#D4AF37;'>● ONLINE</div>", unsafe_allow_html=True)
    st.markdown("---")

# --- 1. HİZMET KATALOĞU (Müşteri Vitrini) ---
def render_services_catalog():
    render_header("Hizmetler & Çözümler", "Artificial Staff Enterprise Ekosistemi")
    
    st.info("İşletmenizi global bir markaya dönüştürmek için ihtiyacınız olan 9 temel yapı taşı.")

    # Hizmet Verileri
    services = [
        ("💻", "Web & Teknoloji", "ABD tüketici algısına uygun, yüksek dönüşüm odaklı e-ticaret altyapısı."),
        ("🏛️", "LLC Kurulumu", "Delaware/Wyoming kurulumu, EIN, Banka hesabı ve Stripe/PayPal çözümü."),
        ("✈️", "Lojistik & Gümrük", "Depodan kapıya uçtan uca nakliye. Express kargo ile 2-4 günde teslimat."),
        ("🏭", "3PL Depolama", "NJ ve CA eyaletlerinde stratejik depolar. 24 saatte sipariş işleme."),
        ("🛒", "Pazaryeri Yönetimi", "Amazon, Etsy, Walmart hesap açılışı ve A9 algoritmasına uygun SEO."),
        ("📱", "Sosyal Medya", "Markayı 'Yaşam Tarzı'na dönüştüren içerik üretimi ve Influencer pazarlaması."),
        ("📢", "Reklam (Ads)", "Meta ve Google reklamlarında yüksek ROAS (Yatırım Getirisi) hedefli yönetim."),
        ("🤖", "Otomasyon (CRM)", "Sipariş ve fatura süreçlerinde insan hatasını sıfıra indiren sistemler."),
        ("🤝", "B2B AI Satış", "Yapay zeka ile ABD'li toptancıları bulup otomatik iletişime geçen satış ordusu.")
    ]

    # Grid Yapısı
    for i in range(0, len(services), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(services):
                icon, title, desc = services[i+j]
                with cols[j]:
                    st.markdown(f"""
                    <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:10px; border:1px solid #333; height:200px;">
                        <div style="font-size:30px; margin-bottom:10px;">{icon}</div>
                        <h4 style="color:#fff; margin:0;">{title}</h4>
                        <p style="color:#888; font-size:12px; margin-top:5px;">{desc}</p>
                    </div>
                    """, unsafe_allow_html=True)
        st.write("") # Boşluk

# --- 2. DASHBOARD ---
def render_dashboard():
    render_header("Global Operasyon Merkezi", "Anlık Veri Akışı")
    
    metrics = get_dashboard_metrics()
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric(metrics["revenue"]["label"], metrics["revenue"]["value"], metrics["revenue"]["delta"])
    with c2: st.metric(metrics["region"]["label"], metrics["region"]["value"], metrics["region"]["delta"])
    with c3: st.metric(metrics["visitors"]["label"], metrics["visitors"]["value"], metrics["visitors"]["delta"])
    with c4: st.metric(metrics["conversion"]["label"], metrics["conversion"]["value"], metrics["conversion"]["delta"])

    st.markdown("### 📈 Büyüme Projeksiyonu")
    st.plotly_chart(get_sales_chart(), use_container_width=True)

# --- 3. ARTIS AI ---
def render_artis_ai():
    render_header("ARTIS AI", "Yapay Zeka Operasyon Asistanı")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba! Ben ARTIS. Global operasyonlarınız için buradayım."}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Sorunuzu yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        response = get_artis_response(prompt)
        time.sleep(0.5)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

# --- 4. LOJİSTİK ---
def render_logistics():
    render_header("Lojistik Ağı", "Canlı Takip")
    c1, c2 = st.columns([3, 1])
    with c1: st.plotly_chart(get_map_chart(), use_container_width=True)
    with c2: 
        st.info("📦 **TR-8821**: İstanbul -> NY (Gümrükte)")
        st.success("✅ **EU-1029**: İstanbul -> Berlin (Teslim Edildi)")

# --- 5. PAZARLAMA ---
def render_marketing():
    render_header("Pazarlama 360°", "Kanal Performansı")
    c1, c2 = st.columns(2)
    with c1: st.plotly_chart(get_marketing_chart(), use_container_width=True)
    with c2:
        st.metric("Google ROAS", "4.2x", "+0.3x")
        st.metric("Meta ROAS", "3.1x", "-0.1x")
