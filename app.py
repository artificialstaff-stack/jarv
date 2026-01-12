# app.py
import streamlit as st
from styles import apply_custom_styles
from views import render_step1_consulting, render_step2_action, render_step3_tracking

# Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff", layout="wide", page_icon="AS")

# Tasarımı Yükle (EN ÖNEMLİ KISIM)
apply_custom_styles()

# Yan Menü Tasarımı
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-family: 'Cormorant Garamond'; font-size: 36px; margin:0; color:#C5A059;">AS</h1>
        <span style="font-size: 10px; letter-spacing: 2px; color: #666;">ARTIFICIAL STAFF</span>
    </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio("", 
        ["01 // VISION (Jarvis)", "02 // START (Başvuru)", "03 // TRACK (İzleme)"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("<div style='text-align:center; font-size:10px; color:#444;'>US & TR OPERATIONS<br>© 2025</div>", unsafe_allow_html=True)

# Yönlendirme
if "VISION" in menu:
    render_step1_consulting()
elif "START" in menu:
    render_step2_action()
elif "TRACK" in menu:
    render_step3_tracking()
