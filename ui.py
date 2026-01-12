import streamlit as st

def apply_luxury_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&display=swap');
        
        /* Ana Arka Plan */
        .stApp {
            background: radial-gradient(circle at top right, #101216, #050505);
            color: #d1d1d1;
            font-family: 'Inter', sans-serif;
        }

        /* Sidebar (Sol Menü) Tasarımı */
        [data-testid="stSidebar"] {
            background-color: #0c0d0f !important;
            border-right: 1px solid rgba(184, 155, 94, 0.2);
        }

        /* Sekme ve Butonlar */
        .stButton>button {
            border: 1px solid #B89B5E !important;
            background: transparent !important;
            color: #B89B5E !important;
            border-radius: 0px;
            transition: 0.3s;
            width: 100%;
        }
        .stButton>button:hover {
            background: #B89B5E !important;
            color: black !important;
            box-shadow: 0 0 15px rgba(184, 155, 94, 0.4);
        }

        /* Başlıklar */
        .brand-title {
            font-family: 'Cinzel', serif;
            color: #B89B5E;
            text-align: center;
            letter-spacing: 5px;
            font-size: 1.8rem;
            margin-bottom: 30px;
        }
        
        /* Kartlar */
        .premium-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(184, 155, 94, 0.2);
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="brand-title">ARTIFICIAL STAFF</div>', unsafe_allow_html=True)
        st.markdown("---")
        menu = st.radio(
            "OPERASYON MERKEZİ",
            ["🤖 Jarvis AI", "📦 Envanter Takip", "🚢 Lojistik Durumu", "💰 Muhasebe & Vergi", "📈 Strateji Geliştirme", "🏢 Şirket Bilgileri"],
            index=0
        )
        st.markdown("---")
        st.caption("Premium Member Access v2.5")
        return menu
