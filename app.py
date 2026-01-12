import streamlit as st
from styles import load_css
from views import render_dashboard, render_artis_ai, render_logistics, render_marketing, render_services_catalog

# 1. Page Config
st.set_page_config(
    page_title="Artificial Staff - Enterprise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Load Styles
load_css()

# 3. Sidebar Logic
with st.sidebar:
    # Logo Area
    st.markdown("""
        <div style='text-align: center; margin-bottom: 30px;'>
            <h1 style='color: #D4AF37 !important; font-size: 40px; margin:0; letter-spacing: -2px;'>AS</h1>
            <span style='font-size: 10px; letter-spacing: 4px; color: #666; font-weight: 600;'>ENTERPRISE</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation (Updated with Services)
    page = st.radio(
        label="Menü",
        options=["HİZMETLERİMİZ", "DASHBOARD", "ARTIS (AI)", "LOJİSTİK", "PAZARLAMA", "AYARLAR"],
        label_visibility="collapsed"
    )
    
    # Sidebar Footer
    st.markdown("""
        <div style='position: fixed; bottom: 30px; width: 200px; text-align: center; opacity: 0.5;'>
            <span style='color: #444; font-size: 10px;'>v2.3 ARTIS Upgrade</span>
        </div>
    """, unsafe_allow_html=True)

# 4. Page Routing
if page == "HİZMETLERİMİZ":
    render_services_catalog()
elif page == "DASHBOARD":
    render_dashboard()
elif page == "ARTIS (AI)":
    render_artis_ai()
elif page == "LOJİSTİK":
    render_logistics()
elif page == "PAZARLAMA":
    render_marketing()
else:
    # Settings Page Placeholder
    st.title("Ayarlar")
    st.info("Sistem versiyonu: 2.3.0 (Stable)")
    st.text("Kullanıcı yetkileri: Admin")
