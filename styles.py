# styles.py
import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* FONTLAR */
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;600&display=swap');

        /* GENEL AYARLAR */
        .stApp { background-color: #080808; font-family: 'Inter', sans-serif; }
        
        /* SIDEBAR */
        section[data-testid="stSidebar"] { background-color: #000000; border-right: 1px solid #222; }
        
        /* RENKLER VE BUTONLAR */
        h1, h2, h3 { font-family: 'Cormorant Garamond', serif !important; color: #ffffff !important; }
        p, label, li { color: #b0b0b0; font-family: 'Inter', sans-serif; }
        
        .stButton > button {
            background-color: #C5A059; color: #000; border: none; font-weight: 600;
            padding: 10px 20px; transition: all 0.3s; width: 100%; border-radius: 4px;
        }
        .stButton > button:hover { background-color: #d4b06a; box-shadow: 0 0 15px rgba(197, 160, 89, 0.3); }

        /* INPUT ALANLARI */
        .stTextInput > div > div > input, .stSelectbox > div > div > div { 
            background-color: #121212; color: white; border: 1px solid #333; border-radius: 4px;
        }
        .stTextInput > div > div > input:focus { border-color: #C5A059; }

        /* --- LOGIN EKRANI İÇİN ÖZEL CSS --- */
        .login-container {
            border: 1px solid #333;
            padding: 40px;
            border-radius: 10px;
            background-color: #0a0a0a;
            box-shadow: 0 0 50px rgba(0,0,0,0.8);
            text-align: center;
            max-width: 400px;
            margin: auto;
            margin-top: 50px;
        }
        
        /* KART TASARIMLARI */
        .premium-card {
            background: rgba(255,255,255,0.03); padding: 20px; border-left: 2px solid #333; margin-bottom: 20px;
        }
        .premium-card:hover { border-left-color: #C5A059; background: rgba(255,255,255,0.05); }
        
        .metric-value { font-size: 24px; color: #fff; display: block; font-weight: bold; }
        .metric-label { font-size: 10px; color: #C5A059; letter-spacing: 1px; text-transform: uppercase; }
        
        /* CHAT BALONLARI */
        .stChatMessage { background-color: #111; border: 1px solid #222; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)
