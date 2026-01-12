import streamlit as st

def load_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&family=Share+Tech+Mono&display=swap');
            
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background-color: #050505;
                color: #E0E0E0;
            }
            
            h1, h2, h3 {
                font-family: 'Cinzel', serif !important;
                color: #FFFFFF;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            
            /* FORM ALANLARI (EXPANDER) */
            .streamlit-expanderHeader {
                background-color: #111;
                border: 1px solid #333;
                border-radius: 8px;
                color: #D4AF37; /* Gold Başlıklar */
                font-family: 'Cinzel';
            }
            
            /* INPUTLAR */
            .stTextInput input, .stSelectbox div, .stNumberInput input {
                background-color: #0A0A0A;
                border: 1px solid #333;
                border-radius: 5px;
                color: #FFF;
            }
            .stTextInput input:focus {
                border-color: #D4AF37;
            }

            /* BUTONLAR */
            .stButton button {
                background-color: #D4AF37;
                color: #000;
                font-weight: bold;
                border: none;
                transition: 0.3s;
                width: 100%;
            }
            .stButton button:hover {
                background-color: #FFF;
                color: #000;
            }

            /* CHAT KUTUSU */
            .stChatMessage {
                background-color: #111;
                border: 1px solid #222;
                border-radius: 10px;
            }

            /* NAVBAR */
            .custom-navbar {
                position: fixed;
                top: 0; left: 0; width: 100%; height: 60px;
                background: rgba(0,0,0,0.95);
                border-bottom: 1px solid #333;
                z-index: 9999;
                display: flex; align-items: center; justify-content: space-between;
                padding: 0 40px;
            }
            .nav-logo { font-family: 'Cinzel'; font-size: 1.5rem; color: #FFF; }
            .nav-cta { color: #D4AF37; font-family: 'Share Tech Mono'; }

        </style>
    """, unsafe_allow_html=True)
