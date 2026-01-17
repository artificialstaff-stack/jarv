import streamlit as st
import time
import random

# ==============================================================================
# 🗄️ 1. KULLANICI VERİTABANI (MEVCUT YAPI KORUNDU)
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
# 🎨 2. GTA STYLE ASSETS & CSS (YENİ TASARIM)
# ==============================================================================
def get_gta_assets():
    """Rastgele görsel ve ipucu seçer"""
    images = [
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Network
        "https://images.unsplash.com/photo-1607799275518-d58665d096c2?q=80&w=2070&auto=format&fit=crop", # Server Room
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", # Cyberpunk
        "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=2070&auto=format&fit=crop"  # Team/Work
    ]
    tips = [
        "ARTIS v2.4: Operasyonel verimliliği %40 artırır.",
        "İPUCU: Admin paneline erişmek için yetkili hesap kullanın.",
        "SİSTEM: Verileriniz 256-bit SSL ile şifrelenmektedir.",
        "ARTIS AI: İş süreçlerinizi optimize etmek için arka planda çalışır.",
        "BİLİYOR MUYDUNUZ? Raporları 'Panel' sekmesinden PDF olarak alabilirsiniz."
    ]
    return random.choice(images), random.choice(tips)

def inject_login_css(selected_image):
    st.markdown(f"""
    <style>
        /* Standart Streamlit Boşluklarını Sıfırla */
        .block-container {{
            padding: 0 !important;
            max-width: 100%;
        }}
        [data-testid="stAppViewContainer"] {{
            background-color: #0e1117;
        }}
        
        /* SOL TARAFTAKİ GÖRSEL ALANI (GTA STYLE) */
        .gta-visual {{
            height: 100vh;
            background-image: url('{selected_image}');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 60px;
            position: relative;
        }}
        
        /* Görsel Üzeri Karartma (Yazı Okunurluğu İçin) */
        .gta-visual::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to top, rgba(0,0,0,0.95), rgba(0,0,0,0.1));
            z-index: 1;
        }}
        
        /* İçerik Animasyonu */
        .gta-content {{
            position: relative;
            z-index: 2;
            color: white;
            animation: slideUp 1.2s ease-out;
        }}
        
        .gta-title {{
            font-size: 60px;
            font-weight: 900;
            letter-spacing: -2px;
            line-height: 1;
            margin-bottom: 20px;
            text-transform: uppercase;
        }}
        
        .gta-tip-box {{
            border-left: 4px solid #FF4B4B; /* Streamlit kırmızısı veya marka rengin */
            padding-left: 20px;
            margin-bottom: 40px;
        }}
        
        .gta-tip-text {{
            font-size: 18px;
            font-weight: 300;
            color: #e0e0e0;
            font-family: 'Courier New', monospace; /* Terminal havası */
        }}

        @keyframes slideUp {{
            from {{ opacity: 0; transform: translateY(40px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* SAĞ TARAF (LOGIN FORM) */
        .login-container {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100vh;
            padding: 10% 15%;
            background-color: #0e1117;
        }}
        
        /* Input Alanları Makyajı */
        .stTextInput input {{
            background-color: #1a1c24 !important;
            border: 1px solid #2d2f36 !important;
            color: white !important;
            border-radius: 8px;
            padding: 15px;
        }}
        .stTextInput input:focus {{
            border-color: #FF4B4B !important;
            box-shadow: 0 0 0 1px #FF4B4B !important;
        }}
        
        /* Footer Gizle */
        footer {{display: none !important;}}
        header {{display: none !important;}}
        
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🔐 3. DOĞRULAMA (MEVCUT YAPI KORUNDU)
# ==============================================================================
def verify_user(username, password):
    if username in USERS and USERS[username]["pass"] == password:
        return USERS[username]
    return None

# ==============================================================================
# 🚀 4. RENDER FONKSİYONU (YENİ LAYOUT)
# ==============================================================================
def render_login_page():
    # Rastgele veri çek
    bg_image, tip_text = get_gta_assets()
    
    # CSS'i yükle
    inject_login_css(bg_image)
    
    # EKRANI İKİYE BÖL: [SOL: Görsel %60] - [SAĞ: Form %40]
    col_visual, col_form = st.columns([1.6, 1])
    
    # --- SOL KOLON (GTA GÖRSEL & BİLGİ) ---
    with col_visual:
        st.markdown(f"""
        <div class="gta-visual">
            <div class="gta-content">
                <div class="gta-title">ARTIS<br>SYSTEMS</div>
                <div class="gta-tip-box">
                    <div class="gta-tip-text">{tip_text}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- SAĞ KOLON (GİRİŞ FORMU) ---
    with col_form:
        # Dikey ortalama için container
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # Logo veya İkon
        st.markdown("## 👋 Tekrar Hoş Geldiniz")
        st.markdown("<p style='color: #666; margin-bottom: 30px;'>Hesabınıza erişmek için bilgilerinizi girin.</p>", unsafe_allow_html=True)

        # Form Başlat
        with st.form("login_form"):
            username = st.text_input("Kullanıcı Adı", placeholder="admin", key="login_user")
            password = st.text_input("Şifre", type="password", placeholder="••••••", key="login_pass")
            
            st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)
            
            submit_btn = st.form_submit_button("GİRİŞ YAP", use_container_width=True, type="primary")
        
        # Form Logic (Eski kodunuzdaki mantıkla aynı)
        if submit_btn:
            with st.spinner("Sistem başlatılıyor..."):
                time.sleep(0.8) # Efekt için bekleme
                user = verify_user(username, password)
                
                if user:
                    st.session_state.logged_in = True
                    st.session_state.user_data = user
                    
                    if user['role'] == 'admin':
                        st.toast(f"Yönetici Erişimi: {user['name']}", icon="🛡️")
                    else:
                        st.toast(f"Hoş geldin, {user['name']}!", icon="🚀")
                    
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Hatalı kullanıcı adı veya şifre.")

        # Alt Bilgi (Footer benzeri)
        st.markdown("""
            <div style="margin-top: 40px; text-align: center; color: #444; font-size: 12px;">
            ARTIS Global Operations Engine v2.4.1<br>
            Secure Connection
            </div>
        """, unsafe_allow_html=True)
        
        # Demo Bilgisi (Geliştirici için - İstersen kaldırabilirsin)
        with st.expander("🔑 Demo Hesapları", expanded=False):
            st.code("Admin: admin / admin\nUser : demo  / 1234", language="text")

        st.markdown('</div>', unsafe_allow_html=True) # Container kapat
