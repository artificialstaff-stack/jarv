import streamlit as st

def render_landing():
    # --- CSS: MANUS TARZI TEMİZ ARAYÜZ ---
    st.markdown("""
        <style>
        /* Ana arka planı temizle */
        .stApp {
            background-color: #0e0e0e; /* Manus Dark Theme */
            background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #0e0e0e 50%);
        }
        
        /* Header Gizle */
        header {visibility: hidden;}
        
        /* Ortalanmış İçerik */
        .landing-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 10vh;
            text-align: center;
        }
        
        /* Başlık */
        .landing-title {
            font-size: 60px;
            font-weight: 400;
            color: #e5e5e5;
            font-family: 'Times New Roman', serif; /* Manus benzeri serif font */
            margin-bottom: 40px;
        }
        
        /* Öneri Çipleri (Butonlar) */
        .suggestion-btn {
            background-color: transparent;
            border: 1px solid #333;
            color: #888;
            border-radius: 20px;
            padding: 8px 16px;
            font-size: 14px;
            margin: 0 5px;
            cursor: pointer;
            transition: all 0.3s;
            display: inline-block;
        }
        .suggestion-btn:hover {
            border-color: #d4af37;
            color: #d4af37;
        }

        /* Input Alanı Özelleştirme */
        .stTextInput input {
            background-color: #1a1a1a !important;
            border: 1px solid #333 !important;
            color: white !important;
            border-radius: 24px !important;
            padding: 15px 20px !important;
            font-size: 16px !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }
        .stTextInput input:focus {
            border-color: #d4af37 !important;
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.2) !important;
        }
        
        /* Navigasyon Barı */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
        }
        .nav-logo { font-size: 20px; font-weight: bold; color: white; }
        .nav-link { color: #888; text-decoration: none; margin-left: 20px; font-size: 14px; cursor: pointer;}
        .nav-link:hover { color: white; }
        
        </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown('<div class="nav-logo">ARTIS</div>', unsafe_allow_html=True)
    with c2:
        # Sağ üst menü (Login/Register)
        # Buradaki butonlar app.py'deki state'i değiştirecek
        col_space, col_login, col_reg = st.columns([6, 1, 1])
        with col_login:
            if st.button("Giriş Yap", type="secondary"):
                st.session_state.page = "Login"
                st.rerun()
        with col_reg:
            if st.button("Kaydol", type="primary"):
                st.session_state.page = "Login" # Kayıt da login sayfasına atsın şimdilik
                st.rerun()

    # --- ANA İÇERİK ---
    st.markdown('<div class="landing-container"><div class="landing-title">Sizin için ne yapabilirim?</div></div>', unsafe_allow_html=True)

    # Arama Çubuğu (Giriş Noktası)
    # Form kullanarak Enter tuşunu yakalıyoruz
    with st.form("landing_search", border=False):
        c_space1, c_input, c_space2 = st.columns([1, 2, 1])
        with c_input:
            prompt = st.text_input("Prompt", placeholder="Bir şeyler yazın...", label_visibility="collapsed")
            
            # Altın Renkli Submit Butonu (İkon gibi)
            submit = st.form_submit_button("BAŞLA", use_container_width=True)

    # Öneri Butonları (Dummy)
    st.markdown("""
        <div style="text-align:center; margin-top: 20px;">
            <span class="suggestion-btn">📄 Gümrük Raporu Hazırla</span>
            <span class="suggestion-btn">📦 Lojistik Maliyeti Hesapla</span>
            <span class="suggestion-btn">📈 ABD Pazar Analizi</span>
        </div>
    """, unsafe_allow_html=True)

    # Alt Bilgi
    st.markdown("""
        <div style="text-align:center; margin-top: 100px; color: #444; font-size: 12px;">
            ARTIS AI v2.4 | Global Operations Engine
        </div>
    """, unsafe_allow_html=True)

    # --- AKSİYON MANTIĞI ---
    if submit and prompt:
        # Kullanıcı bir şey yazdı!
        # Promptu hafızaya at ve Login'e yönlendir
        st.session_state.pending_prompt = prompt
        st.session_state.page = "Login"
        st.rerun()

if __name__ == "__main__":
    render_landing()
