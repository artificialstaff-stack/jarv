import streamlit as st
import time
import random
import re  # Email ve Telefon kontrolü için regex kütüphanesi

# ==============================================================================
# 1. AYARLAR
# ==============================================================================
try:
    st.set_page_config(page_title="ARTIS - Global Access", layout="wide", initial_sidebar_state="collapsed")
except:
    pass

# ==============================================================================
# 2. İÇERİK HAVUZU
# ==============================================================================
def get_assets():
    # İnsansız, yüksek kaliteli Lojistik ve Teknoloji görselleri
    backgrounds = [
        "https://images.unsplash.com/photo-1578575437130-527eed3abbec?q=80&w=2070&auto=format&fit=crop", # Gece Limanı/Lojistik
        "https://images.unsplash.com/photo-1516110833967-0b5716ca1387?q=80&w=2074&auto=format&fit=crop", # Yapay Zeka/Veri
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop", # Finans Merkezi/Gökdelenler
        "https://images.unsplash.com/photo-1605218456194-bccca572a661?q=80&w=2070&auto=format&fit=crop"  # Konteyner Gemisi
    ]

    messages = [
        "► ABD Pazarına Açılan Kapınız: 1.1 Trilyon $'lık Fırsat.",
        "► Türkiye'deki fabrikanızdan Amerika'daki müşteriye uçtan uca yönetim.",
        "► Gümrük, Lojistik ve Depolama süreçlerinde %100 Otonom Takip.",
        "► Amazon FBA ve Walmart entegrasyonu ile satışlarınızı katlayın.",
        "► ARTIS: Yerel Üreticiden Global Markaya Dönüşüm Motoru."
    ]
    
    return random.choice(backgrounds), messages

# ==============================================================================
# 3. CSS (YENİ "AMBER & NAVY" TEMASI)
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
            top: 60px;
            left: 60px;
            z-index: 999;
            font-family: 'Courier New', monospace;
        }}

        .typewriter-line {{
            display: block;
            font-size: 18px; /* Daha okunaklı */
            font-weight: bold;
            color: #ffffff;
            text-shadow: 0 2px 4px rgba(0,0,0,0.9);
            background: linear-gradient(90deg, rgba(0,0,0,0.8), transparent);
            padding: 10px 20px;
            margin-bottom: 12px;
            border-left: 5px solid #f59e0b; /* AMBER (ALTIN/TURUNCU) ÇİZGİ */
            
            /* Animasyon */
            overflow: hidden;
            white-space: nowrap;
            width: 0;
            opacity: 0;
            animation: typeText 1.5s steps(50, end) forwards;
        }}
        
        .typewriter-line:nth-child(1) {{ animation-delay: 0.5s; opacity: 1; }}
        .typewriter-line:nth-child(2) {{ animation-delay: 2.5s; opacity: 1; }}
        .typewriter-line:nth-child(3) {{ animation-delay: 4.5s; opacity: 1; }}
        .typewriter-line:nth-child(4) {{ animation-delay: 6.5s; opacity: 1; }}
        .typewriter-line:nth-child(5) {{ animation-delay: 8.5s; opacity: 1; }}

        @keyframes typeText {{
            0% {{ width: 0; opacity: 1; }}
            100% {{ width: 100%; opacity: 1; }}
        }}

        /* --- SAĞ TARAF: GÖZE ÇARPAN GİRİŞ KUTUSU --- */
        /* Streamlit Tabs Styling */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 10px;
            background-color: transparent;
            margin-bottom: 20px;
        }}
        .stTabs [data-baseweb="tab"] {{
            height: 50px;
            white-space: pre-wrap;
            background-color: rgba(255,255,255,0.05);
            border-radius: 8px;
            color: #cbd5e1;
            font-weight: 600;
            border: 1px solid rgba(255,255,255,0.1);
            flex: 1; /* Tabları eşit genişliğe yay */
        }}
        .stTabs [data-baseweb="tab"][aria-selected="true"] {{
            background-color: #f59e0b !important; /* AMBER RENK */
            color: black !important;
            border: none;
        }}

        /* Kutu Tasarımı */
        div[data-testid="column"]:nth-of-type(2) {{
            background: rgba(11, 15, 25, 0.95); /* ÇOK KOYU LACİVERT/SİYAH (Neredeyse opak) */
            padding: 40px;
            border-radius: 20px;
            border: 2px solid #f59e0b; /* ÇERÇEVE RENGİ: AMBER/ALTIN */
            box-shadow: 0 0 40px rgba(245, 158, 11, 0.25); /* DIŞA PARLAMA EFEKTİ */
            margin-top: 10vh;
        }}

        /* Inputlar */
        .stTextInput input, .stSelectbox div[data-baseweb="select"] {{
            background-color: #1e293b !important;
            border: 1px solid #475569 !important;
            color: white !important;
            border-radius: 8px !important;
        }}
        .stTextInput input:focus {{
            border-color: #f59e0b !important; /* Focus olunca Amber */
            box-shadow: 0 0 10px rgba(245, 158, 11, 0.4) !important;
        }}
        
        /* Buton */
        .stButton button {{
            background: linear-gradient(90deg, #f59e0b 0%, #d97706 100%) !important; /* ALTIN DEGRADE */
            color: black !important; /* Yazı Siyah */
            font-weight: 800 !important;
            border: none !important;
            height: 50px !important;
            font-size: 16px !important;
            border-radius: 8px !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: transform 0.2s;
        }}
        .stButton button:hover {{
            transform: scale(1.02);
            box-shadow: 0 5px 20px rgba(245, 158, 11, 0.5);
            color: white !important;
        }}
        
        /* Linkler ve Yazılar */
        h3 {{ color: white !important; }}
        p {{ color: #94a3b8 !important; }}
        .stCheckbox span {{ color: #cbd5e1 !important; }}
        a {{ color: #f59e0b !important; }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. YARDIMCI FONKSİYONLAR (DOĞRULAMA)
# ==============================================================================
def validate_registration(email, phone):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Geçersiz e-posta formatı."
    if len(phone) < 10 or not phone.isdigit():
        return False, "Telefon numarası en az 10 haneli olmalı ve sadece rakam içermelidir."
    return True, ""

# ==============================================================================
# 5. RENDER EKRANI
# ==============================================================================
def render_login_page():
    bg, messages = get_assets()
    inject_css(bg)
    
    # Grid: Sol(1.5) - Orta(1.2 - BÜYÜTTÜK) - Sağ(0.3)
    col1, col2, col3 = st.columns([1.5, 1.2, 0.3])
    
    # --- SAĞ TARAF: TABLI GİRİŞ/KAYIT SİSTEMİ ---
    with col2:
        st.markdown("<h2 style='text-align:center; color:white; margin-bottom:5px;'>ARTIS PANEL</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; margin-bottom:20px; font-size:14px;'>Türkiye'den Amerika'ya İhracatın Dijital Köprüsü</p>", unsafe_allow_html=True)

        # TABLARI OLUŞTUR
        tab_login, tab_register = st.tabs(["GİRİŞ YAP", "KAYIT OL"])
        
        # --- TAB 1: GİRİŞ YAP ---
        with tab_login:
            with st.form("login_form"):
                user = st.text_input("E-Posta veya Kullanıcı Adı", placeholder="ornek@sirket.com")
                pw = st.text_input("Şifre", type="password", placeholder="••••••••")
                
                st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
                
                c1, c2 = st.columns([1, 1])
                with c1:
                    st.checkbox("Beni Hatırla", value=True)
                with c2:
                    st.markdown("<div style='text-align:right; padding-top:2px;'><a href='#' style='text-decoration:none;'>Şifremi Unuttum</a></div>", unsafe_allow_html=True)
                
                st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
                
                if st.form_submit_button("SİSTEME GİRİŞ", type="primary", use_container_width=True):
                    if user == "admin" and pw == "admin":
                        with st.spinner("Güvenli bağlantı kuruluyor..."):
                            time.sleep(1)
                        st.session_state.logged_in = True
                        st.rerun()
                    else:
                        st.error("Giriş bilgileri hatalı.")

        # --- TAB 2: KAYIT OL (ÜRETİCİLER İÇİN) ---
        with tab_register:
            st.markdown("<div style='font-size:12px; color:#cbd5e1; margin-bottom:10px;'>Amerika pazarına açılmak için ilk adımı atın.</div>", unsafe_allow_html=True)
            
            with st.form("register_form"):
                company_name = st.text_input("Firma Adı (Ünvan)", placeholder="Örn: Yılmaz Tekstil A.Ş.")
                sector = st.selectbox("Sektörünüz", ["Tekstil & Giyim", "Mobilya & Dekorasyon", "Gıda & İçecek", "Otomotiv Yedek Parça", "Diğer"])
                
                rc1, rc2 = st.columns(2)
                with rc1:
                    email_reg = st.text_input("Kurumsal E-Posta", placeholder="info@yilmaz.com")
                with rc2:
                    phone_reg = st.text_input("Cep Telefonu", placeholder="532XXXXXXX")

                pass_reg = st.text_input("Şifre Oluştur", type="password")
                
                st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
                
                if st.form_submit_button("HESAP OLUŞTUR", type="primary", use_container_width=True):
                    # Validasyon (Doğrulama)
                    is_valid, error_msg = validate_registration(email_reg, phone_reg)
                    
                    if not company_name:
                        st.warning("Lütfen firma adını giriniz.")
                    elif not is_valid:
                        st.error(error_msg)
                    else:
                        st.success(f"Tebrikler! {company_name} için başvurunuz alındı. Müşteri temsilcimiz sizinle iletişime geçecek.")
                        time.sleep(2)
                        # Burada normalde veritabanına kayıt yapılır

    # --- SOL ÜST: ANİMASYONLU YAZILAR ---
    html_code = ""
    for msg in messages:
        html_code += f'<div class="typewriter-line">{msg}</div>'
    
    st.markdown(f'<div class="terminal-container">{html_code}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    render_login_page()
