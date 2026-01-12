import streamlit as st
import pandas as pd
import data

def render_inventory():
    st.title("📋 Envanter Yönetimi")
    
    col_act, col_search = st.columns([1, 1])
    with col_act:
        if st.button("➕ Yeni Ürün Ekle"):
            data.log_activity("Yeni ürün formu açıldı")
            st.toast("Form modülü yükleniyor...", icon="⏳")
    
    # Tablo
    df = pd.DataFrame({
        "SKU": ["TR-001", "TR-002", "TR-003", "TR-004"],
        "Ürün Adı": ["İpek Eşarp", "Organik Pamuk", "Deri Çanta", "Seramik Kupa"],
        "Stok": [1200, 5000, 350, 0],
        "Durum": ["✅ Yeterli", "✅ Yeterli", "⚠️ Kritik", "❌ Tükendi"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
