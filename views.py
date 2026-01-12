# views.py
import streamlit as st
import time
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- 1. EKRAN: STRATEJİK DANIŞMANLIK (JARVIS) ---
def render_step1_consulting():
    st.markdown("## 🧠 Global Entegrasyon Asistanı")
    st.markdown("""
    <div style='background-color: #1c1c24; padding: 15px; border-radius: 10px; border-left: 5px solid #00a8ff;'>
    <strong>Artificial Staff Vizyonu:</strong> Yerel pazardaki rekabetten sıyrılıp, dünyanın en büyük ekonomisine açılmanız için gereken 
    tüm altyapıyı (Hukuk, Finans, Lojistik, Yazılım) tek çatı altında sunuyoruz.
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": COMPANY_DATA}]
        # İlk mesajı daha profesyonel yaptık
        st.session_state.messages.append({"role": "assistant", "content": "Jarvis v4.2 Online. ABD operasyonunuz, LLC kurulumu veya lojistik süreçleri hakkında stratejik planlamaya hazırım."})

    # Mesajları Göster
    for msg in st.session_state.messages:
        if msg["role"] == "system": continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input Alanı
    if prompt := st.chat_input("Soru sorun (Örn: Neden Delaware eyaletinde şirket kurmalıyım?)"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Artificial Staff veritabanı analiz ediliyor..."):
                response_text = get_ai_response(st.session_state.messages)
                st.markdown(response_text)
        
        st.session_state.messages.append({"role": "assistant", "content": response_text})

# --- 2. EKRAN: OPERASYON BAŞLATMA (FORM) ---
def render_step2_action():
    st.markdown("## 🚀 Operasyon Kurulum Merkezi")
    st.write("Markanızı global bir oyuncuya dönüştürmek için resmi süreci başlatın.")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Kurumsal Kimlik")
        c_name = st.text_input("Tescil Edilecek Şirket İsmi")
        owner = st.text_input("Hissedar Ad Soyad (Pasaporttaki hali)")
        email = st.text_input("Kurumsal İletişim E-Posta")
        sector = st.selectbox("Hedef Sektör", ["E-Ticaret (Amazon/Etsy/Walmart)", "B2B İhracat", "Yazılım & SaaS", "Lojistik & Tedarik", "Diğer"])
    
    with col2:
        st.subheader("Entegrasyon Paketi")
        # Paket isimlerini ve açıklamalarını sunuma uygun hale getirdik
        plan = st.radio("Hizmet Seviyesi Seçimi", 
            [
                "GLOBAL STARTUP ($1500) | LLC + Banka + Temel Lojistik", 
                "ENTERPRISE SCALING ($2500) | Full Entegrasyon + B2B AI Satış + Marka Kaydı"
            ], 
            index=0
        )
        
        st.info("""
        **Seçilen Paket Kapsamı:**
        * 🏢 **Yasal:** LLC Kurulumu, EIN, Registered Agent (Delaware/Wyoming).
        * 🏦 **Finans:** Mercury/Brex Banka Hesabı, Stripe & PayPal Altyapısı.
        * 📦 **Lojistik:** Uçtan Uca Nakliye ve Gümrükleme Desteği.
        * ⚡ **Teknoloji:** 0.4s Hızlı Web Altyapısı ve SEO (Enterprise Pakette).
        """)

    st.divider()
    
    if st.button("RESMİ BAŞVURU SÜRECİNİ BAŞLAT", type="primary"):
        if c_name and owner:
            st.session_state["active_order"] = {
                "company": c_name,
                "owner": owner,
                "plan": plan,
                "status": "Compliance Check (Uyumluluk Kontrolü)",
                "progress": 5
            }
            st.success("✅ Başvuru sisteme işlendi. Operasyon ekibimiz uyumluluk kontrollerini başlattı. 'Durum İzle' ekranından takip edebilirsiniz.")
            time.sleep(1.5)
            st.rerun()
        else:
            st.error("⚠️ Lütfen yasal işlemler için şirket ismi ve hissedar bilgilerini eksiksiz giriniz.")

# --- 3. EKRAN: SÜREÇ TAKİBİ (DASHBOARD) ---
def render_step3_tracking():
    st.markdown("## 📊 Operasyon Kontrol Paneli")
    
    if "active_order" not in st.session_state:
        st.warning("⚠️ Henüz aktif bir global operasyon kaydı bulunamadı. Lütfen 'İşe Başla' menüsünden kurulumu başlatın.")
        st.stop()
    
    data = st.session_state["active_order"]
    
    # Dashboard Metrikleri
    c1, c2, c3 = st.columns(3)
    c1.metric("Şirket", data["company"], "US Entity")
    c2.metric("Paket", "Enterprise" if "Enterprise" in data["plan"] else "Startup", "Active")
    c3.metric("Tahmini Teslim", "3-5 İş Günü", "On Time")
    
    st.divider()
    
    st.subheader("Canlı Süreç Akışı")
    st.progress(data["progress"])
    
    st.caption(f"📍 Mevcut Aşama: **{data['status']}**")
    
    col_checklist, col_logs = st.columns([1, 1])
    
    with col_checklist:
        st.markdown("### 📝 Yapılacaklar Listesi")
        st.checkbox("Başvuru & KYC Doğrulaması", value=True, disabled=True)
        st.checkbox("Eyalet Dosyalama (State Filing)", value=(data['progress'] > 20), disabled=True)
        st.checkbox("EIN (Vergi No) Tahsisi", value=False, disabled=True)
        st.checkbox("Mercury Banka Hesabı Açılışı", value=False, disabled=True)
        st.checkbox("Global Lojistik Entegrasyonu", value=False, disabled=True)
        
    with col_logs:
        st.markdown("### 📡 Sistem Logları")
        st.code(f"""
        [SYSTEM] New Order Created: {data['company']} LLC
        [INFO] Region: US-East-1
        [STATUS] Verifying identity documents...
        [STATUS] Waiting for State approval...
        """, language="bash")
