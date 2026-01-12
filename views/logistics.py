import streamlit as st
import brain
def render_logistics():
    st.title("📦 Lojistik")
    st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
