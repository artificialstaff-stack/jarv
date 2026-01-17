import streamlit as st
import time

def render_login_page():
    # --- CSS: AUTH CARD THEME ---
    st.markdown("""
        <style>
        .stApp {
            background-color: #000000;
        }
        
        /* Kartın Ortalanması */
        .auth-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 90vh; /* Dikey ortalama */
            width: 100%;
        }
        
        .auth-card {
            width: 400px;
            padding: 20px;
            text-align: center;
        }

        /* Başlıklar */
        .auth-icon {
            font-size: 40px;
            margin-bottom: 20px;
        }
        .auth-header {
            color: #ffffff;
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 10px;
            font-family: sans-serif;
        }
        .auth-sub {
            color: #888;
            font-size: 14px;
            margin-bottom: 30px;
        }

        /* Sosyal Butonlar (Görünüm) */
        .social-button {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            background-color: #1a1a1a;
            color: white;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #333;
            margin-bottom: 12px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s;
        }
        .social-button:hover {
            background-color: #252525;
        }
        .social-icon { margin-right: 10px; }

        /* Ayırıcı */
        .divider {
            display: flex;
            align-items: center;
            text-align: center;
            color: #444;
            font-size: 12px;
            margin: 20px 0;
        }
        .divider::before, .divider::after {
            content: '';
            flex: 1;
            border-bottom: 1px solid #333;
        }
        .divider::before { margin-right: .5em; }
        .divider::after { margin-left: .5em; }

        /* Form Elemanları */
        div[data-testid="stTextInput"] input {
            background-color: #0a0a0a !important;
            border: 1px solid #333 !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 12px !important;
        }
        div[data-testid="stTextInput"] input:focus {
            border-color: #d4af37 !important;
            box-shadow: 0 0 0 1px #d4af37;
        }
        
        /* Ana Buton */
        div[data-testid="stFormSubmitButton"] button {
            background-color: #e5e5e5 !important;
            color: black !important;
            border: none !important;
            width: 100% !important;
            border-radius: 8px !important;
            padding: 12px !important;
            font-weight: bold !important;
        }
        div[data-testid="stFormSubmitButton"] button:hover {
            background-color: #ffffff !important;
        }

        /* Linkler */
        .footer-links {
            margin-top: 20px;
            font-size: 12px;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    # Ortalamak için kolon yapısı
    c1, c2, c3 = st.columns([1, 1, 1])

    with c2:
        # HTML Kart Yapısı
        st.markdown("""
            <div class="auth-container">
                <div class="auth-card">
                    <div class="auth-icon">👋</div>
                    <div class="auth-header">Giriş yap veya kaydol</div>
                    <div class="auth-sub">ARTIS ile yaratmaya başlayın</div>
                    
                    <div class="social-button">
                        <span class="social-icon">G</span> Google ile devam et
                    </div>
                    <div class="social-button">
                        <span class="social-icon"></span> Apple ile devam et
                    </div>
                    
                    <div class="divider">Ya da</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Form (Python Mantığı)
        # CSS ile yukarıdaki HTML kutusunun içine görsel olarak "monte" edilmiş gibi duracak
        with st.form("login_form"):
            email = st.text_input("email", placeholder="E-posta adresinizi girin", label_visibility="collapsed")
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            password = st.text_input("password", placeholder="Şifre", type="password", label_visibility="collapsed")
            
            st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
            
            # Bu buton CSS ile gri/beyaz yapıldı
            submit = st.form_submit_button("Devam et", use_container_width=True)

        # Giriş Mantığı
        if submit:
            if email == "admin" and password == "admin":
                st.success("Başarılı")
                st.session_state.logged_in = True
                st.session_state.page = "Dashboard"
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Hatalı giriş (Demo: admin/admin)")

        st.markdown("""
            <div style="text-align:center; font-size:11px; color:#444; margin-top:20px;">
                Hizmet Şartları ve Gizlilik Politikası
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_login_page()
