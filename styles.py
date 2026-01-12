# styles.py
import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* FONTLAR */
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');

        /* GENEL ATMOSFER */
        .stApp { 
            background-color: #050505; 
            font-family: 'Inter', sans-serif;
            background-image: radial-gradient(circle at 50% 50%, #111 0%, #000 100%);
        }
        
        section[data-testid="stSidebar"] { 
            background-color: #000000; 
            border-right: 1px solid rgba(255, 255, 255, 0.1); 
        }
        
        /* HEADER DÜZELTME */
        div.block-container { padding-top: 2rem; }

        /* --- GLASSMORPHISM KARTLAR --- */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-5px);
            border-color: #D4AF37;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        /* METRİK KUTULARI */
        div[data-testid="stMetric"] {
            background-color: #0a0a0a;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #222;
        }
        div[data-testid="stMetric"]:hover {
            border-color: #D4AF37;
        }

        /* INPUT ALANLARI - MODERN */
        .stTextInput > div > div > input, .stSelectbox > div > div > div { 
            background-color: #0f0f0f; 
            color: white; 
            border: 1px solid #333; 
            border-radius: 6px;
            height: 45px;
        }
        .stTextInput > div > div > input:focus { border-color: #D4AF37; box-shadow: 0 0 10px rgba(212, 175, 55, 0.2); }

        /* BUTONLAR - NEON GOLD */
        .stButton > button {
            background: linear-gradient(45deg, #D4AF37, #B69246);
            color: #000; 
            border: none; 
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            padding: 12px 24px;
            border-radius: 6px;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
            color: #fff;
            transform: scale(1.02);
        }
        
        /* TABLO VE GRAFİKLER */
        div[data-testid="stDataFrame"] { border: 1px solid #333; border-radius: 10px; }

        /* TYPOGRAPHY */
        h1, h2, h3 { font-family: 'Cormorant Garamond', serif !important; color: #fff !important; text-shadow: 0 0 10px rgba(255,255,255,0.1); }
        p, span, label { color: #aaa; }
        
        /* INTRO VE LOGIN KAPSAYICILARI */
        .intro-text-wrapper {
            background: rgba(0,0,0,0.6);
            padding: 40px;
            border-radius: 20px;
            border: 1px solid rgba(212, 175, 55, 0.3);
            box-shadow: 0 0 50px rgba(0,0,0,0.8);
        }
    </style>
    """, unsafe_allow_html=True)
