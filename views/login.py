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
    # Premium, İnsansız, Koyu Tonlu Arka Planlar
    backgrounds = [
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop", # Finans/Gökdelen (Mavi tonlu)
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", # Server Room (Siyah tonlu)
        "https://images.unsplash.com/photo-1605218456194-bccca572a661?q=80&w=2070&auto=format&fit=crop", # Konteyner Gemisi (Ticaret)
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=2070&auto=format&fit=crop"  # Matrix Code (Yazılım)
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
# 3. CSS (LUXURY GOLD & ONYX THEME)
# ==============================================================================
def inject_css(bg_url):
    st.markdown(f"""
    <style>
        /* --- ARKA PLAN & KARARTMA --- */
        .stApp {{
            background-image: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('{bg_url}');
            background-size: cover;
            background-position: center;
            height: 100vh;
            overflow: hidden !important;
        }}
        .block-container {{ padding: 0 !important; margin: 0 !important; max-width: 100% !important; }}
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}

        /* --- SOL ÜST YAZILAR --- */
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
            border-left: 3px solid #d4af37; /* GOLD ÇİZGİ */
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

        /* --- GİRİŞ KUTUSU (SPOTLIGHT) --- */
        div[data-testid="column"]:nth-of-type(2) {{
            background-color: #050505; /* PITCH BLACK */
            padding: 40px;
            border-radius: 16px;
            border: 1px solid rgba(212, 175, 55, 0.3); /* İNCE GOLD ÇERÇEVE */
            box-shadow: 0 0 60px rgba(0,0,0, 1); /* Derin Gölge */
            margin-top: 5vh;
            position: relative;
            z-index: 100;
        }}

        /* --- FORM ELEMANLARI DÜZENLEMESİ (FIX) --- */
        
        /* Input Alanları */
        .stTextInput input {{
            background-color: #121212 !important;
            border: 1px solid #333 !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 10px 15px !important;
        }}
        .stTextInput input:focus {{
            border-color: #d4af37 !important; /* Focus Gold */
            box-shadow: 0 0 8px rgba(212, 175, 55, 0.3) !important;
        }}

        /* --- SELECTBOX (AÇILIR MENÜ) DÜZELTME --- */
        /* Sorun çıkaran buton kaymasını engeller */
        div[data-baseweb="select"] > div {{
            background-color: #121212 !important;
            border: 1px solid #333 !important;
            color: white !important;
            border-radius: 8px !important;
            display: flex;
            align-items: center; /* Dikey ortalama */
        }}
        /* Menü içindeki yazılar */
        div[data-baseweb="select"] span {{
            color: #e2e8f0 !important;
        }}
        /* Menü açılınca çıkan liste */
        ul[data-baseweb="menu"] {{
            background-color: #121212 !important;
            border: 1px solid #333 !important;
        }}
        li[data-baseweb="option"] {{
            color: white !important;
        }}

        /* --- BUTONLAR (PREMIUM GOLD) --- */
        .stButton button {{
            /* METALİK GOLD DEGRADE */
            background: linear-gradient(135deg, #d4af37 0%, #aa8c2c 100%) !important;
            color: #000000 !important; /* Siyah Yazı (Kontrast için) */
            font-weight: 800 !important;
            border: none !important;
            height: 50px !important;
            font-size: 15px !important;
            border-radius: 8px !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2);
        }}
        .stButton button:hover {{
            background: linear-gradient(135deg, #ebd168 0%, #d4af37 100%) !important; /* Açık Gold */
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
        }}

        /* --- TABS --- */
        .stTabs [data-baseweb="tab-list"] {{ border-bottom: 1px solid #333; }}
        .stTabs [data-baseweb="tab"] {{ color: #666; }}
        .stTabs [data-baseweb="tab"][aria-selected="true"] {{
            color: #d4af37 !important; /* Seçili Tab Gold */
            border-top-color: #d4af37 !important;
        }}

        /* Diğer */
        h2 {{ color: white !important; }}
        p {{ color: #888 !important; }}
        a {{ color: #d4af37 !important; text-decoration: none; }}
        .stCheckbox span {{ color: #aaa !important; font-size: 13px; }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. VALİDASYON (SAAS MANTIĞI)
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
    
    # Grid: Sol(1.4) - Orta(1.2) - Sağ(0.4)
    col1, col2, col3 = st.columns([1.4, 1.2, 0.4])
    
    with col2:
        st.markdown("<h2 style='text-align:center; margin-bottom:5px;'>ARTIS PANEL</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; margin-bottom:20px; font-size:13px;'>Global Operasyon & İhracat Yönetim Sistemi</p>", unsafe_allow_html=True)

        # TABLAR
        tab_login, tab_apply = st.tabs(["GİRİŞ YAP", "BAŞVURU YAP"])
        
        # --- GİRİŞ ---
        with tab_login:
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
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
                
                if st.form_submit_button("GÜVENLİ GİRİŞ", type="primary", use_container_width=True):
                    if user == "admin" and pw == "admin":
                        with st.spinner("Giriş yapılıyor..."):
                            time.sleep(1)
                        st.session_state.logged_in = True
                        st.rerun()
                    else:
                        st.error("Hatalı giriş.")

        # --- BAŞVURU (SAAS ANALİZİ) ---
        with tab_apply:
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; margin-bottom:15px; font-size:12px;'>Amerika pazarı için üretici ön değerlendirme.</p>", unsafe_allow_html=True)
            
            with st.form("apply_form"):
                # 1. Satır: Firma
                company = st.text_input("Firma Ünvanı", placeholder="Şirket Adı A.Ş.")
                
                # 2. Satır: Sektör & Durum (Yanyana)
                r1_c1, r1_c2 = st.columns(2)
                with r1_c1:
                    # CSS Fix'i sayesinde artık düzgün görünecek
                    sector = st.selectbox("Sektörünüz", ["Tekstil", "Mobilya", "Gıda", "Otomotiv", "Kozmetik", "Diğer"])
                with r1_c2:
                    status = st.selectbox("İhracat Deneyimi", ["Yeni Başlıyorum", "Orta Seviye", "Profesyonel"])

                # 3. Satır: Hacim & Hedef (Yanyana)
                r2_c1, r2_c2 = st.columns(2)
                with r2_c1:
                    volume = st.selectbox("Aylık Tahmini Ürün", ["0 - 100", "100 - 1000", "1000+"])
                with r2_c2:
                    target = st.selectbox("Hedef Pazar", ["Sadece ABD", "Kuzey Amerika", "Global"])

                st.markdown("---") 
                
                # 4. Satır: İletişim
                r3_c1, r3_c2 = st.columns(2)
                with r3_c1:
                    email = st.text_input("E-Posta", placeholder="info@...")
                with r3_c2:
                    phone = st.text_input("Telefon", placeholder="05XX...")

                st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
                
                if st.form_submit_button("HEMEN BAŞVUR", type="primary", use_container_width=True):
                    valid, msg = validate_application(email, phone, company)
                    if valid:
                        st.success("Başvuru alındı! Uzmanlarımız sizi arayacak.")
                    else:
                        st.warning(msg)

    # --- YAZILAR ---
    html_code = ""
    for msg in messages:
        html_code += f'<div class="typewriter-line">{msg}</div>'
    st.markdown(f'<div class="terminal-container">{html_code}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    render_login_page()
