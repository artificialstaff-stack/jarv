import streamlit as st

def load_css():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        
        <style>
            :root {
                --bg-dark: #050505;
                --gold: #D4AF37;
                --glass-border: rgba(255, 255, 255, 0.1);
            }
            .stApp { background-color: var(--bg-dark); font-family: 'Inter', sans-serif; }
            header[data-testid="stHeader"], footer {display: none;}
            section[data-testid="stSidebar"] { background-color: #080808; border-right: 1px solid var(--glass-border); }
            
            /* Login */
            div[data-baseweb="input"] { background-color: rgba(255, 255, 255, 0.05); border: 1px solid var(--glass-border); color: white; }
            div[data-testid="stButton"] button { background: linear-gradient(45deg, #D4AF37, #B69246); color: black; border: none; font-family: 'Cinzel'; width: 100%; }
            div[data-testid="stButton"] button:hover { transform: scale(1.02); }

            /* Welcome Text */
            .welcome-text { font-family: 'Inter'; font-size: 22px; color: #ddd; text-align: center; font-weight: 300; animation: fadeIn 1s; }
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

            /* Hub Card */
            .hub-card {
                background: linear-gradient(145deg, rgba(20,20,20,1) 0%, rgba(5,5,5,1) 100%);
                border: 1px solid var(--glass-border); border-radius: 12px; padding: 30px;
                text-align: center; height: 200px; display: flex; flex-direction: column; 
                align-items: center; justify-content: center; transition: 0.3s;
            }
            .hub-card:hover { border-color: var(--gold); transform: translateY(-5px); }
            .hub-icon { font-size: 32px; color: var(--gold); margin-bottom: 15px; }
            .hub-title { font-family: 'Cinzel'; font-size: 18px; color: white; }
            .hub-desc { font-size: 12px; color: #888; margin-top: 5px; }

            /* Service Mini Card */
            .service-mini-card { background: rgba(255,255,255,0.02); border-left: 2px solid var(--gold); padding: 10px; margin-bottom: 8px; }
        </style>
    """, unsafe_allow_html=True)
