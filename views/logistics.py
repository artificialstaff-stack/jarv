import streamlit as st
import brain

def render_logistics():
    st.title("📦 Lojistik ve Sevkiyat")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
    
    with col2:
        st.success("Depo Durumu: MÜSAİT")
        st.info("Sıradaki Sevkiyat: 2 Gün")
        with st.container(border=True):
            st.markdown("### 📍 Canlı Konum")
            st.write("Konteyner ID: **TR-8821**")
            st.write("Konum: **Atlantik Okyanusu**")
            st.write("Tahmini Varış: **14 Ocak**")
