# views.py
import streamlit as st
import time
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- YARDIMCI: LOGIN EKRANI ---
def render_login():
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.markdown("""
        <div class="login-container">
            <h1 style="color:#C5A059 !important; font-size: 60px; margin-bottom: 0;">AS</h1>
            <p style="letter-spacing: 3px; font-size: 12px; margin-bottom: 30px; color: #666;">ARTIFICIAL STAFF | ENTERPRISE ACCESS</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: center; margin-bottom: 10px;'>Giriş Yapın</div>", unsafe_allow_html=True)
        username = st.text_input("Kullanıcı Adı", placeholder="admin")
        password = st.text_input("Şifre", type="password", placeholder="1234")
        
        if st.button("SİSTEME GİRİŞ YAP"):
            if username == "admin" and password == "1234": 
                st.session_state["logged_in"] = True
                st.session_state["user_name"] = "Sayın Yönetici"
                st.success("Erişim İzni Verildi. Yönlendiriliyorsunuz...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Erişim Reddedildi: Hatalı Kimlik Bilgileri.")

# --- 1. EKRAN: KARŞILAMA & VİZYON (MANIFESTO) ---
def render_welcome():
    st.markdown("""
    <div>
        <span style="color:#C5A059; letter-spacing:2px; font-size:12px;">01 // VISION</span>
        <h1 style="font-size: 56px; margin-top:0;">Global Entegrasyon</h1>
        <p style="font-size: 20px; color: #ccc; max-width: 800px;">
            Yerel pazardaki rekabetten sıyrılıp, dünyanın en büyük ekonomisine açılmanız için 
            gereken tüm altyapıyı (Hukuk, Finans, Lojistik, Yazılım) tek çatı altında sunuyoruz.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Misyonumuz")
        st.info("Tek merkezden 9 farklı hizmet ile 'TL Gider, Dolar Gelir' modelini şirketinize entegre etmek.")
    with col2:
        st.markdown("### Sonraki Adım")
        st.write("Sizi ve markanızı tanımamız için lütfen profil kurulumunu tamamlayın.")
        if st.button("PROFİL KURULUMUNA BAŞLA ->"):
            st.session_state["current_page"] = "PROFILE"
            st.rerun()

# --- 2. EKRAN: MÜŞTERİ TANIMA (PROFILE) ---
def render_profile():
    st.markdown("## 👤 Marka & Profil Analizi")
    st.write("Size en uygun yol haritasını çıkarmamız için aşağıdaki bilgileri doldurun.")
    st.divider()
    
    with st.form("kyc_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Marka Adı")
            st.selectbox("Mevcut Durum", ["Henüz Şirketim Yok", "Türkiye'de Şirketim Var", "Yurtdışına Satış Yapıyorum"])
            st.number_input("Yatırım Bütçesi ($)", min_value=1000, step=500)
        with col2:
            st.text_input("Yetkili Ad Soyad")
            st.selectbox("Hedef Sektör", ["E-Ticaret (Amazon/Etsy)", "Yazılım / SaaS", "B2B İhracat", "Lojistik"])
            st.selectbox("Öncelikli Hedef", ["Şirket Kurmak (LLC)", "Pazaryeri Hesabı Açmak", "Lojistik Çözmek", "Tam Entegrasyon"])
            
        submitted = st.form_submit_button("ANALİZİ TAMAMLA VE ROTAYI OLUŞTUR")
        
        if submitted:
            st.session_state["profile_completed"] = True
            st.success("Profiliniz yapay zeka tarafından analiz edildi. Sizin için uygun paketler hazırlanıyor.")
            time.sleep(1.5)
            st.session_state["current_page"] = "SERVICE_SELECT" # Otomatik Yönlendirme
            st.rerun()

# --- 3. EKRAN: SERVİS SEÇİMİ & YÖNLENDİRME ---
def render_service_selection():
    st.markdown("## 🧭 Operasyon Rotası Seçimi")
    st.write("Profilinize uygun 3 farklı strateji belirlendi. Hangisiyle ilerlemek istersiniz?")
    st.divider()
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("#### 🚀 STARTUP PACK")
        st.caption("Hızlı başlangıç yapmak isteyenler için.")
        st.markdown("""
        * LLC Kurulumu
        * Banka Hesabı (Mercury)
        * EIN Numarası
        """)
        if st.button("SEÇ: STARTUP ($1500)"):
            st.session_state["selected_plan"] = "Startup"
            st.session_state["current_page"] = "EXECUTION" # Kuruluma Git
            st.rerun()

    with c2:
        st.markdown("#### 💎 ENTERPRISE")
        st.caption("Tam kapsamlı uçtan uca çözüm.")
        st.markdown("""
        * **Her Şey Dahil**
        * Lojistik Altyapısı
        * Web Sitesi & SEO
        * Pazarlama Desteği
        """)
        if st.button("SEÇ: ENTERPRISE ($2500)"):
            st.session_state["selected_plan"] = "Enterprise"
            st.session_state["current_page"] = "EXECUTION"
            st.rerun()

    with c3:
        st.markdown("#### 🧠 CONSULTING")
        st.caption("Emin değil misiniz?")
        st.markdown("""
        * Jarvis ile Strateji
        * Pazar Analizi
        * Soru - Cevap
        """)
        if st.button("JARVIS İLE KONUŞ"):
            st.session_state["current_page"] = "JARVIS"
            st.rerun()

# --- 4. EKRAN: JARVIS (ESKİ STRATEJİ EKRANI) ---
def render_jarvis():
    st.markdown("## 🧠 Jarvis Strateji Merkezi")
    st.caption("Artificial Staff Yapay Zeka Ajanı")
    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": COMPANY_DATA}]
        st.session_state.messages.append({"role": "assistant", "content": "Jarvis Online. Profilinizi inceledim. Hangi konuda desteğe ihtiyacınız var?"})

    for msg in st.session_state.messages:
        if msg["role"] == "system": continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Sorunuzu yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Analiz ediliyor..."):
                response = get_ai_response(st.session_state.messages) # brain.py'den gelir
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- 5. EKRAN: KURULUM (EXECUTION) ---
def render_execution():
    st.markdown("## ⚙️ Operasyon Başlatılıyor")
    st.info(f"Seçilen Paket: **{st.session_state.get('selected_plan', 'Standart')}**")
    st.write("Resmi süreç başlatılıyor. Lütfen aşağıdaki sözleşmeyi onaylayın.")
    
    with st.expander("Sözleşme Detayları (Tıklayın)"):
        st.write("1. Taraflar... 2. Hizmet Kapsamı... 3. Ödeme Koşulları...")
        
    agree = st.checkbox("Hizmet şartlarını okudum ve onaylıyorum.")
    
    if st.button("ÖDEME VE BAŞVURU TAMAMLA", disabled=not agree):
        st.success("Tebrikler! İşlem başarıyla alındı. Takip ekranına yönlendiriliyorsunuz.")
        time.sleep(2)
        st.session_state["active_order"] = {
            "company": "Yeni Başvuru", 
            "plan": st.session_state.get('selected_plan', 'Standart'),
            "status": "Evrak Bekleniyor",
            "progress": 10
        }
        st.session_state["current_page"] = "TRACKING" # Takip ekranı menüden seçilebilir
        st.rerun()
