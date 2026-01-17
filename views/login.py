import streamlit as st
import time
import random

# ==============================================================================
# 1. TEMEL AYARLAR (Tam Ekran, Geniş Mod)
# ==============================================================================
st.set_page_config(page_title="ARTIS - Operasyon Girişi", layout="wide", initial_sidebar_state="collapsed")

# ==============================================================================
# 2. İÇERİK VE MESAJ HAVUZU (MÜŞTERİ ODAKLI)
# ==============================================================================
def get_login_assets():
    # Yüksek kaliteli, teknolojik/cyber arka planlar
    backgrounds = [
        "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=2070&auto=format&fit=crop", # Çip/Veri Yolu
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop", # Global Ağ
        "https://images.unsplash.com/photo-1607799275518-d58665d096c2?q=80&w=2070&auto=format&fit=crop", # Server Odası
    ]
    
    # Müşteri Faydası Odaklı Mesajlar (Matrix mantığıyla sırayla gelecekler)
    # Kibirli değil, çözüm odaklı.
    benefits = [
        "► Operasyonel maliyetlerde %40'a varan optimizasyon sağlayın.",
        "► 7/24 kesintisiz iş akışı: Sistem uyumaz, sadece elektrik tüketir.",
        "► İnsan kaynağınızı rutin işlerden kurtarıp, stratejik büyümeye yönlendirin.",
        "► Hatasız ve otonom süreç yönetimi ile iş yükünüzü minimize edin.",
        "► ARTIS: Geleceğin operasyon altyapısına bugünden erişim."
    ]
    
    return random.choice(backgrounds), benefits

# ==============================================================================
# 3. CSS - "DİJİTAL VERİ AKIŞI" TASARIMI
# ==============================================================================
def inject_custom_css(bg_url):
    st.markdown(f"""
    <style>
        /* --- ANA SAYFA YAPISI (SCROLL YOK) --- */
        .stApp {{
            background-image: url('{bg_url}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            overflow: hidden !important; /* Scroll engelleme */
        }}

        /* Streamlit boşluklarını sıfırla */
        .block-container {{ padding: 0 !important; margin: 0 !important; max-width: 100% !important; }}
        header, footer, [data-testid="stSidebar"] {{ display: none !important; }}

        /* --- SAĞ TARAF: GİRİŞ KUTUSU (GLASSMORPHISM) --- */
        div[data-testid="column"]:nth-of-type(2) {{
            background: rgba(13, 17, 23, 0.7); /* Koyu, şeffaf arka plan */
            backdrop-filter: blur(12px);       /* Buzlu cam efekti */
            padding: 50px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
            margin-top: 20vh; /* Dikey konum */
        }}

        /* Input Alanları */
        .stTextInput input {{
            background-color: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(99, 102, 241, 0.3) !important; /* Hafif mor/mavi çerçeve */
            color: #e2e8f0 !important;
            border-radius: 8px !important;
            padding: 12px !important;
        }}
        .stTextInput input:focus {{
            border-color: #818cf8 !important;
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.3) !important;
        }}
        
        /* Buton */
        .stButton button {{
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important; /* Modern degrade */
            border: none !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 12px !important;
            border-radius: 8px !important;
            transition: transform 0.2s;
        }}
        .stButton button:hover {{ transform: scale(1.02); }}
        
        /* Checkbox ve Linkler */
        .stCheckbox span {{ color: #94a3b8 !important; font-size: 14px; }}
        a {{ color: #94a3b8 !important; text-decoration: none; font-size: 14px; transition: color 0.3s; }}
        a:hover {{ color: #818cf8 !important; }}

        /* --- SOL ALT: "MATRİX MANTIKLI" VERİ AKIŞI --- */
        .data-stream-container {{
            position: fixed;
            bottom: 50px;
            left: 50px;
            z-index: 999;
            max-width: 700px;
            font-family: 'Courier New', monospace; /* Dijital/Kod hissiyatı için */
        }}
        
        /* Her bir satırın stili */
        .data-line {{
            color: #60a5fa; /* Açık mavi, dijital renk */
            font-size: 18px;
            margin-bottom: 12px;
            opacity: 0; /* Başlangıçta gizli */
            animation: digitalReveal 0.8s cubic-bezier(0.22, 0.61, 0.36, 1) forwards;
            border-left: 3px solid rgba(96, 165, 250, 0.5);
            padding-left: 15px;
            text-shadow: 0 0 8px rgba(96, 165, 250, 0.4);
            white-space: nowrap;
            overflow: hidden;
        }}
        
        /* Sırayla gelmeleri için gecikmeler (Matrix mantığı) */
        .data-line:nth-child(1) {{ animation-delay: 0.5s; }}
        .data-line:nth-child(2) {{ animation-delay: 2.5s; }}
        .data-line:nth-child(3) {{ animation-delay: 4.5s; }}
        .data-line:nth-child(4) {{ animation-delay: 6.5s; }}
        .data-line:nth-child(5) {{ animation-delay: 8.5s; }}

        /* Belirme Animasyonu (Hafif glitch efektli) */
        @keyframes digitalReveal {{
            0% {{ 
                opacity: 0; 
                transform: translateX(-30px) scaleX(0.9);
                text-shadow: 5px 0 10px rgba(255,255,255,0.5); /* Başlangıçta parlama */
                filter: blur(4px);
            }}
            60% {{
                opacity: 0.8;
                transform: translateX(5px);
                filter: blur(0px);
            }}
            100% {{ 
                opacity: 1; 
                transform: translateX(0) scaleX(1);
                text-shadow: 0 0 8px rgba(96, 165, 250, 0.4);
            }}
        }}

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. ANA RENDER FONKSİYONU
# ==============================================================================
def render_login_page():
    bg_image, benefit_messages = get_login_assets()
    inject_custom_css(bg_image)
    
    # Yerleşim: Sol boşluk, Orta form, Sağ boşluk
    # Formu biraz sağa yaslıyoruz.
    col1, col2, col3 = st.columns([0.8, 0.8, 1.4])
    
    # --- GİRİŞ FORMU (ORTA KOLON) ---
    with col2:
        st.markdown("<h2 style='color:white; margin-bottom:10px;'>Sisteme Giriş</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#94a3b8; margin-bottom:30px; font-size:14px;'>ARTIS Operasyon Yönetim Paneli</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("Kullanıcı Adı", placeholder="Kullanıcı adınız", label_visibility="collapsed")
            st.write("")
            password = st.text_input("Şifre", type="password", placeholder="••••••••", label_visibility="collapsed")
            st.write("")
            
            c_rem, c_link = st.columns([1, 1])
            with c_rem:
                st.checkbox("Beni Hatırla", value=True)
            with c_link:
                 st.markdown("<div style='text-align:right; padding-top:2px;'><a href='#'>Şifremi Unuttum</a></div>", unsafe_allow_html=True)

            st.write("")
            submit = st.form_submit_button("GÜVENLİ GİRİŞ", type="primary", use_container_width=True)
            
            if submit:
                if username == "admin" and password == "admin":
                    with st.spinner("Bağlantı kuruluyor..."):
                        time.sleep(1)
                    st.success("Kimlik doğrulandı.")
                    st.session_state.logged_in = True
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Kimlik bilgileri hatalı.")

    # --- SOL ALT: DİJİTAL VERİ AKIŞI (HTML KUTUSU) ---
    # Mesajları döngüye sokup HTML oluşturuyoruz
    html_lines = ""
    for msg in benefit_messages:
        html_lines += f'<div class="data-line">{msg}</div>'

    st.markdown(f"""
    <div class="data-stream-container">
        {html_lines}
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# ÇALIŞTIR
# ==============================================================================
if __name__ == "__main__":
    render_login_page()
