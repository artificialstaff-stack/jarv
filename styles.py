import streamlit as st

def load_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

            /* --- 1. GLOBAL RESET (SİMSİYAH TEMA) --- */
            :root {
                --bg-color: #000000;
                --card-bg: #0a0a0a;
                --text-white: #ffffff;
                --text-gray: #888888;
                --accent-gold: #D4AF37; 
                --hover-bg: #1a1a1a;
            }

            .stApp {
                background-color: var(--bg-color);
                font-family: 'Inter', sans-serif;
                color: var(--text-white);
            }

            /* Streamlit varsayılanlarını gizle */
            header, footer, #MainMenu {display: none !important;}
            .block-container {
                padding-top: 0rem !important;
                padding-bottom: 0rem !important;
                padding-left: 0rem !important;
                padding-right: 0rem !important;
                max-width: 100% !important;
            }

            /* --- 2. NAVBAR --- */
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px 40px;
                background: rgba(0,0,0,0.8);
                backdrop-filter: blur(10px);
                position: fixed;
                top: 0;
                width: 100%;
                z-index: 999;
                border-bottom: 1px solid rgba(255,255,255,0.05);
            }
            .nav-logo {
                font-size: 20px;
                font-weight: 800;
                color: white;
                letter-spacing: -1px;
            }
            .nav-links a {
                color: var(--text-gray);
                text-decoration: none;
                margin: 0 15px;
                font-size: 14px;
                transition: 0.3s;
            }
            .nav-links a:hover { color: white; }
            .nav-btn {
                background: white;
                color: black;
                padding: 8px 20px;
                border-radius: 20px;
                font-weight: 600;
                font-size: 13px;
                text-decoration: none;
            }

            /* --- 3. HERO SECTION (VİDEODAKİ GİBİ) --- */
            .hero-container {
                height: 85vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                background: radial-gradient(circle at center, #1a1a1a 0%, #000000 70%);
                padding: 0 20px;
                margin-top: 60px;
            }
            .hero-badge {
                border: 1px solid #333;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 12px;
                color: var(--text-gray);
                margin-bottom: 20px;
                background: rgba(255,255,255,0.05);
            }
            .hero-title {
                font-size: 72px;
                font-weight: 800;
                line-height: 1.1;
                margin-bottom: 20px;
                background: linear-gradient(180deg, #fff 0%, #aaa 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: -2px;
            }
            .hero-sub {
                font-size: 18px;
                color: var(--text-gray);
                max-width: 600px;
                margin-bottom: 40px;
            }
            .hero-cta {
                background: var(--text-white);
                color: black;
                padding: 15px 40px;
                border-radius: 30px;
                font-weight: 600;
                font-size: 16px;
                text-decoration: none;
                transition: transform 0.2s;
            }
            .hero-cta:hover { transform: scale(1.05); }

            /* --- 4. BENTO GRID (KARTLAR) --- */
            .bento-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                padding: 40px;
                max-width: 1400px;
                margin: 0 auto;
            }
            .bento-card {
                background-color: var(--card-bg);
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 24px;
                padding: 30px;
                height: 300px;
                display: flex;
                flex-direction: column;
                justify-content: flex-end;
                transition: all 0.4s ease;
                position: relative;
                overflow: hidden;
                cursor: pointer;
            }
            .bento-card:hover {
                background-color: var(--hover-bg);
                border-color: rgba(255,255,255,0.2);
                transform: translateY(-5px);
            }
            .card-img-placeholder {
                position: absolute;
                top: 0; left: 0; width: 100%; height: 100%;
                background: linear-gradient(to bottom, transparent, #000);
                opacity: 0.5;
                z-index: 1;
            }
            .card-content {
                position: relative;
                z-index: 2;
            }
            .card-title {
                font-size: 24px;
                font-weight: 700;
                margin-bottom: 10px;
                color: white;
            }
            .card-desc {
                font-size: 14px;
                color: var(--text-gray);
            }
            .card-icon {
                position: absolute;
                top: 20px;
                right: 20px;
                font-size: 24px;
                color: var(--text-white);
                z-index: 2;
            }

            /* Responsive */
            @media (max-width: 768px) {
                .hero-title { font-size: 42px; }
                .nav-links { display: none; }
                .bento-grid { grid-template-columns: 1fr; }
            }
        </style>
    """, unsafe_allow_html=True)
