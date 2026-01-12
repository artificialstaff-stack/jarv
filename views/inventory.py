import streamlit as st
import pandas as pd

def render_inventory():
    st.title("📋 Envanter")
    df = pd.DataFrame({"Ürün": ["İpek Eşarp", "Pamuk", "Çanta"], "Stok": [1200, 5000, 350], "Durum": ["✅", "✅", "⚠️"]})
    st.dataframe(df, use_container_width=True)
    with st.expander("➕ Ürün Ekle"):
        st.text_input("Ad")
        st.button("Ekle")
