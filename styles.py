import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;600&family=Share+Tech+Mono&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        
        <style>
            /* --- GLOBAL RESET --- */
            :root {
                --bg-dark: #050505;
                --gold: #D4AF37;
                --gold-dim: rgba(212, 175, 55, 0.5);
                --glass-bg: rgba(255, 255, 255, 0.03);
                --glass-border: rgba(255, 255, 255, 0.08);
                --text-white: #FFFFFF;
            }

            .stApp {
                background-color: var(--bg-dark);
                font-family: 'Inter', sans-serif;
            }

            /* Header/Footer Gizleme */
            header[data-testid="stHeader"], footer {display: none;}

            /* --- MATRIX TYPEWRITER EFFECT --- */
            .neo-text {
                font-family: 'Share Tech Mono', monospace; /* Matrix benzeri font */
                color: var(--gold);
                font-size: 24px;
                line-height: 1.6;
                white-space: pre-wrap;
                text-shadow: 0 0 10px rgba(212, 175, 55, 0.4);
            }
            
            .cursor {
                display: inline-block;
                width: 10px;
                height: 24px;
                background-color: var(--gold);
                animation: blink 1s infinite;
                vertical-align: middle;
            }

            @keyframes blink {
                0%, 100% { opacity: 1; }
                50% { opacity: 0; }
            }

            /* --- HUB MODULE CARDS (BALONCUK YERİNE) --- */
            .hub-card {
                background: linear-gradient(145deg, rgba(20,20,20,1) 0%, rgba(5,5,5,1) 100%);
                border: 1px solid var(--glass-border);
                border-radius: 12px;
                padding: 40px;
                text-align: center;
                cursor: pointer;
                transition: all 0.4s ease;
                height: 250px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                box-shadow: 0 0 20px rgba(0,0,0,0.8);
            }

            .hub-card:hover {
                border-color: var(--gold);
                box-shadow: 0 0 30px rgba(212, 175, 55, 0.15);
                transform: translateY(-5px);
            }

            .hub-icon {
                font-size: 40px;
                color: var(--gold);
                margin-bottom: 20px;
                text-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
            }

            .hub-title {
                font-family: 'Cinzel', serif;
                font-size: 20px;
                color: white;
                letter-spacing: 2px;
            }

            .hub-desc {
                font-family: 'Inter', sans-serif;
                font-size: 12px;
                color: #666;
                margin-top: 10px;
            }

            /* --- SERVICE GRID (İÇERİK) --- */
            .service-mini-card {
                background: rgba(255,255,255,0.02);
                border-left: 2px solid var(--gold);
                padding: 15px;
                margin-bottom: 10px;
                transition: 0.3s;
            }
            .service-mini-card:hover {
                background: rgba(212, 175, 55, 0.05);
                padding-left: 20px;
            }

            /* --- SCROLLBAR --- */
            ::-webkit-scrollbar { width: 6px; }
            ::-webkit-scrollbar-track { background: #000; }
            ::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
        </style>
    """, unsafe_allow_html=True)
