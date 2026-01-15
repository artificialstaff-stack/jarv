import streamlit as st

def inject_llc_css():
    st.markdown("""
    <style>
        .llc-card {
            background: rgba(20, 20, 22, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 20px;
        }
        .status-pill-active {
            background: rgba(16, 185, 129, 0.1);
            color: #10B981;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            border: 1px solid rgba(16, 185, 129, 0.2);
        }
        .gold-highlight { color: #C5A059; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

def render():
    inject_llc_css()
    
    # Header: Legal Entity
    st.markdown("""
        <div style='margin-bottom: 35px;'>
            <h1 style='font-size: 2.5rem; font-weight: 800;'>⚖️ LLC & Şirket Yönetimi</h1>
            <p style='color: #888;'>Amerika Birleşik Devletleri yasal varlık ve vergi süreçleri yönetim merkezi.</p>
        </div>
    """, unsafe_allow_html=True)

    # Üst Metrikler (Kurulum Durumu)
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown("""
            <div class='llc-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>ŞİRKET DURUMU</div>
                <div style='font-size: 1.8rem; font-weight: 800; margin: 5px 0;'>Wyoming LLC</div>
                <span class='status-pill-active'>AKTİF / GOOD STANDING</span>
            </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
            <div class='llc-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>EIN NUMARASI</div>
                <div style='font-size: 1.8rem; font-weight: 800; margin: 5px 0;'>Onaylandı</div>
                <div style='color: #C5A059; font-size: 0.8rem; font-weight: 700;'>IRS KAYDI TAMAM</div>
            </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
            <div class='llc-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>REGISTERED AGENT</div>
                <div style='font-size: 1.8rem; font-weight: 800; margin: 5px 0;'>Yenilendi</div>
                <div style='color: #3B82F6; font-size: 0.8rem; font-weight: 700;'>2026 PERİYODU AKTİF</div>
            </div>
        """, unsafe_allow_html=True)

    # Ana Bölümler: Finansal Erişim ve Yasal Süreçler
    left, right = st.columns([1.2, 1], gap="large")

    with left:
        st.markdown("### 🏦 Finansal Erişim & Bankacılık")
        
        st.markdown("""
        <div class='llc-card'>
            <p style='color:#ccc;'>Amerikan şirketiniz üzerinden küresel ödeme altyapınız hazır.</p>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px;'>
                <div style='background: rgba(255,255,255,0.03); padding: 15px; border-radius: 12px; border: 1px solid #222;'>
                    <div style='font-size: 12px; color: #888;'>BANKA</div>
                    <div style='font-weight: 700;'>Mercury Bank</div>
                    <div style='color: #10B981; font-size: 11px;'>Bağlı</div>
                </div>
                <div style='background: rgba(255,255,255,0.03); padding: 15px; border-radius: 12px; border: 1px solid #222;'>
                    <div style='font-size: 12px; color: #888;'>ÖDEME SİSTEMİ</div>
                    <div style='font-weight: 700;'>Stripe / PayPal</div>
                    <div style='color: #10B981; font-size: 11px;'>Doğrulandı</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 💸 Doların Yolculuğu")
        st.info("Müşteri Ödemesi (Stripe) ➔ US Banka Hesabı (Mercury) ➔ TR Banka Hesabı")
        
        st.markdown("---")
        st.markdown("#### 📄 Yasal Belgeler")
        belgeler = ["Articles of Organization", "Operating Agreement", "EIN Confirmation (CP575)", "Certificate of Good Standing"]
        for b in belgeler:
            st.button(f"📥 {b}", key=b, use_container_width=True)

    with right:
        st.markdown("### 📍 Şirket Bilgileri")
        st.markdown("""
        <div class='llc-card'>
            <div style='margin-bottom: 15px;'>
                <div style='font-size: 11px; color: #888;'>RESMİ İŞ ADRESİ</div>
                <div style='font-size: 14px;'>1309 Coffeen Avenue STE 1200,<br>Sheridan, Wyoming 82801</div>
            </div>
            <div style='border-top: 1px solid #222; padding-top: 15px;'>
                <div style='font-size: 11px; color: #888;'>EYALET AVANTAJI</div>
                <div style='font-size: 14px; color: #C5A059;'>%0 Eyalet Gelir Vergisi (Wyoming)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🛡️ Compliance & Uyumluluk")
        compliance = {
            "Yıllık Rapor (Annual Report)": "1 Mayıs 2026",
            "Federal Vergi Beyanı (Form 1120)": "15 Nisan 2026",
            "BOI Raporlaması": "Tamamlandı"
        }
        for task, date in compliance.items():
            st.write(f"✅ {task} : **{date}**")

    st.markdown("---")
    st.caption("Artificial Staff LLC | Legal & Compliance Division v4.2")
