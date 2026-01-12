import streamlit as st
from styles import load_css
from views import render_navbar, render_hero, render_bento_grid

# 1. Sayfa Ayarları (Tam ekran modu)
st.set_page_config(
    page_title="Artificial Staff",
    layout="wide",
    initial_sidebar_state="collapsed" # Sidebar'ı kapattım çünkü tasarımda üst menü var
)

# 2. CSS Yükle
load_css()

# 3. Sayfa Yapısını Kur
render_navbar()
render_hero()
render_bento_grid()

# 4. Alt Bilgi (Footer benzeri)
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #444; font-size: 12px; padding-bottom: 40px;">
    © 2026 Artificial Staff LLC. All rights reserved.
</div>
""", unsafe_allow_html=True)
