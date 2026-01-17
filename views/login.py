import streamlit as st
import time

def render_login_page():
    # --- CSS: CLEAN AUTH THEME ---
    st.markdown("""
        <style>
        .stApp {
            background-color: #000000;
            height: 100vh;
        }
        header, footer { display: none !important; }
        
        .login-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 90vh; /* Centered vertically */
        }
        
        .auth-card {
            width: 100%;
            max-width: 400px;
            text-align: center;
        }
        
        .auth-title {
            font-size: 28px;
            font-weight: 600;
            color: white;
            margin-bottom: 10px;
        }
        
        .auth-sub {
            color: #888;
            font-size: 14px;
            margin-bottom: 30px;
        }

        /* Social Buttons */
        .social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 12px;
            margin-bottom: 12px;
            background-color: #1a1a1a;
            border: 1px solid #333;
            border-radius: 8px;
            color: white;
            font-size: 14px;
            cursor: pointer;
            transition: 0.2s;
        }
        .social-btn:hover {
            background-color: #252525;
            border-color: #555;
        }

        /* Divider */
        .divider {
            display: flex;
            align-items: center;
            text-align: center;
            color: #444;
            margin: 25px 0;
            font-size: 12px;
        }
        .divider::before, .divider::after {
            content: '';
            flex: 1;
            border-bottom: 1px solid #333;
        }
        .divider:not(:empty)::before { margin-right: .5em; }
        .divider:not(:empty)::after { margin-left: .5em; }

        /* Inputs */
        .stTextInput input {
            background-color: #0a0a0a !important;
            border: 1px solid #333 !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 12px !important;
        }
        .stTextInput input:focus {
            border-color: #d4af37 !important;
        }
        
        /* Main Button */
        div.stButton > button {
            background-color: #e5e5e5 !important;
            color: black !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            border: none !important;
            height: 45px !important;
            width: 100% !important;
        }
        div.stButton > button:hover {
            background-color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Layout
    c1, c2, c3 = st.columns([1, 1, 1])
    
    with c2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # Header
        st.markdown("""
            <div class="auth-card">
                <div style="font-size: 40px; margin-bottom: 20px;">👋</div>
                <div class="auth-title">Giriş yap veya kaydol</div>
                <div class="auth-sub">ARTIS ile operasyonlarını yönetmeye başla</div>
            </div>
        """, unsafe_allow_html=True)

        # Mock Social Buttons (HTML display only for UI)
        st.markdown("""
            <div class="social-btn"> <span style="margin-right:10px">G</span> Google ile devam et</div>
            <div class="social-btn"> <span style="margin-right:10px"></span> Apple ile devam et</div>
            <div class="divider">Ya da</div>
        """, unsafe_allow_html=True)

        # Login Form
        with st.form("login_form"):
            email = st.text_input("E-posta adresi", placeholder="isim@sirket.com", label_visibility="collapsed")
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            password = st.text_input("Şifre", type="password", placeholder="••••••••", label_visibility="collapsed")
            
            st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
            submit = st.form_submit_button("Devam et", use_container_width=True)

        # Login Logic
        if submit:
            if email == "admin" and password == "admin":
                st.success("Giriş Başarılı!")
                st.session_state.logged_in = True
                st.session_state.page = "Dashboard"
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Hatalı bilgi (Demo: admin / admin)")

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    render_login_page()
