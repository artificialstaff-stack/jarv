import streamlit as st
import time
import random

# ==============================================================================
# ⚙️ 1. SAYFA YAPILANDIRMASI (ZORUNLU - EN BAŞTA)
# ==============================================================================
try:
    st.set_page_config(page_title="ARTIS - Giriş", layout="wide", initial_sidebar_state="collapsed")
except:
    pass

# ==============================================================================
# 🖌️ 2. CSS - AGRESIF NO-SCROLL (KAYDIRMA ENGELLEYİCİ)
# ==============================================================================
def inject_css(bg_image):
    st.markdown(f"""
    <style>
        /* 1. SCROLLBAR'I TAMAMEN GİZLE (Chrome, Safari, Edge) */
        ::-webkit-scrollbar {{
            display: none;
        }}
        
        /* Firefox için Scrollbar gizle */
        .stApp {{
            scrollbar-width: none;
            overflow: hidden !important; /* Kaydırmayı kitle */
            height: 100vh !important;
        }}

        /* 2. STREAMLIT'İN İNATÇI ÜST BOŞLUĞUNU YOK ET */
        .block-container {{
            padding-top: 0rem !important; /* En önemli satır burası */
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            margin: 0 !important;
            max-width: 100% !important;
        }}
        
        /* 3. HEADER, FOOTER, SIDEBAR'I YOK ET */
        header {{ display: none !important; visibility: hidden !important; }}
        footer {{ display: none !important; }}
        [data-testid="stSidebar"] {{ display: none !important; }}
        
        /* 4. KOLONLAR ARASI BOŞLUKLARI SIFIRLA */
        [data-testid="column"] {{
            padding: 0 !important;
            overflow: hidden !important;
        }}
        
        div[data-testid="stVerticalBlock"] {{
            gap: 0 !important;
        }}

        /* --- SOL PANEL (RESİM) --- */
        .left-panel {{
            height: 100vh;
            width: 100%;
            background-image: url('{bg_image}');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 80px;
            position: relative;
        }}
        
        .left-panel::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.1) 100%);
            z-index: 1;
        }}
        
        /* Animasyonlu Yazı */
        .hero-content {{
            position: relative;
            z-index: 2;
            animation: slideUp 1.2s ease-out;
        }}
        
        .hero-title {{
            font-size: 3.5rem; /* Biraz küçülttüm sığması garanti olsun */
            font-weight: 900;
            line-height: 1;
            margin-bottom: 15px;
            text-transform: uppercase;
            color: #ffffff;
            text-shadow: 0px 10px 30px rgba(0,0,0,0.8);
        }}
        
        .hero-subtitle {{
            font-size: 1.1rem;
            color: #d1d5db;
            border-left: 5px solid #FF4B4B;
            padding-left: 15px;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(90deg, rgba(0,0,0,0.6), transparent);
        }}

        @keyframes slideUp {{
            from {{ opacity: 0; transform: translateY(50px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* --- SAĞ PANEL (FORM) --- */
        .right-panel-wrapper {{
            height: 100vh;
            width: 100%;
            background-color: #09090b;
            display: flex;
            align-items: center; /* Dikey Ortala */
            justify-content: center; /* Yatay Ortala */
        }}
        
        .login-box {{
            width: 360px; /* Kompakt genişlik */
            padding: 40px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            backdrop-filter: blur(10px);
        }}
        
        .box-title {{
            font-size: 24px;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 5px;
        }}
        
        .box-desc {{
            font-size: 12px;
            color: #71717a;
            text-align: center;
            margin-bottom: 25px;
        }}
        
        /* Input Stilleri */
        .stTextInput input {{
            background-color: #18181b !important;
            border: 1px solid #27272a !important;
            color: white !important;
            padding: 10px 15px !important;
            border-radius: 10px !important;
            font-size: 14px !important;
        }}
        
        .stTextInput input:focus {{
            border-color: #FF4B4B !important;
            box-shadow: 0 0 0 2px rgba(255, 75, 75, 0.2) !important;
        }}

        /* Şifremi Unuttum Linki */
        .forgot-pass {{
            text-align: right;
            margin-top: 10px;
            font-size: 11px;
        }}
        .forgot-pass a {{
            color: #71717a;
            text-decoration: none;
            transition: 0.3s;
        }}
        .forgot-pass a:hover {{
            color: #FF4B4B;
        }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🎲 3. İÇERİK HAVUZU
# ==============================================================================
def get_gta_content():
    images = [
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", # Cyberpunk
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Network
        "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=2070&auto=format&fit=crop", # Chip
    ]
    texts = [
        {"t": "GLOBAL<br>OPERATIONS", "s": "Tüm operasyon süreçleriniz tek bir panelde."},
        {"t": "MAKSİMUM<br>GÜVENLİK", "s": "Verileriniz uçtan uca şifreleme ile korunmaktadır."},
        {"t": "ARTIS<br>INTELLIGENCE", "s": "Yapay zeka motoru ile %40 verimlilik artışı."}
    ]
    return random.choice(images), random.choice(texts)

# ==============================================================================
# 🚀 4. RENDER FONKSİYONU
# ==============================================================================
def render_login_page():
    
    # İçerik ve CSS Yükle
    bg_image, content = get_gta_content()
    inject_css(bg_image)
    
    # EKRANI İKİYE BÖL: Sol (%60), Sağ (%40)
    col1, col2 = st.columns([1.6, 1])
    
    # --- SOL TARAFI DOLDUR ---
    with col1:
        st.markdown(f"""
        <div class="left-panel">
            <div class="hero-content">
                <div class="hero-title">{content['t']}</div>
                <div class="hero-subtitle">{content['s']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- SAĞ TARAFI DOLDUR ---
    with col2:
        # Wrapper div ile formu tam ortalıyoruz
        st.markdown('<div class="right-panel-wrapper">', unsafe_allow_html=True)
        
        # Giriş Kutusunu Başlat
        st.markdown(f"""
        <div class="login-box">
            <div class="box-title">Giriş Yap</div>
            <div class="box-desc">Panel erişimi için kimliğinizi doğrulayın</div>
        """, unsafe_allow_html=True)
        
        # Form
        with st.form("login_form", border=False):
            username = st.text_input("Kullanıcı Adı", placeholder="admin", label_visibility="collapsed")
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            password = st.text_input("Şifre", type="password", placeholder="••••••••", label_visibility="collapsed")
            
            st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
            
            # Hatırla ve Buton Düzeni
            col_chk, col_btn = st.columns([1, 1.5])
            with col_chk:
                st.checkbox("Hatırla", value=True)
            with col_btn:
                submit_btn = st.form_submit_button("GİRİŞ", type="primary", use_container_width=True)

        # Şifremi Unuttum Linki
        st.markdown("""
            <div class="forgot-pass">
                <a href="#">Şifremi Unuttum?</a>
            </div>
        </div> </div> """, unsafe_allow_html=True)

        # İşlem Mantığı
        if submit_btn:
            if username == "admin" and password == "admin":
                with st.spinner("Oturum açılıyor..."):
                    time.sleep(1)
                st.success("Giriş Başarılı!")
                st.session_state.logged_in = True
                st.session_state.username = username
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Hatalı kullanıcı adı veya şifre.")

# Test için
if __name__ == "__main__":
    render_login_page()
