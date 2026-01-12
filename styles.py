# styles.py
import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* FONTLAR */
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');

        /* GENEL */
        .stApp { background-color: #030303; font-family: 'Inter', sans-serif; }
        section[data-testid="stSidebar"] { background-color: #000000; border-right: 1px solid #222; }
        
        /* GİZLİ TEKNİK: Üstteki beyaz boşluğu yok et */
        div.block-container { padding-top: 1rem; padding-bottom: 0rem; }

        /* INTRO OVERLAY (TAM EKRAN KAPLAMA) */
        .intro-overlay {
            position: fixed;
            top: 0; 
            left: 0; 
            width: 100vw; 
            height: 100vh;
            background-color: #000;
            z-index: 999999;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            overflow: hidden;
        }
        
        .intro-bg-video {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            object-fit: cover;
            opacity: 0.5;
            z-index: 1;
        }
        
        .intro-text-wrapper {
            z-index: 10;
            position: relative;
            background: rgba(0,0,0,0.4); /* Yazı okunsun diye hafif karartma */
            padding: 40px;
            border-radius: 20px;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(212, 175, 55, 0.3);
        }

        /* --- BUTONLAR --- */
        .stButton > button {
            background-color: #D4AF37; 
            color: #000; 
            border: none; 
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #fff;
            box-shadow: 0 0 15px #D4AF37;
        }

        /* LOGIN KUTUSU */
        .login-box {
            border: 1px solid #333;
            padding: 50px;
            background-color: #0a0a0a;
            border-top: 4px solid #D4AF37;
            text-align: center;
            margin-top: 10vh;
        }
    </style>
    """, unsafe_allow_html=True)
