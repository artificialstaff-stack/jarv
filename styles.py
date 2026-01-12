# styles.py
import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* 1. FONTLARI YÜKLE (Inter & Cormorant Garamond) */
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;600&display=swap');

        /* 2. GENEL ARKA PLAN VE RENKLER */
        .stApp {
            background-color: #080808; /* Deep Black */
            font-family: 'Inter', sans-serif;
        }
        
        /* Sidebar (Yan Menü) */
        section[data-testid="stSidebar"] {
            background-color: #000000;
            border-right: 1px solid #222;
        }
        
        /* Yazı Renkleri */
        h1, h2, h3 {
            font-family: 'Cormorant Garamond', serif !important;
            color: #ffffff !important;
            font-weight: 600 !important;
            letter-spacing: -0.5px;
        }
        
        p, div, label {
            color: #b0b0b0; /* Soft Grey */
            font-weight: 300;
        }
        
        /* 3. ÖZEL VURGU RENGİ (MAT ALTIN/BRONZ: #C5A059) */
        a { color: #C5A059 !important; }
        
        /* 4. GİRİŞ ALANLARI (INPUTS) - Stealth Mod */
        .stTextInput > div > div > input, .stSelectbox > div > div > div {
            background-color: #121212;
            color: #ffffff;
            border: 1px solid #333;
            border-radius: 4px; /* Hafif oval */
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #C5A059;
            box-shadow: 0 0 5px rgba(197, 160, 89, 0.3);
        }

        /* 5. BUTONLAR - Lüks Görünüm */
        .stButton > button {
            background-color: #C5A059; /* Gold Accent */
            color: #000000;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            border: none;
            border-radius: 2px;
            padding: 12px 24px;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .stButton > button:hover {
            background-color: #d4b06a;
            box-shadow: 0 5px 15px rgba(197, 160, 89, 0.2);
            color: #000;
        }
        
        /* 6. JARVIS CHAT BALONLARI */
        .stChatMessage {
            background-color: transparent;
            border: 1px solid #222;
            border-radius: 8px;
        }
        
        /* Asistan Mesajı (Gold Border) */
        div[data-testid="stChatMessage"]:nth-child(even) {
            border-left: 3px solid #C5A059;
            background-color: #111;
        }
        
        /* 7. PROGRESS BAR */
        .stProgress > div > div > div > div {
            background-color: #C5A059;
        }
        
        /* 8. RADIO BUTTONS & CHECKBOXES */
        .stRadio div[role="radiogroup"] > label {
            background-color: #111;
            border: 1px solid #222;
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 5px;
            transition: border 0.3s;
        }
        
        .stRadio div[role="radiogroup"] > label:hover {
            border-color: #C5A059;
        }

        /* 9. ÖZEL HTML KARTLAR İÇİN CSS */
        .premium-card {
            background: rgba(255,255,255,0.03);
            padding: 20px;
            border-left: 2px solid #333;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .premium-card:hover {
            border-left-color: #C5A059;
            background: rgba(255,255,255,0.05);
        }
        .metric-value {
            font-family: 'Inter', sans-serif;
            font-size: 32px;
            font-weight: 700;
            color: #fff;
            display: block;
        }
        .metric-label {
            font-size: 11px;
            color: #C5A059;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }
        .section-tag {
            font-size: 10px;
            color: #C5A059;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 5px;
            display: block;
        }
    </style>
    """, unsafe_allow_html=True)
