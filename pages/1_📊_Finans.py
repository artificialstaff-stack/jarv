import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logic')))
import brain

st.set_page_config(page_title="Finans", page_icon="📊", layout="wide")

# CSS
st.markdown("<style>.stApp {background-color: #343541; color: white;}</style>", unsafe_allow_html=True)

st.title("📊 Finansal Öngörü")

# KPI Kartları
c1, c2, c3 = st.columns(3)
c1.metric("Tahmini Ciro (Aylık)", "$45,000", "+24%")
c2.metric("Net Kâr Marjı", "%32", "+4%")
c3.metric("Lojistik Gideri", "$4,200", "-12%")

st.markdown("---")
st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
