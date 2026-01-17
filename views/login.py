import streamlit as st
import time
import random

# ==============================================================================
# 1. TEMEL YAPILANDIRMA (SAYFA AYARLARI)
# ==============================================================================
try:
    st.set_page_config(page_title="ARTIS - Global Access", layout="wide", initial_sidebar_state="collapsed")
except:
    pass

# ==============================================================================
# 2. İÇERİK HAVUZU (GERÇEKÇİ VERİLER & GÖRSELLER)
# ==============================================================================
def get_dynamic_assets():
    # 1. ARKA PLANLAR (Unsplash'ten Yüksek Çözünürlüklü - Lojistik/Global/Tech)
    backgrounds = [
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop", # Gökdelenler/Finans (New York Vibe)
        "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=2070&auto=format&fit=crop", # Lojistik/Liman/Konteyner
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Dünya/Network/Data
        "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?q=80&w=2832&auto=format&fit=crop"   # E-ticaret/Depo/Otomasyon
    ]

    # 2. VURUCU VERİLER (Typewriter için Satır Satır)
    # Her satırın uzunluğuna göre animasyon süresi CSS'te ayarlanacak.
    messages = [
        "► ABD E-Ticaret Pazarı 1.1 Trilyon Dolar seviyesini aştı. Payınızı almaya hazır mısınız?",
        "► Walmart ve Amazon FBA entegrasyonu ile ürünleriniz 48 saatte müşteride.",
        "► Manuel süreçleri yok edin: Personel maliyetlerinde %60 net tasarruf sağlayın.",
        "► 7/24 Otonom Sistem: Siz uyurken ARTIS siparişleri işler, faturaları keser.",
        "► Hedef: Türkiye'den Global Pazara saniyeler içinde erişim."
    ]
    
    return random.choice(backgrounds), messages

# ==============================================================================
# 3. CSS (TYPEWRITER EFEKTİ & NO-SCROLL)
# ==============================================================================
def inject_css(bg_url):
    st.markdown(f"""
    <style>
        /* --- TEMEL SAYFA (KAYDIRMA YOK) --- */
        .stApp {{
            background-image: url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            overflow: hidden !important;
        }}
        
        /* Gereksizleri Gizle */
        .block-container {{ padding: 0 !important; margin: 0 !important; max-width: 100% !important; }}
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}
        
        /* --- SOL ALT: TYPEWRITER (DAKTİLO) VERİ ALANI --- */
        .terminal-container {{
            position: fixed;
            bottom: 50px;
            left: 60px;
            z-index: 99;
            font-family: 'Courier New', monospace; /* Kod görünümü */
            color: #00ff41; /* Matrix yeşili veya Beyaz/Mavi olabilir */
        }}

        .typewriter-line {{
            display: block;
            font-size: 18px;
            font-weight: 600;
            color: #ffffff; /* Beyaz yazı */
            text-shadow: 2px 2px 4px #000000; /* Okunabilirlik için gölge */
            background-color: rgba(0,0,0,0.6); /* Arkasına hafif siyah şerit */
            padding: 5px 10px;
            margin-bottom: 8px;
            border-left: 4px solid #FF4B4B; /* Sol çizgi */
            
            /* Animasyon Başlangıç Değerleri */
            overflow: hidden; /* Taşanı gizle (harf harf gelmesi için) */
            white-space: nowrap; /* Alt satıra inme */
            width: 0; /* Başlangıçta görünmez */
            opacity: 0;
            
            /* Animasyon Tanımı */
            animation: typeText 2s steps(60, end) forwards;
        }}

        /* SIRALI GELİŞ GECİKMELERİ (DELAY) */
        /* Her cümle bittikten sonra diğeri başlasın */
        .typewriter-line:nth-child(1) {{ animation-delay: 0.5s; opacity: 1; }}
        .typewriter-line:nth-child(2) {{ animation-delay: 3.0s; opacity: 1; }} /* 1. bitince başla */
        .typewriter-line:nth-child(3) {{ animation-delay: 5.5s; opacity: 1; }}
        .typewriter-line:nth-child(4) {{ animation-delay: 8.0s; opacity: 1; }}
        .typewriter-line:nth-child(5) {{ animation-delay: 10.5s; opacity: 1; }}

        /* DAKTİLO ANİMASYONU */
        @keyframes typeText {{
            0% {{ width: 0; opacity: 1; }}
            100% {{ width: 100%; opacity: 1; }} 
            /* width: 100% yazının tamamını açar */
        }}

        /* --- SAĞ TARAFTAKİ GİRİŞ KUTUSU --- */
        div[data-testid="column"]:nth-of-type(2) {{
            background: rgba(15, 23, 42, 0.75); /* Koyu Lacivert/Siyah Transparan */
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
            margin-top: 15vh; /* Yukarıdan boşluk */
        }}

        /* Inputlar */
        .stTextInput input {{
            background-color: rgba(0, 0, 0, 0.3) !important;
            border: 1px solid #334155 !important;
            color: white !important;
        }}
        .stTextInput input:focus {{
            border-color: #FF4B4B !important;
        }}
        
        /* Buton */
        .stButton button {{
            background-color: #FF4B4B !important;
            color: white !important;
            font-weight: bold !important;
            border: none !important;
            transition: all 0.3s ease;
        }}
        .stButton button:hover {{
            background-color: #ff3333 !important;
            transform: scale(1.02);
        }}
        
        /* Linkler */
        a {{ color: #94a3b8 !important; text-decoration: none; font-size: 13px; }}
        a:hover {{ color: white !important; }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. ANA RENDER FONKSİYONU
# ==============================================================================
def render_login_page():
    # 1. Verileri Çek
    bg, lines = get_dynamic_assets()
    
    # 2. CSS'i Bas
    inject_css(bg)
    
    # 3. Layout (Sağda Kutu Olsun)
    # [Boşluk %50] - [Kutu %30] - [Boşluk %20]
    col1, col2, col3 = st.columns([1.5, 1, 0.5])
    
    # --- SAĞ KOLON (GİRİŞ FORMU) ---
    with col2:
        st.markdown("<h2 style='color:white; margin-bottom:5px;'>Sisteme Giriş</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#cbd5e1; font-size:14px; margin-bottom:25px;'>ARTIS Global Operations Engine</p>", unsafe_allow_html=True)

        with st.form("login_form"):
            user_input = st.text_input("Kullanıcı Adı", placeholder="admin", label_visibility="collapsed")
            st.write("")
            pass_input = st.text_input("Şifre", type="password", placeholder="••••••••", label_visibility="collapsed")
            st.write("")
            
            c1, c2 = st.columns([1,1])
            with c1:
                st.checkbox("Beni Hatırla", value=True)
            with c2:
                st.markdown("<div style='text-align:right; margin-top:3px;'><a href='#'>Şifremi Unuttum</a></div>", unsafe_allow_html=True)
            
            st.write("")
            if st.form_submit_button("GÜVENLİ GİRİŞ", type="primary", use_container_width=True):
                # Login Kontrolü
                if user_input == "admin" and pass_input == "admin":
                    with st.spinner("Panel bağlantısı kuruluyor..."):
                        time.sleep(1)
                    st.success("Giriş Onaylandı.")
                    st.session_state.logged_in = True
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Kullanıcı adı veya şifre hatalı.")

    # --- SOL ALT (TYPEWRITER DATA ALANI) ---
    # Bu kısım HTML/CSS ile sabitlendiği için kolonların dışına yazıyoruz.
    
    # Mesajları HTML formatına çevir
    html_content = ""
    for line in lines:
        html_content += f'<div class="typewriter-line">{line}</div>'
    
    st.markdown(f"""
    <div class="terminal-container">
        {html_content}
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# ÇALIŞTIR
# ==============================================================================
if __name__ == "__main__":
    render_login_page()
