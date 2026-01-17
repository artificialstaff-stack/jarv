import streamlit as st
import time
import random

# ==============================================================================
# 1. TEMEL AYARLAR
# ==============================================================================
st.set_page_config(page_title="ARTIS Login", layout="wide", initial_sidebar_state="collapsed")

# ==============================================================================
# 2. İÇERİK HAVUZU (GTA STYLE)
# ==============================================================================
def get_gta_assets():
    # Yüksek kaliteli, koyu temalı arka planlar
    backgrounds = [
        "https://images.unsplash.com/photo-1535868463750-c78d9543614f?q=80&w=2076&auto=format&fit=crop", # Cyberpunk City
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", # Tech Room
        "https://images.unsplash.com/photo-1519608487953-e999c9dc296f?q=80&w=2070&auto=format&fit=crop", # Dark Mist
        "https://images.unsplash.com/photo-1614064641938-3e821efd8536?q=80&w=2070&auto=format&fit=crop"  # Abstract Blue
    ]
    
    # Kayan yazılar
    tips = [
        {"h": "ARTIS INTELLIGENCE", "t": "Yapay zeka motoru iş süreçlerinizi %40 hızlandırır."},
        {"h": "GLOBAL CONNECT", "t": "Dünyanın her yerinden güvenli ve şifreli erişim."},
        {"h": "VERİ GÜVENLİĞİ", "t": "Tüm operasyon verileriniz uçtan uca şifrelenmektedir."},
        {"h": "OPERASYON YÖNETİMİ", "t": "Tek panelden tüm lojistik ağını kontrol edin."}
    ]
    return random.choice(backgrounds), random.choice(tips)

# ==============================================================================
# 3. CSS (BÜYÜ YAPIYORUZ - OVERLAY TEKNİĞİ)
# ==============================================================================
def inject_custom_css(bg_url):
    st.markdown(f"""
    <style>
        /* --- A. SAYFAYI DONDUR VE ARKA PLANI YAPIŞTIR --- */
        .stApp {{
            background-image: url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            height: 100vh;
            overflow: hidden !important; /* Asla kaydırma çubuğu çıkmasın */
        }}

        /* Streamlit'in kendi boşluklarını yok et */
        .block-container {{
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }}
        
        /* Gereksiz elementleri gizle */
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}

        /* --- B. GİRİŞ KUTUSU STİLİ (GLASSMORPHISM) --- */
        /* Bu class'ı formun olduğu kolona vereceğiz */
        div[data-testid="column"]:nth-of-type(2) {{
            background: rgba(0, 0, 0, 0.6); /* Yarı saydam siyah */
            backdrop-filter: blur(15px);     /* Arkayı bulanıklaştır */
            -webkit-backdrop-filter: blur(15px);
            padding: 40px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            margin-top: 15vh; /* Yukarıdan biraz boşluk bırak */
        }}

        /* Input Alanlarını Özelleştir */
        .stTextInput input {{
            background-color: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            color: white !important;
            border-radius: 10px !important;
            height: 50px !important;
        }}
        
        .stTextInput input:focus {{
            border-color: #FF4B4B !important;
            box-shadow: 0 0 15px rgba(255, 75, 75, 0.3) !important;
        }}

        /* Giriş Butonu */
        .stButton button {{
            background: linear-gradient(90deg, #FF4B4B 0%, #FF2E2E 100%) !important;
            border: none !important;
            color: white !important;
            font-weight: bold !important;
            height: 50px !important;
            border-radius: 10px !important;
            transition: all 0.3s ease !important;
        }}
        .stButton button:hover {{
            transform: scale(1.02);
            box-shadow: 0 10px 20px rgba(255, 75, 75, 0.4);
        }}

        /* --- C. SOL ALTTAKİ ANİMASYONLU YAZI (SABİT POZİSYON) --- */
        .gta-info-box {{
            position: fixed;
            bottom: 60px;
            left: 60px;
            max-width: 600px;
            z-index: 999;
            color: white;
            animation: slideUpFade 1.5s ease-out forwards;
        }}
        
        .gta-header {{
            font-size: 50px;
            font-weight: 900;
            line-height: 1;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: -1px;
            text-shadow: 0 5px 15px rgba(0,0,0,0.8);
        }}
        
        .gta-text {{
            font-size: 18px;
            font-weight: 300;
            color: #e0e0e0;
            border-left: 4px solid #FF4B4B;
            padding-left: 20px;
            background: linear-gradient(90deg, rgba(0,0,0,0.8), transparent);
            padding-right: 20px;
        }}

        @keyframes slideUpFade {{
            0% {{ opacity: 0; transform: translateY(40px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
        
        /* Checkbox rengi */
        .stCheckbox span {{ color: #ccc !important; }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. GİRİŞ MANTIĞI
# ==============================================================================
def render_login_page():
    # 1. Rastgele İçerik Seç
    bg, data = get_gta_assets()
    
    # 2. CSS'i Sayfaya Enjekte Et
    inject_custom_css(bg)
    
    # 3. YERLEŞİM PLANI (GRID SİSTEMİ)
    # Ekranı 3 parçaya bölüyoruz: [BOŞLUK] - [GİRİŞ KUTUSU] - [BOŞLUK]
    # Böylece giriş kutusu sağ tarafta "yüzen" bir ada gibi duracak.
    col1, col2, col3 = st.columns([1, 0.8, 0.2]) 
    # Not: col2 giriş kutusunun genişliğidir. Artırırsan genişler.
    
    # --- ORTA/SAĞ KOLON: GİRİŞ FORMU ---
    with col2:
        st.markdown("<br>", unsafe_allow_html=True) # Üstten biraz it
        
        st.markdown('<h2 style="color:white; margin-bottom:0; text-align:center;">Giriş Yap</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#aaa; margin-bottom:30px; text-align:center;">ARTIS Operasyon Paneli</p>', unsafe_allow_html=True)

        with st.form("login_form"):
            username = st.text_input("Kullanıcı Adı", placeholder="admin", label_visibility="collapsed")
            st.write("")
            password = st.text_input("Şifre", type="password", placeholder="••••••••", label_visibility="collapsed")
            
            st.write("")
            c1, c2 = st.columns([1,1])
            with c1:
                st.checkbox("Beni Hatırla", value=True)
            with c2:
                pass # Boş bırak, buton aşağıda
            
            st.write("")
            submit = st.form_submit_button("SİSTEME GİRİŞ", type="primary", use_container_width=True)
        
        # Form Altı Link
        st.markdown('<div style="text-align:center; margin-top:15px;"><a href="#" style="color:#666; font-size:12px; text-decoration:none;">Şifremi Unuttum?</a></div>', unsafe_allow_html=True)

        if submit:
            if username == "admin" and password == "admin":
                with st.spinner("Kimlik doğrulanıyor..."):
                    time.sleep(1)
                st.success("Başarılı!")
                st.session_state.logged_in = True
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Hatalı bilgi.")

    # 4. SOL ALT KÖŞE (HTML İLE EKLENEN SABİT YAZI)
    # Bu kısım Streamlit kolonlarından bağımsızdır, CSS ile sabitlenmiştir.
    st.markdown(f"""
    <div class="gta-info-box">
        <div class="gta-header">{data['h']}</div>
        <div class="gta-text">{data['t']}</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 5. ÇALIŞTIR
# ==============================================================================
if __name__ == "__main__":
    render_login_page()
