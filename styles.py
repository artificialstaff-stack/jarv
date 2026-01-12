import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        
        <style>
            /* [STYLE-01] GLOBAL THEME */
            :root {
                --bg-dark: #050505;
                --gold: #D4AF37;
                --glass-border: rgba(255, 255, 255, 0.1);
            }
            .stApp { background-color: var(--bg-dark); font-family: 'Inter', sans-serif; }
            header[data-testid="stHeader"], footer { display: none; }

            /* [STYLE-02] SIDEBAR */
            section[data-testid="stSidebar"] {
                background-color: #080808;
                border-right: 1px solid var(--glass-border);
            }
            /* Menü butonlarını özelleştirme */
            .stRadio > div > label {
                padding: 10px; border-radius: 5px; transition: 0.3s;
                border: 1px solid transparent; margin-bottom: 5px;
            }
            .stRadio > div > label:hover {
                background: rgba(255,255,255,0.05); border-color: var(--gold); color: var(--gold);
            }

            /* [STYLE-03] LOGIN SCREEN */
            div[data-baseweb="input"] {
                background-color: rgba(255,255,255,0.05);
                border: 1px solid var(--glass-border);
                color: white; border-radius: 8px;
            }
            div[data-testid="stButton"] button {
                background: linear-gradient(45deg, #D4AF37, #B69246);
                color: #000; font-family: 'Cinzel', serif; font-weight: bold;
                border: none; width: 100%; padding: 12px; transition: 0.3s;
            }
            div[data-testid="stButton"] button:hover {
                box-shadow: 0 0 20px rgba(212,175,55,0.4); transform: scale(1.02);
            }

            /* [STYLE-04] WELCOME ANIMATION TEXT */
            .welcome-text {
                font-family: 'Inter'; font-size: 24px; color: #ddd;
                text-align: center; font-weight: 300; animation: fadeIn 1s;
            }
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

            /* [STYLE-05] HUB CARDS */
            .hub-card {
                background: linear-gradient(145deg, rgba(20,20,20,1) 0%, rgba(5,5,5,1) 100%);
                border: 1px solid var(--glass-border); border-radius: 12px;
                padding: 30px; text-align: center; height: 220px;
                display: flex; flex-direction: column; align-items: center; justify-content: center;
                transition: 0.3s;
            }
            .hub-card:hover { border-color: var(--gold); transform: translateY(-5px); }
            .hub-icon { font-size: 32px; color: var(--gold); margin-bottom: 15px; }
            .hub-title { font-family: 'Cinzel'; font-size: 18px; color: white; }
            .hub-desc { font-size: 12px; color: #888; margin-top: 5px; }

            /* [STYLE-06] SERVICE MINI CARDS */
            .service-mini-card {
                background: rgba(255,255,255,0.02); border-left: 2px solid var(--gold);
                padding: 15px; margin-bottom: 10px; border-radius: 0 8px 8px 0;
            }
        </style>
    """, unsafe_allow_html=True)
