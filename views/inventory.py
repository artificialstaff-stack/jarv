import streamlit as st
import pandas as pd

def render_inventory():
    st.title("📋 Envanter Yönetimi")
    
    # Üst Özet
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Toplam SKU", "48", "+2")
    kpi2.metric("Toplam Değer", "$142,000", "+$12k")
    kpi3.metric("Stok Sağlığı", "%92", "Mükemmel")
    
    st.markdown("---")
    
    # Filtreleme Alanı
    c_filter, c_add = st.columns([3, 1])
    with c_filter:
        st.text_input("🔍 Ürün Ara...", placeholder="SKU veya Ürün Adı girin")
    with c_add:
        st.markdown("<br>", unsafe_allow_html=True) # Hizalama boşluğu
        if st.button("➕ Yeni Ürün", use_container_width=True):
            st.toast("Ürün ekleme paneli açılıyor...", icon="📦")
    
    # Gelişmiş Tablo
    data = {
        "Görsel": ["👕", "🧣", "👜", "🧢", "🧴"],
        "SKU": ["TR-101", "TR-102", "TR-103", "TR-104", "TR-105"],
        "Ürün Adı": ["Pamuklu T-Shirt", "İpek Eşarp", "Deri Çanta", "Logolu Şapka", "Organik Losyon"],
        "Stok": [1200, 4500, 45, 800, 2000],
        "Lokasyon": ["Raf A1", "Raf B3", "Raf C1", "Raf A2", "Raf D4"],
        "Durum": ["✅ Müsait", "✅ Müsait", "⚠️ Kritik", "✅ Müsait", "✅ Müsait"]
    }
    df = pd.DataFrame(data)
    
    st.dataframe(
        df, 
        use_container_width=True, 
        column_config={
            "Stok": st.column_config.ProgressColumn("Stok Seviyesi", min_value=0, max_value=5000, format="%d Adet"),
        },
        hide_index=True
    )
