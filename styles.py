import streamlit as st

def load_css():
    st.markdown("""
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

        /* --- 1. GENEL ATMOSFER (AMBIENT GLOW) --- */
        html, body, .stApp { 
            background-color: #050505;
            background-image: 
                radial-gradient(circle at 50% 0%, #1a1a1a 0%, transparent 70%),
                radial-gradient(circle at 80% 10%, rgba(59, 130, 246, 0.05) 0%, transparent 40%);
            color: #E4E4E7; 
            font-family: 'Inter', sans-serif; 
        }

        /* SIDEBAR (Minimalist) */
        section[data-testid="stSidebar"] { 
            background-color: rgba(10, 10, 10, 0.8);
            border-right: 1px solid #1F1F1F;
            backdrop-filter: blur(20px);
        }
        
        /* --- 2. INPUT ALANLARI (Ultra Modern) --- */
        .stTextInput input, .stSelectbox div, .stNumberInput input, .stTextArea textarea, .stChatInput textarea {
            background-color: rgba(255, 255, 255, 0.03) !important; 
            border: 1px solid #27272A; 
            color: #FFF; 
            border-radius: 10px;
            transition: all 0.3s ease;
            font-size: 14px;
        }
        .stTextInput input:focus, .stChatInput textarea:focus { 
            border-color: #3B82F6; 
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
            background-color: rgba(255, 255, 255, 0.05) !important;
        }

        /* --- 3. BUTONLAR (Sessiz Güç) --- */
        .stButton button { 
            background: linear-gradient(180deg, #27272A 0%, #18181B 100%);
            color: #E4E4E7; 
            border: 1px solid #3F3F46; 
            border-radius: 8px; 
            font-weight: 500;
            padding: 0.5rem 1rem;
            transition: all 0.2s;
            box-shadow: 0 1px 2px rgba(0,0,0,0.5);
        }
        .stButton button:hover { 
            border-color: #71717A; 
            color: #FFF;
            transform: translateY(-1px);
        }
        /* Primary Buton (Çıkış) */
        .stButton button[kind="primary"] {
             background: linear-gradient(180deg, #DC2626 0%, #B91C1C 100%);
             border: 1px solid #991B1B;
             color: white;
             box-shadow: 0 0 15px rgba(220, 38, 38, 0.4);
        }

        /* --- 4. NEXT-GEN METRİK KARTLARI (Glassmorphism) --- */
        .pro-metric-card {
            background: rgba(20, 20, 22, 0.6); /* Yarı saydam */
            backdrop-filter: blur(12px);       /* Buzlu cam */
            padding: 24px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            gap: 20px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        .pro-metric-card::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        }
        .pro-metric-card:hover {
             border-color: rgba(255, 255, 255, 0.15);
             transform: translateY(-2px);
             box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
        }
        
        /* İkon Kutusu (Neon Glow) */
        .metric-icon-box {
            width: 52px;
            height: 52px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            flex-shrink: 0;
        }
        /* Renk Temaları */
        .theme-blue   { background: rgba(59, 130, 246, 0.1); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.2); }
        .theme-green  { background: rgba(34, 197, 94, 0.1);  color: #4ADE80; border: 1px solid rgba(34, 197, 94, 0.2); }
        .theme-purple { background: rgba(168, 85, 247, 0.1); color: #C084FC; border: 1px solid rgba(168, 85, 247, 0.2); }
        .theme-orange { background: rgba(249, 115, 22, 0.1); color: #FB923C; border: 1px solid rgba(249, 115, 22, 0.2); }
        .theme-red    { background: rgba(239, 68, 68, 0.1);  color: #F87171; border: 1px solid rgba(239, 68, 68, 0.2); }

        /* Tipografi */
        .metric-label { color: #A1A1AA; font-size: 0.85rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em; }
        .metric-value { color: #FFF; font-size: 1.8rem; font-weight: 800; margin: 4px 0; letter-spacing: -0.02em; }
        
        .metric-delta { font-size: 0.85rem; font-weight: 600; display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; border-radius: 20px;}
        .delta-up   { background: rgba(34, 197, 94, 0.1); color: #4ADE80; }
        .delta-down { background: rgba(239, 68, 68, 0.1); color: #F87171; }
        .delta-flat { background: rgba(161, 161, 170, 0.1); color: #A1A1AA; }

        /* --- 5. CHAT ARAYÜZÜ (Custom Bubbles) --- */
        div[data-testid="stChatMessage"] {
            background-color: transparent;
            padding: 1rem;
            border-radius: 12px;
        }
        div[data-testid="stChatMessage"][data-author="user"] {
            background-color: rgba(59, 130, 246, 0.08);
            border: 1px solid rgba(59, 130, 246, 0.1);
        }
        
        /* Grafikler */
        .js-plotly-plot .plotly .main-svg { background: transparent !important; }
        div[data-testid="stVerticalBlock"] > div.stPlotlyChart {
            background: rgba(20, 20, 22, 0.4);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 15px;
        }

        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
