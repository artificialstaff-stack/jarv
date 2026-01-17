import streamlit as st
import time
import random

# ==============================================================================
# ⚙️ SAYFA YAPILANDIRMASI (EN BAŞTA)
# ==============================================================================
st.set_page_config(
    page_title="ARTIS - Giriş",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 🗄️ KULLANICI VERİLERİ (MEVCUT YAPI)
# ==============================================================================
USERS = {
    "demo": {"pass": "1234", "name": "Ahmet Yılmaz", "role": "user"},
    "admin": {"pass": "admin", "name": "Sistem Yöneticisi", "role": "admin"}
}

# ==============================================================================
# 🎨 GTA TARZI İÇERİK HAVUZU
# ==============================================================================
def get_gta_content():
    # Arka plan görselleri (Yüksek Kalite)
    images = [
        "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=2070&auto=format&fit=crop", # Chip/Tech
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Network/Globe
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop"  # Cyberpunk
    ]
    
    # Animasyonlu Yazılar (Başlık + Alt Açıklama)
    stories = [
        {"title": "GLOBAL OPERATIONS", "desc": "Dünya genelindeki tüm veri akışı tek bir merkezden yönetiliyor."},
        {"title": "YAPAY ZEKA ENTEGRASYONU", "desc": "ARTIS AI motoru, verimliliği %40 artırmak için devrede."},
        {"title": "MAKSİMUM GÜVENLİK", "desc": "Uçtan uca şifreleme ile verileriniz siber tehditlere karşı koruma altında."}
    ]
    
    return random.choice(images), random.choice(stories)

# ==============================================================================
# 🖌️ CSS VE TASARIM MOTORU
# ==============================================================================
def inject_css(bg_image):
    st.markdown(f"""
    <style>
        /* 1. TÜM BOŞLUKLARI VE KAYDIRMAYI YOK ET */
        .stApp {{ overflow: hidden !important; }}
        
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}
        
        .block-container {{
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }}
        
        /* 2. SOL TARAF (Görsel ve Animasyon) */
        .left-panel {{
            height: 100vh;
            width: 100%;
            background-image: url('{bg_image}');
            background-size: cover;
            background-position: center;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 80px;
        }}
        
        .left-panel::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to right, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.4) 100%);
            z-index: 1;
        }}
        
        .content-box {{
            position: relative;
            z-index: 2;
            max-width: 80%;
            animation: slideIn 1s ease-out;
        }}
        
        .big-title {{
            font-size: 5rem;
            font-weight: 900;
            line-height: 0.9;
            color: #ffffff;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: -2px;
            text-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        
        .sub-desc {{
            font-size: 1.2rem;
            color: #d1d5db;
            border-left: 4px solid #3b82f6; /* Mavi vurgu */
            padding-left: 20px;
            background: linear-gradient(90deg, rgba(0,0,0,0.5), transparent);
        }}

        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateX(-50px); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}

        /* 3. SAĞ TARAF (Login Formu) */
        .right-panel {{
            height: 100vh;
            background-color: #09090b; /* Çok koyu gri/siyah */
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }}
        
        /* Glassmorphism Giriş Kartı */
        .login-card {{
            width: 380px; /* Daha kompakt genişlik */
            padding: 40px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
            backdrop-filter: blur(10px);
        }}
        
        .card-header {{
            font-size: 24px;
            font-weight: 700;
            color: white;
            margin-bottom: 5px;
            text-align: center;
        }}
        
        .card-sub {{
            font-size: 13px;
            color: #a1a1aa;
            text-align: center;
            margin-bottom: 30px;
        }}

        /* Input alanlarını özelleştir */
        .stTextInput input {{
            background-color: #18181b !important;
            border: 1px solid #27272a !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 10px 15px !important;
            font-size: 14px !important;
        }}
        
        .stTextInput input:focus {{
            border-color: #3b82f6 !important;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
        }}
        
        /* Checkbox Stili */
        .stCheckbox label span {{
            color: #a1a1aa !important;
            font-size: 13px !important;
        }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🔐 GİRİŞ MANTIĞI
# ==============================================================================
def render_login_page():
    bg_image, story = get_gta_content()
    inject_css(bg_image)
    
    # Ekranı Böl: Sol (%65) - Sağ (%35)
    col1, col2 = st.columns([1.8, 1])
    
    # --- SOL KOLON (Görsel Hikaye) ---
    with col1:
        st.markdown(f"""
        <div class="left-panel">
            <div class="content-box">
                <div class="big-title">{story['title']}</div>
                <div class="sub-desc">{story['desc']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- SAĞ KOLON (Giriş Formu) ---
    with col2:
        # Formu dikeyde ortalamak için bir wrapper
        st.markdown('<div class="right-panel">', unsafe_allow_html=True)
        
        # Giriş Kartı Başlangıcı
        st.markdown(f"""
        <div class="login-card">
            <div class="card-header">Hoş Geldiniz</div>
            <div class="card-sub">ARTIS Operasyon Paneline erişin</div>
        """, unsafe_allow_html=True)

        # Form
        with st.form("login_form", border=False):
            username = st.text_input("Kullanıcı Adı", placeholder="örn: admin", label_visibility="collapsed")
            st.write("") # Küçük boşluk
            password = st.text_input("Şifre", type="password", placeholder="••••••••", label_visibility="collapsed")
            
            # Form İçi Layout: Beni Hatırla ve Buton
            c1, c2 = st.columns([1,1])
            with c1:
                remember = st.checkbox("Beni Hatırla")
            
            st.write("")
            submit = st.form_submit_button("Giriş Yap", type="primary", use_container_width=True)

        # Şifremi Unuttum (Buton görünümünde link)
        if st.button("Şifremi Unuttum?", type="tertiary", use_container_width=True):
             st.toast("Lütfen sistem yöneticisi ile iletişime geçin: it@artis.com", icon="🔒")
        
        # HTML Kart Kapanışı
        st.markdown('</div>', unsafe_allow_html=True) # login-card end
        
        # Alt Bilgi
        st.markdown("""
            <div style="margin-top: 20px; font-size: 11px; color: #52525b;">
            © 2026 ARTIS Inc. v2.4.1
            </div>
            </div> 
        """, unsafe_allow_html=True) # right-panel end

        # İşlem Mantığı
        if submit:
            user = USERS.get(username)
            if user and user["pass"] == password:
                with st.spinner("Kimlik doğrulanıyor..."):
                    time.sleep(0.8)
                st.success(f"Giriş Başarılı! Hoşgeldin {user['name']}")
                st.session_state.logged_in = True
                st.session_state.user_data = user
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Kullanıcı adı veya şifre hatalı.")

# Çalıştır
if __name__ == "__main__":
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        
    if not st.session_state.logged_in:
        render_login_page()
    else:
        st.write("İçerdesiniz!")
        if st.button("Çıkış"):
            st.session_state.logged_in = False
            st.rerun()
