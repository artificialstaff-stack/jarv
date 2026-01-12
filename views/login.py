import streamlit as st
import time
import sys
import os

# Logic import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logic')))
import data

def render_login_page():
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center;'>ARTIS <span style='color:#1F6FEB'>.OS</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8B949E;'>Authorized Personnel Only</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            username = st.text_input("Kullanıcı Adı")
            password = st.text_input("Şifre", type="password")
            
            if st.button("Giriş Yap", use_container_width=True):
                user = data.verify_user(username, password)
                if user:
                    st.session_state.user_data = user
                    st.session_state.logged_in = True
                    st.toast(f"Hoş geldiniz, {user['name']}", icon="🔓")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Erişim reddedildi.")
