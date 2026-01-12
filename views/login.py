import streamlit as st
import sys, os, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logic')))
import data

def render_login_page():
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br><h1 style='text-align:center;'>ARTIS <span style='color:#1F6FEB'>.OS</span></h1>", unsafe_allow_html=True)
        with st.container(border=True):
            u = st.text_input("Kullanıcı Adı")
            p = st.text_input("Şifre", type="password")
            if st.button("Giriş Yap", use_container_width=True):
                user = data.verify_user(u, p)
                if user:
                    st.session_state.user_data = user
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Hatalı giriş.")
