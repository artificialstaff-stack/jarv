import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logic')))
import brain

st.set_page_config(page_title="Lojistik", page_icon="✈️", layout="wide")

# CSS
st.markdown("<style>.stApp {background-color: #343541; color: white;}</style>", unsafe_allow_html=True)

st.title("✈️ Global Lojistik Ağı")
st.info("Rota: İstanbul (IST) ➔ Washington DC (IAD)")

st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

st.markdown("""
### 📦 Depo Durumu (Washington DC)
* **Kapasite:** %12 Dolu
* **Son Giriş:** 2 Saat Önce
* **Gümrük:** ✅ Sorunsuz
""")
