import streamlit as st

def apply_tech_style():
    st.markdown("""
    <style>
        /* --- FONTLAR --- */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Orbitron:wght@400;700&display=swap');
        
        /* --- GENEL SAYFA YAPISI --- */
        .stApp {
            background-color: #050505;
            background-image: 
                radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
                radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), 
                radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%);
            color: #e0e0e0;
            font-family: 'Inter', sans-serif;
        }

        /* --- SIDEBAR (SOL PANEL) --- */
        section[data-testid="stSidebar"] {
            background-color: rgba(10, 10, 15, 0.8);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }

        /* --- BAŞLIKLAR (Gradient Efekt) --- */
        h1, h2, h3 {
            font-family: 'Orbitron', sans-serif;
            background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
        }

        /* --- CHAT MESAJ KUTULARI --- */
        .stChatMessage {
            background-color: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 10px;
            transition: transform 0.2s;
        }
        .stChatMessage:hover {
            border-color: rgba(0, 201, 255, 0.3);
            background-color: rgba(255, 255, 255, 0.05);
        }

        /* --- INPUT ALANI --- */
        .stChatInput textarea {
            background-color: #111 !important;
            color: white !important;
            border: 1px solid #333 !important;
            border-radius: 20px !important;
        }

        /* --- METRİK KARTLARI --- */
        div[data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.02);
            padding: 15px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        div[data-testid="stMetricLabel"] {
            font-size: 0.8rem;
            color: #888;
        }
        div[data-testid="stMetricValue"] {
            font-family: 'Orbitron', sans-serif;
            color: #00C9FF;
        }
    </style>
    """, unsafe_allow_html=True)
