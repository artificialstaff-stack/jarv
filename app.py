import streamlit as st
import sys
import os
import time

# Brain modülünü güvenli import et
try:
    import brain
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))
    try:
        import brain
    except ImportError:
        sys.path.append(os.path.dirname(__file__))
        import brain

# ==========================================
# 🔐 MÜŞTERİ VERİTABANI (SİMÜLASYON)
# Buraya müşterilerini ekleyebilirsin.
# ==========================================
CLIENT_DATABASE = {
    "demo": {
        "password": "1234",
        "name": "Ahmet Yılmaz",
        "brand": "Anatolia Tekstil",
        "sector": "Tekstil & Moda",
        "product": "İpek Eşarp Koleksiyonu"
    },
    "tech": {
        "password": "admin",
        "name": "Mehmet Demir",
        "brand": "TechOne",
        "sector": "Yazılım",
        "product": "SaaS Yazılımı"
    }
}

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(
    page_title="ARTIS | Giriş Yap",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed" # Girişte menü kapalı olsun
)

# 2. PREMIUM CSS (Giriş Ekranı Odaklı)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .stApp {
        background-color: #0E1117;
        color: #E0E0E0;
    }

    /* GİRİŞ KUTUSU TASARIMI */
    .login-container {
        background-color: #161B22;
        padding: 40px;
        border-radius: 12px;
        border: 1px solid #30363D;
        box-shadow: 0 20px 50px rgba(0,0,0,0.7);
        text-align: center;
    }
    
    /* Input Alanları */
    .stTextInput input {
        background-color: #0D1117 !important;
        border: 1px solid #30363D;
        color: white;
        padding: 10px;
        border-radius: 6px;
    }
    .stTextInput input:focus {
        border-color: #1F6FEB;
        box-shadow: 0 0 0 1px #1F6FEB;
    }

    /* Buton */
    .stButton button {
        background-color: #238636; /* GitHub Yeşili - Güven Verir */
        color: white;
        font-weight: 600;
        border: none;
        width: 100%;
        padding: 12px;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #2EA043;
    }

    /* Sidebar ve Menü */
    section[data-testid="stSidebar"] { background-color: #161B22; border-right: 1px solid #30363D; }
    
    /* Chat Alanı */
    .stChatInput { position: fixed; bottom: 30px; width: 70% !important; left: 55%; transform: translateX(-50%); z-index: 999; }
    
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# 🔒 DURUM 1: GİRİŞ EKRANI (LOGIN PAGE)
# =========================================================
if not st.session_state.logged_in:
    
    # Ekranı ortalamak için kolonlar
    col1, col2, col3 = st.columns([1, 0.8, 1])
    
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        # Logo
        st.markdown("<h1 style='text-align:center; font-size: 3rem;'>ARTIS <span style='color:#1F6FEB'>.OS</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8B949E; margin-bottom:30px;'>Authorized Personnel Only</p>", unsafe_allow_html=True)
        
        # Login Kutusu
        with st.container():
            st.markdown('<div class="login-container">', unsafe_allow_html=True)
            
            username = st.text_input("Kullanıcı Adı", placeholder="ID Giriniz")
            password = st.text_input("Şifre", type="password", placeholder="••••••••")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("SİSTEME GİRİŞ YAP"):
                # Kullanıcı Doğrulama
                if username in CLIENT_DATABASE and CLIENT_DATABASE[username]["password"] == password:
                    
                    # Kullanıcı verisini çek ve kaydet
                    user_info = CLIENT_DATABASE[username]
                    st.session_state.user_data = user_info
                    st.session_state.logged_in = True
                    
                    # Toast mesajı
                    st.toast(f"Hoş geldiniz, {user_info['name']}", icon="✅")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Hatalı kullanıcı adı veya şifre.")
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; color:#444; font-size:12px; margin-top:20px;'>© 2026 ARTIS Secure Systems. All rights reserved.</p>", unsafe_allow_html=True)

# =========================================================
# 🔓 DURUM 2: ANA UYGULAMA (DASHBOARD)
# =========================================================
else:
    # Sidebar'ı tekrar aç
    st.markdown("<style>section[data-testid='stSidebar'] {display: block !important;}</style>", unsafe_allow_html=True)

    # --- SIDEBAR ---
    with st.sidebar:
        # Marka Logosu
        brand_name = st.session_state.user_data['brand']
        st.markdown(f"""
        <div style="background:#21262D; padding:20px; border-radius:10px; text-align:center; border:1px solid #30363D; margin-bottom:20px;">
            <h2 style="margin:0; color:#E0E0E0; font-size:24px;">{brand_name[:2].upper()}</h2>
            <div style="color:#8B949E; font-size:14px;">{brand_name}</div>
        </div>
        """, unsafe_allow_html=True)
        
        page = st.radio("NAVIGASYON", ["💬 AI ASİSTAN", "📊 FİNANSAL TABLO", "📦 LOJİSTİK AĞI"], label_visibility="collapsed")
        
        st.markdown("---")
        st.caption(f"Kullanıcı: **{st.session_state.user_data['name']}**")
        
        if st.button("Güvenli Çıkış", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.messages = []
            st.rerun()

    # --- SAYFA İÇERİKLERİ ---
    
    # 1. AI ASİSTAN
    if page == "💬 AI ASİSTAN":
        if not st.session_state.messages:
            # Boş ekran yerine selamlama
            st.markdown(f"<h1 style='text-align:center; margin-top: 50px;'>Merhaba, {st.session_state.user_data['name']} 👋</h1>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center; color:#8B949E;'>{st.session_state.user_data['brand']} operasyonları için hazırım.</p>", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            if c1.button("💰 Maliyet Analizi", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": "Lojistik maliyetlerimi hesapla."})
                st.rerun()
            if c2.button("📦 Stok Durumu", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": "Depodaki stok durumu nedir?"})
                st.rerun()
            if c3.button("🚀 Büyüme Planı", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": "ABD pazarında nasıl büyüyebilirim?"})
                st.rerun()
        
        else:
            chat_box = st.container(height=600)
            for msg in st.session_state.messages:
                with chat_box.chat_message(msg["role"]):
                    st.markdown(msg["content"])
        
        if prompt := st.chat_input("Bir talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.rerun()

        # Cevap Üretme
        if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
            # Chat ekranını tekrar çiz (kullanıcı mesajını göster)
            if st.session_state.messages: # Tekrar kontrol
                 with st.chat_message("user"):
                    st.markdown(st.session_state.messages[-1]["content"])

            with st.chat_message("assistant"):
                placeholder = st.empty()
                full_resp = ""
                try:
                    stream = brain.get_streaming_response(st.session_state.messages, st.session_state.user_data)
                    for chunk in stream:
                        full_resp += chunk
                        placeholder.markdown(full_resp + "▌")
                    placeholder.markdown(full_resp)
                except Exception:
                    placeholder.error("Bağlantı hatası.")
            st.session_state.messages.append({"role": "assistant", "content": full_resp})

    # 2. FİNANS
    elif page == "📊 FİNANSAL TABLO":
        st.markdown("## 📊 Finansal Genel Bakış")
        col1, col2, col3 = st.columns(3)
        col1.metric("Aylık Ciro", "$45,200", "+%12")
        col2.metric("Toplam Kâr", "$18,400", "+%8")
        col3.metric("Lojistik Gideri", "$4,100", "-%2")
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

    # 3. LOJİSTİK
    elif page == "📦 LOJİSTİK AĞI":
        st.markdown("## 📦 Canlı Sevkiyat Takibi")
        st.success(f"✅ {st.session_state.user_data['product']} sevkiyatı gümrükten geçti.")
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
