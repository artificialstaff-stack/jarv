import streamlit as st
import data

def render_forms():
    st.title("📝 Talep ve İşlem Formları")
    
    tab1, tab2 = st.tabs(["📦 Yeni Sevkiyat", "🔧 Teknik Destek"])
    
    with tab1:
        with st.form("shipment_form"):
            st.text_input("Koli Adedi")
            st.date_input("Gönderim Tarihi")
            st.text_area("Notlar")
            if st.form_submit_button("Sevkiyat Oluştur"):
                data.log_activity("Yeni sevkiyat talebi oluşturuldu")
                st.success("Talebiniz alındı!")
