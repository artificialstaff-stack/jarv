import streamlit as st
import time
import random

# ==============================================================================
# 1. TEMEL AYARLAR (EN BAŞTA)
# ==============================================================================
try:
    st.set_page_config(page_title="ARTIS Login", layout="wide", initial_sidebar_state="collapsed")
except:
    pass

# ==============================================================================
# 2. VERİTABANI (MOCK)
# ==============================================================================
USERS = {
    "admin": {"pass": "admin", "name": "Yönetici", "role": "admin"},
    "demo": {"pass": "1234", "name": "Demo User", "role": "user"}
}

# ==============================================================================
# 3. CSS "RESET" & TASARIM (AGRESİF STİL)
# ==============================================================================
def load_css(bg_url):
    st.markdown(f"""
    <style>
        /* --- A. SAYFA YAPISINI SIFIRLA (SCROLL ENGELLEME) --- */
        
        /* 1. Tüm sayfa kapsayıcısını ekrana kilitle */
        .stApp {{
            overflow: hidden !important;
            height: 100vh !important;
            background-color: #0E1117; /* Sağ tarafın rengi */
        }}
        
        /* 2. Streamlit'in varsayılan boşluklarını YOK ET */
        .block-container {{
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            height: 100vh !important;
        }}
        
        /* 3. Header, Footer ve Sidebar'ı tamamen kaldır */
        header, footer, section[data-testid="stSidebar"] {{
            display: none !important;
        }}

        /* --- B. KOLON YAPISI (SOL VE SAĞ PANEL) --- */
        
        /* Kolonlar arası boşluğu sil */
        div[data-testid="column"] {{
            padding: 0 !important;
        }}
        
        div[data-testid="stHorizontalBlock"] {{
            gap: 0 !important;
        }}

        /* --- SOL TARAF: GÖRSEL ALANI --- */
        .split-left {{
            height: 100vh;
            width: 100%;
            background-image: url('{bg_url}');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: flex-end; /* Yazıyı aşağı it */
            padding: 60px;
            position: relative;
        }}
        
        /* Resim üzerine siyah perde */
        .split-left::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.2));
            z-index: 1;
        }}
        
        /* Yazı Grubu */
        .text-group {{
            position: relative;
            z-index: 2;
            margin-bottom: 20px;
        }}
        
        .brand-title {{
            font-size: 80px;
            font-weight: 900;
            color: white;
            line-height: 0.9;
            margin-bottom: 20px;
            letter-spacing: -2px;
        }}
        
        .brand-subtitle {{
            font-size: 18px;
            color: #d0d0d0;
            border-left: 5px solid #FF4B4B;
            padding-left: 20px;
            max-width: 500px;
        }}

        /* --- SAĞ TARAF: LOGIN ALANI --- */
        /* Bu class'ı sağdaki div'e vereceğiz */
        .login-container {{
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            background-color: #0E1117;
            padding: 0 50px;
        }}
        
        /* Giriş Kartı */
        .auth-card {{
            width: 100%;
            max-width: 400px;
            padding: 20px;
        }}
        
        .login-header {{
            font-size: 32px;
            font-weight: bold;
            color: white;
            margin-bottom: 10px;
        }}
        
        .login-desc {{
            color: #6c757d;
            margin-bottom: 40px;
            font-size: 14px;
        }}

        /* --- INPUT ALANLARI --- */
        .stTextInput input {{
            background-color: #161b22 !important;
            border: 1px solid #30363d !important;
            color: white !important;
            height: 50px !important;
            border-radius: 6px !important;
        }}
        
        .stTextInput input:focus {{
            border-color: #FF4B4B !important;
        }}
        
        /* Buton */
        .stButton button {{
            background-color: #FF4B4B !important;
            color: white !important;
            border: none !important;
            height: 50px !important;
            font-weight: bold !important;
            border-radius: 6px !important;
            margin-top: 10px;
        }}
        .stButton button:hover {{
            background-color: #ff3333 !important;
        }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. İÇERİK YÖNETİMİ
# ==============================================================================
def get_content():
    images = [
        "https://images.unsplash.com/photo-1620641788421-7f1c338e420a?q=80&w=2070&auto=format&fit=crop", # Dark Cyber
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", # Tech Room
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=2070&auto=format&fit=crop"  # Matrix Code
    ]
    texts = [
        {"h": "ARTIS<br>CORE", "p": "Yeni nesil operasyon yönetim sistemi."},
        {"h": "FUTURE<br>READY", "p": "Verileriniz yapay zeka ile işleniyor."},
        {"h": "SECURE<br>ACCESS", "p": "Uçtan uca şifreli bağlantı güvenliği."}
    ]
    return random.choice(images), random.choice(texts)

# ==============================================================================
# 5. ANA EKRAN (RENDER)
# ==============================================================================
def render_login_page():
    
    # Verileri al
    bg_img, content = get_content()
    load_css(bg_img)
    
    # EKRANI İKİYE BÖL (SOL %65 - SAĞ %35)
    # gap="small" diyerek Streamlit'in varsayılan boşluğunu en aza indiriyoruz, CSS gerisini hallediyor.
    col1, col2 = st.columns([1.7, 1], gap="small")
    
    # --- SOL KOLON (GÖRSEL) ---
    with col1:
        st.markdown(f"""
        <div class="split-left">
            <div class="text-group">
                <div class="brand-title">{content['h']}</div>
                <div class="brand-subtitle">{content['p']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    # --- SAĞ KOLON (FORM) ---
    with col2:
        # Sağ tarafı ortalamak için boş konteyner hilesi yerine,
        # CSS ile özelleştirilmiş bir alan yaratıyoruz.
        
        st.markdown('<div class="login-container"><div class="auth-card">', unsafe_allow_html=True)
        
        st.markdown('<div class="login-header">Giriş Yap</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-desc">Hesabınıza erişmek için bilgilerinizi girin.</div>', unsafe_allow_html=True)
        
        # Form
        username = st.text_input("Kullanıcı Adı", placeholder="admin", label_visibility="collapsed")
        password = st.text_input("Şifre", type="password", placeholder="••••••••", label_visibility="collapsed")
        
        # Checkbox ve Şifremi Unuttum (Yan Yana)
        c1, c2 = st.columns([1,1])
        with c1:
            st.checkbox("Beni Hatırla")
        with c2:
            st.markdown('<div style="text-align:right; padding-top:5px;"><a href="#" style="color:#6c757d; text-decoration:none; font-size:14px;">Şifremi Unuttum</a></div>', unsafe_allow_html=True)

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        # Buton
        if st.button("GİRİŞ YAP", use_container_width=True):
            user = USERS.get(username)
            if user and user['pass'] == password:
                st.success("Giriş yapılıyor...")
                st.session_state.logged_in = True
                time.sleep(1)
                st.rerun()
            else:
                st.error("Hatalı kullanıcı adı veya şifre")

        st.markdown('</div></div>', unsafe_allow_html=True) # Divleri kapat

# ==============================================================================
# 6. ÇALIŞTIRMA (APP.PY TARAFINDAN ÇAĞRILACAK)
# ==============================================================================
if __name__ == "__main__":
    render_login_page()
