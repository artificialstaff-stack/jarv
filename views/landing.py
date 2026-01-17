import streamlit as st

def render_landing():
    # --- ADVANCED CSS INJECTION FOR MANUS REPLICATION ---
    st.markdown("""
        <style>
        /* IMPORT FONTS: Inter for UI, Newsreader/Times for Headings */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Newsreader:ital,wght@0,400;0,500;1,400&display=swap');

        /* 1. GLOBAL RESET & THEME */
        .stApp {
            background-color: #F9F9F9; /* Exact off-white from Manus */
            color: #111111;
            font-family: 'Inter', sans-serif;
        }
        
        /* Eliminate Streamlit's default padding */
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            max-width: 100% !important;
        }
        header, footer { display: none !important; }

        /* 2. NAVBAR (PIXEL PERFECT FLEXBOX) */
        .navbar-container {
            width: 100%;
            padding: 16px 48px; /* Matches screenshot spacing */
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: transparent;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        /* Left Side: Logo & Links */
        .nav-left {
            display: flex;
            align-items: center;
            gap: 40px;
        }
        .logo-text {
            font-family: 'Newsreader', serif; /* Serif font for Brand */
            font-size: 26px;
            font-weight: 600;
            color: #000;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
        }
        /* Icon placeholder logic can go here if needed */
        
        .nav-items {
            display: flex;
            gap: 24px;
        }
        .nav-item {
            font-size: 14px;
            color: #555;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s ease;
        }
        .nav-item:hover { color: #000; }

        /* Right Side: Auth Buttons (Targeting Streamlit Buttons via Keys) */
        /* Login Button (Black) */
        div[data-testid="column"] button[key="login_btn"] {
            background-color: #111 !important;
            color: #fff !important;
            border: 1px solid #111 !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            padding: 8px 20px !important;
            border-radius: 8px !important;
            line-height: 1 !important;
            height: 36px !important;
            min-height: 0px !important;
            margin: 0 !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        div[data-testid="column"] button[key="login_btn"]:hover {
            background-color: #333 !important;
            border-color: #333 !important;
        }

        /* Signup Button (White/Gray) */
        div[data-testid="column"] button[key="signup_btn"] {
            background-color: #fff !important;
            color: #111 !important;
            border: 1px solid #E0E0E0 !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            padding: 8px 20px !important;
            border-radius: 8px !important;
            line-height: 1 !important;
            height: 36px !important;
            min-height: 0px !important;
            margin: 0 !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        div[data-testid="column"] button[key="signup_btn"]:hover {
            background-color: #F5F5F5 !important;
            border-color: #D0D0D0 !important;
        }

        /* 3. HERO SECTION (CENTERED TYPOGRAPHY) */
        .hero-wrapper {
            margin-top: 12vh; /* Adjusted for visual balance */
            margin-bottom: 40px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .hero-heading {
            font-family: 'Newsreader', serif;
            font-size: 68px; /* Large, bold serif */
            font-weight: 400;
            color: #111;
            letter-spacing: -1.5px;
            line-height: 1.1;
            margin: 0;
        }

        /* 4. SEARCH INPUT (THE PILL) */
        /* Container Logic */
        div[data-testid="stForm"] {
            max-width: 720px;
            margin: 0 auto;
            position: relative;
            /* Box shadow for the entire form area if desired, 
               but placing it on input is safer for Streamlit */
        }

        /* The Input Field Itself */
        div[data-testid="stTextInput"] input {
            height: 68px !important;
            border-radius: 34px !important; /* Fully rounded pill */
            border: 1px solid #E0E0E0 !important;
            background-color: #FFFFFF !important;
            color: #111 !important;
            /* Padding: Left for (+) icon, Right for (->) button */
            padding-left: 60px !important; 
            padding-right: 60px !important; 
            font-size: 19px !important;
            font-family: 'Inter', sans-serif;
            box-shadow: 0 4px 16px rgba(0,0,0,0.06); /* Soft elevation */
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }
        div[data-testid="stTextInput"] input:focus {
            border-color: #CCC !important;
            box-shadow: 0 8px 28px rgba(0,0,0,0.12); /* Lift effect on focus */
            outline: none !important;
        }
        div[data-testid="stTextInput"] input::placeholder {
            color: #999;
            font-weight: 400;
        }

        /* FAKE LEFT (+) ICON using CSS ::after on the container */
        div[data-testid="stTextInput"] {
            position: relative;
        }
        div[data-testid="stTextInput"]::after {
            content: '+';
            position: absolute;
            left: 28px;
            top: 50%;
            transform: translateY(-55%);
            font-size: 26px;
            color: #AAA;
            font-weight: 300;
            pointer-events: none;
            z-index: 5;
        }

        /* SUBMIT BUTTON (Black Circle Arrow) */
        /* Positioning it INSIDE the input on the right */
        div[data-testid="stFormSubmitButton"] button {
            position: absolute;
            top: -62px; /* Needs calibration based on input height */
            right: 10px;
            width: 48px !important;
            height: 48px !important;
            border-radius: 50% !important;
            background-color: #111 !important;
            color: #FFF !important;
            border: none !important;
            padding: 0 !important;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            transition: transform 0.2s ease, background-color 0.2s;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        div[data-testid="stFormSubmitButton"] button:hover {
            transform: scale(1.05);
            background-color: #000 !important;
        }
        /* Hide default text */
        div[data-testid="stFormSubmitButton"] button p { display: none; }
        /* Add Arrow Icon */
        div[data-testid="stFormSubmitButton"] button::before {
            content: '↑'; /* Unicode Up Arrow */
            font-size: 22px;
            font-weight: 500;
        }

        /* 5. SUGGESTION CARDS (GRID LAYOUT) */
        .section-label {
            max-width: 720px;
            margin: 60px auto 16px auto;
            padding-left: 4px;
            font-size: 14px;
            font-weight: 600;
            color: #111;
            font-family: 'Inter', sans-serif;
        }

        /* Styling Streamlit Buttons to look like Cards */
        .suggestion-grid div.stButton > button {
            width: 100%;
            background-color: #FFFFFF !important;
            border: 1px solid #EAEAEA !important;
            border-radius: 16px !important; /* Slightly more rounded */
            padding: 20px 24px !important;
            height: auto !important;
            min-height: 100px !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: flex-start !important;
            justify-content: center !important;
            text-align: left !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02) !important;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        .suggestion-grid div.stButton > button:hover {
            border-color: #CCC !important;
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.06) !important;
        }
        
        /* Card Text Styling */
        .suggestion-grid div.stButton > button p {
            font-family: 'Inter', sans-serif;
            font-size: 15px;
            color: #111;
            line-height: 1.5;
            margin: 0;
        }
        /* Icon styling within markdown if used, or emojis */
        
        </style>
    """, unsafe_allow_html=True)

    # --- 1. NAVBAR SECTION ---
    # Using columns to place Logo (Left) and Buttons (Right)
    # Ratios: Logo(2) - Spacer(5) - Buttons(1.5)
    col_nav_1, col_nav_spacer, col_nav_2 = st.columns([2, 5, 1.5])
    
    with col_nav_1:
        st.markdown("""
        <div class="nav-left">
            <a href="#" class="logo-text">⚡ ARTIS</a>
            <div class="nav-items" style="margin-left:32px;">
                <a href="#" class="nav-item">Özellikler</a>
                <a href="#" class="nav-item">Kaynaklar</a>
                <a href="#" class="nav-item">Fiyatlandırma</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_nav_2:
        # Nested columns for tight button spacing
        c_btn_1, c_btn_2 = st.columns(2)
        with c_btn_1:
            if st.button("Giriş yap", key="login_btn"):
                st.session_state.page = "Login"
                st.rerun()
        with c_btn_2:
            if st.button("Kaydol", key="signup_btn"):
                st.session_state.page = "Login"
                st.rerun()

    # --- 2. HERO SECTION ---
    st.markdown("""
        <div class="hero-wrapper">
            <h1 class="hero-heading">Sizin için ne yapabilirim?</h1>
        </div>
    """, unsafe_allow_html=True)

    # --- 3. SEARCH INPUT ---
    # Using a form allows the "Enter" key to work naturally
    with st.form("search_form", border=False):
        # Centering columns: [Spacer] [Input] [Spacer]
        c_l, c_center, c_r = st.columns([1, 6, 1])
        with c_center:
            # The placeholder has leading spaces because CSS moves the text cursor, but the placeholder text stays put in some browsers.
            # Ideally, we rely on the CSS padding-left to push both placeholder and text.
            prompt = st.text_input("prompt", placeholder="Lojistik maliyetlerini analiz et...", label_visibility="collapsed")
            
            # The Submit Button (Styled as Black Arrow)
            submit = st.form_submit_button("Submit") 

    # --- 4. SUGGESTION CARDS ---
    st.markdown('<div class="section-label">Ne inşa ediyorsunuz?</div>', unsafe_allow_html=True)

    # Grid Container
    col_grid = st.columns([1, 6, 1])[1] # Reuse the center column width
    
    # We wrap this in a container div class for specific CSS targeting
    with col_grid:
        st.markdown('<div class="suggestion-grid">', unsafe_allow_html=True)
        
        # Row 1
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

        # Row 2
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
        
        st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. LOGIC HANDLER ---
    if submit and prompt:
        st.session_state.pending_prompt = prompt
        st.session_state.page = "Login"
        st.rerun()

if __name__ == "__main__":
    render_landing()
