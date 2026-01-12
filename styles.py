import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
        
        <style>
            /* --- GLOBAL THEME --- */
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

            /* Header/Footer Gizle */
            header[data-testid="stHeader"] {display: none;}
            footer {display: none;}

            /* --- TYPOGRAPHY --- */
            h1, h2, h3, h4 {
                font-family: 'Cinzel', serif !important;
                color: var(--text-white) !important;
                font-weight: 600 !important;
            }
            
            p, span, label, div {
                font-family: 'Inter', sans-serif;
                color: var(--text-silver);
            }

            /* --- SIDEBAR --- */
            section[data-testid="stSidebar"] {
                background-color: #000000;
                border-right: 1px solid var(--border-light);
            }
            
            /* Sidebar Radio Buttons */
            .stRadio > div { background-color: transparent; }
            .stRadio > div > label {
                background-color: transparent;
                color: var(--text-silver);
                border: 1px solid transparent;
                padding: 12px;
                border-radius: 8px;
                transition: all 0.3s;
                cursor: pointer;
            }
            .stRadio > div > label:hover {
                color: var(--gold);
                background-color: var(--bg-card);
                border: 1px solid var(--border-light);
            }
            /* Seçili Olan */
            .stRadio > div [data-testid="stMarkdownContainer"] > p {
                font-size: 14px;
                font-weight: 500;
            }

            /* --- METRIC CARDS (Bento Grid) --- */
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
                color: #4ade80 !important; /* Canlı yeşil */
            }
            div[data-testid="metric-container"] div[data-testid="stMetricDelta"] svg {
                fill: #4ade80 !important;
            }

            /* --- NOTIFICATION PANEL FIX --- */
            /* Bu class'lar views.py içinde kullanılacak */
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

            /* --- CHAT INTERFACE (JARVIS) --- */
            .chat-message {
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 10px;
                font-family: 'Inter', sans-serif;
                font-size: 14px;
                max-width: 80%;
            }
            .chat-user {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid var(--border-light);
                margin-left: auto;
                color: white;
                text-align: right;
            }
            .chat-bot {
                background-color: rgba(212, 175, 55, 0.1); /* Gold tint */
                border: 1px solid rgba(212, 175, 55, 0.2);
                margin-right: auto;
                color: #ddd;
            }

            /* --- SCROLLBAR --- */
            ::-webkit-scrollbar { width: 6px; }
            ::-webkit-scrollbar-track { background: #000; }
            ::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
            ::-webkit-scrollbar-thumb:hover { background: var(--gold); }
        </style>
    """, unsafe_allow_html=True)
