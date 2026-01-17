import streamlit as st
import time
import random

# ==============================================================================
# 1. AYARLAR
# ==============================================================================
try:
    st.set_page_config(page_title="ARTIS Operations", layout="wide", initial_sidebar_state="collapsed")
except:
    pass

# ==============================================================================
# 2. GÖRSEL VE METİN HAVUZU (İNSANSIZ & PAZAR ODAKLI)
# ==============================================================================
def get_assets():
    # Sadece teknoloji, şehir, veri ve lojistik (İNSAN YOK)
    backgrounds = [
        "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=2070&auto=format&fit=crop", # Teknoloji Ekibi (Soyut)
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Dünya/Ağ
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", # Cyberpunk Server
        "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=2070&auto=format&fit=crop", # Liman/Lojistik
        "https://images.unsplash.com/photo-1480074568708-e7b720bb6fce?q=80&w=2070&auto=format&fit=crop"  # Gece Şehri
    ]

    # Pazar Verileri ve Vaatler
    messages = [
        "► ABD E-Ticaret Hacmi: 1.1 Trilyon $ (2024 Verisi).",
        "► Rakipleriniz manuel işlem yaparken siz otonom büyüyün.",
        "► Lojistik maliyetlerinde %60 net tasarruf fırsatı.",
        "► 7/24 Kesintisiz Operasyon: Sadece elektrik maliyetiyle.",
        "► Hedef: Türkiye'den Global Pazara saniyeler içinde erişim."
    ]
    
    return random.choice(backgrounds), messages

# ==============================================================================
# 3. CSS (TURKUAZ TEMA & SOL ÜST YAZI)
# ==============================================================================
def inject_css(bg_url):
    st.markdown(f"""
    <style>
        /* SCROLL ENGELLEME */
        .stApp {{
            background-image: url('{bg_url}');
            background-size: cover;
            background-position: center;
            height: 100vh;
            overflow: hidden !important;
        }}
        .block-container {{ padding: 0 !important; margin: 0 !important; max-width: 100% !important; }}
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}

        /* --- SOL ÜST: TYPEWRITER YAZILARI --- */
        .terminal-container {{
            position: fixed;
            top: 80px;       /* Yukarıdan boşluk */
            left: 50px;      /* Soldan boşluk */
            z-index: 999;
            font-family: 'Courier New', monospace;
        }}

        .typewriter-line {{
            display: block;
            font-size: 16px;
            font-weight: bold;
            color: #ecfeff; /* Çok açık mavi */
            text-shadow: 0 2px 5px rgba(0,0,0,0.9);
            background: linear-gradient(90deg, rgba(0,0,0,0.8), transparent);
            padding: 8px 15px;
            margin-bottom: 10px;
            border-left: 4px solid #06b6d4; /* TURKUAZ Çizgi */
            
            /* Animasyon */
            overflow: hidden;
            white-space: nowrap;
            width: 0;
            opacity: 0;
            animation: typeText 1.5s steps(50, end) forwards;
        }}
        
        /* Animasyon Gecikmeleri */
        .typewriter-line:nth-child(1) {{ animation-delay: 0.5s; opacity: 1; }}
        .typewriter-line:nth-child(2) {{ animation-delay: 2.5s; opacity: 1; }}
        .typewriter-line:nth-child(3) {{ animation-delay: 4.5s; opacity: 1; }}
        .typewriter-line:nth-child(4) {{ animation-delay: 6.5s; opacity: 1; }}
        .typewriter-line:nth-child(5) {{ animation-delay: 8.5s; opacity: 1; }}

        @keyframes typeText {{
            0% {{ width: 0; opacity: 1; }}
            100% {{ width: 100%; opacity: 1; }}
        }}

        /* --- SAĞ TARAF: GİRİŞ KUTUSU (MAVİ & KÜÇÜK) --- */
        div[data-testid="column"]:nth-of-type(2) {{
            background: rgba(15, 23, 42, 0.85); /* Koyu Lacivert Arka Plan */
            backdrop-filter: blur(15px);
            padding: 30px;                       /* İç boşluğu azalttım (Küçüldü) */
            border-radius: 12px;
            border: 1px solid rgba(56, 189, 248, 0.2); /* İnce Mavi Çerçeve */
            box-shadow: 0 10px 40px rgba(0,0,0,0.7);
            margin-top: 15vh;
        }}

        /* Inputlar */
        .stTextInput input {{
            background-color: rgba(30, 41, 59, 0.8) !important;
            border: 1px solid #334155 !important;
            color: white !important;
            height: 40px !important; /* Yükseklik azaldı */
            font-size: 14px !important;
        }}
        .stTextInput input:focus {{
            border-color: #06b6d4 !important; /* Turkuaz Focus */
            box-shadow: 0 0 10px rgba(6, 182, 212, 0.3) !important;
        }}

        /* Buton: Mavi Degrade */
        .stButton button {{
            background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%) !important;
            color: white !important;
            border: none !important;
            height: 45px !important;
            font-weight: 600 !important;
            transition: all 0.3s;
        }}
        .stButton button:hover {{
            background: linear-gradient(90deg, #0ea5e9 0%, #3b82f6 100%) !important;
            box-shadow: 0 5px 15px rgba(37, 99, 235, 0.4);
            transform: scale(1.02);
        }}
        
        /* Linkler */
        a {{ color: #94a3b8 !important; text-decoration: none; font-size: 12px; }}
        a:hover {{ color: #38bdf8 !important; }}
        .stCheckbox span {{ font-size: 13px; color: #cbd5e1 !important; }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. RENDER
# ==============================================================================
def render_login_page():
    bg, messages = get_assets()
    inject_css(bg)
    
    # EKRAN PLANI:
    # Sol Boşluk (2) | Giriş Kutusu (0.8 - Daha Dar) | Sağ Boşluk (0.2)
    col1, col2, col3 = st.columns([2, 0.8, 0.2])
    
    # --- GİRİŞ FORMU ---
    with col2:
        st.markdown("<h3 style='text-align:center; color:white; margin:0; padding:0;'>Giriş Yap</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#94a3b8; font-size:12px; margin-bottom:20px;'>ARTIS Global Operations</p>", unsafe_allow_html=True)

        with st.form("login_form"):
            user = st.text_input("Kullanıcı", placeholder="admin", label_visibility="collapsed")
            st.markdown("<div style='height:5px'></div>", unsafe_allow_html=True)
            pw = st.text_input("Şifre", type="password", placeholder="••••••", label_visibility="collapsed")
            
            st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
            
            c1, c2 = st.columns([1, 1])
            with c1:
                st.checkbox("Hatırla", value=True)
            with c2:
                st.markdown("<div style='text-align:right; padding-top:2px;'><a href='#'>Şifremi Unuttum</a></div>", unsafe_allow_html=True)

            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            
            if st.form_submit_button("SİSTEME GİRİŞ", type="primary", use_container_width=True):
                if user == "admin" and pw == "admin":
                    st.success("Başarılı")
                    st.session_state.logged_in = True
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Hatalı giriş")

    # --- SOL ÜST: YAZILAR ---
    html_code = ""
    for msg in messages:
        html_code += f'<div class="typewriter-line">{msg}</div>'
    
    st.markdown(f'<div class="terminal-container">{html_code}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    render_login_page()
