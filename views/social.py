import streamlit as st

def inject_social_css():
    st.markdown("""
    <style>
        .social-card {
            background: rgba(20, 20, 22, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .platform-pill {
            background: rgba(139, 92, 246, 0.1);
            color: #A78BFA;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            border: 1px solid rgba(139, 92, 246, 0.2);
            margin-right: 8px;
        }
        .ugc-badge {
            background: rgba(16, 185, 129, 0.1);
            color: #10B981;
            padding: 2px 8px;
            border-radius: 6px;
            font-size: 10px;
            font-weight: 800;
        }
    </style>
    """, unsafe_allow_html=True)

def render():
    inject_social_css()
    
    # Header: Brand Building
    st.markdown("""
        <div style='margin-bottom: 35px;'>
            <h1 style='font-size: 2.5rem; font-weight: 800;'>📱 Sosyal Medya Yönetimi</h1>
            <p style='color: #888;'>Marka kimliğinizi global trendlerle birleştirerek Amerikan pazarında topluluk inşa ediyoruz.</p>
        </div>
    """, unsafe_allow_html=True)

    # Üst Metrikler: Erişebilirlik ve Etkileşim
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown("""
            <div class='social-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>TOPLAM ERİŞİM (REACH)</div>
                <div style='font-size: 2.5rem; font-weight: 800; color: #fff;'>1.2M</div>
                <div style='color: #34D399; font-size: 0.8rem;'>● Viral Yayılım Aktif</div>
            </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
            <div class='social-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>ETKİLEŞİM ORANI (ERR)</div>
                <div style='font-size: 2.5rem; font-weight: 800; color: #fff;'>%6.4</div>
                <div style='color: #34D399; font-size: 0.8rem;'>● Topluluk Bağlılığı Yüksek</div>
            </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
            <div class='social-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>AKTİF UGC İÇERİĞİ</div>
                <div style='font-size: 2.5rem; font-weight: 800; color: #fff;'>124</div>
                <div style='color: #C5A059; font-size: 0.8rem;'>● Tüketici Kanıtı Güçlü</div>
            </div>
        """, unsafe_allow_html=True)

    # Ana İçerik: Strateji ve Influencer
    left, right = st.columns([1.2, 1], gap="large")

    with left:
        st.markdown("### 🎨 Marka Hikayeleştirme & Görsel Dil")
        
        with st.expander("💎 Premium İçerik Üretimi", expanded=True):
            st.write("Amerikan estetik algısına uygun, yüksek kaliteli fotoğraf ve video prodüksiyonu.")
            st.markdown("<span class='platform-pill'>Instagram</span><span class='platform-pill'>Pinterest</span>", unsafe_allow_html=True)

        with st.expander("✍️ İngilizce Copywriting"):
            st.write("Kültürel nüanslara, Amerikan argosuna ve yerel deyimlere hakim metin yazımı.")
            st.caption("Fayda: Yerli bir marka algısı oluşturma.")

        with st.expander("🎥 Viral Reels & TikTok Stratejisi"):
            st.write("Trend sesler ve 'hook' odaklı kurgularla organik büyümeyi patlatan kısa videolar.")
            st.markdown("<span class='platform-pill'>TikTok</span><span class='platform-pill'>Reels</span>", unsafe_allow_html=True)

    with right:
        st.markdown("### 🤝 Influencer & Topluluk")
        
        st.markdown("""
        <div class='social-card'>
            <div style='font-weight: 700; color: #fff; margin-bottom: 15px;'>Micro-Influencer Ağı</div>
            <p style='color: #888; font-size: 13px;'>ABD pazarında niş kitlelere sahip 15+ içerik üreticisi ile güven transferi sağlanıyor.</p>
            <div style='border-top: 1px solid #222; margin: 15px 0; padding-top: 15px;'>
                <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
                    <span style='font-size: 13px;'>UGC Videoları</span>
                    <span class='ugc-badge'>24 YENİ</span>
                </div>
                <div style='display: flex; justify-content: space-between;'>
                    <span style='font-size: 13px;'>Yorum Yanıtlama</span>
                    <span style='color: #10B981; font-size: 12px;'>7/24 AKTİF</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📊 Detaylı İçerik Takvimini Aç", use_container_width=True):
            st.info("Ocak 2026 içerik takvimi hazırlanıyor...")

    st.markdown("---")
    st.caption("Artificial Staff LLC | Social & Creative Division v4.2")
