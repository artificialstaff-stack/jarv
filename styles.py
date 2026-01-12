import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
        
        <style>
            /* --- 1. GLOBAL RESET & THEME --- */
            :root {
                --bg-dark: #050505;
                --bg-card: rgba(255, 255, 255, 0.03);
                --border-light: rgba(255, 255, 255, 0.08);
                --gold: #D4AF37;
                --text-silver: #888888;
                --text-white: #FFFFFF;
            }

            .stApp {
                background-color: var(--bg-dark);
                font-family: 'Inter', sans-serif;
            }

            /* Hide Streamlit Header/Footer/Menu */
            header[data-testid="stHeader"] {display: none;}
            footer {display: none;}
            #MainMenu {display: none;}
            
            /* --- 2. TYPOGRAPHY --- */
            h1, h2, h3, h4 {
                font-family: 'Cinzel', serif !important;
                color: var(--text-white) !important;
                font-weight: 600 !important;
            }
            
            p, span, label, div {
                font-family: 'Inter', sans-serif;
                color: var(--text-silver);
            }

            /* --- 3. SIDEBAR STYLING --- */
            section[data-testid="stSidebar"] {
                background-color: #000000;
                border-right: 1px solid var(--border-light);
            }
            
            /* Custom Sidebar Nav Buttons (Radio) */
            .stRadio > div { background-color: transparent; }
            .stRadio > div > label {
                background-color: transparent;
                color: var(--text-silver);
                border: 1px solid transparent;
                padding: 12px;
                border-radius: 8px;
                transition: all 0.3s;
                cursor: pointer;
                margin-bottom: 5px;
            }
            .stRadio > div > label:hover {
                color: var(--gold);
                background-color: var(--bg-card);
                border: 1px solid var(--border-light);
            }
            
            /* Selected State */
            .stRadio > div [data-testid="stMarkdownContainer"] > p {
                font-size: 14px;
                font-weight: 500;
            }

            /* --- 4. BENTO GRID METRIC CARDS --- */
            div[data-testid="metric-container"] {
                background-color: var(--bg-card);
                backdrop-filter: blur(10px);
                border: 1px solid var(--border-light);
                padding: 20px;
                border-radius: 12px;
                transition: transform 0.3s ease, border-color 0.3s ease;
            }
            div[data-testid="metric-container"]:hover {
                transform: translateY(-4px);
                border-color: rgba(212, 175, 55, 0.4);
            }
            div[data-testid="metric-container"] label {
                font-size: 11px !important;
                text-transform: uppercase;
                letter-spacing: 1.5px;
            }
            div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
                font-size: 28px !important;
                color: var(--text-white) !important;
            }
            div[data-testid="metric-container"] div[data-testid="stMetricDelta"] {
                background-color: rgba(46, 125, 50, 0.15);
                padding: 4px 8px;
                border-radius: 4px;
                color: #4ade80 !important; /* Vivid Green */
            }
            div[data-testid="metric-container"] div[data-testid="stMetricDelta"] svg {
                fill: #4ade80 !important;
            }

            /* --- 5. NOTIFICATION PANEL (HTML/CSS) --- */
            .notification-box {
                background-color: var(--bg-card);
                border: 1px solid var(--border-light);
                border-radius: 12px;
                padding: 20px;
                height: 400px;
                overflow-y: auto;
            }
            .notif-item {
                display: flex;
                align-items: flex-start;
                padding: 12px;
                margin-bottom: 12px;
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.02);
                border-left: 2px solid #333;
                transition: all 0.2s;
            }
            .notif-item:hover {
                background: rgba(255, 255, 255, 0.05);
                border-left: 2px solid var(--gold);
            }
            .status-dot {
                min-width: 8px;
                height: 8px;
                border-radius: 50%;
                margin-top: 6px;
                margin-right: 12px;
                box-shadow: 0 0 5px rgba(255,255,255,0.2);
            }
            .notif-content h4 {
                font-family: 'Inter', sans-serif !important;
                font-size: 14px !important;
                margin: 0 !important;
                color: var(--text-white) !important;
                font-weight: 600 !important;
            }
            .notif-content p {
                font-size: 12px !important;
                margin: 4px 0 0 0 !important;
                color: #888 !important;
                line-height: 1.4 !important;
            }

            /* --- 6. SCROLLBAR --- */
            ::-webkit-scrollbar { width: 6px; }
            ::-webkit-scrollbar-track { background: #000; }
            ::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
            ::-webkit-scrollbar-thumb:hover { background: var(--gold); }
        </style>
    """, unsafe_allow_html=True)
