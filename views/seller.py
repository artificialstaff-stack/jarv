import streamlit as st
import pandas as pd

def inject_seller_css():
    st.markdown("""
    <style>
        .seller-card {
            background: rgba(20, 20, 22, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .seller-card:hover {
            border-color: rgba(197, 160, 89, 0.3);
            transform: translateY(-2px);
        }
        .channel-badge {
            padding: 4px 12px;
            border-radius: 8px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
        }
        .active-status { background: rgba(16, 185, 129, 0.1); color: #10B981; }
        .pending-status { background: rgba(245, 158, 11, 0.1); color: #F59E0B; }
    </style>
    """, unsafe_allow_html=True)

def render():
    inject_seller_css()
    
    # Header: Multi-Channel Management
    st.markdown("""
        <div style='margin-bottom: 35px;'>
            <h1 style='font-size: 2.5rem; font-weight: 800;'>🏪 Pazaryeri Yönetimi</h1>
            <p style='color: #888;'>Amazon, Etsy ve Walmart mağazalarınızın merkezi büyüme ve operasyon paneli.</p>
        </div>
    """, unsafe_allow_html=True)

    # Üst Metrikler: A9 Algoritma & SEO Performansı
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown("""
            <div class='seller-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>A9 SEO SKORU</div>
                <div style='font-size: 2.5rem; font-weight: 800; color: #fff;'>92<span style='font-size: 1rem; color: #34D399;'>/100</span></div>
                <div style='color: #34D399; font-size: 0.8rem;'>● Listing Optimizasyonu Tamam</div>
            </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
            <div class='seller-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>REKLAM VERİMLİLİĞİ (ROAS)</div>
                <div style='font-size: 2.5rem; font-weight: 800; color: #fff;'>4.8x</div>
                <div style='color: #34D399; font-size: 0.8rem;'>● PPC Kampanyaları Optimize Edildi</div>
            </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
            <div class='seller-card'>
                <div style='color: #888; font-size: 0.8rem; font-weight: 600;'>DÖNÜŞÜM ORANI (CR)</div>
                <div style='font-size: 2.5rem; font-weight: 800; color: #fff;'>%18.4</div>
                <div style='color: #A78BFA; font-size: 0.8rem;'>● A+ Content Etkisi: +%15</div>
            </div>
        """, unsafe_allow_html=True)

    # Kanal Durumları ve Büyüme Taktikleri
    left, right = st.columns([1, 1.2], gap="large")

    with left:
        st.markdown("### 🌐 Aktif Kanallar")
        channels = [
            {"name": "Amazon US", "status": "Aktif", "type": "active-status", "brand": "Brand Registry Tamam"},
            {"name": "Etsy Global", "status": "Aktif", "type": "active-status", "brand": "Star Seller Adayı"},
            {"name": "Walmart", "status": "Onay Bekliyor", "type": "pending-status", "brand": "Kategori Başvurusu Yapıldı"}
        ]
        
        for c in channels:
            st.markdown(f"""
                <div class='seller-card' style='padding: 18px;'>
                    <div style='display: flex; justify-content: space-between; align-items: center;'>
                        <div style='font-weight: 700; color: #fff;'>{c['name']}</div>
                        <span class='channel-badge {c['type']}'>{c['status']}</span>
                    </div>
                    <div style='font-size: 12px; color: #C5A059; margin-top: 8px;'>{c['brand']}</div>
                </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown("### 🚀 Satış Artırma & SEO")
        with st.expander("🔍 A9 Algorithm & SEO", expanded=True):
            st.write("Amerikalıların aradığı İngilizce anahtar kelimelerle başlık ve açıklama optimizasyonu.")
            st.caption("Fayda: Organik sıralamada ilk sayfa hedefi.")

        with st.expander("🖼️ A+ / Enhanced Content"):
            st.write("Ürün sayfasında dönüşüm oranını artıran görsel hikayeleştirme ve modül kurulumları.")
            st.caption("Durum: Tüm SKU'lar için yayında.")

        with st.expander("📣 PPC & Reklam Yönetimi"):
            st.write("Düşük ACOS ve yüksek satış hacmi odaklı sponsorlu ürün reklamları.")
            st.caption("Strateji: Keyword Harvester Bot aktif.")

    # Alt Bilgi
    st.markdown("---")
    st.caption("Artificial Staff LLC | Marketplace Growth Division v4.2")
