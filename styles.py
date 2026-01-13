import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
        
        /* GENEL ATMOSFER (Koyu ve Asil) */
        html, body, .stApp { 
            background-color: #050505; 
            color: #E0E0E0; 
            font-family: 'Inter', sans-serif; 
        }

        /* SIDEBAR */
        section[data-testid="stSidebar"] { 
            background-color: #0A0A0A; 
            border-right: 1px solid #1F1F1F; 
        }
        
        /* INPUT ALANLARI (Minimal) */
        .stTextInput input, .stSelectbox div, .stNumberInput input, .stTextArea textarea {
            background-color: #121212 !important; 
            border: 1px solid #333; 
            color: #FFF; 
            border-radius: 8px;
        }
        .stTextInput input:focus { border-color: #444; }

        /* BUTONLAR (Modern Gri) */
        .stButton button { 
            background-color: #1A1A1A; 
            color: #FFF; 
            border: 1px solid #333; 
            border-radius: 8px; 
            transition: 0.2s; 
        }
        .stButton button:hover { 
            border-color: #666; 
            background-color: #222; 
        }

        /* KARTLAR (Çerçeve Yok, Hafif Dolgu Var) */
        div[data-testid="metric-container"] {
            background-color: #111;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #222; /* Çok ince border */
        }
        
        /* TABLOLAR VE GRAFİKLER */
        .stDataFrame, .js-plotly-plot {
            border-radius: 12px;
            overflow: hidden;
        }

        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
