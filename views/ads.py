import streamlit as st

def inject_ads_css():
    st.markdown("""
    <style>
        .ads-card {
            background: rgba(20, 20, 22, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .ads-card:hover {
            border-color: rgba(59, 130, 246, 0.3);
            transform: translateY(-2px);
        }
        .roi-badge {
            background: rgba(59, 130, 246, 0.1);
            color: #3B82F6;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }
        .metric-sub {
            color: #888;
            font-size: 12px;
            margin-top: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

def render():
    inject_ads_css()
    
    # Header: Performance Marketing
    st.markdown("""
        <div style='margin-bottom: 35px;'>
            <h1 style='font-size: 2.5rem; font-weight: 800;'>🎯 Reklam Yönetimi</h1>
            <p style='color: #888;'>Bütçenizi harcamaya değil, yatırıma dönüştürüyoruz. Meta ve Google'da nokta atışı hedefleme.</p>
        </div>
    """, unsafe_allow_html=True)

    # Üst Metrikler: Karlılık ve ROI
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown("""
            <div class='ads-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>REKLAM GETİRİSİ (ROAS)</div>
                <div style='font-size: 2.5rem; font-weight: 800; color: #fff;'>5.2x</div>
                <div class='metric-sub'>Her 1$ harcama için kazanılan ciro.</div>
            </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
            <div class='ads-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>EDİNME MALİYETİ (CPA)</div>
                <div style='font-size: 2.5rem; font-weight: 800; color: #fff;'>$14.50</div>
                <div class='metric-sub'>Bir yeni müşteri kazanma maliyeti.</div>
            </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
            <div class='ads-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>MÜŞTERİ ÖMRÜ DEĞERİ (LTV)</div>
                <div style='font-size: 2.5rem; font-weight: 800; color: #fff;'>$180</div>
                <div class='metric-sub'>Sadık müşteri yaratma odaklı verimlilik.</div>
            </div>
        """, unsafe_allow_html=True)

    # Stratejik Kanallar ve Kampanyalar
    left, right = st.columns([1.2, 1], gap="large")

    with left:
        st.markdown("### 📊 Kanal Stratejileri")
        
        with st.expander("🔵 Meta Ads (FB & Instagram)", expanded=True):
            st.write("İlgi alanı ve davranışsal hedefleme ile doğru kitleyi bulma stratejisi aktif.")
            st.markdown("<span class='roi-badge'>Erişim Odaklı</span>", unsafe_allow_html=True)

        with st.expander("🔴 Google Ads (Search & Shopping)"):
            st.write("Satın alma niyeti (High-Intent) yüksek aramaları yakalayan özel kampanya kurguları.")
            st.markdown("<span class='roi-badge'>Niyet Odaklı</span>", unsafe_allow_html=True)

        with st.expander("🔄 Retargeting (Yeniden Pazarlama)"):
            st.write("Sepette ürün unutan veya siteyi inceleyen ziyaretçileri reklamlarla geri kazanma süreci.")
            st.markdown("<span class='roi-badge'>Dönüşüm Odaklı</span>", unsafe_allow_html=True)

    with right:
        st.markdown("### 💰 Bütçe Dağılımı")
        
        st.markdown("""
        <div class='ads-card'>
            <div style='font-weight: 700; color: #fff; margin-bottom: 20px;'>Aktif Bütçe Tahsisi</div>
            <div style='margin-bottom: 15px;'>
                <div style='display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 5px;'>
                    <span>Meta Ads</span><span>%55</span>
                </div>
                <div style='background: #222; height: 6px; border-radius: 3px;'>
                    <div style='background: #3B82F6; height: 6px; width: 55%; border-radius: 3px;'></div>
                </div>
            </div>
            <div style='margin-bottom: 15px;'>
                <div style='display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 5px;'>
                    <span>Google Ads</span><span>%35</span>
                </div>
                <div style='background: #222; height: 6px; border-radius: 3px;'>
                    <div style='background: #EF4444; height: 6px; width: 35%; border-radius: 3px;'></div>
                </div>
            </div>
            <div>
                <div style='display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 5px;'>
                    <span>Retargeting</span><span>%10</span>
                </div>
                <div style='background: #222; height: 6px; border-radius: 3px;'>
                    <div style='background: #10B981; height: 6px; width: 100%; border-radius: 3px;'></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📈 Detaylı ROI Raporunu İndir", use_container_width=True):
            st.success("Ocak ayı reklam performans raporu oluşturuldu.")

    st.markdown("---")
    st.caption("Artificial Staff LLC | Performance Marketing Division v4.2")
