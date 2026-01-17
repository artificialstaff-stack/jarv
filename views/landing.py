import streamlit as st

def render_landing():
    # --- MANUS / PERPLEXITY STYLE CSS ---
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

        /* 1. GENEL AYARLAR (Light Theme) */
        .stApp {
            background-color: #F9F9F9; /* Manus arkaplan rengi */
            color: #000000;
            font-family: 'Inter', sans-serif;
        }
        
        /* Streamlit varsayılanlarını temizle */
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            max-width: 100% !important;
        }
        header, footer { display: none !important; }

        /* 2. NAVBAR (ÜST MENÜ) */
        .navbar-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 18px 40px;
            background-color: transparent;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        .nav-left {
            display: flex;
            align-items: center;
            gap: 40px;
        }
        
        .nav-logo {
            font-family: 'Times New Roman', serif; /* Serif Logo */
            font-size: 26px;
            font-weight: 600;
            color: #000;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .nav-links {
            display: flex;
            gap: 24px;
        }
        .nav-link {
            font-size: 14px;
            color: #555;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }
        .nav-link:hover { color: #000; }

        /* 3. HERO (BAŞLIK ALANI) */
        .hero-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 8vh; /* Görseldeki boşluk */
            text-align: center;
        }
        
        .hero-title {
            font-family: 'Times New Roman', serif; /* Manus Başlık Fontu */
            font-size: 64px;
            color: #111;
            font-weight: 400;
            letter-spacing: -1.5px;
            margin-bottom: 40px;
        }

        /* 4. ARAMA ÇUBUĞU (EN ÖNEMLİ KISIM) */
        div[data-testid="stForm"] {
            width: 100%;
            max-width: 750px; /* Genişlik görseldeki ile aynı */
            margin: 0 auto;
            position: relative;
        }
        
        div[data-testid="stTextInput"] input {
            background-color: #FFFFFF !important;
            border: 1px solid #E5E5E5 !important;
            color: #000 !important;
            border-radius: 20px !important; /* Köşeler */
            padding: 22px 60px 22px 50px !important; /* İkonlar için boşluk */
            font-size: 17px !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.03);
            transition: all 0.2s;
        }
        div[data-testid="stTextInput"] input:focus {
            border-color: #DDD !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }
        
        /* Sol Taraftaki (+) İkonu (Pseudo-element inputa eklenemediği için CSS hilesi) */
        /* Streamlit inputunun başına ikon koymak zor olduğu için placeholder kullanıyoruz veya dışarıdan div ekliyoruz.
           Burada görsel sadelik için inputu temiz bırakıyoruz. */

        /* SAĞDAKİ SİYAH OK BUTONU (Submit) */
        div[data-testid="stFormSubmitButton"] button {
            position: absolute;
            top: -62px;
            right: 12px;
            background-color: #000000 !important; /* Simsiyah */
            color: white !important;
            border-radius: 50% !important;
            width: 36px !important;
            height: 36px !important;
            border: none !important;
            padding: 0 !important;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.2s;
            z-index: 5;
        }
        div[data-testid="stFormSubmitButton"] button:hover {
            transform: scale(1.1);
            background-color: #222 !important;
        }
        div[data-testid="stFormSubmitButton"] button::after {
            content: '↑'; /* Yukarı Ok */
            font-size: 18px;
            font-weight: bold;
        }
        /* "GO" yazısını gizle */
        div[data-testid="stFormSubmitButton"] button p { display: none; }


        /* 5. KARTLAR (GRID YAPISI) */
        .section-label {
            max-width: 750px;
            margin: 60px auto 15px auto;
            text-align: left;
            font-size: 14px;
            font-weight: 600;
            color: #111;
            padding-left: 5px;
        }

        /* Streamlit butonlarını KART gibi gösterme */
        div.stButton > button {
            width: 100%;
            background-color: #FFFFFF !important;
            border: 1px solid #EAEAEA !important;
            border-radius: 12px !important;
            padding: 15px 20px !important;
            text-align: left !important;
            height: auto !important;
            min-height: 80px !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: flex-start !important;
            box-shadow: none !important;
            transition: all 0.2s;
        }
        div.stButton > button:hover {
            border-color: #CCC !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
            transform: translateY(-1px);
        }
        div.stButton > button p {
            text-align: left;
            line-height: 1.4;
            color: #333;
        }

        /* Navbar Butonları Özel Stil */
        /* Giriş Yap (Siyah) */
        button[key="login_btn"] {
            background-color: #000 !important;
            color: #fff !important;
            border-radius: 8px !important;
            padding: 6px 16px !important;
            font-size: 13px !important;
            min-height: 0 !important;
            height: 36px !important;
            border: none !important;
        }
        /* Kaydol (Beyaz) */
        button[key="signup_btn"] {
            background-color: #fff !important;
            color: #000 !important;
            border: 1px solid #E5E5E5 !important;
            border-radius: 8px !important;
            padding: 6px 16px !important;
            font-size: 13px !important;
            min-height: 0 !important;
            height: 36px !important;
        }

        </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR (HTML + Streamlit Columns) ---
    # Navbar'ı HTML ve Streamlit kolonlarını karıştırarak yapıyoruz ki butonlar çalışsın.
    
    # 1. Logo ve Linkler (Sol)
    # 2. Butonlar (Sağ)
    
    col_nav_left, col_nav_spacer, col_btn1, col_btn2 = st.columns([6, 4, 0.8, 0.8])
    
    with col_nav_left:
        st.markdown("""
        <div class="nav-left">
            <div class="nav-logo">
                <img src="https://cdn-icons-png.flaticon.com/512/16020/16020054.png" width="24" style="opacity:0.8"/> ARTIS
            </div>
            <div class="nav-links">
                <a class="nav-link">Özellikler</a>
                <a class="nav-link">Kaynaklar</a>
                <a class="nav-link">Fiyatlandırma</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_btn1:
        # "Giriş Yap" -> Siyah Buton (CSS ile key="login_btn" hedeflendi)
        if st.button("Giriş yap", key="login_btn"):
            st.session_state.page = "Login"
            st.rerun()
            
    with col_btn2:
        # "Kaydol" -> Beyaz Buton (CSS ile key="signup_btn" hedeflendi)
        if st.button("Kaydol", key="signup_btn"):
            st.session_state.page = "Login"
            st.rerun()

    # --- HERO AREA ---
    st.markdown('<div class="hero-section"><div class="hero-title">Sizin için ne yapabilirim?</div></div>', unsafe_allow_html=True)

    # --- SEARCH BAR ---
    with st.form("landing_search", border=False):
        # Inputu ortalamak için boşluk kolonları
        c_l, c_center, c_r = st.columns([1, 6, 1])
        with c_center:
            # Placeholder başına boşluk koyarak ikona yer açıyoruz
            prompt = st.text_input("search", placeholder="      Lojistik maliyetlerini analiz et...", label_visibility="collapsed")
            # CSS ile Inputun içine taşınan Siyah Yuvarlak Buton
            submit = st.form_submit_button("GO")
            
            # "+" İkonu (Inputun içinde gibi görünen sol ikon)
            st.markdown("""
            <style>
            /* Inputun solundaki + ikonunu simüle eden CSS */
            div[data-testid="stTextInput"]::before {
                content: '+';
                position: absolute;
                left: 20px;
                top: 50%;
                transform: translateY(-50%);
                font-size: 20px;
                color: #999;
                z-index: 2;
                pointer-events: none;
            }
            </style>
            """, unsafe_allow_html=True)

    # --- ÖNERİ KARTLARI ---
    st.markdown('<div class="section-label">Ne inşa ediyorsunuz?</div>', unsafe_allow_html=True)

    # Grid Yapısı: 750px genişliğinde, ortalanmış
    col_grid_main = st.columns([1, 6, 1])[1] # Ortadaki kolonu al
    
    with col_grid_main:
        c_row1_1, c_row1_2 = st.columns(2)
        
        with c_row1_1:
            # Kart 1
            if st.button("📦 **Lojistik Maliyet Analizi**\n\nTürkiye'den ABD depolarına en uygun rota ve maliyet hesaplaması.", use_container_width=True):
                st.session_state.pending_prompt = "Lojistik maliyet analizi yap"
                st.session_state.page = "Login"
                st.rerun()
        
        with c_row1_2:
            # Kart 2
            if st.button("⚖️ **Gümrük Mevzuatı**\n\nGTIP koduna göre vergi oranları, belge listesi ve yasal gereklilikler.", use_container_width=True):
                st.session_state.pending_prompt = "Gümrük mevzuatı kontrolü"
                st.session_state.page = "Login"
                st.rerun()

        # İkinci Satır
        c_row2_1, c_row2_2 = st.columns(2)
        with c_row2_1:
            if st.button("📈 **Rakip Pazar Analizi**\n\nAmazon'daki rakiplerin fiyat, stok ve yorum stratejilerini analiz et.", use_container_width=True):
                st.session_state.pending_prompt = "Rakip pazar analizi yap"
                st.session_state.page = "Login"
                st.rerun()
        with c_row2_2:
            if st.button("🤖 **Otomasyon Kurulumu**\n\nSiparişten teslimata %100 otonom iş akışı oluştur ve entegre et.", use_container_width=True):
                st.session_state.pending_prompt = "Otomasyon kurulumu başlat"
                st.session_state.page = "Login"
                st.rerun()

    # --- LOGIC ---
    if submit and prompt:
        st.session_state.pending_prompt = prompt
        st.session_state.page = "Login"
        st.rerun()

if __name__ == "__main__":
    render_landing()
