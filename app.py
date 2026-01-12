import streamlit as st
import time
from styles import apply_tech_style
from ui import render_sidebar, render_inventory_dashboard, render_finance_dashboard
from brain import get_jarvis_response

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="JARVIS 2026",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Stili Uygula
apply_tech_style()

# 3. Sidebar'ı Çiz ve Seçimi Al
selected_tab = render_sidebar()

# 4. Session State (Hafıza) Başlatma
if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = "Jarvis v4.2 Aktif. Neural arayüze hoş geldiniz."
    st.session_state.messages.append({"role": "assistant", "content": intro})

# 5. Ana Ekran Mantığı
if selected_tab == "🤖 JARVIS CORE":
    st.header("Jarvis Neural Interface")
    
    # Mesajları Ekrana Bas
    for msg in st.session_state.messages:
        avatar = "🤖" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    # Kullanıcıdan Girdi Al
    if prompt := st.chat_input("Talimat verin..."):
        # Kullanıcı mesajını ekle
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # AI Cevabını Üret
        with st.chat_message("assistant", avatar="🤖"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Brain dosyasından cevabı al
            ai_response = get_jarvis_response(st.session_state.messages)
            
            # Yazıyor efekti (Typewriter effect)
            for chunk in ai_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})

elif selected_tab == "📦 GLOBAL ENVANTER":
    render_inventory_dashboard()

elif selected_tab == "💰 FİNANSAL ANALİZ":
    render_finance_dashboard()

elif selected_tab == "📊 STRATEJİ":
    st.title("📊 Pazar Stratejisi")
    st.write("Veri madenciliği modülü çalışıyor...")
