# views.py
import streamlit as st
import time
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- YARDIMCI FONKSİYON: PREMIUM KART ---
def premium_metric_card(label, value, desc):
    st.markdown(f"""
    <div class="premium-card">
        <span class="metric-value">{value}</span>
        <span class="metric-label">{label}</span>
        <p style="font-size: 12px; margin-top: 5px; color: #888;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# --- 1. EKRAN: STRATEJİ & JARVIS ---
def render_step1_consulting():
    # HTML Stili Başlık
    st.markdown("""
    <div>
        <span class="section-tag">01 // VISION</span>
        <h1 style="font-size: 48px; margin-top: 0;">Global Entegrasyon</h1>
        <p style="font-size: 18px; color: #ccc;">Operasyon, Büyüme ve Yapay Zeka ile Uçtan Uca İhracat Altyapısı</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # Chat Geçmişi Başlatma
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": COMPANY_DATA}]
        st.session_state.messages.append({"role": "assistant", "content": "Jarvis Online. Artificial Staff stratejik planlama modülü aktif. Size nasıl yardımcı olabilirim?"})

    # Mesajları Göster
    for msg in st.session_state.messages:
        if msg["role"] == "system": continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input Alanı
    if prompt := st.chat_input("Stratejik sorunuzu yöneltin..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Analiz ediliyor..."):
                response_text = get_ai_response(st.session_state.messages)
                st.markdown(response_text)
        
        st.session_state.messages.append({"role": "assistant", "content": response_text})

# --- 2. EKRAN: OPERASYON BAŞLAT (FORM) ---
def render_step2_action():
    st.markdown("""
    <div>
        <span class="section-tag">LEGAL ENTITY</span>
        <h1>Operasyon Kurulumu</h1>
        <p>Amerika'da resmi şirket sahibi olarak global ticarete başlayın.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### Kurumsal Kimlik")
        c_name = st.text_input("Tescil Edilecek Şirket İsmi", placeholder="Örn: Global Tech LLC")
        owner = st.text_input("Hissedar Ad Soyad", placeholder="Pasaporttaki gibi")
        email = st.text_input("Kurumsal E-Posta")
        sector = st.selectbox("Sektör", ["E-Ticaret", "B2B İhracat", "Yazılım/SaaS", "Lojistik"])
    
    with col2:
        st.markdown("### Hizmet Paketi")
        
        # HTML tarzı paket gösterimi
        plan = st.radio("Seçiminiz", 
            ["GLOBAL STARTUP ($1500)", "ENTERPRISE SCALING ($2500)"],
            captions=["LLC + Banka + Temel Lojistik", "Full Entegrasyon + AI Satış + Marka Kaydı"]
        )
        
        st.markdown("---")
        # HTML'deki gibi 'List' yapısı
        st.markdown("""
        <ul style="color: #aaa; font-size: 14px; list-style-type: none; padding-left: 0;">
            <li style="margin-bottom: 10px;">✓ <strong>Yasal:</strong> Delaware/Wyoming Eyalet Kurulumu</li>
            <li style="margin-bottom: 10px;">✓ <strong>Finans:</strong> Mercury Bank & Stripe Entegrasyonu</li>
            <li style="margin-bottom: 10px;">✓ <strong>Ofis:</strong> Yasal US Adresi ve Registered Agent</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    if st.button("SÜRECİ BAŞLAT"):
        if c_name and owner:
            st.session_state["active_order"] = {
                "company": c_name,
                "owner": owner,
                "plan": plan,
                "status": "Compliance Check",
                "progress": 5
            }
            st.success("Başvuru alındı. Operasyon ekibi yönlendiriliyor.")
            time.sleep(1)
            st.rerun()
        else:
            st.warning("Lütfen kurumsal bilgileri tamamlayın.")

# --- 3. EKRAN: DASHBOARD (İZLEME) ---
def render_step3_tracking():
    if "active_order" not in st.session_state:
        st.info("Aktif operasyon bulunamadı. Lütfen 'İşe Başla' ekranından kurulum yapın.")
        st.stop()
        
    data = st.session_state["active_order"]

    st.markdown("""
    <div>
        <span class="section-tag">05 // DASHBOARD</span>
        <h1>Operasyon Kontrol</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # HTML DOSYASINDAKİ METRİK KARTLARIN AYNISI
    col1, col2, col3 = st.columns(3)
    with col1:
        premium_metric_card("US ENTITY", data["company"], "Delaware LLC")
    with col2:
        premium_metric_card("PACKAGE", "Enterprise" if "Enterprise" in data["plan"] else "Startup", "Active Plan")
    with col3:
        premium_metric_card("ESTIMATED", "3-5 Days", "Completion Time")

    st.markdown("### Canlı Süreç")
    st.progress(data["progress"])
    st.caption(f"STATUS: {data['status'].upper()}")
    
    st.markdown("---")
    
    c_check, c_logs = st.columns(2)
    with c_check:
        st.markdown("#### Yapılacaklar")
        st.checkbox("Compliance Check", value=True, disabled=True)
        st.checkbox("State Filing", value=False, disabled=True)
        st.checkbox("EIN Number", value=False, disabled=True)
    
    with c_logs:
        st.markdown("#### Sistem Logları")
        st.code(f"""
        > SYSTEM INTIIATED...
        > CLIENT: {data['owner']}
        > REGION: US-EAST-1
        > STATUS: WAITING FOR APPROVAL
        """, language="bash")
