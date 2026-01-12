# styles.py
import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* Genel Arka Plan */
        .stApp { background-color: #0e1117; color: white; }
        
        /* Input Alanları */
        .stTextInput > div > div > input { 
            background-color: #262730; 
            color: white; 
            border-radius: 10px;
        }
        
        /* Butonlar */
        .stButton > button {
            background-color: #00a8ff;
            color: white;
            border-radius: 8px;
            border: none;
            width: 100%;
        }
        .stButton > button:hover {
            background-color: #0077b6;
        }
        
        /* İlerleme Çubuğu (Step 3 için) */
        .stProgress > div > div > div > div { 
            background-color: #00ff41; 
        }
        
        /* Chat Balonları */
        .stChatMessage {
            background-color: #1c1c24;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
