import streamlit as st
import time

# ==============================================================================
# 🗄️ 1. KULLANICI VERİTABANI (MOCK DATA)
# ==============================================================================
USERS = {
    "demo": {
        "pass": "1234",
        "name": "Ahmet Yılmaz",
        "brand": "Anatolia Home",
        "role": "user",  # Standart kullanıcı
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
        "role": "admin", # [ÖNEMLİ] Bu 'admin' olmazsa panel butonu gözükmez!
        "plan": "Internal",
        "avatar": "SA"
    }
}

# ==============================================================================
# 🎨 2. LOGIN CSS (AURORA THEME)
# ==============================================================================
def inject_login_css():
    st.markdown("""
    <style>
        /* Sidebar'ı Gizle */
        section[data-testid="stSidebar"] { display: none !important; }
        
        /* Ana Arka Plan */
        .stApp {
            background-color: #000000;
            background-image: 
                radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(139, 92, 246, 0.15) 0px, transparent 50%);
        }

        /* Giriş Kartı */
        .login-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(20px);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            text-align: center;
        }

        /* Başlıklar */
        .login-logo { font-size: 42px; margin-bottom: 10px; }
        .login-title { font-size: 24px; font-weight: 700; color: #FFF; margin-bottom: 8px; }
        .login-subtitle { font-size: 14px; color: #A1A1AA; margin-bottom: 30px; }
        
        /* Input Alanlarını Özelleştir */
        .stTextInput input {
            background-color: rgba(0, 0, 0, 0.3) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: white !important;
        }
        .stTextInput input:focus {
            border-color: #3B82F6 !important;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🔐 3. DOĞRULAMA
# ==============================================================================
def verify_user(username, password):
    if username in USERS and USERS[username]["pass"] == password:
        return USERS[username]
    return None

# ==============================================================================
# 🚀 4. RENDER FONKSİYONU
# ==============================================================================
def render_login_page():
    inject_login_css()
    
    # Ortalamak için kolonlar
    col1, col2, col3 = st.columns([1, 1.2, 1])
    
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # HTML Kartı Başlat
        st.markdown("""
        <div class="login-card">
            <div class="login-logo">⚡</div>
            <div class="login-title">ARTIS'e Giriş Yap</div>
            <div class="login-subtitle">Yeni nesil operasyon yönetim sistemi</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Form
        username = st.text_input("Kullanıcı Adı", placeholder="Kullanıcı Adı", label_visibility="collapsed")
        password = st.text_input("Şifre", type="password", placeholder="••••••", label_visibility="collapsed")
        
        st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
        
        if st.button("Giriş Yap", type="primary", use_container_width=True):
            with st.spinner("Kimlik doğrulanıyor..."):
                time.sleep(0.8)
            
            user = verify_user(username, password)
            
            if user:
                st.session_state.logged_in = True
                st.session_state.user_data = user
                
                # Rol tabanlı karşılama mesajı
                if user['role'] == 'admin':
                    st.toast(f"Yönetici Erişimi Doğrulandı: {user['name']}", icon="🛡️")
                else:
                    st.toast(f"Hoş geldin, {user['name']}!", icon="🚀")
                
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Hatalı kullanıcı adı veya şifre.")

        # Demo Bilgisi (Geliştirici İpuçları)
        with st.expander("🔑 Giriş Bilgileri"):
            st.code("""
Admin: admin / admin
User : demo  / 1234
            """, language="text")
