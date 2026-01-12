import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        
        <style>
            /* --- GLOBAL RESET --- */
            :root {
                --bg-dark: #050505;
                --gold: #D4AF37;
                --gold-glow: rgba(212, 175, 55, 0.3);
                --glass-bg: rgba(255, 255, 255, 0.03);
                --glass-border: rgba(255, 255, 255, 0.08);
                --text-white: #FFFFFF;
                --text-gray: #A0A0A0;
            }

            .stApp {
                background-color: var(--bg-dark);
                font-family: 'Inter', sans-serif;
            }

            /* Header/Footer Gizleme */
            header[data-testid="stHeader"], footer {display: none;}

            /* --- SERVICE CARDS (LÜKS KARTLAR) --- */
            .service-card {
                background: linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.01) 100%);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid var(--glass-border);
                border-radius: 16px;
                padding: 30px 25px;
                height: 280px; /* Kartları eşitlemek için */
                transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                position: relative;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
            }

            /* Hover Efekti: Kart yukarı kalkar ve kenarı parlar */
            .service-card:hover {
                transform: translateY(-8px);
                border-color: var(--gold);
                box-shadow: 0 15px 40px -10px rgba(0,0,0,0.8), 0 0 20px -10px var(--gold-glow);
            }

            /* İkon Tasarımı */
            .card-icon {
                font-size: 32px;
                background: -webkit-linear-gradient(45deg, #D4AF37, #F3E5AB);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 20px;
                filter: drop-shadow(0 0 10px rgba(212,175,55,0.3));
            }

            /* Başlık Tasarımı */
            .card-title {
                font-family: 'Cinzel', serif;
                font-size: 18px;
                font-weight: 600;
                color: var(--text-white);
                margin-bottom: 12px;
                letter-spacing: 0.5px;
            }

            /* Açıklama Tasarımı */
            .card-desc {
                font-family: 'Inter', sans-serif;
                font-size: 13px;
                color: var(--text-gray);
                line-height: 1.6;
                font-weight: 300;
            }

            /* --- SIDEBAR --- */
            section[data-testid="stSidebar"] {
                background-color: #000000;
                border-right: 1px solid var(--glass-border);
            }
            
            /* Sidebar Butonları */
            .stRadio > div > label {
                color: var(--text-gray);
                padding: 12px;
                border-radius: 8px;
                transition: 0.3s;
                border: 1px solid transparent;
            }
            .stRadio > div > label:hover {
                color: var(--gold);
                background: var(--glass-bg);
                border-color: var(--glass-border);
            }
            /* Seçili Olan */
            .stRadio > div [data-testid="stMarkdownContainer"] > p {
                font-weight: 600;
                letter-spacing: 1px;
            }

            /* --- SCROLLBAR --- */
            ::-webkit-scrollbar { width: 6px; }
            ::-webkit-scrollbar-track { background: #000; }
            ::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
        </style>
    """, unsafe_allow_html=True)
