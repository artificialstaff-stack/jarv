import streamlit as st
from styles import load_css
from views import render_cinematic_intro, render_main_hub, render_dashboard, render_artis_ai, render_logistics, render_marketing

# 1. Ayarlar
st.set_page_config(
    page_title="Artificial Staff - Enterprise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Yükle
load_css()

# 3. Yan Menü
with st.sidebar:
    st.markdown("<h1 style='text-align:center; color:#D4AF37; margin-bottom:0;'>AS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; letter-spacing:2px; font-size:10px; margin-top:0;'>ENTERPRISE</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 'HİZMETLERİMİZ' sekmesi artık 'ANA MERKEZ' (Hub) oldu
    page = st.radio(
        label="Menü",
        options=["ANA MERKEZ", "DASHBOARD", "ARTIS (AI)", "LOJİSTİK", "PAZARLAMA"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("© 2026 Artificial Staff LLC")

# 4. Sayfa Yönlendirme Mantığı
if page == "ANA MERKEZ":
    # Burada önce Intro çalışır, bitince Hub'ı gösterir
    render_cinematic_intro()
elif page == "DASHBOARD":
    render_dashboard()
elif page == "ARTIS (AI)":
    render_artis_ai()
elif page == "LOJİSTİK":
    render_logistics()
elif page == "PAZARLAMA":
    render_marketing()
