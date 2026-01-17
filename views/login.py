import streamlit as st
import time
import random
import re

# ==============================================================================
# 1. AYARLAR
# ==============================================================================
try:
    st.set_page_config(page_title="ARTIS - Premium Access", layout="wide", initial_sidebar_state="collapsed")
except:
    pass

# ==============================================================================
# 2. İÇERİK HAVUZU
# ==============================================================================
def get_assets():
    # Arka planlar (Lojistik, Teknoloji, Şehir)
    backgrounds = [
        "https://images.unsplash.com/photo-1480074568708-e7b720bb6fce?q=80&w=2070&auto=format&fit=crop", # Gece Şehri (Premium)
        "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?q=80&w=2832&auto=format&fit=crop",   # Lojistik Depo
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Dünya Ağı
        "https://images.unsplash.com/photo-1494412574643-35d324688133?q=80&w=2070&auto=format&fit=crop"   # Teknoloji (Anakart)
    ]

    messages = [
        "► ABD E-Ticaret Pazarı: 1.1 Trilyon $'lık Dev Fırsat.",
        "► Üretimden Teslimata: %100 Otonom İhracat Yönetimi.",
        "► Amazon & Walmart Entegrasyonu ile Satışlarınızı Katlayın.",
        "► Lojistik Maliyetlerinde %60 Tasarruf Sağlayın.",
        "► ARTIS: Yerel Güçten Global Markaya."
    ]
    
    return random.choice(backgrounds), messages

# ==============================================================================
# 3. CSS (ONYX & TITANIUM THEME - PREMIUM)
# ==============================================================================
def inject_css(bg_url):
    st.markdown(f"""
    <style>
        /* --- ARKA PLAN VE KARARTMA (SPOTLIGHT) --- */
        .stApp {{
            background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('{bg_url}'); /* %70 KARARTMA */
            background-size: cover;
            background-position: center;
            height: 100vh;
            overflow: hidden !important;
        }}
        .block-container {{ padding: 0 !important; margin: 0 !important; max-width: 100% !important; }}
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}

        /* --- SOL ÜST YAZILAR (DAHA BELİRGİN) --- */
        .terminal-container {{
            position: fixed;
            top: 50px;
            left: 50px;
            z-index: 99;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Daha modern font */
        }}

        .typewriter-line {{
            display: block;
            font-size: 16px;
            font-weight: 500;
            color: #f1f5f9;
            background: rgba(255, 255, 255, 0.1); /* Hafif beyaz zemin */
            backdrop-filter: blur(5px);
            padding: 10px 15px;
            margin-bottom: 10px;
            border-left: 4px solid #ffffff; /* BEYAZ Çizgi */
            border-radius: 0 4px 4px 0;
            
            /* Animasyon */
            overflow: hidden;
            white-space: nowrap;
            width: 0;
            opacity: 0;
            animation: typeText 1.0s cubic-bezier(0.215, 0.610, 0.355, 1.000) forwards; /* Daha akıcı animasyon */
        }}
        
        .typewriter-line:nth-child(1) {{ animation-delay: 0.5s; opacity: 1; }}
        .typewriter-line:nth-child(2) {{ animation-delay: 2.5s; opacity: 1; }}
        .typewriter-line:nth-child(3) {{ animation-delay: 4.5s; opacity: 1; }}
        .typewriter-line:nth-child(4) {{ animation-delay: 6.5s; opacity: 1; }}
        .typewriter-line:nth-child(5) {{ animation-delay: 8.5s; opacity: 1; }}

        @keyframes typeText {{ 0% {{ width: 0; opacity: 1; }} 100% {{ width: 100%; opacity: 1; }} }}

        /* --- GİRİŞ KUTUSU (ODAK NOKTASI) --- */
        
        /* Tab Tasarımı - Minimalist */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 20px;
            background-color: transparent;
            margin-bottom: 20px;
            border-bottom: 1px solid rgba(255,255,255,0.2);
        }}
        .stTabs [data-baseweb="tab"] {{
            height: 40px;
            background-color: transparent;
            border: none;
            color: #94a3b8;
            font-weight: 600;
            font-size: 14px;
        }}
        .stTabs [data-baseweb="tab"][aria-selected="true"] {{
            color: #ffffff !important;
            border-bottom: 2px solid #ffffff; /* Seçili olanın altında beyaz çizgi */
        }}

        /* Ana Kutu - KAPKARA VE OPAK */
        div[data-testid="column"]:nth-of-type(2) {{
            background: #000000; /* TAM SİYAH */
            padding: 50px;
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.2); /* İnce Gümüş Çerçeve */
            box-shadow: 0 0 80px rgba(0,0,0, 0.9); /* ÇOK GÜÇLÜ GÖLGE */
            margin-top: 8vh;
            position: relative;
            z-index: 100;
        }}

        /* Inputlar - Modern */
        .stTextInput input, .stSelectbox div[data-baseweb="select"] {{
            background-color: #111111 !important; /* Koyu gri */
            border: 1px solid #333333 !important;
            color: white !important;
            height: 50px !important;
            border-radius: 12px !important;
            padding-left: 15px !important;
            transition: all 0.3s;
        }}
        .stTextInput input:focus {{
            border-color: #ffffff !important; /* Focus olunca BEYAZ */
            background-color: #000000 !important;
        }}
        
        /* PREMIUM BUTON: BEYAZ ZEMİN, SİYAH YAZI */
        .stButton button {{
            background-color: #ffffff !important;
            color: #000000 !important;
            font-weight: 800 !important;
            border: none !important;
            height: 55px !important;
            font-size: 15px !important;
            border-radius: 12px !important;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
        }}
        .stButton button:hover {{
            background-color: #e2e8f0 !important; /* Hafif grileşme */
            transform: scale(1.01);
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.4); /* Beyaz parlama */
        }}
        
        /* Yazılar */
        h2 {{ font-family: 'Helvetica Neue', sans-serif; font-weight: 700; letter-spacing: -1px; }}
        a {{ color: #94a3b8 !important; text-decoration: none; font-size: 13px; transition: 0.3s; }}
        a:hover {{ color: white !important; }}
        .stCheckbox span {{ color: #94a3b8 !important; }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. VALIDATION
# ==============================================================================
def validate_registration(email, phone):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Geçersiz e-posta adresi."
    if len(phone) < 10 or not phone.isdigit():
        return False, "Telefon numarası geçersiz."
    return True, ""

# ==============================================================================
# 5. RENDER
# ==============================================================================
def render_login_page():
    bg, messages = get_assets()
    inject_css(bg)
    
    # Grid: Sol(1.4) - Orta(1.2) - Sağ(0.4)
    # Orta kolon, giriş kutusunun olduğu yer.
    col1, col2, col3 = st.columns([1.4, 1.2, 0.4])
    
    # --- SAĞ TARAF: PREMIUM LOGIN BOX ---
    with col2:
        st.markdown("<h2 style='text-align:center; color:white; margin-bottom:5px;'>ARTIS PANEL</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#64748b; margin-bottom:30px; font-size:14px;'>Global Operasyon Yönetim Sistemi</p>", unsafe_allow_html=True)

        # SEKMELER (Minimalist)
        tab_login, tab_register = st.tabs(["GİRİŞ YAP", "BAŞVURU YAP"])
        
        # --- TAB 1: GİRİŞ ---
        with tab_login:
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            with st.form("login_form"):
                user = st.text_input("Kullanıcı Adı", placeholder="admin")
                st.markdown("<div style='height:5px'></div>", unsafe_allow_html=True)
                pw = st.text_input("Şifre", type="password", placeholder="••••••••")
                
                st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
                
                c1, c2 = st.columns([1, 1])
                with c1:
                    st.checkbox("Beni Hatırla", value=True)
                with c2:
                    st.markdown("<div style='text-align:right; padding-top:2px;'><a href='#'>Şifremi Unuttum</a></div>", unsafe_allow_html=True)
                
                st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
                
                if st.form_submit_button("GÜVENLİ GİRİŞ", type="primary", use_container_width=True):
                    if user == "admin" and pw == "admin":
                        with st.spinner("Kimlik doğrulanıyor..."):
                            time.sleep(1)
                        st.session_state.logged_in = True
                        st.rerun()
                    else:
                        st.error("Bilgiler hatalı.")

        # --- TAB 2: KAYIT (BAŞVURU) ---
        with tab_register:
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            st.markdown("<p style='color:#64748b; font-size:12px; margin-bottom:15px;'>Amerika pazarı için üretici başvurusu.</p>", unsafe_allow_html=True)
            
            with st.form("register_form"):
                company = st.text_input("Firma Ünvanı", placeholder="Şirket Adı A.Ş.")
                sector = st.selectbox("Sektör", ["Tekstil", "Gıda", "Otomotiv", "Mobilya", "Kozmetik", "Diğer"])
                
                rc1, rc2 = st.columns(2)
                with rc1:
                    email = st.text_input("Kurumsal E-Posta", placeholder="info@...")
                with rc2:
                    phone = st.text_input("Telefon", placeholder="5XX...")
                
                st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
                
                if st.form_submit_button("HEMEN BAŞVUR", type="primary", use_container_width=True):
                    valid, msg = validate_registration
