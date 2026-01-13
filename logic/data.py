import streamlit as st
import time

# ==============================================================================
# 🗄️ 1. MOCK USER DATABASE (GELİŞMİŞ VERİ)
# ==============================================================================
# Gerçek bir SaaS sisteminde bu veriler veritabanından (PostgreSQL/Firebase) gelir.
USERS = {
    "demo": {
        "pass": "1234",
        "name": "Ahmet Yılmaz",
        "brand": "Anatolia Home",
        "role": "CEO & Kurucu",
        "email": "ahmet@anatolia.com",
        "plan": "Enterprise",
        "avatar": "AY"
    },
    "ops": {
        "pass": "1234",
        "name": "Elif Kaya",
        "brand": "Anatolia Ops",
        "role": "Operasyon Müdürü",
        "email": "elif@anatolia.com",
        "plan": "Pro",
        "avatar": "EK"
    },
    "depo": {
        "pass": "1234",
        "name": "Mehmet Demir",
        "brand": "Washington Hub",
        "role": "Depo Sorumlusu",
        "email": "mehmet@anatolia.com",
        "plan": "Starter",
        "avatar": "MD"
    },
    "admin": {
        "pass": "admin",
        "name": "Sistem Yöneticisi",
        "brand": "ARTIS HQ",
        "role": "Süper Admin",
        "email": "support@artis.ai",
        "plan": "Internal",
        "avatar": "SA"
    }
}

# ==============================================================================
# 🎨 2. LOGIN SAYFASI CSS
# ==============================================================================
def inject_login_css():
    st.markdown("""
    <style>
        /* Giriş sayfasında Sidebar'ı gizle */
        section[data-testid="stSidebar"] { display: none !important; }
        
        /* Ana arka plan düzenlemesi (Merkezleme) */
        .stApp {
            align-items: center;
            justify-content: center;
            display: flex;
        }

        /* Giriş Kartı */
        .login-card {
            background-color: #09090B;
            border: 1px solid #27272A;
            border-radius: 24px;
            padding: 40px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
            width: 100%;
            max-width: 420px;
            margin: auto;
            position: relative;
            overflow: hidden;
        }
        
        /* Üstteki Renkli Çizgi (Brand Accent) */
        .login-card::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; height: 4px;
            background: linear-gradient(90deg, #3B82F6, #8B5CF6);
        }

        /* Başlıklar */
        .login-title { font-size: 24px; font-weight: 700; color: #FFF; margin-bottom: 8px; text-align: center; }
        .login-subtitle { font-size: 14px; color: #A1A1AA; text-align: center; margin-bottom: 30px; }
        
        /* Alt Bilgi */
        .login-footer {
            margin-top: 20px;
            text-align: center;
            font-size: 12px;
            color: #52525B;
        }
        .login-footer a { color: #71717A; text-decoration: none; transition: 0.3s; }
        .login-footer a:hover { color: #E4E4E7; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🔐 3. DOĞRULAMA MANTIĞI
# ==============================================================================
def verify_user(username, password):
    """Kullanıcı adı ve şifreyi kontrol eder."""
    if username in USERS:
        if USERS[username]["pass"] == password:
            return USERS[username]
    return None

# ==============================================================================
# 🚀 4. ANA RENDER FONKSİYONU
# ==============================================================================
def render_login_page():
    inject_login_css()
    
    # Sayfayı dikey ve yatayda ortalamak için boş kolonlar
    col1, col2, col3 = st.columns([1, 1.2, 1])
    
    with col2:
        # Konteyner ile "Kart" görünümü oluşturuyoruz
        with st.container(border=False):
            st.markdown("""
            <div class="login-card">
                <div style="display:flex; justify-content:center; margin-bottom:20px;">
                    <div style="width:50px; height:50px; background:linear-gradient(135deg, #3B82F6, #8B5CF6); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:28px;">⚡</div>
                </div>
                <div class="login-title">ARTIS'e Giriş Yap</div>
                <div class="login-subtitle">Yeni nesil operasyon yönetim sistemi</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Form Alanı (Streamlit Inputları HTML içine gömülemediği için altına koyuyoruz)
            # Görsel bütünlük için CSS ile bunları da "card" gibi hissettireceğiz veya temiz tutacağız.
            
            username = st.text_input("Kullanıcı Adı", placeholder="demo", label_visibility="collapsed")
            password = st.text_input("Şifre", type="password", placeholder="••••••", label_visibility="collapsed")
            
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            
            if st.button("Giriş Yap", type="primary", use_container_width=True):
                with st.spinner("Kimlik doğrulanıyor..."):
                    time.sleep(0.8) # Gerçekçilik efekti
                
                user = verify_user(username, password)
                
                if user:
                    st.session_state.logged_in = True
                    st.session_state.user_data = user
                    st.toast(f"Hoş geldin, {user['name']}!", icon="👋")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Hatalı kullanıcı adı veya şifre.")

            # Hızlı Erişim (Demo Amaçlı)
            with st.expander("🔑 Demo Hesap Bilgileri", expanded=False):
                st.code("""User: demo\nPass: 1234""", language="text")

            # Footer
            st.markdown("""
            <div class="login-footer">
                <a href="#">Şifremi Unuttum</a> • <a href="#">Destek ile İletişime Geç</a>
                <br><br>
                © 2026 ARTIS AI Inc.
            </div>
            """, unsafe_allow_html=True)
