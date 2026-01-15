import streamlit as st
import pandas as pd

def inject_website_css():
    st.markdown("""
    <style>
        /* Modern Glassmorphism Kartları */
        .web-card {
            background: rgba(20, 20, 22, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 20px;
        }
        .tech-pill {
            background: rgba(197, 160, 89, 0.1);
            color: #C5A059;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            border: 1px solid rgba(197, 160, 89, 0.2);
            margin-right: 8px;
        }
    </style>
    """, unsafe_allow_html=True)

def render():
    inject_website_css()
    
    # Header Bölümü
    st.markdown("""
        <div style='margin-bottom: 30px;'>
            <h1 style='font-size: 2.5rem; font-weight: 800;'>🌐 Web Sitesi & UX Yönetimi</h1>
            <p style='color: #888;'>Global vitrininiz: Amerikan pazarı için optimize edilmiş, satış odaklı altyapı.</p>
        </div>
    """, unsafe_allow_html=True)

    # Üst Metrikler (Sunumdaki Teknik Veriler)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='web-card'>
                <div style='color: #34D399; font-size: 0.8rem; font-weight: 700;'>YÜKLENME HIZI</div>
                <div style='font-size: 2.5rem; font-weight: 800;'>0.4s</div>
                <div style='color: #34D399; font-size: 0.8rem;'>● Core Web Vitals Geçti</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class='web-card'>
                <div style='color: #3B82F6; font-size: 0.8rem; font-weight: 700;'>GÜVENLİK</div>
                <div style='font-size: 2.5rem; font-weight: 800;'>SSL</div>
                <div style='color: #3B82F6; font-size: 0.8rem;'>● 256-Bit Şifreleme Aktif</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class='web-card'>
                <div style='color: #A78BFA; font-size: 0.8rem; font-weight: 700;'>SEO SKORU</div>
                <div style='font-size: 2.5rem; font-weight: 800;'>98/100</div>
                <div style='color: #A78BFA; font-size: 0.8rem;'>● Semantik Kodlama Tamam</div>
            </div>
        """, unsafe_allow_html=True)

    # Ana İçerik Alanı
    left_col, right_col = st.columns([1.5, 1], gap="large")

    with left_col:
        st.markdown("### 🎨 Tasarım & Dönüşüm (UX)")
        with st.expander("🇺🇸 Amerikan Tüketici Algısı", expanded=True):
            st.write("Yerel alışkanlıklara uygun UX tasarımı ile kullanıcıların güvenini kazanıyoruz.")
            st.progress(95, text="Tüketici Güven Endeksi")
            
        with st.expander("📱 Mobil Öncelikli (Mobile-First)"):
            st.write("Trafiğin %80'ini karşılayan kusursuz mobil deneyim ve checkout süreci.")
            st.progress(92, text="Mobil Uyumluluk")

        with st.expander("🧠 Nöro-Pazarlama"):
            st.write("Satın alma kararlarını tetikleyen renk paleti ve stratejik buton yerleşimleri.")

    with right_col:
        st.markdown("### 🛠 Teknoloji Stack")
        st.markdown("""
            <div class='web-card'>
                <p>Sitenizde kullanılan modern teknolojiler:</p>
                <span class='tech-pill'>React</span>
                <span class='tech-pill'>Next.js</span>
                <span class='tech-pill'>Shopify Plus</span>
                <span class='tech-pill'>Node.js</span>
                <div style='margin-top: 20px; border-top: 1px solid #222; padding-top: 15px;'>
                    <p style='font-size: 13px; color: #888;'>Hizmet: <b>Full Enterprise Management</b></p>
                    <p style='font-size: 13px; color: #888;'>Durum: <b>Geliştirme Tamamlandı</b></p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Siteyi Canlıda Görüntüle", use_container_width=True):
            st.toast("Yönlendiriliyorsunuz...")

    # Sayfa Alt Bilgisi
    st.markdown("---")
    st.caption("Artificial Staff LLC | Web Infrastructure Division v4.2")
