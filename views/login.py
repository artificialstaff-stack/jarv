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
    # PREMIUM ARKA PLANLAR (High-End Tech & Architecture)
    backgrounds = [
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop", # Finans Merkezi (Mavi/Gri)
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Global Ağ (Siyah/Mavi)
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", # Server (Karanlık)
        "https://images.unsplash.com/photo-1493934558415-9d19f0b2b4d2?q=80&w=2054&auto=format&fit=crop"  # Matrix/Derin Teknoloji
    ]

    # FOMO YARATAN MESAJLAR
    messages = [
        "► ABD E-Ticaret Hacmi: 1.1 Trilyon $ (Fırsatı Kaçırmayın).",
        "► Üretimden Teslimata: %100 Otonom İhracat Yönetimi.",
        "► Amazon FBA & Walmart Entegrasyonu ile Satışları Katlayın.",
        "► Lojistik Operasyonlarında %60 Maliyet Tasarrufu.",
        "► ARTIS: Yerel Güçten Global Markaya Dönüşüm Motoru."
    ]
    
    return random.choice(backgrounds), messages

# ==============================================================================
# 3. CSS (SPOTLIGHT THEME - BLACK & PLATINUM)
# ==============================================================================
def inject_css(bg_url):
    st.markdown(f"""
    <style>
        /* --- ARKA PLAN (SPOTLIGHT İÇİN KARARTMA) --- */
        .stApp {{
            /* Arka plana %80 Siyah Perde Çektik - Kutu öne çıksın diye */
            background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url('{bg_url}');
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
            font-family: 'Segoe UI', monospace;
        }}

        .typewriter-line {{
            font-size: 15px;
            color: #94a3b8; /* Sönük Gri - Gözü yormasın, kutuya baksın */
            margin-bottom: 8px;
            border-left: 3px solid #3b82f6; /* Elektrik Mavisi Çizgi */
            padding-left: 15px;
            opacity: 0;
            animation: fadeInMove 1s ease forwards;
        }}
        
        .typewriter-line:nth-child(1) {{ animation-delay: 0.5s; }}
        .typewriter-line:nth-child(2) {{ animation-delay: 2.5s; }}
        .typewriter-line:nth-child(3) {{ animation-delay: 4.5s; }}
        .typewriter-line:nth-child(4) {{ animation-delay: 6.5s; }}

        @keyframes fadeInMove {{
            from {{ opacity: 0; transform: translateX(-20px); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}

        /* --- SAĞ KOLON (GİRİŞ KUTUSU) --- */
        
        /* KUTU TASARIMI (SPOTLIGHT EFFECT) */
        div[data-testid="column"]:nth-of-type(2) {{
            background-color: #000000; /* TAM SİYAH */
            padding: 50px;
            border-radius: 20px;
            /* ÖNE ÇIKARAN EFEKT BURADA: */
            border: 1px solid rgba(255, 255, 255, 0.15); /* İnce Gümüş Çerçeve */
            box-shadow: 0 0 100px rgba(0,0,0, 1); /* Arkaya çok koyu gölge */
            margin-top: 5vh;
            position: relative;
            z-index: 100;
        }}

        /* Sekmeler (Tabs) */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 10px;
            background-color: #111;
            padding: 5px;
            border-radius: 10px;
            margin-bottom: 25px;
        }}
        .stTabs [data-baseweb="tab"] {{
            height: 40px;
            background-color: transparent;
            border: none;
            color: #64748b;
            font-weight: 600;
            border-radius: 8px;
        }}
        .stTabs [data-baseweb="tab"][aria-selected="true"] {{
            background-color: #333 !important; /* Seçili Tab Koyu Gri */
            color: #fff !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }}

        /* Inputlar (Form Alanları) */
        .stTextInput input, .stSelectbox div[data-baseweb="select"] {{
            background-color: #0a0a0a !important;
            border: 1px solid #333 !important;
            color: white !important;
            height: 48px !important;
            border-radius: 8px !important;
            padding-left: 15px !important;
        }}
        .stTextInput input:focus {{
            border-color: #ffffff !important; /* Focus olunca BEYAZ yanar */
            background-color: #000 !important;
        }}

        /* BUTON TASARIMI (EN ÖNEMLİ KISIM) */
        /* Beyaz Buton - Siyah Yazı -> En Premium Kombinasyon */
        .stButton button {{
            background-color: #ffffff !important;
            color: #000000 !important;
            font-weight: 800 !important;
            border: none !important;
            height: 55px !important;
            font-size: 15px !important;
            border-radius: 8px !important;
            transition: all 0.3s ease;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
        }}
        .stButton button:hover {{
            background-color: #e2e8f0 !important;
            transform: scale(1.02);
            box-shadow: 0 0 30px rgba(255, 255, 255, 0.3); /* Parlama artar */
        }}

        /* Yazı Stilleri */
        h2 {{ color: white !important; font-family: 'Helvetica', sans-serif; letter-spacing: -1px; }}
        p {{ color: #94a3b8 !important; }}
        a {{ color: #64748b !important; text-decoration: none; font-size: 13px; }}
        a:hover {{ color: white !important; }}
        .stCheckbox span {{ color: #64748b !important; font-size: 13px; }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. SAAS ANALİZ & VALİDASYON
# ==============================================================================
def validate_application(email, phone, company):
    if not company or len(company) < 3:
        return False, "Firma ünvanı geçerli değil."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Kurumsal e-posta formatı hatalı."
    if len(phone) < 10 or not phone.isdigit():
        return False, "Telefon numarası eksik veya hatalı."
    return True, ""

# ==============================================================================
# 5. RENDER SAYFASI
# ==============================================================================
def render_login_page():
    bg, messages = get_assets()
    inject_css(bg)
    
    # GRID SİSTEMİ: Ortadaki kutuyu biraz daha büyüttüm (1.3)
    # [Sol Boşluk] - [Kutu] - [Sağ Boşluk]
    col1, col2, col3 = st.columns([1.3, 1.3, 0.4])
    
    with col2:
        # BAŞLIK
        st.markdown("<h2 style='text-align:center; margin-bottom:5px;'>ARTIS PANEL</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; margin-bottom:25px; font-size:13px;'>Global Operasyon & İhracat Yönetim Sistemi</p>", unsafe_allow_html=True)

        # SEKMELER
        tab_login, tab_apply = st.tabs(["GİRİŞ YAP", "BAŞVURU YAP"])
        
        # --- 1. GİRİŞ FORMU ---
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
                
                if st.form_submit_button("GÜVENLİ GİRİŞ", type="primary", use_container_width=True):
                    if user == "admin" and pw == "admin":
                        with st.spinner("Yetkilendirme sağlanıyor..."):
                            time.sleep(1)
                        st.session_state.logged_in = True
                        st.rerun()
                    else:
                        st.error("Giriş bilgileri doğrulanamadı.")

        # --- 2. BAŞVURU FORMU (SAAS ANALİZİ) ---
        with tab_apply:
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            st.markdown("<p style='color:#64748b; font-size:12px; text-align:center; margin-bottom:15px;'>Amerika pazarı için üretici ön değerlendirme formu.</p>", unsafe_allow_html=True)
            
            with st.form("apply_form"):
                # Firma Kimliği
                company = st.text_input("Firma Ünvanı", placeholder="Örn: Yılmaz Tekstil A.Ş.")
                
                c_sec, c_exp = st.columns(2)
                with c_sec:
                    sector = st.selectbox("Sektörünüz", ["Tekstil & Giyim", "Mobilya", "Gıda", "Otomotiv", "Kozmetik", "Endüstriyel", "Diğer"])
                with c_exp:
                    # Kritik Soru: Müşteriyi segmentlere ayırır
                    status = st.selectbox("İhracat Durumu", ["Henüz Başlamadım", "Yeni Başladım (Az Hacim)", "Profesyonel İhracatçıyım"])

                # Hacim ve Hedef (Lead Scoring için)
                c_vol, c_target = st.columns(2)
                with c_vol:
                    volume = st.selectbox("Aylık Tahmini Gönderi", ["0 - 50 Adet", "50 - 500 Adet", "500 - 5000 Adet", "5000+ Adet"])
                with c_target:
                    target = st.selectbox("Hedef Pazar", ["Sadece ABD", "ABD + Kanada", "Avrupa", "Global"])

                st.markdown("---") # Ayırıcı çizgi
                
                # İletişim
                c_email, c_phone = st.columns(2)
                with c_email:
                    email = st.text_input("Kurumsal E-Posta", placeholder="info@firma.com")
                with c_phone:
                    phone = st.text_input("Yetkili Telefon", placeholder="05XX...")

                st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
                
                if st.form_submit_button("BAŞVURUYU GÖNDER", type="primary", use_container_width=True):
                    valid, msg = validate_application(email, phone, company)
                    
                    if not valid:
                        st.error(msg)
                    else:
                        st.success("Başvurunuz başarıyla alındı! İhracat uzmanlarımız 24 saat içinde sizinle iletişime geçecektir.")
                        time.sleep(3)

    # --- SOL ÜST YAZILAR ---
    html_code = ""
    for msg in messages:
        html_code += f'<div class="typewriter-line">{msg}</div>'
    st.markdown(f'<div class="terminal-container">{html_code}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    render_login_page()
