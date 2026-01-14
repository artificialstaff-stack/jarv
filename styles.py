import streamlit as st

def load_css():
    """
    Injects the 'Enterprise-Grade' CSS design system into the Streamlit app.
    Fixes sidebar conflicts and applies a high-end dark theme.
    """
    
    # --- 1. TEMEL AYARLAR & DEĞİŞKENLER ---
    st.markdown("""
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

        :root {
            /* Palette: Deep Dark Mode */
            --bg-app: #000000;
            --bg-secondary: #09090B;
            --bg-card: rgba(255, 255, 255, 0.03);
            
            /* Text */
            --text-primary: #FAFAFA;
            --text-secondary: #A1A1AA;
            
            /* Borders & Glass */
            --border-subtle: rgba(255, 255, 255, 0.08);
            --border-focus: rgba(255, 255, 255, 0.15);
            
            /* Accents (Neon) */
            --accent-blue: #3B82F6;
            --accent-purple: #8B5CF6;
            --accent-green: #10B981;
            --accent-red: #EF4444;
        }

        /* Global Reset */
        html, body, .stApp {
            background-color: var(--bg-app);
            font-family: 'Inter', sans-serif;
            color: var(--text-primary);
        }
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: var(--bg-app); }
        ::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #555; }
    </style>
    """, unsafe_allow_html=True)

    # --- 2. HEADER & SIDEBAR DÜZENİ (KRİTİK BÖLÜM) ---
    st.markdown("""
    <style>
        /* Header'ı şeffaf yap ama YOK ETME (Butonun yaşaması için) */
        header[data-testid="stHeader"] {
            background: transparent !important;
            pointer-events: none; /* Tıklamaları alta geçir */
        }
        
        /* Sidebar Tasarımı */
        section[data-testid="stSidebar"] {
            background-color: #050505;
            border-right: 1px solid var(--border-subtle);
            box-shadow: 10px 0 30px rgba(0,0,0,0.5);
        }
        
        /* Sidebar içindeki elementlerin rengi */
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
            color: #E4E4E7;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- 3. INPUTLAR & BUTONLAR (MİKRO ETKİLEŞİMLER) ---
    st.markdown("""
    <style>
        /* Inputs: Modern React Style */
        .stTextInput input, .stSelectbox div[data-baseweb="select"], .stNumberInput input, .stTextArea textarea, .stChatInput textarea {
            background-color: var(--bg-secondary) !important;
            border: 1px solid var(--border-subtle) !important;
            color: var(--text-primary) !important;
            border-radius: 10px !important;
            font-size: 14px;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* Input Focus Glow */
        .stTextInput input:focus, .stChatInput textarea:focus {
            border-color: var(--accent-blue) !important;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
            transform: translateY(-1px);
        }

        /* Buttons: Alive & Tactile */
        .stButton button {
            background: linear-gradient(180deg, #27272A 0%, #18181B 100%);
            border: 1px solid var(--border-subtle);
            color: #E4E4E7;
            font-weight: 600;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            transition: all 0.2s ease;
        }
        
        .stButton button:hover {
            border-color: #52525B;
            color: #FFF;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        }

        /* Primary Action Button (Mavi) */
        .stButton button[kind="primary"] {
            background: linear-gradient(135deg, var(--accent-blue) 0%, #2563EB 100%);
            border: none;
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.3);
        }
        .stButton button[kind="primary"]:hover {
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.5);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- 4. GELİŞMİŞ KART & METRİK TASARIMLARI ---
    st.markdown("""
    <style>
        /* PRO METRIC CARD */
        .pro-metric-card {
            background: var(--bg-card);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 24px;
            display: flex;
            align-items: center;
            gap: 20px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        
        .pro-metric-card:hover {
            transform: translateY(-4px);
            border-color: rgba(255, 255, 255, 0.15);
            box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.5);
        }

        /* Icon Container */
        .metric-icon-box {
            width: 52px; height: 52px;
            border-radius: 14px;
            display: flex; align-items: center; justify-content: center;
            font-size: 24px;
            flex-shrink: 0;
        }
        
        /* Themes */
        .theme-blue { background: rgba(59, 130, 246, 0.1); color: var(--accent-blue); border: 1px solid rgba(59, 130, 246, 0.2); }
        .theme-green { background: rgba(16, 185, 129, 0.1); color: var(--accent-green); border: 1px solid rgba(16, 185, 129, 0.2); }
        .theme-purple { background: rgba(139, 92, 246, 0.1); color: var(--accent-purple); border: 1px solid rgba(139, 92, 246, 0.2); }
        .theme-orange { background: rgba(249, 115, 22, 0.1); color: #F97316; border: 1px solid rgba(249, 115, 22, 0.2); }
        .theme-red { background: rgba(239, 68, 68, 0.1); color: var(--accent-red); border: 1px solid rgba(239, 68, 68, 0.2); }

        /* Typography */
        .metric-label { font-size: 12px; font-weight: 600; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.5px; }
        .metric-value { font-size: 28px; font-weight: 700; color: #FFF; letter-spacing: -0.5px; line-height: 1.1; margin-top: 4px; }
        
        /* Delta Badge */
        .metric-delta {
            display: inline-flex; align-items: center; gap: 4px;
            padding: 2px 8px; border-radius: 999px;
            font-size: 11px; font-weight: 700;
            margin-top: 8px; width: fit-content;
        }
        .delta-up { background: rgba(16, 185, 129, 0.15); color: #34D399; }
        .delta-down { background: rgba(239, 68, 68, 0.15); color: #F87171; }

        /* Chart Containers */
        .stPlotlyChart {
            background: transparent;
            border-radius: 16px;
        }
    </style>
    """, unsafe_allow_html=True)
