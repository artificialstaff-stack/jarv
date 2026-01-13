import streamlit as st

def load_css():
    st.markdown("""
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* GENEL ATMOSFER (Derin Premium Karanlık) */
        html, body, .stApp { 
            background-color: #09090B; /* Daha sofistike bir siyah */
            color: #E4E4E7; 
            font-family: 'Inter', sans-serif; 
        }

        /* SIDEBAR */
        section[data-testid="stSidebar"] { 
            background-color: #121214; 
            border-right: 1px solid #27272A; 
        }
        
        /* INPUT ALANLARI (Minimalist) */
        .stTextInput input, .stSelectbox div, .stNumberInput input, .stTextArea textarea, .stChatInput textarea {
            background-color: #18181B !important; 
            border: 1px solid #27272A; 
            color: #FFF; 
            border-radius: 12px; /* Daha yumuşak köşeler */
        }
        .stTextInput input:focus, .stChatInput textarea:focus { border-color: #3B82F6; }

        /* BUTONLAR (Modern) */
        .stButton button { 
            background-color: #18181B; 
            color: #FFF; 
            border: 1px solid #27272A; 
            border-radius: 12px; 
            font-weight: 500;
            transition: 0.2s; 
        }
        .stButton button:hover { 
            border-color: #52525B; 
            background-color: #27272A; 
        }
        /* Primary Buton (Çıkış vb. için) */
        .stButton button[kind="primary"] {
             background-color: #DC2626 !important;
             border: none;
        }

        /* --- YENİ PRO METRİK KARTLARI --- */
        .pro-metric-card {
            background-color: #121214;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #27272A;
            display: flex;
            align-items: center;
            gap: 20px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* Premium gölge */
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        .pro-metric-card:hover {
             border-color: #3F3F46;
             transform: translateY(-3px); /* Üzerine gelince hafif yükselme efekti */
        }
        
        /* İkon Kutusu */
        .metric-icon-box {
            width: 56px;
            height: 56px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            flex-shrink: 0;
        }
        /* İkon Renk Temaları (Hafif parlayan arka planlar) */
        .theme-blue { background: rgba(59, 130, 246, 0.15); color: #60A5FA; }
        .theme-green { background: rgba(34, 197, 94, 0.15); color: #4ADE80; }
        .theme-purple { background: rgba(168, 85, 247, 0.15); color: #C084FC; }
        .theme-orange { background: rgba(249, 115, 22, 0.15); color: #FB923C; }

        /* Metrik Yazıları */
        .metric-info div:first-child { color: #A1A1AA; font-size: 0.95rem; font-weight: 500; letter-spacing: 0.02em; } /* Label */
        .metric-info div:nth-child(2) { color: #FFF; font-size: 1.75rem; font-weight: 700; margin: 8px 0; } /* Value */
        
        /* Delta (Değişim) */
        .metric-delta { font-size: 0.9rem; font-weight: 600; display: inline-flex; align-items: center; gap: 4px;}
        .delta-up { color: #4ADE80; }
        .delta-down { color: #F87171; }
        .delta-flat { color: #A1A1AA; }

        /* Standart Konteynerlar (Grafikler için) */
        div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div.st-emotion-cache-1r6slb0 {
             border: 1px solid #27272A !important;
             background-color: #121214;
             border-radius: 16px;
        }

        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
