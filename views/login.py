import streamlit as st
import time
import random

# ==============================================================================
# ⚙️ 1. SAYFA AYARLARI (ZORUNLU - EN BAŞTA)
# ==============================================================================
st.set_page_config(
    page_title="ARTIS - Giriş",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 🖌️ 2. CSS - AGRESİF STİL (SCROLL ENGELLEME)
# ==============================================================================
def inject_css(bg_image):
    st.markdown(f"""
    <style>
        /* A. SAYFAYI KİLİTLE (SCROLL YOK) */
        .stApp {{
            overflow: hidden !important;
            height: 100vh !important;
        }}
        
        /* B. STREAMLIT BOŞLUKLARINI SIFIRLA */
        .block-container {{
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            height: 100vh !important;
        }}
        
        /* Header, Footer, Sidebar GİZLE */
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}
        
        /* C. İKİ KOLONU YANYANA YAPIŞTIR (GAP SİL) */
        [data-testid="column"] {{
            padding: 0 !important;
        }}
        
        [data-testid="stHorizontalBlock"] {{
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
            justify-content: flex-end; /* Yazıyı alta it */
            padding: 60px;
            position: relative;
        }}
        
        /* Karartma Perdesi */
        .left-panel::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.2) 100%);
            z-index: 1;
        }}
        
        /* Yazı Alanı */
        .hero-text {{
            position: relative;
            z-index: 2;
            color: white;
            margin-bottom: 40px; /* Alttan biraz yukarıda kalsın */
        }}
        
        .hero-title {{
            font-size: 3.5rem; /* Yazıyı biraz küçülttüm sığsın diye */
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 15px;
            text-transform: uppercase;
        }}
        
        .hero-subtitle {{
            font-size: 1.1rem;
            color: #ccc;
            border-left: 4px solid #ff4b4b;
            padding-left: 15px;
        }}

        /* --- SAĞ PANEL (FORM) --- */
        .right-panel-wrapper {{
            height: 100vh;
            background-color: #050505; /* Simsiyah arka plan */
            display: flex;
            align-items: center; /* Dikey Ortala */
            justify-content: center; /* Yatay Ortala */
        }}
        
        /* Login Kartı */
        .login-box {{
            width: 360px; /* Daha kompakt */
            padding: 30px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(5px);
        }}
        
        .box-header {{
            font-size: 22px;
            font-weight: bold;
            color: white;
            margin-bottom: 5px;
        }}
        
        .box-sub {{
            font-size: 12px;
            color: #888;
            margin-bottom: 25px;
        }}
        
        /* Inputları Güzelleştir */
        .stTextInput input {{
            background-color: #121212 !important;
            border: 1px solid #333 !important;
            color: #fff !important;
            padding: 10px !important;
            font-size: 14px !important;
            border-radius: 8px !important;
        }}
        
        .stTextInput input:focus {{
            border-color: #ff4b4b !important;
        }}
        
        /* Link Stili (Şifremi Unuttum) */
        .forgot-link {{
            text-align: right;
            font-size: 12px;
            margin-top: 10px;
        }}
        .forgot-link a {{
            color: #666;
            text-decoration: none;
            transition: 0.3s;
        }}
        .forgot-link a:hover {{
            color: #fff;
        }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🎲 3. İÇERİK HAVUZU (GTA STYLE)
# ==============================================================================
def get_content():
    images = [
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", # Teknoloji
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Dünya
    ]
    texts = [
        {"t": "GLOBAL<br>OPERATIONS", "s": "Tüm operasyon süreçleriniz tek ekranda."},
        {"t": "MAKSİMUM<br>GÜVENLİK", "s": "Uçtan uca şifreleme ile verileriniz güvende."},
        {"t": "ARTIS<br>INTELLIGENCE", "s": "Yapay zeka destekli iş akış yönetimi."}
    ]
    return random.choice(images), random.choice(texts)

# ==============================================================================
# 🚀 4. ANA UYGULAMA
# ==============================================================================
def main():
    bg, txt = get_content()
    inject_css(bg)
    
    # EKRANI BÖL (SOL %60 - SAĞ %40)
    col1, col2 = st.columns([1.5, 1])
    
    # --- SOL TARAFI DOLDUR ---
    with col1:
        st.markdown(f"""
        <div class="left-panel">
            <div class="hero-text">
                <div class="hero-title">{txt['t']}</div>
                <div class="hero-subtitle">{txt['s']}</div>
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
            <div class="box-header">Giriş Yap</div>
            <div class="box-sub">Panel erişimi için kimliğinizi doğrulayın</div>
        """, unsafe_allow_html=True)
        
        # Form
        with st.form("login"):
            kullanici = st.text_input("Kullanıcı Adı", placeholder="admin", label_visibility="collapsed")
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True) # İnce boşluk
            sifre = st.text_input("Şifre", type="password", placeholder="••••••", label_visibility="collapsed")
            
            st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
            
            # Hatırla ve Buton
            c_chk, c_btn = st.columns([1, 1.5])
            with c_chk:
                st.checkbox("Hatırla", value=True)
            with c_btn:
                btn = st.form_submit_button("GİRİŞ", type="primary", use_container_width=True)

        # Şifremi Unuttum Linki
        st.markdown("""
            <div class="forgot-link">
                <a href="#">Şifremi Unuttum?</a>
            </div>
        </div> </div> """, unsafe_allow_html=True)

        # İşlem
        if btn:
            # Login Mantığı (Mock)
            with st.spinner(""):
                time.sleep(0.5)
            if kullanici == "admin" and sifre == "admin":
                st.success("Giriş Başarılı!")
                time.sleep(0.5)
                # st.switch_page("dashboard.py") # Sayfa yönlendirme
            else:
                st.error("Hatalı bilgi.")

if __name__ == "__main__":
    main()
