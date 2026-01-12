# styles.py
import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* --- FONTLAR & TEMEL --- */
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');

        .stApp { background-color: #030303; font-family: 'Inter', sans-serif; }
        section[data-testid="stSidebar"] { background-color: #000000; border-right: 1px solid #222; }
        
        /* RENKLER */
        h1, h2, h3 { font-family: 'Cormorant Garamond', serif !important; color: #ffffff !important; }
        .gold-text { color: #D4AF37 !important; }
        
        /* --- TAM EKRAN VIDEO INTRO KATMANI --- */
        .intro-overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: #000;
            z-index: 99999;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        
        .intro-content {
            z-index: 2;
            animation: fadeIn 2s ease-in;
        }
        
        .intro-bg-video {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            object-fit: cover;
            opacity: 0.4;
            z-index: 1;
        }

        /* INTRO BUTONU */
        .enter-btn {
            margin-top: 40px;
            padding: 15px 50px;
            background: transparent;
            border: 2px solid #D4AF37;
            color: #D4AF37;
            font-family: 'Cinzel', serif;
            font-size: 18px;
            cursor: pointer;
            transition: all 0.4s;
            text-transform: uppercase;
            letter-spacing: 3px;
        }
        .enter-btn:hover {
            background: #D4AF37;
            color: #000;
            box-shadow: 0 0 30px rgba(212, 175, 55, 0.4);
        }

        /* --- KÜÇÜLTÜLMÜŞ "TUTORIAL" WIDGET (SAĞ ALT) --- */
        .mini-player-widget {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 200px;
            background: #111;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 10px;
            z-index: 9990;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
            transition: all 0.3s;
            cursor: pointer;
        }
        .mini-player-widget:hover {
            border-color: #D4AF37;
            transform: translateY(-5px);
        }
        .mini-label {
            color: #D4AF37;
            font-size: 10px;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 5px;
            display: block;
        }
        
        /* STANDART UI ELEMANLARI */
        .stButton > button {
            background-color: #D4AF37; color: #000; border: none; font-weight: 600;
            padding: 10px 20px; transition: all 0.3s; width: 100%; border-radius: 4px;
        }
        .stTextInput > div > div > input, .stSelectbox > div > div > div { 
            background-color: #121212; color: white; border: 1px solid #333; border-radius: 4px;
        }
        
        /* LOGIN KUTUSU */
        .login-container {
            border: 1px solid #222; padding: 40px; border-radius: 0;
            background-color: #050505; box-shadow: 0 0 50px rgba(0,0,0,0.9);
            text-align: center; max-width: 400px; margin: auto; margin-top: 50px;
            border-top: 3px solid #D4AF37;
        }

        /* ANIMASYONLAR */
        @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    </style>
    """, unsafe_allow_html=True)
