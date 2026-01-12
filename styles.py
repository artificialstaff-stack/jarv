import streamlit as st

def load_css():
    st.markdown("""
        <style>
            /* 1. IMPORTS & TYPOGRAPHY */
            @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&family=Share+Tech+Mono&display=swap');
            
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background-color: #000000;
                color: #E0E0E0;
            }
            
            h1, h2, h3 {
                font-family: 'Cinzel', serif !important;
                color: #FFFFFF;
                text-transform: uppercase;
                letter-spacing: 2px;
                text-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
            }
            
            /* Metric Values */
            div[data-testid="stMetricValue"] {
                font-family: 'Share Tech Mono', monospace;
                color: #D4AF37 !important; /* Gold */
                text-shadow: 0 0 5px #D4AF37;
            }

            /* 2. UI OVERRIDES */
            /* Hide Default Header/Footer */
            header {visibility: hidden;}
            footer {visibility: hidden;}
            #MainMenu {visibility: hidden;}
            
            /* Main Container Adjustment for Fixed Navbar */
            .main .block-container {
                padding-top: 5rem;
                padding-left: 2rem;
                padding-right: 2rem;
                max-width: 100%;
            }

            /* Sidebar - The Command Center */
            section[data-testid="stSidebar"] {
                background-color: #050505;
                border-right: 1px solid #1A1A1A;
            }
            section[data-testid="stSidebar"] h1 {
                font-size: 1.2rem;
                color: #D4AF37;
            }

            /* 3. INPUT FIELDS (Perplexity Style) */
            .stTextInput input {
                background-color: #0A0A0A;
                border: 1px solid #333;
                border-radius: 20px;
                color: #FFF;
                padding: 10px 15px;
            }
            .stTextInput input:focus {
                border-color: #D4AF37;
                box-shadow: 0 0 10px rgba(212, 175, 55, 0.2);
            }

            /* 4. CUSTOM COMPONENTS */
            
            /* Navbar */
            .custom-navbar {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 70px;
                background: rgba(0, 0, 0, 0.8);
                backdrop-filter: blur(10px);
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 40px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }
            .nav-logo {
                font-family: 'Cinzel';
                font-size: 1.5rem;
                color: #FFF;
                font-weight: bold;
            }
            .nav-links {
                font-family: 'Inter';
                font-size: 0.9rem;
                color: #AAA;
            }
            .nav-cta {
                color: #D4AF37;
                border: 1px solid #D4AF37;
                padding: 5px 15px;
                border-radius: 4px;
                font-family: 'Share Tech Mono';
            }

            /* Bento Grid Card */
            .hub-card {
                background: rgba(20, 20, 20, 0.6);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                padding: 25px;
                transition: all 0.3s ease;
                height: 200px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                cursor: pointer;
            }
            .hub-card:hover {
                border-color: #D4AF37;
                box-shadow: 0 0 20px rgba(212, 175, 55, 0.1);
                transform: translateY(-5px);
            }
            .card-title {
                font-family: 'Cinzel';
                font-size: 1.2rem;
                margin-bottom: 10px;
                color: #FFF;
            }
            .card-desc {
                font-family: 'Inter';
                font-size: 0.8rem;
                color: #888;
            }
            
            /* Buttons */
            .stButton button {
                background-color: transparent;
                border: 1px solid #D4AF37;
                color: #D4AF37;
                font-family: 'Cinzel';
                transition: 0.3s;
                border-radius: 4px;
            }
            .stButton button:hover {
                background-color: #D4AF37;
                color: #000;
            }
            
            /* Animations */
            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
            .animate-text {
                animation: fadeIn 1.5s ease-out forwards;
            }
        </style>
    """, unsafe_allow_html=True)
