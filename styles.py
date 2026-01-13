import streamlit as st

def load_css():
    """
    Injects the 'Enterprise-Grade' CSS design system into the Streamlit app.
    
    Architecture:
    1. RESET & VARIABLES: Define color palette (#000000, #09090B, #18181B) and fonts.
    2. CORE LAYOUT: Override Streamlit's default padding and background logic.
    3. ATOMIC COMPONENTS: Styles for Buttons, Inputs, and text elements.
    4. MOLECULES: Complex card designs (Pro Metric, Chat Bubbles).
    5. ANIMATIONS: Keyframes for pulsing dots and hover states.
    """
    
    # --- 1. CSS VARIABLES & RESET ---
    base_styles = """
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

        :root {
            /* Palette: Deep Dark Mode */
            --bg-app: #000000;
            --bg-secondary: #09090B;
            --bg-card: rgba(24, 24, 27, 0.6);
            
            /* Text */
            --text-primary: #FAFAFA;
            --text-secondary: #A1A1AA;
            
            /* Borders & Glass */
            --border-subtle: rgba(255, 255, 255, 0.08);
            --border-focus: rgba(255, 255, 255, 0.15);
            --glass-shine: rgba(255, 255, 255, 0.03);
            
            /* Accents (Neon) */
            --accent-blue: #3B82F6;
            --accent-purple: #8B5CF6;
            --accent-green: #10B981;
            --accent-red: #EF4444;
        }

        /* Global Reset */
        html, body, .stApp {
            background-color: var(--bg-app);
            font-family: 'Inter', -apple-system, sans-serif;
            color: var(--text-primary);
        }
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: var(--bg-app); }
        ::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #555; }
    </style>
    """

    # --- 2. LAYOUT & SIDEBAR ---
    layout_styles = """
    <style>
        /* Sidebar Glassmorphism */
        section[data-testid="stSidebar"] {
            background-color: rgba(9, 9, 11, 0.85);
            border-right: 1px solid var(--border-subtle);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
        }
        
        /* Remove Streamlit Header Whitespace */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 5rem !important;
        }
        header[data-testid="stHeader"] { display: none; }
        footer { display: none; }
    </style>
    """

    # --- 3. INPUTS & BUTTONS (MICRO-INTERACTIONS) ---
    component_styles = """
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
            font-weight: 500;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            transition: all 0.2s ease;
            box-shadow: 0 1px 2px rgba(0,0,0,0.5);
        }
        
        .stButton button:hover {
            border-color: #52525B;
            color: #FFF;
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        }

        /* Primary Action Button */
        .stButton button[kind="primary"] {
            background: linear-gradient(135deg, var(--accent-blue) 0%, #2563EB 100%);
            border: none;
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.4);
        }
        .stButton button[kind="primary"]:hover {
            box-shadow: 0 0 30px rgba(59, 130, 246, 0.6);
        }
    </style>
    """

    # --- 4. ADVANCED DASHBOARD COMPONENTS ---
    dashboard_styles = """
    <style>
        /* PRO METRIC CARD 
           Design: Flexbox layout with glowing icon container and badge system.
        */
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
        
        /* Top Highlight Line */
        .pro-metric-card::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
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
            position: relative;
        }
        
        /* Themes */
        .theme-blue { background: rgba(59, 130, 246, 0.1); color: var(--accent-blue); border: 1px solid rgba(59, 130, 246, 0.2); box-shadow: 0 0 15px rgba(59, 130, 246, 0.1); }
        .theme-green { background: rgba(16, 185, 129, 0.1); color: var(--accent-green); border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: 0 0 15px rgba(16, 185, 129, 0.1); }
        .theme-purple { background: rgba(139, 92, 246, 0.1); color: var(--accent-purple); border: 1px solid rgba(139, 92, 246, 0.2); box-shadow: 0 0 15px rgba(139, 92, 246, 0.1); }
        .theme-orange { background: rgba(249, 115, 22, 0.1); color: #F97316; border: 1px solid rgba(249, 115, 22, 0.2); box-shadow: 0 0 15px rgba(249, 115, 22, 0.1); }
        .theme-red { background: rgba(239, 68, 68, 0.1); color: var(--accent-red); border: 1px solid rgba(239, 68, 68, 0.2); box-shadow: 0 0 15px rgba(239, 68, 68, 0.1); }

        /* Typography */
        .metric-info { display: flex; flex-direction: column; }
        .metric-label { font-size: 13px; font-weight: 500; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }
        .metric-value { font-size: 28px; font-weight: 700; color: #FFF; letter-spacing: -0.02em; line-height: 1.1; }
        
        /* Delta Badge (Pill Shape) */
        .metric-delta {
            display: inline-flex; align-items: center; gap: 4px;
            padding: 2px 8px; border-radius: 999px;
            font-size: 11px; font-weight: 600;
            margin-top: 6px; width: fit-content;
        }
        .delta-up { background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.2); }
        .delta-down { background: rgba(239, 68, 68, 0.15); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.2); }
        .delta-flat { background: rgba(161, 161, 170, 0.15); color: #A1A1AA; border: 1px solid rgba(161, 161, 170, 0.2); }

        /* Chart Containers */
        .stPlotlyChart {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 16px;
            transition: border-color 0.3s;
        }
        .stPlotlyChart:hover { border-color: var(--border-focus); }
    </style>
    """
    
    # --- 5. COMBINE & INJECT ---
    st.markdown(base_styles + layout_styles + component_styles + dashboard_styles, unsafe_allow_html=True)
