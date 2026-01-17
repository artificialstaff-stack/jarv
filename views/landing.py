import streamlit as st

def render_landing():
    # --- MANUS TARZI GLOBAL CSS ---
    st.markdown("""
        <style>
        /* 1. GENEL AYARLAR */
        .stApp {
            background-color: #000000;
            color: #ffffff;
        }
        
        /* Streamlit'in varsayılan header ve footer'ını gizle */
        header[data-testid="stHeader"] { visibility: hidden; }
        footer { visibility: hidden; }
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            max-width: 100% !important;
        }

        /* 2. NAVBAR (LOGO VE SAĞ ÜST BUTONLAR) */
        .navbar-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 999;
            background: transparent;
        }
        .nav-logo {
            font-family: 'Times New Roman', serif;
            font-size: 24px;
            font-weight: bold;
            color: #e5e5e5;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        /* 3. ORTALANMIŞ İÇERİK (BAŞLIK VE INPUT) */
        .main-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 80vh; /* Ekranın ortasına gelsin */
            text-align: center;
        }
        
        .hero-title {
            font-family: 'Times New Roman', serif; /* Manus'un imza fontu */
            font-size: 56px;
            color: #e5e5e5;
            margin-bottom: 40px;
            font-weight: 400;
        }

        /* 4. ARAMA ÇUBUĞU (INPUT) ÖZELLEŞTİRME */
        /* Streamlit input kutusunu tamamen değiştiriyoruz */
        div[data-testid="stTextInput"] {
            width: 600px !important; /* Genişlik */
            margin: 0 auto;
        }
        
        div[data-testid="stTextInput"] input {
            background-color: #1a1a1a !important; /* Koyu gri zemin */
            color: #ffffff !important;
            border: 1px solid #333 !important;
            border-radius: 16px !important; /* Hafif yuvarlak köşeler */
            padding: 25px 20px !important; /* İç boşluk */
            font-size: 18px !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        div[data-testid="stTextInput"] input:focus {
            border-color: #555 !important;
            background-color: #1f1f1f !important;
            box-shadow: 0 0 0 2px rgba(255,255,255,0.1);
        }
        /* Label'ı gizle */
        div[data-testid="stTextInput"] label { display: none; }

        /* 5. ÖNERİ BUTONLARI */
        .suggestions {
            display: flex;
            gap: 10px;
            margin-top: 25px;
            justify-content: center;
        }
        .suggestion-chip {
            background-color: transparent;
            border: 1px solid #333;
            color: #888;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .suggestion-chip:hover {
            border-color: #666;
            color: #fff;
            background-color: #1a1a1a;
        }
        
        /* Butonları Gizle (Navigasyon butonlarını HTML ile yaptık ama işlevsellik için st.button kullanacağız, onları şeffaf yapıyoruz) */
        button[kind="secondary"] {
            background: #1a1a1a !important;
            color: white !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
            padding: 5px 15px !important;
        }
        button[kind="primary"] {
            background: #ffffff !important;
            color: black !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 5px 15px !important;
            font-weight: 600 !important;
        }

        </style>
        
        <div class="navbar-container">
            <div class="nav-logo">
                ✨ ARTIS
            </div>
            </div>
        
    """, unsafe_allow_html=True)

    # --- NAVBAR BUTONLARI (SAĞ ÜST) ---
    # Streamlit butonlarını CSS ile navbar'ın sağına yerleştirmek zor olduğu için
    # Sayfanın en üstüne kolonlar koyup padding ile hizalıyoruz.
    c1, c2, c3 = st.columns([8, 1, 1])
    with c2:
        if st.button("Giriş yap", key="nav_login", type="secondary"):
            st.session_state.page = "Login"
            st.rerun()
    with c3:
        if st.button("Kaydol", key="nav_signup", type="primary"):
            st.session_state.page = "Login" # Kayıt da aynı sayfaya gitsin
            st.rerun()

    # --- ANA İÇERİK ---
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Başlık
    st.markdown('<div class="hero-title">Sizin için ne yapabilirim?</div>', unsafe_allow_html=True)

    # Arama Formu
    # Form kullanarak "Enter" tuşuna basıldığında tetiklenmesini sağlıyoruz
    with st.form("landing_search_form", border=False):
        # Ortalamak için kolon hilesi
        col_left, col_center, col_right = st.columns([1, 2, 1])
        
        with col_center:
            prompt = st.text_input("search", placeholder="Lojistik maliyetlerini analiz et...", label_visibility="collapsed")
            # Görünmez buton (Enter tuşu için gerekli)
            submit = st.form_submit_button("Gönder", use_container_width=True)

    # Öneri Butonları (Görsel)
    st.markdown("""
        <div class="suggestions">
            <div class="suggestion-chip">📄 Gümrük Raporu</div>
            <div class="suggestion-chip">📦 Stok Tahmini</div>
            <div class="suggestion-chip">📈 Pazar Analizi</div>
            <div class="suggestion-chip">🤖 Otomasyon Kur</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True) # End main-content

    # --- YÖNLENDİRME MANTIĞI ---
    # Submit butonuna basılmasa bile text_input enter ile submit tetikler.
    # Ancak Streamlit formlarında buton görünmek zorunda. CSS ile gizleyebiliriz ama
    # şimdilik 'Gönder' butonu işlevsel kalsın.
    
    # CSS ile submit butonunu gizleyelim (Sadece Enter çalışsın hissi vermek için)
    st.markdown("""
    <style>
    div[data-testid="stFormSubmitButton"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

    if submit and prompt:
        st.session_state.pending_prompt = prompt
        st.session_state.page = "Login"
        st.rerun()

if __name__ == "__main__":
    render_landing()
