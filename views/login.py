import streamlit as st
import time
import random
import re

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
    backgrounds = [
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop", 
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", 
        "https://images.unsplash.com/photo-1605218456194-bccca572a661?q=80&w=2070&auto=format&fit=crop", 
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=2070&auto=format&fit=crop" 
    ]

    messages = [
        "► ABD E-Ticaret Hacmi: 1.1 Trilyon $ (Fırsat Kapısı).",
        "► Üretimden Teslimata: %100 Otonom Süreç Yönetimi.",
        "► Rakipleriniz Manuel Çalışırken Siz Otomasyonla Kazanın.",
        "► Amazon FBA & Walmart Entegrasyonu ile Satışları Katlayın.",
        "► ARTIS: Yerel Üreticiden Global Markaya."
    ]
    
    return random.choice(backgrounds), messages

# ==============================================================================
# 3. CSS (GOLD & ONYX THEME - KESİN ÇÖZÜM)
# ==============================================================================
def inject_css(bg_url):
    st.markdown(f"""
    <style>
        /* --- ARKA PLAN --- */
        .stApp {{
            background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url('{bg_url}');
            background-size: cover;
            background-position: center;
            height: 100vh;
            overflow: hidden !important;
        }}
        .block-container {{ padding: 0 !important; margin: 0 !important; max-width: 100% !important; }}
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}

        /* --- SOL YAZILAR --- */
        .terminal-container {{
            position: fixed;
            top: 50px;
            left: 50px;
            z-index: 99;
            font-family: 'Segoe UI', sans-serif;
        }}
        .typewriter-line {{
            font-size: 15px;
            font-weight: 500;
            color: #e2e8f0; 
            margin-bottom: 8px;
            border-left: 3px solid #d4af37;
            background: linear-gradient(90deg, rgba(212, 175, 55, 0.1), transparent);
            padding: 8px 15px;
            opacity: 0;
            animation: fadeInMove 1s ease forwards;
        }}
        .typewriter-line:nth-child(1) {{ animation-delay: 0.5s; }}
        .typewriter-line:nth-child(2) {{ animation-delay: 2.5s; }}
        .typewriter-line:nth-child(3) {{ animation-delay: 4.5s; }}
        .typewriter-line:nth-child(4) {{ animation-delay: 6.5s; }}
        .typewriter-line:nth-child(5) {{ animation-delay: 8.5s; }}
        
        @keyframes fadeInMove {{ from {{ opacity: 0; transform: translateX(-20px); }} to {{ opacity: 1; transform: translateX(0); }} }}

        /* --- GİRİŞ KUTUSU --- */
        div[data-testid="column"]:nth-of-type(2) {{
            background-color: #050505;
            padding: 40px;
            border-radius: 16px;
            border: 1px solid rgba(212, 175, 55, 0.3);
            box-shadow: 0 0 80px rgba(0,0,0, 1);
            margin-top: 5vh;
            position: relative;
            z-index: 100;
        }}

        /* --- INPUT ALANLARI --- */
        .stTextInput input {{
            background-color: #121212 !important;
            border: 1px solid #333 !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 10px 15px !important;
        }}
        .stTextInput input:focus {{
            border-color: #d4af37 !important;
            box-shadow: 0 0 8px rgba(212, 175, 55, 0.3) !important;
        }}

        /* --- SELECTBOX DÜZELTME --- */
        div[data-baseweb="select"] > div {{
            background-color: #121212 !important;
            border: 1px solid #333 !important;
            color: white !important;
            border-radius: 8px !important;
            display: flex;
            align-items: center;
        }}
        div[data-baseweb="select"] span {{ color: #e2e8f0 !important; }}
        ul[data-baseweb="menu"] {{ background-color: #121212 !important; border: 1px solid #333 !important; }}
        li[data-baseweb="option"] {{ color: white !important; }}

        /* --- BUTONLAR (KIRMIZIYI YOK ETME VE GOLD YAPMA) --- */
        /* Streamlit'in tüm buton varyasyonlarını hedefliyoruz */
        div[data-testid="stFormSubmitButton"] > button,
        button[kind="primary"],
        button[kind="secondary"],
        .stButton > button {{
            background: linear-gradient(135deg, #d4af37 0%, #aa8c2c 100%) !important; /* GOLD DEGRADE */
            background-color: #d4af37 !important; /* Yedek renk */
            color: #000000 !important; /* Siyah Yazı */
            border: none !important;
            font-weight: 800 !important;
            height: 50px !important;
            font-size: 15px !important;
            border-radius: 8px !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2) !important;
            transition: all 0.3s ease !important;
        }}

        /* Hover Efekti */
        div[data-testid="stFormSubmitButton"] > button:hover,
        button[kind="primary"]:hover,
        .stButton > button:hover {{
            background: linear-gradient(135deg, #ebd168 0%, #d4af37 100%) !important;
            color: #000000 !important;
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4) !important;
        }}
        
        /* Buton tıklandığında (Active) */
        div[data-testid="stFormSubmitButton"] > button:active {{
            color: #000000 !important;
            background-color: #d4af37 !important;
        }}

        /* --- TABS --- */
        .stTabs [data-baseweb="tab-list"] {{ border-bottom: 1px solid #333; gap: 10px; }}
        .stTabs [data-baseweb="tab"] {{ color: #666; border-radius: 5px; }}
        .stTabs [data-baseweb="tab"][aria-selected="true"] {{
            color: #000000 !important;
            background-color: #d4af37 !important; /* Seçili Tab Gold Arka Plan */
            font-weight: bold;
        }}

        /* Diğer */
        h2 {{ color: white !important; }}
        p {{ color: #888 !important; }}
        a {{ color: #d4af37 !important; text-decoration: none; }}
        .stCheckbox span {{ color: #aaa !important; font-size: 13px; }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. VALİDASYON
# ==============================================================================
def validate_application(email, phone, company):
    if not company or len(company) < 2:
        return False, "Firma adı gereklidir."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Geçersiz e-posta formatı."
    if len(phone) < 10 or not phone.isdigit():
        return False, "Telefon numarası hatalı."
    return True, ""

# ==============================================================================
# 5. EKRAN RENDER
# ==============================================================================
def render_login_page():
    bg, messages = get_assets()
    inject_css(bg)
    
    col1, col2, col3 = st.columns([1.4, 1.2, 0.4])
    
    with col2:
        st.markdown("<h2 style='text-align:center; margin-bottom:5px;'>ARTIS PANEL</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; margin-bottom:20px; font-size:13px;'>Global Operasyon & İhracat Yönetim Sistemi</p>", unsafe_allow_html=True)

        tab_login, tab_apply = st.tabs(["GİRİŞ YAP", "BAŞVURU YAP"])
        
        # --- GİRİŞ ---
        with tab_login:
            st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
            with st.form("login_form"):
                user = st.text_input("Kullanıcı Adı", placeholder="admin")
                pw = st.text_input("Şifre", type="password", placeholder="••••••••")
                
                st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
                
                c1, c2 = st.columns([1, 1])
                with c1:
                    st.checkbox("Beni Hatırla", value=True)
                with c2:
                    st.markdown("<div style='text-align:right; padding-top:2px;'><a href='#'>Şifremi Unuttum</a></div>", unsafe_allow_html=True)
                
                st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
                
                # type="primary" olmasına rağmen CSS ezecek
                if st.form_submit_button("GÜVENLİ GİRİŞ", type="primary", use_container_width=True):
                    if user == "admin" and pw == "admin":
                        with st.spinner("Giriş yapılıyor..."):
                            time.sleep(1)
                        st.session_state.logged_in = True
                        st.rerun()
                    else:
                        st.error("Hatalı giriş.")

        # --- BAŞVURU ---
        with tab_apply:
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; margin-bottom:15px; font-size:12px;'>Amerika pazarı için üretici ön değerlendirme.</p>", unsafe_allow_html=True)
            
            with st.form("apply_form"):
                company = st.text_input("Firma Ünvanı", placeholder="Şirket Adı A.Ş.")
                
                r1_c1, r1_c2 = st.columns(2)
                with r1_c1:
                    sector = st.selectbox("Sektörünüz", ["Tekstil", "Mobilya", "Gıda", "Otomotiv", "Kozmetik", "Diğer"])
                with r1_c2:
                    status = st.selectbox("İhracat Deneyimi", ["Yeni Başlıyorum", "Orta Seviye", "Profesyonel"])

                r2_c1, r2_c2 = st.columns(2)
                with r2_c1:
                    volume = st.selectbox("Aylık Tahmini Ürün", ["0 - 100", "100 - 1000", "1000+"])
                with r2_c2:
                    target = st.selectbox("Hedef Pazar", ["Sadece ABD", "Kuzey Amerika", "Global"])

                st.markdown("---") 
                
                r3_c1, r3_c2 = st.columns(2)
                with r3_c1:
                    email = st.text_input("E-Posta", placeholder="info@...")
                with r3_c2:
                    phone = st.text_input("Telefon", placeholder="05XX...")

                st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
                
                if st.form_submit_button("HEMEN BAŞVUR", type="primary", use_container_width=True):
                    valid, msg = validate_application(email, phone, company)
                    if valid:
                        st.success("Başvuru alındı!")
                    else:
                        st.warning(msg)

    # --- YAZILAR ---
    html_code = ""
    for msg in messages:
        html_code += f'<div class="typewriter-line">{msg}</div>'
    st.markdown(f'<div class="terminal-container">{html_code}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    render_login_page()
