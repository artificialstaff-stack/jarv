# app.py
import streamlit as st
from styles import apply_custom_styles
from views import render_step1_consulting, render_step2_action, render_step3_tracking

# 1. Sayfa Ayarları
st.set_page_config(page_title="Jarvis Interface", layout="wide", page_icon="🤖")

# 2. Stilleri Yükle
apply_custom_styles()

# 3. Yan Menü (Navigasyon)
with st.sidebar:
    st.title("ARTIFICIAL STAFF")
    st.markdown("---")
    menu = st.radio(
        "OPERASYON ADIMLARI", 
        ["1. BİLGİ AL (Jarvis)", "2. İŞE BAŞLA (Form)", "3. DURUM İZLE (Takip)"]
    )
    st.markdown("---")
    st.success("🟢 Jarvis Core: Online")

# 4. Seçime Göre Ekranı Getir
if menu == "1. BİLGİ AL (Jarvis)":
    render_step1_consulting()

elif menu == "2. İŞE BAŞLA (Form)":
    render_step2_action()

elif menu == "3. DURUM İZLE (Takip)":
    render_step3_tracking()
