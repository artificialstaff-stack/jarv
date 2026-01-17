import streamlit as st
import time
import random

# ==============================================================================
# 1. TEMEL YAPILANDIRMA
# ==============================================================================
try:
    st.set_page_config(page_title="ARTIS - Secure Access", layout="wide", initial_sidebar_state="collapsed")
except:
    pass

# ==============================================================================
# 2. İÇERİK HAVUZU (İNSANSIZ - TEKNOLOJİ & LOJİSTİK)
# ==============================================================================
def get_assets():
    # İnsan içermeyen, yüksek kaliteli teknolojik ve lojistik arka planlar
    backgrounds = [
        "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2613&auto=format&fit=crop", # Şehir/Gece/Network
        "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=2070&auto=format&fit=crop", # Çip/Devre
        "https://images.unsplash.com/photo-1558494949-ef526b0042a0?q=80&w=2070&auto=format&fit=crop", # Server Odası/Veri
        "https://images.unsplash.com/photo-1494412574643-35d324688133?q=80&w=2070&auto=format&fit=crop", # Anakart/Macro
        "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=2070&auto=format&fit=crop"  # Lojistik/Konteyner
    ]

    # Vurucu Pazar Verileri (Typewriter Efekti İçin)
    messages = [
        "► ABD E-Ticaret Pazarı 1.1 Trilyon Dolar hacmine ulaştı.",
        "► Rakipleriniz manuel süreçlerle zaman kaybederken siz öne geçin.",
        "► Lojistik maliyetlerinde %60'a varan net tasarruf imkanı.",
        "► 7/24 Otonom Sistem: Siz uyurken ARTIS çalışmaya devam eder.",
        "► Global Pazara saniyeler içinde, hatasız erişim sağlayın."
    ]
    
    return random.choice(backgrounds), messages

# ==============================================================================
# 3. CSS (YENİ RENK PALETİ & SOL ÜST YERLEŞİM)
# ==============================================================================
def inject_css(bg_url):
    st.markdown(f"""
    <style>
        /* --- GENEL SAYFA AYARLARI --- */
        .stApp {{
            background-image: url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            overflow: hidden !important;
        }}
        
        .block-container {{ padding: 0 !important; margin: 0 !important; max-width: 100% !important; }}
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}

        /* --- SOL ÜST: TYPEWRITER ALANI --- */
        .terminal-container {{
            position: fixed;
            top: 40px;      /* ARTIK YUKARIDA */
            left: 50px;     /* SOLDA */
            z-index: 99;
            font-family: 'Courier New', monospace;
        }}

        .typewriter-line {{
            display: block;
            font-size: 16px; /* Yazı boyutu ideal */
            font-weight: 600;
            color: #e0f2fe; /* Çok açık mavi/beyaz */
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
            background: linear-gradient(90deg, rgba(0,0,0,0.7), transparent); /* Siyah degrade şerit */
            padding: 8px 15px;
            margin-bottom: 8px;
            border-left: 3px solid #06b6d4; /* Turkuaz Çizgi (Yeni Renk) */
            border-radius: 0 4px 4px 0;
            
            /* Animasyon Ayarları */
            overflow: hidden;
            white-space: nowrap;
            width: 0;
            opacity: 0;
            animation: typeText 1.5s steps(50, end) forwards;
        }}

        /* GECİKMELER */
        .typewriter-line:nth-child(1) {{ animation-delay: 0.5s; opacity: 1; }}
        .typewriter-line:nth-child(2) {{ animation-delay: 2.5s; opacity: 1; }}
        .typewriter-line:nth-child(3) {{ animation-delay: 4.5s; opacity: 1; }}
        .typewriter-line:nth-child(4) {{ animation-delay: 6.5s; opacity: 1; }}
        .typewriter-line:nth-child(5) {{ animation-delay: 8.5s; opacity: 1; }}

        @keyframes typeText {{
            0% {{ width: 0; opacity: 1; }}
            100% {{ width: 100%; opacity: 1; }}
        }}

        /* --- SAĞ TARAF: KOMPAKT GİRİŞ KUTUSU --- */
        div[data-testid="column"]:nth-of-type(2) {{
            background: rgba(10, 10, 10, 0.85); /* Çok koyu gri/siyah */
            backdrop-filter: blur(20px);        /* Güçlü bulanıklık */
            padding: 30px;                      /* DAHA AZ BOŞLUK (KÜÇÜLTME) */
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08); /* İnce gümüş çerçeve */
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
            margin-top: 20vh;
        }}

        /* Başlıklar */
        .login-header {{
            font-size: 22px;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 5px;
            letter-spacing: 0.5px;
        }}
        .login-sub {{
            font-size: 12px;
            color: #94a3b8;
            text-align: center;
            margin-bottom: 25px;
        }}

        /* Inputlar - Daha Kompakt */
        .stTextInput input {{
            background-color: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            height: 42px !important; /* Yüksekliği azalttım */
            border-radius: 8px !important;
            font-size: 14px !important;
        }}
        
        /* Input Focus Rengi: MAVİ/TURKUAZ */
        .stTextInput input:focus {{
            border-color: #06b6d4 !important; /* Turkuaz */
            box-shadow: 0 0 10px rgba(6, 182, 212, 0.2) !important;
        }}
        
        /* Buton - Yeni Renk Paleti (Mavi Degrade) */
        .stButton button {{
            background: linear-gradient(90deg, #0ea5e9 0%, #2563eb 100%) !important; /* Okyanus Mavisi */
            color: white !important;
            font-weight: 600 !important;
            border: none !important;
            height: 45px !important;
            border-radius: 8px !important;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
        }}
        .stButton button:hover {{
            background: linear-gradient(90deg, #38bdf8 0%, #3b82f6 100%) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
        }}
        
        /* Checkbox ve Link */
        .stCheckbox span {{ color: #cbd5e1 !important; font-size: 13px; }}
        a {{ color: #94a3b8 !important; text-decoration: none; font-size: 12px; transition: 0.3s; }}
        a:hover {{ color: #38bdf8 !important; }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. RENDER (GÖRÜNTÜLEME)
# ==============================================================================
def render_login_page():
    bg, lines = get_assets()
    inject_css(bg)
    
    # Grid: [Boşluk] - [Form] - [Boşluk]
    # Ortadaki sütunu (0.7) yaparak kutuyu daralttım.
    col1, col2, col3 = st.columns([1.5, 0.7, 0.3])
    
    # --- FORM ALANI (SAĞ/ORTA) ---
    with col2:
        # HTML Başlıklar (CSS ile stillendirildi)
        st.markdown('<div class="login-header">Giriş Yap</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-sub">ARTIS Global Operations</div>', unsafe_allow_html=True)

        with st.form("login_form"):
            user = st.text_input("Kullanıcı Adı", placeholder="admin", label_visibility="collapsed")
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True) # İnce boşluk
            password = st.text_input("Şifre", type="password", placeholder="•••••••", label_visibility="collapsed")
            
            st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
            
            # Alt satır (Hatırla & Link)
            c1, c2 = st.columns([1.2, 1])
            with c1:
                st.checkbox("Beni Hatırla", value=True)
            with c2:
                st.markdown("<div style='text-align:right; padding-top:2px;'><a href='#'>Şifremi Unuttum</a></div>", unsafe_allow_html=True)
            
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            
            if st.form_submit_button("SİSTEME GİRİŞ", type="primary", use_container_width=True):
                if user == "admin" and password == "admin":
                    with st.spinner("Yetki kontrolü..."):
                        time.sleep(0.8)
                    st.success("Başarılı")
                    st.session_state.logged_in = True
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Giriş başarısız.")

    # --- SOL ÜST: TYPEWRITER MESAJLARI ---
    html_content = ""
    for line in lines:
        html_content += f'<div class="typewriter-line">{line}</div>'
    
    st.markdown(f"""
    <div class="terminal-container">
        {html_content}
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_login_page()
