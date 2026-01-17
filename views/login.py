import streamlit as st
import time
import random

# ==============================================================================
# ⚙️ SAYFA AYARLARI (EN BAŞTA OLMALI)
# "layout='wide'" ekranı tam genişlikte kullanmamızı sağlar.
# ==============================================================================
st.set_page_config(
    page_title="ARTIS - Giriş",
    layout="wide",  # BU ÇOK ÖNEMLİ: Ekranı geniş moda alır
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 🗄️ 1. KULLANICI VERİTABANI (MEVCUT VERİLERİN)
# ==============================================================================
USERS = {
    "demo": {
        "pass": "1234",
        "name": "Ahmet Yılmaz",
        "brand": "Anatolia Home",
        "role": "user",
        "plan": "Enterprise",
        "avatar": "AY"
    },
    "tech": {
        "pass": "1234",
        "name": "Elon M.",
        "brand": "Cyber Systems",
        "role": "user",
        "plan": "Unlimited",
        "avatar": "EM"
    },
    "admin": {
        "pass": "admin",
        "name": "Sistem Yöneticisi",
        "brand": "ARTIS HQ",
        "role": "admin",
        "plan": "Internal",
        "avatar": "SA"
    }
}

# ==============================================================================
# 🎨 2. GTA TARZI GÖRSELLER VE SÖZLER
# ==============================================================================
def get_random_content():
    images = [
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", # Cyberpunk
        "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=2070&auto=format&fit=crop", # Chip
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Network
        "https://images.unsplash.com/photo-1607799275518-d58665d096c2?q=80&w=2070&auto=format&fit=crop"  # Server
    ]
    tips = [
        "ARTIS v2.4: Operasyonel verimliliği %40 artırır.",
        "İPUCU: Admin paneline erişmek için yetkili hesap kullanın.",
        "GÜVENLİK: Verileriniz 256-bit SSL ile şifrelenmektedir.",
        "ARTIS AI: İş süreçlerinizi optimize etmek için arka planda çalışır.",
        "HATIRLATMA: Şifrenizi kimseyle paylaşmayın."
    ]
    return random.choice(images), random.choice(tips)

# ==============================================================================
# 🎨 3. CSS (TASARIM MOTORU)
# ==============================================================================
def inject_css(bg_image):
    st.markdown(f"""
    <style>
        /* 1. Streamlit'in varsayılan boşluklarını YOK ET */
        .block-container {{
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }}
        
        /* Sidebar ve Header'ı gizle */
        [data-testid="stSidebar"] {{ display: none; }}
        header {{ display: none !important; }}
        footer {{ display: none !important; }}
        
        /* Ana Arka Plan Rengi */
        [data-testid="stAppViewContainer"] {{
            background-color: #050505;
        }}

        /* --- SOL TARAFTAKİ RESİM ALANI --- */
        .split-left {{
            height: 100vh;
            width: 100%;
            background-image: url('{bg_image}');
            background-size: cover;
            background-position: center;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: flex-end; /* Yazıyı alta yasla */
            padding: 60px;
        }}
        
        /* Resmin üzerine siyah perde (yazı okunsun diye) */
        .split-left::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.1) 60%);
            z-index: 1;
        }}

        /* --- SOL TARAFTAKİ YAZILAR --- */
        .gta-content {{
            position: relative;
            z-index: 2;
            animation: slideUp 1.2s ease-out;
        }}
        
        .gta-logo {{
            font-size: 64px;
            font-weight: 900;
            color: white;
            line-height: 1;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: -2px;
        }}
        
        .gta-tip {{
            font-size: 18px;
            color: #d1d5db;
            border-left: 5px solid #FF4B4B; /* Kırmızı çizgi */
            padding-left: 15px;
            font-family: monospace;
            margin-top: 20px;
        }}

        /* --- SAĞ TARAFTAKİ FORM ALANI --- */
        .login-wrapper {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 90vh; /* Formu dikey ortala */
            padding: 40px;
        }}
        
        .form-title {{
            font-size: 32px;
            font-weight: bold;
            color: white;
            margin-bottom: 10px;
        }}
        
        /* Input stilleri */
        .stTextInput input {{
            background-color: #18181b !important;
            border: 1px solid #27272a !important;
            color: white !important;
            padding: 12px !important;
        }}
        
        .stTextInput input:focus {{
            border-color: #FF4B4B !important;
        }}

        /* Animasyon Keyframe */
        @keyframes slideUp {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🔐 4. DOĞRULAMA MANTIĞI
# ==============================================================================
def verify_user(username, password):
    if username in USERS and USERS[username]["pass"] == password:
        return USERS[username]
    return None

# ==============================================================================
# 🚀 5. EKRAN RENDER (ANA FONKSİYON)
# ==============================================================================
def render_login_page():
    # 1. Rastgele içerik seç
    bg_image, tip_text = get_random_content()
    
    # 2. CSS'i sayfaya enjekte et
    inject_css(bg_image)
    
    # 3. EKRANI BÖL (Sol: 1.5 birim, Sağ: 1 birim)
    col1, col2 = st.columns([1.7, 1])
    
    # --- SOL KOLON (GTA GÖRSELİ) ---
    with col1:
        # Streamlit görseli yerine HTML div kullanıyoruz ki tam otursun
        st.markdown(f"""
        <div class="split-left">
            <div class="gta-content">
                <div class="gta-logo">ARTIS<br>SYSTEMS</div>
                <div class="gta-tip">{tip_text}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- SAĞ KOLON (LOGIN FORM) ---
    with col2:
        st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
        
        st.markdown('<div class="form-title">Giriş Yap</div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#a1a1aa; margin-bottom:30px;">Hesabınıza erişmek için bilgilerinizi girin.</p>', unsafe_allow_html=True)

        with st.form("login_form"):
            username = st.text_input("Kullanıcı Adı", placeholder="admin", label_visibility="collapsed")
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True) # Ara boşluk
            password = st.text_input("Şifre", type="password", placeholder="••••••", label_visibility="collapsed")
            
            st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True) # Ara boşluk
            
            submit_btn = st.form_submit_button("SİSTEME GİR", type="primary", use_container_width=True)

        if submit_btn:
            with st.spinner("Bağlantı kuruluyor..."):
                time.sleep(1) # Gerilim efekti :)
                user = verify_user(username, password)
                
                if user:
                    st.success("Giriş onaylandı.")
                    st.session_state.logged_in = True
                    st.session_state.user_data = user
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Kimlik doğrulama başarısız.")
        
        # Demo bilgileri
        with st.expander("Geliştirici Giriş Bilgileri"):
             st.code("Admin: admin / admin\nUser : demo / 1234", language="text")

        st.markdown("""
            <div style="margin-top: 50px; font-size: 11px; color: #444; text-align: center;">
            ARTIS Global Operations v2.4.1<br>
            Secure Server Connection
            </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True) # Wrapper close

# Eğer bu dosya doğrudan çalıştırılırsa testi gör
if __name__ == "__main__":
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        render_login_page()
    else:
        st.write(f"Giriş Yapıldı! Hoşgeldin {st.session_state.user_data['name']}")
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()
