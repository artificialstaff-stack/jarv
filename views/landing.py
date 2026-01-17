import streamlit as st

def render_landing():
    # --- CSS: MANUS STYLE DARK THEME ---
    st.markdown("""
        <style>
        .stApp {
            background-color: #000000;
            background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000000 60%);
        }
        
        header, footer { visibility: hidden; }
        
        .landing-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 15vh;
            text-align: center;
        }
        
        .landing-title {
            font-size: 56px;
            font-weight: 400;
            color: #e5e5e5;
            font-family: "Times New Roman", serif;
            margin-bottom: 40px;
            letter-spacing: -1px;
        }
        
        /* Input Field Styling */
        .stTextInput input {
            background-color: #111 !important;
            border: 1px solid #333 !important;
            color: white !important;
            border-radius: 24px !important;
            padding: 25px 25px !important;
            font-size: 18px !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            transition: all 0.3s ease;
        }
        .stTextInput input:focus {
            border-color: #d4af37 !important;
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.15) !important;
        }
        
        /* Suggestion Buttons */
        .suggestion-btn {
            display: inline-block;
            background: transparent;
            border: 1px solid #333;
            color: #888;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
            margin: 5px;
            cursor: pointer;
            transition: 0.3s;
        }
        .suggestion-btn:hover {
            border-color: #666;
            color: #eee;
        }

        /* Navbar */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown('<div style="font-size:24px; font-weight:bold; color:white;">ARTIS</div>', unsafe_allow_html=True)
    with c2:
        # Right side buttons
        col_spacer, col_login, col_reg = st.columns([6, 1, 1])
        with col_login:
            if st.button("Giriş", type="secondary"):
                st.session_state.page = "Login"
                st.rerun()
        with col_reg:
            if st.button("Kaydol", type="primary"):
                st.session_state.page = "Login"
                st.rerun()

    # --- MAIN CONTENT ---
    st.markdown('<div class="landing-container"><div class="landing-title">Sizin için ne yapabilirim?</div></div>', unsafe_allow_html=True)

    # Search Bar Form
    with st.form("landing_search", border=False):
        c_space1, c_input, c_space2 = st.columns([1, 2, 1])
        with c_input:
            prompt = st.text_input("Prompt", placeholder="Lojistik maliyetlerini analiz et...", label_visibility="collapsed")
            
            # Invisible submit button logic
            submitted = st.form_submit_button("Başla", use_container_width=True)

    # Suggestions
    st.markdown("""
        <div style="text-align:center; margin-top:20px;">
            <span class="suggestion-btn">📄 Gümrük Raporu Oluştur</span>
            <span class="suggestion-btn">📦 Stok Tahmini Yap</span>
            <span class="suggestion-btn">📈 ABD Pazar Analizi</span>
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown('<div style="position:fixed; bottom:20px; width:100%; text-align:center; color:#444; font-size:12px;">ARTIS Global Operations Engine</div>', unsafe_allow_html=True)

    # Logic: Redirect to Login on Submit
    if submitted and prompt:
        st.session_state.pending_prompt = prompt
        st.session_state.page = "Login"
        st.rerun()
