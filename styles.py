import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        html, body, .stApp { background-color: #0E1117; color: #E6E6E6; font-family: 'Inter', sans-serif; }
        
        /* Sidebar */
        section[data-testid="stSidebar"] { background-color: #161B22; border-right: 1px solid #30363D; }
        
        /* Inputlar */
        .stTextInput input, .stSelectbox div, .stNumberInput input, .stTextArea textarea {
            background-color: #0D1117 !important; border: 1px solid #30363D; color: #E6E6E6; border-radius: 6px;
        }
        .stTextInput input:focus { border-color: #1F6FEB; }

        /* Butonlar */
        .stButton button { background-color: #238636; color: white; border: none; border-radius: 6px; transition: 0.2s; }
        .stButton button:hover { background-color: #2EA043; }

        /* Kartlar */
        div[data-testid="metric-container"] { background-color: #21262D; padding: 15px; border-radius: 8px; border: 1px solid #30363D; }
        
        /* Menü Görünümü (Radio Button) */
        .stRadio div[role="radiogroup"] > label {
            background-color: transparent; padding: 10px; border-radius: 6px; margin-bottom: 2px; cursor: pointer; transition: 0.2s;
        }
        .stRadio div[role="radiogroup"] > label:hover { background-color: #21262D; }
        .stRadio div[role="radiogroup"] > label[data-checked="true"] { background-color: #1F6FEB; color: white !important; }
        .stRadio div[role="radiogroup"] > label > div:first-child { display: none; }
        
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
