import streamlit as st
import data

def render_settings():
    st.title("⚙️ Ayarlar")
    
    user = st.session_state.user_data
    
    with st.container(border=True):
        st.subheader("👤 Profil Bilgileri")
        c1, c2 = st.columns(2)
        c1.text_input("Ad Soyad", value=user['name'], disabled=True)
        c2.text_input("Marka", value=user['brand'], disabled=True)
        st.text_input("Mevcut Plan", value=user.get('plan', 'Standart'), disabled=True)

    with st.container(border=True):
        st.subheader("🔒 Güvenlik")
        st.text_input("Eski Şifre", type="password")
        st.text_input("Yeni Şifre", type="password")
        if st.button("Şifreyi Güncelle"):
            data.log_activity("Şifre değiştirildi")
            st.success("Şifreniz güncellendi.")
