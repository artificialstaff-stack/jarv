import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Cinzel:wght@500;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        
        <style>
            /* --- 1. GLOBAL TEMELLER (PERPLEXITY DARK) --- */
            :root {
                --bg-color: #191A1A; /* Perplexity tarzı koyu gri */
                --sidebar-bg: #111111;
                --gold: #D4AF37;
                --text-main: #E8E8E8;
                --text-dim: #9ca3af;
                --border-color: rgba(255, 255, 255, 0.1);
                --input-bg: #202222;
            }

            .stApp {
                background-color: var(--bg-color);
                font-family: 'Inter', sans-serif;
                color: var(--text-main);
            }

            /* Gereksizleri Gizle */
            header[data-testid="stHeader"], footer {display: none;}
            
            /* --- 2. SIDEBAR (Sol Menü) --- */
            section[data-testid="stSidebar"] {
                background-color: var(--sidebar-bg);
                border-right: 1px solid var(--border-color);
            }
            .stRadio > div > label {
                color: var(--text-dim);
                padding: 10px 15px;
                border-radius: 8px;
                transition: all 0.2s;
                font-weight: 500;
                border: 1px solid transparent;
            }
            .stRadio > div > label:hover {
                color: var(--gold);
                background-color: rgba(212, 175, 55, 0.05);
                border-color: rgba(212, 175, 55, 0.2);
            }
            /* Seçili Olan */
            .stRadio > div [data-testid="stMarkdownContainer"] > p {
                font-weight: 600;
                color: #fff;
            }

            /* --- 3. INPUT ALANI (PERPLEXITY STYLE SEARCH) --- */
            /* Chat Input ve Text Input */
            .stTextInput input, .stChatInput textarea {
                background-color: var(--input-bg) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 24px !important; /* Yuvarlak köşeler */
                color: white !important;
                padding: 15px 20px !important;
                font-size: 16px !important;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            }
            .stTextInput input:focus, .stChatInput textarea:focus {
                border-color: var(--gold) !important;
                box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.2) !important;
            }

            /* --- 4. BUTONLAR (Pill/Chip Style) --- */
            div[data-testid="stButton"] button {
                background-color: rgba(255, 255, 255, 0.05);
                color: var(--text-dim);
                border: 1px solid var(--border-color);
                border-radius: 20px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
                transition: 0.3s;
            }
            div[data-testid="stButton"] button:hover {
                border-color: var(--gold);
                color: var(--gold);
                background-color: rgba(212, 175, 55, 0.05);
            }

            /* --- 5. KARTLAR (Minimalist & Clean) --- */
            .info-card {
                background-color: #202222;
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 24px;
                transition: transform 0.2s, border-color 0.2s;
                height: 100%;
            }
            .info-card:hover {
                border-color: rgba(212, 175, 55, 0.5);
                transform: translateY(-2px);
            }
            .card-icon {
                font-size: 24px;
                color: var(--gold);
                margin-bottom: 16px;
            }
            .card-title {
                font-family: 'Inter', sans-serif;
                font-size: 16px;
                font-weight: 600;
                color: #fff;
                margin-bottom: 8px;
            }
            .card-desc {
                font-size: 13px;
                color: var(--text-dim);
                line-height: 1.5;
            }

            /* --- 6. METRIK KUTULARI --- */
            div[data-testid="metric-container"] {
                background-color: #202222;
                border: 1px solid var(--border-color);
                padding: 20px;
                border-radius: 12px;
            }
            div[data-testid="metric-container"] label {
                font-size: 12px;
                color: var(--text-dim);
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
                font-family: 'Inter', sans-serif;
                font-size: 28px;
                color: #fff;
            }

            /* --- 7. KARŞILAMA YAZISI --- */
            .hero-title {
                font-family: 'Cinzel', serif;
                font-size: 48px;
                text-align: center;
                background: linear-gradient(180deg, #FFFFFF 0%, #888888 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 10px;
            }
            .hero-subtitle {
                font-family: 'Inter', sans-serif;
                font-size: 16px;
                text-align: center;
                color: var(--text-dim);
                margin-bottom: 40px;
                font-weight: 300;
            }
        </style>
    """, unsafe_allow_html=True)
