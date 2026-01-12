# styles.py
import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* FONTLAR */
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');

        .stApp { background-color: #030303; font-family: 'Inter', sans-serif; }
        section[data-testid="stSidebar"] { background-color: #000000; border-right: 1px solid #222; }
        div.block-container { padding-top: 1rem; padding-bottom: 0rem; }

        /* BUTONLAR */
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
        
        h1, h2, h3 { font-family: 'Cormorant Garamond', serif !important; color: #fff !important; }
        p, label { color: #aaa; }
    </style>
    """, unsafe_allow_html=True)
