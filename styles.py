import streamlit as st

def load_css():
    """
    Enterprise-Grade CSS System v2.0
    - Silicon Valley Dark Theme
    - Gold Accent Integration (#C5A059)
    - High-End Typography
    """
    
    # --- 1. GLOBAL AYARLAR & DEĞİŞKENLER ---
    st.markdown("""
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

        :root {
            /* Palette: Deep Dark Mode */
            --bg-app: #000000;
            --bg-secondary: #0A0A0A;
            --bg-card: rgba(20, 20, 22, 0.6);
            
            /* Text */
            --text-primary: #FAFAFA;
            --text-secondary: #A1A1AA;
            --text-muted: #71717A;
            
            /* Borders & Glass */
            --border-subtle: rgba(255, 255, 255, 0.08);
            --border-active: rgba(197, 160, 89, 0.3); /* Gold Border */
            
            /* Accents (Kurumsal Altın) */
            --accent-gold: #C5A059;
            --accent-gold-dim: rgba(197, 160, 89, 0.1);
            
            /* Functional Colors */
            --success: #10B981;
            --warning: #F59E0B;
            --danger: #EF4444;
            --info: #3B82F6;
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
        ::-webkit-scrollbar-thumb:hover { background: var(--accent-gold); }
    </style>
    """, unsafe_allow_html=True)

    # --- 2. HEADER & SIDEBAR (PREMIUM LOOK) ---
    st.markdown("""
    <style>
        /* Header'ı Yok Et (Tam Ekran Hissi) */
        header[data-testid="stHeader"] {
            background: transparent !important;
            pointer-events: none;
            height: 0px;
        }
        
        /* Sidebar Tasarımı */
        section[data-testid="stSidebar"] {
            background-color: #050505;
            border-right: 1px solid var(--border-subtle);
            box-shadow: 20px 0 50px rgba(0,0,0,0.5);
        }
        
        /* Radyo Butonları (Menü Öğeleri) - En Önemli Kısım */
        .stRadio > div[role="radiogroup"] > label {
            background: transparent;
            border: 1px solid transparent;
            padding: 10px 15px;
            border-radius: 8px;
            margin-bottom: 2px;
            transition: all 0.2s ease;
            cursor: pointer;
        }
        
        /* Hover Efekti */
        .stRadio > div[role="radiogroup"] > label:hover {
            background: rgba(255, 255, 255, 0.03);
            border-color: rgba(255, 255, 255, 0.1);
        }

        /* Seçili Olan Menü Öğesi */
        .stRadio > div[role="radiogroup"] > label[data-checked="true"] {
            background: var(--accent-gold-dim) !important;
            border: 1px solid var(--border-active) !important;
        }
        
        /* Seçili Yazı Rengi */
        .stRadio > div[role="radiogroup"] > label[data-checked="true"] p {
            color: var(--accent-gold) !important;
            font-weight: 600 !important;
        }
        
        /* Radyo Dairelerini Gizle (Temiz Görünüm) */
        .stRadio div[role="radiogroup"] label div:first-child {
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- 3. INPUTLAR & BUTONLAR (ALTIN DOKUNUŞ) ---
    st.markdown("""
    <style>
        /* Inputs */
        .stTextInput input, .stSelectbox div[data-baseweb="select"], .stNumberInput input, .stTextArea textarea, .stChatInput textarea {
            background-color: var(--bg-secondary) !important;
            border: 1px solid var(--border-subtle) !important;
            color: var(--text-primary) !important;
            border-radius: 10px !important;
            font-size: 14px;
        }
        
        /* Focus State (Gold Glow) */
        .stTextInput input:focus, .stChatInput textarea:focus {
            border-color: var(--accent-gold) !important;
            box-shadow: 0 0 0 1px rgba(197, 160, 89, 0.3);
        }

        /* Buttons */
        .stButton button {
            background: linear-gradient(180deg, #18181B 0%, #09090B 100%);
            border: 1px solid var(--border-subtle);
            color: #E4E4E7;
            font-weight: 500;
            border-radius: 8px;
            transition: all 0.2s ease;
        }
        
        .stButton button:hover {
            border-color: var(--accent-gold);
            color: var(--accent-gold);
            transform: translateY(-1px);
        }

        /* Primary Action Button (Gold) */
        .stButton button[kind="primary"] {
            background: linear-gradient(135deg, #C5A059 0%, #A07E3C 100%);
            border: none;
            color: #000 !important; /* Altın üstüne siyah yazı okunur */
            font-weight: 700;
            box-shadow: 0 4px 15px rgba(197, 160, 89, 0.2);
        }
        .stButton button[kind="primary"]:hover {
            box-shadow: 0 6px 20px rgba(197, 160, 89, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- 4. BENTO GRID KARTLARI (GLASSMORPHISM) ---
    st.markdown("""
    <style>
        /* Glass Card */
        .metric-card, .seller-card, .social-card, .ads-card, .web-card, .llc-card {
            background: var(--bg-card);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 24px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* Hover Effect */
        .metric-card:hover, .seller-card:hover {
            border-color: var(--border-active);
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
            transform: translateY(-2px);
        }

        /* Icon Box */
        .icon-box {
            width: 48px; height: 48px;
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            font-size: 24px;
            margin-bottom: 15px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
        }
    </style>
    """, unsafe_allow_html=True)
