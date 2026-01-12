import streamlit as st
import time
from brain import get_dashboard_metrics, get_sales_chart, get_map_chart, get_marketing_chart, get_artis_response

# --- HEADER ---
def render_header(title, subtitle):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### {title}")
        st.caption(subtitle)
    with col2:
        st.markdown("<div style='text-align:right; color:#D4AF37; font-size:12px;'>● ONLINE</div>", unsafe_allow_html=True)
    st.markdown("---")

# --- 0. CINEMATIC INTRO (MATRIX STYLE) ---
def render_cinematic_intro():
    """
    Bu fonksiyon site ilk açıldığında çalışır.
    Neo/Matrix tarzı yazıyı yazar ve sonra ana ekrana dönüşür.
    """
    # Eğer intro daha önce izlendiyse direkt Hub'a geç
    if 'intro_complete' in st.session_state and st.session_state.intro_complete:
        render_main_hub()
        return

    # Boş bir alan yarat
    intro_placeholder = st.empty()
    
    # Yazılacak Metin (Manifesto)
    manifesto_lines = [
        "Uyanın...",
        "Yerel pazarın sınırları sizi boğuyor.",
        "Maliyetleriniz artıyor, kârınız eriyor.",
        "Siz Dolar kazanmak istiyorsunuz, ama sistem sizi TL'ye hapsediyor.",
        "...",
        "Biz bir köprüyüz.",
        "Biz bir anahtarız.",
        "Coğrafya kader değildir.",
        "Hoş geldiniz."
    ]

    # Yazı Animasyonu
    full_text = ""
    with intro_placeholder.container():
        st.markdown("<br><br><br>", unsafe_allow_html=True) # Üst boşluk
        text_area = st.empty()
        
        for line in manifesto_lines:
            for char in line:
                full_text += char
                # HTML ile cursor efekti
                text_area.markdown(f"""
                    <div style="display:flex; justify-content:center; align-items:center; height:60vh; text-align:center;">
                        <div class="neo-text">{full_text}<span class="cursor"></span></div>
                    </div>
                """, unsafe_allow_html=True)
                time.sleep(0.04) # Yazma hızı
            
            full_text += "\n" # Satır atla
            time.sleep(0.5)   # Satır sonu bekleme

        time.sleep(1.5) # Yazı bitince bekle
        
        # Animasyon bitişi: Yazılar silinir (Dosyaya dönüşme efekti simülasyonu)
        text_area.markdown(f"""
            <div style="display:flex; justify-content:center; align-items:center; height:60vh; text-align:center;">
                <div class="neo-text" style="color:white; font-size:12px; transition:1s;">
                    SYSTEM INITIALIZED... DATA COMPRESSED TO CORE.
                </div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1.5)

    # Intro bitti, durumu kaydet ve Hub'ı göster
    st.session_state.intro_complete = True
    intro_placeholder.empty()
    st.rerun()

# --- 1. MAIN HUB (ANA MERKEZ) ---
def render_main_hub():
    """
    9 Hizmetin ve Şirket Bilgisinin toplandığı ana ekran.
    """
    render_header("Global Kontrol Paneli", "Artificial Staff Enterprise v2.4")

    # İki Ana Modül (Baloncuk Yerine Lüks Kartlar)
    col1, col2 = st.columns(2)

    # MODÜL 1: SYSTEM CORE (Şirket Manifestosu)
    with col1:
        st.markdown("""
        <div class="hub-card">
            <div class="hub-icon"><i class="fa-solid fa-microchip"></i></div>
            <div class="hub-title">SYSTEM CORE</div>
            <div class="hub-desc">Şirket Vizyonu, Manifesto & Strateji</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Burası Manifesto'nun 'dosya' hali. Tıklayınca açılır gibi Expander
        with st.expander("📂 DOSYAYI AÇ: ARTIFICIAL VIZYONU"):
            st.markdown("""
            **KİMLİK:**
            Artificial Staff LLC, yapay zeka tabanlı bir Operasyon Direktörüdür.
            
            **MİSYON:**
            Türk markalarının yerel rekabetten sıyrılıp, ABD ekonomisine "Uçtan Uca İhracat Altyapısı" ile entegre olmasını sağlamak.
            
            **MOTTO:**
            "Ürünler Türkiye'den, Kazanç Amerika'dan."
            """)

    # MODÜL 2: SERVICE PROTOCOLS (9 Hizmet)
    with col2:
        st.markdown("""
        <div class="hub-card" style="border-color: rgba(212, 175, 55, 0.4);">
            <div class="hub-icon"><i class="fa-solid fa-layer-group"></i></div>
            <div class="hub-title">SERVICE PROTOCOLS</div>
            <div class="hub-desc">9 Entegre Hizmet Modülü</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Burası Hizmetlerin 'dosya' hali.
        with st.expander("📂 DOSYAYI AÇ: HİZMET KATALOĞU", expanded=True):
            render_service_list_compact()

def render_service_list_compact():
    """Hizmetleri Hub içinde kompakt listeler."""
    services = [
        ("💻", "Web & Teknoloji", "ABD odaklı e-ticaret altyapısı."),
        ("🏛️", "LLC Kurulumu", "Delaware şirket, EIN ve Banka hesabı."),
        ("✈️", "Lojistik & Gümrük", "Kapıdan kapıya 2-4 günde teslimat."),
        ("🏭", "3PL Depolama", "NJ ve CA eyaletlerinde stratejik depolar."),
        ("🛒", "Pazaryeri Yönetimi", "Amazon, Etsy, Walmart hesap yönetimi."),
        ("📱", "Sosyal Medya", "Global marka algısı yönetimi."),
        ("📢", "Reklam (Ads)", "Yüksek ROAS hedefli reklam yönetimi."),
        ("🤖", "Otomasyon (CRM)", "İnsan hatasını sıfıra indiren sistemler."),
        ("🤝", "B2B AI Satış", "Yapay zeka ile toptan müşteri bulma.")
    ]
    
    # Hizmetleri 2 sütun halinde listele
    s_c1, s_c2 = st.columns(2)
    for idx, (icon, title, desc) in enumerate(services):
        target_col = s_c1 if idx % 2 == 0 else s_c2
        with target_col:
            st.markdown(f"""
            <div class="service-mini-card">
                <strong style="color:white;">{icon} {title}</strong><br>
                <span style="color:#888; font-size:11px;">{desc}</span>
            </div>
            """, unsafe_allow_html=True)

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
