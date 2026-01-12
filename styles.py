import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&family=Share+Tech+Mono&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        
        <style>
            /* [STYLE-01] GLOBAL RESET */
            :root {
                --bg-dark: #0e0e0e;
                --sidebar-bg: #050505;
                --gold: #D4AF37;
                --border-color: rgba(255, 255, 255, 0.08);
            }
            .stApp { background-color: var(--bg-dark); font-family: 'Inter', sans-serif; }

            /* [STYLE-02] HEADER & SIDEBAR TOGGLE FIX (KRİTİK DÜZELTME) */
            /* Header'ı tamamen gizlemek yerine şeffaf yapıyoruz ki ok tuşu görünsün */
            header[data-testid="stHeader"] {
                background-color: transparent !important;
                z-index: 1;
            }
            
            /* Sadece rahatsız edici renkli şeridi ve hamburger menüyü gizle */
            [data-testid="stDecoration"] {display: none;}
            #MainMenu {visibility: hidden;}
            .stAppDeployButton {display: none;}

            /* [STYLE-03] SIDEBAR TASARIMI */
            section[data-testid="stSidebar"] {
                background-color: var(--sidebar-bg);
                border-right: 1px solid var(--border-color);
                width: 300px !important;
            }
            
            /* Sidebar İçeriği */
            .sidebar-logo {
                font-family: 'Cinzel', serif; font-size: 28px; color: var(--gold);
                text-align: center; letter-spacing: 4px; margin-bottom: 5px;
                text-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
            }
            .sidebar-sub {
                font-family: 'Share Tech Mono', monospace; font-size: 10px; color: #444;
                text-align: center; letter-spacing: 2px; margin-bottom: 40px;
            }

            /* Menü Butonları */
            .stRadio > div { gap: 12px; }
            .stRadio > div > label {
                background-color: transparent; color: #666; padding: 12px 20px;
                border-radius: 4px; font-family: 'Inter', sans-serif; font-size: 12px;
                font-weight: 500; letter-spacing: 1px; border-left: 2px solid transparent;
                transition: all 0.3s; text-transform: uppercase;
            }
            .stRadio > div > label:hover {
                color: white; background: linear-gradient(90deg, rgba(255,255,255,0.05) 0%, transparent 100%);
                border-left: 2px solid var(--gold);
            }
            /* Seçili Olan */
            .stRadio > div [data-testid="stMarkdownContainer"] > p {
                color: var(--gold); font-weight: 700;
            }

            /* Durum Göstergesi (Sidebar Altı) */
            .sidebar-status {
                margin-top: 50px; padding: 20px; border-top: 1px solid #111;
                font-family: 'Share Tech Mono', monospace; font-size: 10px; color: #444;
            }
            .status-dot {
                display: inline-block; width: 6px; height: 6px;
                background-color: #00ff88; border-radius: 50%;
                box-shadow: 0 0 8px #00ff88; margin-right: 6px;
            }

            /* [STYLE-04] PERPLEXITY SEARCH BAR */
            .stChatInput textarea {
                background-color: #1a1a1a !important; border: 1px solid #333 !important;
                border-radius: 30px !important; color: white !important;
                padding: 15px 25px !important;
            }
            .stChatInput textarea:focus {
                border-color: var(--gold) !important;
                box-shadow: 0 0 15px rgba(212, 175, 55, 0.1) !important;
            }

            /* [STYLE-05] CARDS */
            .glass-card {
                background: rgba(255, 255, 255, 0.02); border: 1px solid var(--border-color);
                border-radius: 12px; padding: 25px; transition: 0.3s; height: 100%;
            }
            .glass-card:hover {
                border-color: var(--gold); background: rgba(212, 175, 55, 0.05); transform: translateY(-5px);
            }
        </style>
    """, unsafe_allow_html=True)
