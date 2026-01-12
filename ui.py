import streamlit as st

def apply_luxury_theme():
    st.markdown("""
        <style>
        .stApp { background: #050505; color: #f0f0f0; }
        .brand-text { color: #B89B5E; font-family: 'Cinzel', serif; text-align: center; letter-spacing: 5px; }
        .dashboard-box { background: rgba(184, 155, 94, 0.1); border: 1px solid #B89B5E; border-radius: 10px; padding: 15px; }
        </style>
    """, unsafe_allow_html=True)

def render_dashboard(progress_val, client_name="Müşteri"):
    st.markdown(f"### 📊 Operasyon: {client_name}")
    st.progress(progress_val / 100)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="dashboard-box">Kurulum: **1500 USD**</div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="dashboard-box">Lojistik: **21 Gün**</div>', unsafe_allow_html=True)
