import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        
        <style>
            /* --- GLOBAL AYARLAR --- */
            :root {
                --bg-dark: #050505;
                --gold: #D4AF37;
                --text-white: #FFFFFF;
                --glass-border: rgba(255, 255, 255, 0.1);
                --card-bg: rgba(255, 255, 255, 0.03);
            }

            .stApp {
                background-color: var(--bg-dark);
                font-family: 'Inter', sans-serif;
            }

            /* Header ve Footer'ı Gizle */
            header[data-testid="stHeader"], footer {display: none;}

            /* --- SIDEBAR TASARIMI --- */
            section[data-testid="stSidebar"] {
                background-color: #080808;
                border-right: 1px solid var(--glass-border);
            }
            
            /* --- LOGIN EKRANI --- */
            .login-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin-top: 100px;
            }
            
            /* Input Alanları */
            div[data-baseweb="input"] {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid var(--glass-border);
                color: white;
                border-radius: 8px;
            }
            
            /* Butonlar */
            div[data-testid="stButton"] button {
                background: linear-gradient(45deg, #D4AF37, #B69246);
                color: #000;
                font-weight: bold;
                border: none;
                width: 100%;
                padding: 10px;
                font-family: 'Cinzel', serif;
                transition: 0.3s;
            }
            div[data-testid="stButton"] button:hover {
                box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
                transform: scale(1.02);
                color: #000;
            }

            /* --- KARŞILAMA METNİ (ANIMASYONLU) --- */
            .welcome-text {
                font-family: 'Inter', sans-serif;
                font-size: 24px;
                color: #e0e0e0;
                text-align: center;
                line-height: 1.5;
                font-weight: 300;
                animation: fadeIn 1s ease-in;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            /* --- HUB KARTLARI (BALONCUK YERİNE) --- */
            .hub-card {
                background: linear-gradient(145deg, rgba(20,20,20,1) 0%, rgba(5,5,5,1) 100%);
                border: 1px solid var(--glass-border);
                border-radius: 12px;
                padding: 30px;
                text-align: center;
                height: 220px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            }
            .hub-card:hover {
                border-color: var(--gold);
                transform: translateY(-5px);
                box-shadow: 0 10px 30px rgba(212, 175, 55, 0.1);
            }
            .hub-icon {
                font-size: 32px;
                color: var(--gold);
                margin-bottom: 15px;
            }
            .hub-title {
                font-family: 'Cinzel', serif;
                font-size: 16px;
                color: white;
                margin-bottom: 8px;
            }
            .hub-desc {
                font-size: 12px;
                color: #888;
            }

            /* --- METRIC KARTLARI --- */
            div[data-testid="metric-container"] {
                background-color: var(--card-bg);
                border: 1px solid var(--glass-border);
                padding: 15px;
                border-radius: 10px;
            }
            div[data-testid="metric-container"] label {
                font-family: 'Cinzel', serif;
                color: #888;
            }
            div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
                color: #fff;
            }
        </style>
    """, unsafe_allow_html=True)
