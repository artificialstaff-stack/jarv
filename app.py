import streamlit as st
from styles import load_css
# views.py içindeki tüm render fonksiyonlarını import ediyoruz
from views import render_dashboard, render_ai_manager, render_logistics, render_marketing

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Artificial Staff - Enterprise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Yükle
load_css()

# 3. Sidebar
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; margin-bottom: 30px;'>
            <h1 style='color: #D4AF37 !important; font-size: 40px; margin:0; letter-spacing: -2px;'>AS</h1>
            <span style='font-size: 10px; letter-spacing: 4px; color: #666; font-weight: 600;'>ENTERPRISE</span>
        </div>
    """, unsafe_allow_html=True)
    
    page = st.radio(
        "Navigasyon",
        ["DASHBOARD", "JARVIS (AI)", "LOJİSTİK", "PAZARLAMA", "AYARLAR"],
        label_visibility="collapsed"
    )
    
    st.markdown("""
        <div style='position: fixed; bottom: 30px; width: 200px; text-align: center; opacity: 0.5;'>
            <span style='color: #444; font-size: 10px;'>v2.1.0 Stable Build</span>
        </div>
    """, unsafe_allow_html=True)

# 4. Yönlendirme
if page == "DASHBOARD":
    render_dashboard()
elif page == "JARVIS (AI)":
    render_ai_manager()
elif page == "LOJİSTİK":
    render_logistics()
elif page == "PAZARLAMA":
    render_marketing()
else:
    st.info("Bu modül (Ayarlar) yapım aşamasındadır.")
