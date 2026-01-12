# styles.py
import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');

        .stApp { 
            background-color: #050505; 
            font-family: 'Inter', sans-serif;
            background-image: radial-gradient(circle at 50% 50%, #101010 0%, #000 100%);
        }
        
        div.block-container { padding-top: 2rem; }
        section[data-testid="stSidebar"] { background-color: #000; border-right: 1px solid #222; }

        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }

        /* METRİKLER */
        div[data-testid="stMetric"] {
            background-color: #0a0a0a;
            padding: 15px; border-radius: 8px; border: 1px solid #222;
        }
        
        /* BUTONLAR */
        .stButton > button {
            background: linear-gradient(45deg, #D4AF37, #B69246);
            color: #000; border: none; font-weight: 700;
            text-transform: uppercase; letter-spacing: 1.5px;
            padding: 10px 20px; border-radius: 4px; width: 100%;
        }
        .stButton > button:hover { color: #fff; box-shadow: 0 0 15px #D4AF37; }

        h1, h2, h3 { font-family: 'Cormorant Garamond', serif !important; color: #fff !important; }
        p, label { color: #aaa; }
    </style>
    """, unsafe_allow_html=True)
