import streamlit as st

def load_css():
    """
    Enterprise-Grade CSS System v2.1 (Fix: Menu Visibility)
    """
    
    # --- 1. GLOBAL AYARLAR ---
    st.markdown("""
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        :root {
            --bg-app: #000000;
            --bg-secondary: #0A0A0A;
            --text-primary: #FAFAFA;
            --text-secondary: #A1A1AA;
            --accent-gold: #C5A059;
            --border-subtle: rgba(255, 255, 255, 0.1);
        }

        html, body, .stApp {
            background-color: var(--bg-app);
            font-family: 'Inter', sans-serif;
            color: var(--text-primary);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- 2. SIDEBAR VE MENÜ (GÖRÜNÜRLÜK FİX) ---
    st.markdown("""
    <style>
        /* Header'ı gizle */
        header[data-testid="stHeader"] { background: transparent !important; height: 0px; }
        
        /* Sidebar Arkaplanı */
        section[data-testid="stSidebar"] {
            background-color: #050505 !important;
            border-right: 1px solid var(--border-subtle);
        }

        /* --- MENÜ BUTONLARI (RADYO) --- */
        /* Genel Konteyner Rengi */
        .stRadio {
            background: transparent !important;
        }

        /* Menü Öğesi (Etiket) */
        .stRadio label {
            background: transparent !important;
            color: #E4E4E7 !important; /* YAZIYI BEYAZ YAP */
            padding: 10px 15px !important;
            border-radius: 8px;
            margin-bottom: 2px;
            border: 1px solid transparent;
            transition: all 0.2s ease;
            cursor: pointer;
            width: 100%; /* Tam genişlik */
        }

        /* Menü Öğesi İçindeki Metin (p tagları) */
        .stRadio label p {
            color: #E4E4E7 !important; /* YAZIYI ZORLA BEYAZ YAP */
            font-size: 14px !important;
            font-weight: 500 !important;
        }

        /* Hover (Üzerine Gelince) */
        .stRadio label:hover {
            background: rgba(255, 255, 255, 0.05) !important;
            color: #FFFFFF !important;
        }

        /* SEÇİLİ OLAN ÖĞE (Active State) */
        .stRadio label[data-checked="true"] {
            background: rgba(197, 160, 89, 0.1) !important; /* Altın Zemin */
            border: 1px solid rgba(197, 160, 89, 0.3) !important;
        }

        .stRadio label[data-checked="true"] p {
            color: #C5A059 !important; /* Altın Yazı */
            font-weight: 700 !important;
        }

        /* Radyo Dairelerini (Circle) Gizle - Sadece Yazı Kalsın */
        .stRadio div[role="radiogroup"] > label > div:first-child {
            display: none !important;
        }

    </style>
    """, unsafe_allow_html=True)

    # --- 3. DİĞER BİLEŞENLER (Kartlar ve Butonlar) ---
    st.markdown("""
    <style>
        /* Kart Tasarımı */
        .metric-card, .seller-card, .social-card, .ads-card, .web-card, .llc-card {
            background: rgba(20, 20, 22, 0.6);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 24px;
        }
        
        /* Butonlar */
        .stButton button {
            background: #18181B;
            color: #FFF;
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
        }
        .stButton button:hover {
            border-color: var(--accent-gold);
            color: var(--accent-gold);
        }
    </style>
    """, unsafe_allow_html=True)
