import streamlit as st

def render_landing():
    # --- MANUS STYLE (LIGHT/CLEAN) CSS ---
    st.markdown("""
        <style>
        /* 1. SAYFA YAPISI (BEYAZ/TEMİZ) */
        .stApp {
            background-color: #F9F9F9; /* Hafif kırık beyaz */
            color: #000000;
        }
        
        /* Gereksiz Streamlit boşluklarını yok et */
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            max-width: 100% !important;
        }
        header[data-testid="stHeader"] { display: none; }
        footer { display: none; }

        /* 2. NAVBAR (HEADER) */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            background-color: #F9F9F9;
            position: sticky;
            top: 0;
            z-index: 999;
        }
        
        .nav-logo {
            font-family: 'Times New Roman', serif;
            font-size: 24px;
            font-weight: bold;
            color: #000;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .nav-links {
            display: flex;
            gap: 25px;
            font-size: 14px;
            color: #555;
            font-weight: 500;
        }
        .nav-link:hover { color: #000; cursor: pointer; }

        /* 3. ANA İÇERİK (HERO) */
        .hero-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 80px;
            text-align: center;
        }
        
        .hero-title {
            font-family: 'Times New Roman', serif;
            font-size: 56px;
            color: #111;
            margin-bottom: 40px;
            font-weight: 400;
            letter-spacing: -1px;
        }

        /* 4. ARAMA KUTUSU (MANUS STYLE) */
        div[data-testid="stForm"] {
            border: none;
            padding: 0;
            background: transparent;
            width: 100%;
            max-width: 700px;
            margin: 0 auto;
            position: relative;
        }
        
        div[data-testid="stTextInput"] input {
            background-color: #FFFFFF !important;
            border: 1px solid #E5E5E5 !important;
            color: #000 !important;
            border-radius: 16px !important;
            padding: 25px 50px 25px 25px !important; /* Sağdan boşluk ikon için */
            font-size: 18px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: all 0.2s;
        }
        div[data-testid="stTextInput"] input:focus {
            border-color: #000 !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }

        /* Submit Butonunu Ok İkonu Yapma Hilesi */
        div[data-testid="stFormSubmitButton"] button {
            position: absolute;
            top: -68px; /* Inputun içine taşı */
            right: 10px;
            background-color: #000 !important;
            color: white !important;
            border-radius: 50% !important;
            width: 40px !important;
            height: 40px !important;
            border: none !important;
            padding: 0 !important;
            font-size: 20px !important;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
        }
        div[data-testid="stFormSubmitButton"] button:hover {
            background-color: #333 !important;
            transform: scale(1.05);
        }
        /* Butonun içindeki yazıyı gizle (Streamlit yazıyı zorunlu kılıyor) */
        div[data-testid="stFormSubmitButton"] button p {
            display: none;
        }
        /* Ok ikonu ekle */
        div[data-testid="stFormSubmitButton"] button::after {
            content: '↑';
            font-size: 20px;
            font-weight: bold;
        }

        /* 5. ÖNERİ LİSTESİ (ALTTAKİ KUTULAR) */
        .suggestion-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            max-width: 800px;
            margin: 60px auto 0;
            width: 100%;
            padding: 0 20px;
        }
        
        .suggestion-card {
            background: #FFFFFF;
            border: 1px solid #E5E5E5;
            padding: 15px 20px;
            border-radius: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            transition: all 0.2s;
            text-align: left;
        }
        .suggestion-card:hover {
            border-color: #CCC;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        
        .card-content { display: flex; flex-direction: column; gap: 4px; }
        .card-title { font-weight: 600; font-size: 14px; color: #111; }
        .card-desc { font-size: 12px; color: #666; }
        .card-icon { color: #999; font-size: 18px; }

        /* HEADER BUTONLARI */
        .header-btn-secondary {
            background: #000;
            color: #fff;
            padding: 8px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 600;
            border: none;
        }
        .header-btn-primary {
            background: #fff;
            color: #000;
            padding: 8px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 600;
            border: 1px solid #E5E5E5;
            margin-right: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 1. NAVBAR (Görsel HTML + İşlevsel Butonlar) ---
    c1, c2, c3 = st.columns([6, 1, 1])
    with c1:
        st.markdown("""
        <div class="nav-logo">
            <span style="font-size:20px;">⚡</span> ARTIS
            <span style="margin-left:30px; font-size:14px; color:#666; font-weight:400; font-family:sans-serif;">
                Özellikler &nbsp;&nbsp; Kaynaklar &nbsp;&nbsp; Fiyatlandırma
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        if st.button("Giriş yap", type="primary", use_container_width=True):
            st.session_state.page = "Login"
            st.rerun()
    with c3:
        if st.button("Kaydol", type="secondary", use_container_width=True):
            st.session_state.page = "Login"
            st.rerun()

    # --- 2. HERO SECTION ---
    st.markdown('<div class="hero-container"><div class="hero-title">Sizin için ne yapabilirim?</div></div>', unsafe_allow_html=True)

    # --- 3. ARAMA KUTUSU (FORM) ---
    with st.form("landing_form", border=False):
        # Sol ve Sağ boşluklar ile inputu ortala
        c_fill1, c_input, c_fill2 = st.columns([1, 6, 1])
        with c_input:
            prompt = st.text_input("prompt", placeholder="Örn: ABD pazarı için tekstil gümrük vergilerini listele...", label_visibility="collapsed")
            # Buton (CSS ile ok ikonuna dönüşüyor)
            submit = st.form_submit_button("GO")

    # --- 4. ÖNERİLER (İŞ MODELİNE UYGUN) ---
    # Streamlit butonlarını kullanarak bu listeyi interaktif yapıyoruz.
    # Görseldeki gibi 2 kolonlu yapı.
    
    st.markdown('<div style="max-width:800px; margin: 40px auto 10px auto; color:#111; font-weight:600; font-size:14px; padding-left:20px;">Ne inşa ediyorsunuz?</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    
    # Sol Kolon Önerileri
    with col_a:
        if st.button("📦 Lojistik Maliyet Analizi\nTürkiye'den ABD depolarına en uygun rota ve maliyet.", use_container_width=True):
            st.session_state.pending_prompt = "Lojistik maliyet analizi yap"
            st.session_state.page = "Login"
            st.rerun()
            
        if st.button("⚖️ Gümrük Mevzuatı\nGTIP koduna göre vergi oranları ve belge listesi.", use_container_width=True):
            st.session_state.pending_prompt = "Gümrük mevzuatı kontrolü"
            st.session_state.page = "Login"
            st.rerun()

    # Sağ Kolon Önerileri
    with col_b:
        if st.button("📈 Rakip Pazar Analizi\nAmazon'daki rakiplerin fiyat ve stok stratejileri.", use_container_width=True):
            st.session_state.pending_prompt = "Rakip pazar analizi yap"
            st.session_state.page = "Login"
            st.rerun()

        if st.button("🤖 Otomasyon Kurulumu\nSiparişten teslimata %100 otonom iş akışı.", use_container_width=True):
            st.session_state.pending_prompt = "Otomasyon kurulumu başlat"
            st.session_state.page = "Login"
            st.rerun()

    # --- 5. LOGIC ---
    if submit and prompt:
        st.session_state.pending_prompt = prompt
        st.session_state.page = "Login"
        st.rerun()

if __name__ == "__main__":
    render_landing()
