import streamlit as st

def render():
    st.markdown("## 🚀 AI Lead Gen & B2B Satış")
    st.info("AI Ajanlarımız ABD pazarında sizin için aktif olarak alıcı buluyor.")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Taranan Şirket", "4,250", "USA")
    m2.metric("Atılan Mailler", "850", "Yapay Zeka")
    m3.metric("Sıcak Randevular", "12", "Pipeline")
    
    st.markdown("### 📊 Satış Hunisi (Pipeline)")
    st.progress(85, text="Data Scraping (Tamamlandı)")
    st.progress(40, text="Outreach (Devam Ediyor)")
