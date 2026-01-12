import streamlit as st
import time
from brain import get_dashboard_metrics, get_sales_chart, get_map_chart, get_marketing_chart, get_artis_response

# --- HEADER ---
def render_header(title, subtitle):
    col1, col2 = st.columns([3, 1])
    with col1:
        # Lüks Başlık Yapısı
        st.markdown(f"""
        <div>
            <h2 style='font-family:"Cinzel", serif; color:white; margin-bottom:5px;'>{title}</h2>
            <p style='font-family:"Inter", sans-serif; color:#888; font-size:14px; margin-top:0;'>{subtitle}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align:right; color:#D4AF37; font-size:11px; letter-spacing:1px; margin-top:20px;'>● SYSTEM ONLINE</div>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color:rgba(255,255,255,0.1); margin-top:0;'>", unsafe_allow_html=True)

# --- 1. HİZMET KATALOĞU (YENİLENMİŞ TASARIM) ---
def render_services_catalog():
    render_header("Hizmetler & Çözümler", "Artificial Staff Enterprise Ekosistemi")
    
    # Modern Giriş Metni
    st.markdown("""
    <div style='background:rgba(212, 175, 55, 0.05); border-left:3px solid #D4AF37; padding:15px; border-radius:4px; margin-bottom:40px;'>
        <p style='color:#ddd; font-size:14px; margin:0;'>
            İşletmenizi global bir markaya dönüştürmek için tasarlanan <strong>9 Temel Modül</strong>. 
            Her bir parça, yapay zeka ve otomasyon ile güçlendirilmiştir.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Hizmet Verileri (FontAwesome Sınıfları ile)
    services = [
        ("fa-solid fa-code", "Web & Teknoloji", "ABD tüketici algısına uygun, Google Core Web Vitals uyumlu, yüksek dönüşüm odaklı 'Headless' e-ticaret altyapısı."),
        ("fa-solid fa-building-columns", "LLC Kurulumu", "Delaware/Wyoming kurulumu, EIN, Banka hesabı (Mercury) ve Stripe/PayPal entegrasyonu ile tam finansal özgürlük."),
        ("fa-solid fa-plane-departure", "Lojistik & Gümrük", "İstanbul'dan New York'a uçtan uca nakliye. Express kargo ile 2-4 günde kapı teslimat garantisi."),
        ("fa-solid fa-warehouse", "3PL Depolama", "NJ ve CA eyaletlerinde stratejik depolar. Sipariş geldiği gün paketleme ve kargolama (Same-Day Fulfillment)."),
        ("fa-brands fa-amazon", "Pazaryeri Yönetimi", "Amazon, Etsy, Walmart hesap açılışı. 'Gated' kategorilerin açılması ve A9 algoritmasına uygun SEO."),
        ("fa-solid fa-hashtag", "Sosyal Medya", "Markanızı bir 'Yaşam Tarzı'na dönüştüren içerik üretimi. Influencer pazarlaması ve topluluk yönetimi."),
        ("fa-solid fa-bullhorn", "Reklam (Ads)", "Meta (FB/IG) ve Google Ads yönetiminde yapay zeka destekli hedefleme ile yüksek ROAS (Yatırım Getirisi)."),
        ("fa-solid fa-gears", "Otomasyon (CRM)", "Sipariş, fatura ve müşteri iletişiminde insan hatasını sıfıra indiren Zapier/Make entegrasyonları."),
        ("fa-solid fa-robot", "B2B AI Satış", "Yapay zeka ajanlarımız, ABD'deki toptancıları bulur, analiz eder ve sizin adınıza soğuk e-posta (Cold Email) atar.")
    ]

    # Grid Yapısı (CSS Class'ları styles.py'dan geliyor)
    for i in range(0, len(services), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(services):
                icon_class, title, desc = services[i+j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="service-card">
                        <div class="card-icon"><i class="{icon_class}"></i></div>
                        <div class="card-title">{title}</div>
                        <div class="card-desc">{desc}</div>
                    </div>
                    """, unsafe_allow_html=True)
        st.write("") # Satır aralığı

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
    st.plotly_chart(get_sales_chart(), width="stretch")

# --- 3. ARTIS AI ---
def render_artis_ai():
    render_header("ARTIS AI", "Yapay Zeka Operasyon Asistanı")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba! Ben ARTIS. Global operasyonlarınız için buradayım. Size nasıl yardımcı olabilirim?"}]

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
    with c1: st.plotly_chart(get_map_chart(), width="stretch")
    with c2: 
        st.info("📦 **TR-8821**: İstanbul -> NY (Gümrükte)")
        st.success("✅ **EU-1029**: İstanbul -> Berlin (Teslim Edildi)")

# --- 5. PAZARLAMA ---
def render_marketing():
    render_header("Pazarlama 360°", "Kanal Performansı")
    c1, c2 = st.columns(2)
    with c1: st.plotly_chart(get_marketing_chart(), width="stretch")
    with c2:
        st.metric("Google ROAS", "4.2x", "+0.3x")
        st.metric("Meta ROAS", "3.1x", "-0.1x")
