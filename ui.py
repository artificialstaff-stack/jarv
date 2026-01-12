import streamlit as st

def apply_luxury_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;500&display=swap');
        
        /* Ana Ekran Arka Planı - Uzay Derinliği */
        .stApp {
            background: radial-gradient(circle at 50% 50%, #1a1b21 0%, #050505 100%);
            color: #ffffff;
            font-family: 'Inter', sans-serif;
        }

        /* Cam Efekti Sidebar */
        [data-testid="stSidebar"] {
            background: rgba(15, 15, 15, 0.7) !important;
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(184, 155, 94, 0.2);
            box-shadow: 10px 0 30px rgba(0,0,0,0.5);
        }

        /* Modern Chat Balonları */
        [data-testid="stChatMessage"] {
            background: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-radius: 20px !important;
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        [data-testid="stChatMessage"]:hover {
            border-color: #B89B5E;
            box-shadow: 0 0 20px rgba(184, 155, 94, 0.1);
        }

        /* Yapay Zeka Başlığı - Neon Efekti */
        .brand-title {
            font-family: 'Orbitron', sans-serif;
            color: #B89B5E;
            text-align: center;
            letter-spacing: 10px;
            text-shadow: 0 0 20px rgba(184, 155, 94, 0.5);
            font-size: 2rem;
            margin-bottom: 2rem;
        }

        /* Giriş Kutusu - Floating Look */
        .stChatInputContainer {
            padding-bottom: 30px;
            background: transparent !important;
        }
        .stChatInputContainer input {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(184, 155, 94, 0.3) !important;
            border-radius: 30px !important;
            color: white !important;
            padding: 15px 25px !important;
        }

        /* Dashboard Kartları */
        .stat-card {
            background: linear-gradient(145deg, #1e1e24, #0a0a0c);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(184, 155, 94, 0.1);
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="brand-title">ARTIFICIAL<br>STAFF</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Modern İkonik Menü
        selection = st.radio(
            "COMMAND CENTER",
            ["🤖 JARVIS CORE", "📦 INVENTORY", "🚢 LOGISTICS", "💰 FINANCES", "📈 STRATEGY"],
            index=0
        )
        st.markdown("---")
        st.markdown("🟢 **SİSTEM: AKTİF**")
        st.markdown("🔐 **GÜVENLİK: SSL-V3**")
        return selection
