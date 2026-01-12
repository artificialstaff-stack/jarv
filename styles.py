import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
        
        <style>
            /* --- 1. GLOBAL RESET & TEMEL AYARLAR --- */
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

            /* Streamlit Header/Footer Gizleme */
            header[data-testid="stHeader"] {display: none;}
            footer {display: none;}
            
            /* --- 2. TYPOGRAPHY --- */
            h1, h2, h3 {
                font-family: 'Cinzel', serif !important;
                color: var(--text-white) !important;
                font-weight: 600 !important;
            }
            
            p, span, label {
                color: var(--text-silver);
            }

            /* --- 3. SIDEBAR (YAN MENÜ) --- */
            section[data-testid="stSidebar"] {
                background-color: #000000;
                border-right: 1px solid var(--border-light);
            }
            
            /* Sidebar Navigasyon Butonları */
            .stRadio > div {
                background-color: transparent;
            }
            .stRadio > div > label {
                background-color: transparent;
                color: var(--text-silver);
                border: 1px solid transparent;
                padding: 12px;
                border-radius: 8px;
                transition: all 0.3s;
                cursor: pointer;
                font-family: 'Inter', sans-serif;
                margin-bottom: 5px;
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

            /* --- 4. METRIC CARDS (BENTO GRID) --- */
            div[data-testid="metric-container"] {
                background-color: var(--bg-card);
                backdrop-filter: blur(10px);
                border: 1px solid var(--border-light);
                padding: 24px;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
                transition: transform 0.3s ease, border-color 0.3s ease;
            }
            
            div[data-testid="metric-container"]:hover {
                transform: translateY(-4px);
                border-color: rgba(212, 175, 55, 0.4);
            }

            /* Metrik Etiketleri */
            div[data-testid="metric-container"] label {
                font-size: 12px !important;
                text-transform: uppercase;
                letter-spacing: 1.5px;
                color: var(--text-silver) !important;
            }
            
            /* Metrik Değerleri */
            div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
                font-family: 'Inter', sans-serif;
                font-size: 32px !important;
                color: var(--text-white) !important;
                font-weight: 600;
            }

            /* Delta (Değişim) Değerleri */
            div[data-testid="metric-container"] div[data-testid="stMetricDelta"] {
                font-family: 'Inter', sans-serif;
                background-color: rgba(46, 125, 50, 0.1);
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 12px !important;
            }
            
            /* --- 5. NOTIFICATION PANEL --- */
            .notification-box {
                background-color: var(--bg-card);
                border: 1px solid var(--border-light);
                border-radius: 12px;
                padding: 20px;
                height: 400px;
                overflow-y: auto;
            }
            .notif-header {
                font-family: 'Cinzel', serif;
                color: var(--text-white);
                font-size: 18px;
                margin-bottom: 20px;
                border-bottom: 1px solid var(--border-light);
                padding-bottom: 10px;
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
                width: 8px;
                height: 8px;
                border-radius: 50%;
                margin-top: 6px;
                margin-right: 12px;
                box-shadow: 0 0 5px rgba(255,255,255,0.2);
            }
            .notif-content h4 {
                font-family: 'Inter', sans-serif !important;
                font-size: 14px;
                margin: 0;
                color: var(--text-white);
            }
            .notif-content p {
                font-size: 12px;
                margin: 4px 0 0 0;
                color: #666;
            }
            
            /* Custom Scrollbar */
            ::-webkit-scrollbar { width: 8px; }
            ::-webkit-scrollbar-track { background: #000; }
            ::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
            ::-webkit-scrollbar-thumb:hover { background: var(--gold); }
            
        </style>
    """, unsafe_allow_html=True)
