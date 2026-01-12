import streamlit as st
import brain
import time

def render_navbar():
    st.markdown("""
        <div class="custom-navbar">
            <div class="nav-logo">ARTIS <span style="color:#D4AF37">STAFF</span></div>
            <div class="nav-links">
                OPERATIONS // ANALYTICS // NETWORK
            </div>
            <div class="nav-cta">
                STATUS: ONLINE
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 3rem;'>ARTIS ACCESS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666; font-family: Share Tech Mono;'>ENTER CREDENTIALS TO INITIALIZE KERNEL</p>", unsafe_allow_html=True)
        
        user = st.text_input("IDENTITY", placeholder="Username")
        password = st.text_input("KEY", placeholder="Password", type="password")
        
        if st.button("INITIALIZE SYSTEM"):
            if user == "admin" and password == "admin":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("ACCESS DENIED. INVALID CREDENTIALS.")

def render_hero():
    st.markdown("""
        <div class="animate-text">
            <h1 style="font-size: 3.5rem; margin-bottom: 0;">ARTIFICIAL STAFF <span style="font-size:1rem; vertical-align:top; color:#D4AF37">v2.0</span></h1>
            <p style="font-size: 1.1rem; color: #AAA; max-width: 700px;">
                Hoş geldiniz. Ben sizin Yapay Zeka Operasyon Müdürünüzüm.
                İşletmenizi ABD pazarına entegre etmek için sistem taraması yapmam gerekiyor.
            </p>
        </div>
        <hr style="border-color: #333; margin: 20px 0;">
    """, unsafe_allow_html=True)

def render_command_center():
    """
    Yeni Ana Sayfa Yapısı:
    1. Sistem Modülleri (Gizli/Açılır)
    2. Veri Toplama Formu
    3. Analiz Sonucu
    """
    
    # 1. HİZMET PROTOKOLÜ (Gizlenebilir Modüller)
    with st.expander("📂 SİSTEM MODÜLLERİ VE HİZMET PROTOKOLÜ (GÖRÜNTÜLEMEK İÇİN TIKLAYIN)"):
        st.markdown("### OPERASYONEL YETENEKLER")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("#### 🏛️ LLC KURULUMU\nDelaware/Wyoming şirket açılışı, EIN temini ve Banka hesabı açılışı.")
        with c2:
            st.markdown("#### 📦 LOJİSTİK AĞI\nTürkiye'den ABD depolarına (FBA/3PL) gümrük dahil kapıdan kapıya teslimat.")
        with c3:
            st.markdown("#### 🤖 AI PAZARLAMA\nRakip analizine dayalı otomatik Meta/TikTok reklam yönetimi.")

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. ANALİZ VE VERİ TOPLAMA BÖLÜMÜ
    st.markdown("### 🧬 İŞLETME VEKTÖR ANALİZİ")
    st.markdown("""
    <p style="color:#888; font-size:0.9rem;">
    Sistemin işletmeniz için özelleştirilmiş bir yol haritası (Roadmap) çıkarabilmesi için aşağıdaki verileri giriniz.
    </p>
    """, unsafe_allow_html=True)

    with st.form("business_intake_form"):
        c1, c2 = st.columns(2)
        
        with c1:
            company_name = st.text_input("Şirket / Marka Adı", placeholder="Örn: Anatolia Textiles")
            industry = st.selectbox("Sektör", ["Tekstil & Moda", "Gıda & İçecek", "Kozmetik", "Ev & Dekorasyon", "Yazılım/SaaS", "Diğer"])
            us_entity = st.selectbox("ABD Şirket Durumu", ["Yok (Sadece TR Şirketi)", "Var (LLC/Corp)", "Kurulum Aşamasında"])
            ein_status = st.selectbox("EIN (Vergi No) Durumu", ["Yok", "Var", "Bilmiyorum"])
            
        with c2:
            fulfillment = st.selectbox("Mevcut Lojistik Yöntemi", ["Henüz Yok", "Kendi Depomdan (Türkiye)", "Amazon FBA", "ABD Ara Depo (3PL)"])
            marketing_budget = st.number_input("Aylık ABD Reklam Bütçesi ($)", min_value=0, value=500, step=100)
            target_region = st.multiselect("Hedef Eyaletler/Bölgeler", ["East Coast (NY/NJ)", "West Coast (LA/CA)", "Texas", "Florida"], default=["East Coast (NY/NJ)"])
        
        submitted = st.form_submit_button("ANALİZİ BAŞLAT VE ROTA OLUŞTUR")

    # 3. ANALİZ SONUCU (FORM GÖNDERİLİNCE ÇIKAR)
    if submitted:
        # Loading efekti
        with st.spinner('VERİLER İŞLENİYOR... GLOBAL PAZAR ALGORİTMALARI ÇALIŞTIRILIYOR...'):
            time.sleep(2) # Cinematic bekleme
            
        # Analiz Verilerini Hazırla
        form_data = {
            "us_entity": us_entity,
            "ein_status": ein_status,
            "fulfillment": fulfillment,
            "marketing_budget": marketing_budget
        }
        
        score, report = brain.analyze_client_business(form_data)
        
        # Sonuç Ekranı
        st.markdown("---")
        st.markdown(f"### 📊 ANALİZ SONUCU: UYUMLULUK SKORU %{score}")
        
        # Progress Bar (Custom HTML ile renkli)
        bar_color = "#D4AF37" if score > 70 else "#FF4B4B"
        st.markdown(f"""
            <div style="width:100%; background-color:#222; border-radius:10px; height:20px;">
                <div style="width:{score}%; background-color:{bar_color}; height:20px; border-radius:10px; transition: width 1s;"></div>
            </div><br>
        """, unsafe_allow_html=True)

        if score < 100:
            st.warning("⚠️ SİSTEM, İHRACAT OPERASYONUNUZDA KRİTİK EKSİKLER TESPİT ETTİ. AŞAĞIDAKİ ADIMLARI TAMAMLAYIN:")
            
            for item in report:
                # Bento Grid tarzı uyarı kartları
                st.markdown(f"""
                <div style="border: 1px solid #FF4B4B; background: rgba(50,0,0,0.3); padding: 15px; border-radius: 8px; margin-bottom: 10px;">
                    <div style="color: #FF4B4B; font-family: 'Share Tech Mono'; font-weight: bold;">[{item['criticality']}] // {item['module']}</div>
                    <div style="color: #FFF; font-family: 'Cinzel'; font-size: 1.1rem; margin-top:5px;">{item['action']}</div>
                    <div style="color: #CCC; font-size: 0.9rem; margin-top:5px;">{item['detail']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br><p style='text-align:center; color:#D4AF37;'>BU EKSİKLERİ GİDERMEK İÇİN 'ARTIS AI' ASİSTANINA BAĞLANABİLİRSİNİZ.</p>", unsafe_allow_html=True)
        else:
            st.success("✅ SİSTEM ANALİZİ MÜKEMMEL. OPERASYON BAŞLAMAYA HAZIR.")

# Diğer fonksiyonlar (render_dashboard, render_chat_interface) aynen kalabilir veya views.py'nin geri kalanında kullanılabilir.
def render_dashboard():
    st.markdown("<h3>FINANCIAL TELEMETRY</h3>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("TOTAL REVENUE", "$124,500", "+12%")
    m2.metric("NET PROFIT", "$56,200", "+8%")
    m3.metric("AD SPEND", "$12,400", "-2%")
    m4.metric("ACTIVE SHIPMENTS", "14", "On Time")
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("<p style='font-family: Share Tech Mono; color: #888;'>REVENUE TRAJECTORY (30D)</p>", unsafe_allow_html=True)
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
    with c2:
        st.markdown("<p style='font-family: Share Tech Mono; color: #888;'>SUPPLY CHAIN VISUALIZER</p>", unsafe_allow_html=True)
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

def render_chat_interface():
    st.markdown("<h3>ARTIS INTELLIGENCE CORE</h3>", unsafe_allow_html=True)
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if prompt := st.chat_input("Ask Artis about Logistics, Taxes, or Ads..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            response_text = brain.get_artis_response(prompt)
            st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
