import streamlit as st

def render_landing():
    # --- PIXEL PERFECT MANUS CSS ---
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Newsreader:ital,wght@0,400;0,500;1,400&display=swap');

        /* 1. TEMEL AYARLAR */
        .stApp {
            background-color: #F9F9F9;
            color: #111111;
            font-family: 'Inter', sans-serif;
        }
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            max-width: 100% !important;
        }
        header, footer { display: none !important; }

        /* 2. NAVBAR (ÜST MENÜ) */
        .navbar-container {
            width: 100%;
            padding: 16px 48px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: transparent;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        /* Logo ve Linkler */
        .nav-left {
            display: flex;
            align-items: center;
            gap: 40px;
        }
        .logo-text {
            font-family: 'Newsreader', serif;
            font-size: 26px;
            font-weight: 600;
            color: #000;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
        }
        .nav-items {
            display: flex;
            gap: 24px;
        }
        .nav-item {
            font-size: 14px;
            color: #555;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }
        .nav-item:hover { color: #000; }

        /* Sağ Taraftaki Butonlar */
        div[data-testid="column"] button[key="login_btn"] {
            background-color: #111 !important;
            color: #fff !important;
            border: 1px solid #111 !important;
            border-radius: 8px !important;
            height: 36px !important;
            font-size: 13px !important;
        }
        div[data-testid="column"] button[key="signup_btn"] {
            background-color: #fff !important;
            color: #111 !important;
            border: 1px solid #E0E0E0 !important;
            border-radius: 8px !important;
            height: 36px !important;
            font-size: 13px !important;
        }

        /* 3. HERO (BAŞLIK) */
        .hero-wrapper {
            margin-top: 10vh;
            margin-bottom: 40px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .hero-heading {
            font-family: 'Newsreader', serif;
            font-size: 64px;
            font-weight: 400;
            color: #111;
            letter-spacing: -1.2px;
            line-height: 1.1;
        }

        /* 4. SEARCH INPUT (HAP ŞEKLİ) */
        div[data-testid="stForm"] {
            max-width: 720px;
            margin: 0 auto;
            position: relative;
        }

        div[data-testid="stTextInput"] input {
            height: 64px !important;
            border-radius: 32px !important;
            border: 1px solid #E0E0E0 !important;
            background-color: #FFFFFF !important;
            color: #111 !important;
            padding-left: 56px !important;
            padding-right: 60px !important;
            font-size: 18px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        }
        div[data-testid="stTextInput"] input:focus {
            border-color: #CCC !important;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
            outline: none !important;
        }

        /* SOL "+" İKONU */
        div[data-testid="stTextInput"]::after {
            content: '+';
            position: absolute;
            left: 24px;
            top: 50%;
            transform: translateY(-55%);
            font-size: 24px;
            color: #999;
            font-weight: 300;
            pointer-events: none;
            z-index: 5;
        }

        /* SAĞ "OK" BUTONU */
        div[data-testid="stFormSubmitButton"] button {
            position: absolute;
            top: -56px;
            right: 8px;
            width: 48px !important;
            height: 48px !important;
            border-radius: 50% !important;
            background-color: #000 !important;
            color: #FFF !important;
            border: none !important;
            padding: 0 !important;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
        }
        div[data-testid="stFormSubmitButton"] button::before {
            content: '↑';
            font-size: 20px;
            font-weight: 500;
        }
        div[data-testid="stFormSubmitButton"] button p { display: none; }

        /* 5. ÖNERİ KARTLARI */
        .label-text {
            max-width: 720px;
            margin: 60px auto 16px auto;
            padding-left: 4px;
            font-size: 14px;
            font-weight: 600;
            color: #111;
        }

        div.stButton > button {
            width: 100%;
            background-color: #FFFFFF !important;
            border: 1px solid #EAEAEA !important;
            border-radius: 12px !important;
            padding: 16px 20px !important;
            height: auto !important;
            min-height: 84px !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: flex-start !important;
            text-align: left !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02) !important;
        }
        div.stButton > button:hover {
            border-color: #CCC !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
        }
        div.stButton > button p {
            color: #111;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR LAYOUT ---
    col_nav_1, col_nav_spacer, col_nav_2 = st.columns([2, 5, 1.5])
    
    with col_nav_1:
        st.markdown("""
        <div class="nav-left">
            <a href="#" class="logo-text">⚡ ARTIS</a>
            <div class="nav-items" style="margin-left:20px;">
                <a href="#" class="nav-item">Özellikler</a>
                <a href="#" class="nav-item">Kaynaklar</a>
                <a href="#" class="nav-item">Fiyatlandırma</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_nav_2:
        c_btn_1, c_btn_2 = st.columns(2)
        with c_btn_1:
            if st.button("Giriş yap", key="login_btn"):
                st.session_state.page = "Login"
                st.rerun()
        with c_btn_2:
            if st.button("Kaydol", key="signup_btn"):
                st.session_state.page = "Login"
                st.rerun()

    # --- HERO AREA ---
    st.markdown("""
        <div class="hero-wrapper">
            <h1 class="hero-heading">Sizin için ne yapabilirim?</h1>
        </div>
    """, unsafe_allow_html=True)

    # --- SEARCH FORM ---
    with st.form("search_form", border=False):
        c_l, c_center, c_r = st.columns([1, 6, 1])
        with c_center:
            prompt = st.text_input("prompt", placeholder="Lojistik maliyetlerini analiz et...", label_visibility="collapsed")
            submit = st.form_submit_button("Submit")

    # --- SUGGESTIONS ---
    st.markdown('<div class="label-text">Ne inşa ediyorsunuz?</div>', unsafe_allow_html=True)

    col_grid = st.columns([1, 6, 1])[1]
    
    with col_grid:
        r1_c1, r1_c2 = st.columns(2)
        
        with r1_c1:
            if st.button("📦 **Lojistik Maliyet Analizi**\n\nTürkiye'den ABD'ye en uygun rota ve depo maliyeti hesaplaması.", use_container_width=True):
                st.session_state.pending_prompt = "Lojistik maliyet analizi yap"
                st.session_state.page = "Login"
                st.rerun()

        with r1_c2:
            if st.button("⚖️ **Gümrük Mevzuatı**\n\nGTIP koduna göre vergi oranları ve gerekli belge listesi.", use_container_width=True):
                st.session_state.pending_prompt = "Gümrük mevzuatı kontrolü"
                st.session_state.page = "Login"
                st.rerun()

        r2_c1, r2_c2 = st.columns(2)
        
        with r2_c1:
            if st.button("📈 **Rakip Pazar Analizi**\n\nAmazon'daki rakiplerin fiyat ve stok stratejilerini analiz et.", use_container_width=True):
                st.session_state.pending_prompt = "Rakip pazar analizi yap"
                st.session_state.page = "Login"
                st.rerun()

        with r2_c2:
            if st.button("🤖 **Otomasyon Kurulumu**\n\nSiparişten teslimata %100 otonom iş akışı oluştur.", use_container_width=True):
                st.session_state.pending_prompt = "Otomasyon kurulumu başlat"
                st.session_state.page = "Login"
                st.rerun()

    if submit and prompt:
        st.session_state.pending_prompt = prompt
        st.session_state.page = "Login"
        st.rerun()

if __name__ == "__main__":
    render_landing()
