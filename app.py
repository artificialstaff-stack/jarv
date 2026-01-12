import streamlit as st
from ui import apply_luxury_theme, render_sidebar
from brain import get_jarvis_response

# 1. UI Uygula
apply_luxury_theme()
selected_tab = render_sidebar()

# 2. Session Başlat
if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = "Jarvis Aktif. Amerika operasyon merkezinize hoş geldiniz. Sisteme isminizi ve markanızı tanımlayarak başlayalım."
    st.session_state.messages.append({"role": "assistant", "content": intro})

# 3. Sekme Yönetimi
if selected_tab == "🤖 JARVIS CORE":
    # Chat Alanı
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Talimat bekliyorum..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

    # AI Yanıt Tetikleyici
    if st.session_state.messages[-1]["role"] == "user":
        with st.chat_message("assistant"):
            response = get_jarvis_response(st.session_state.messages)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

elif selected_tab == "📦 INVENTORY":
    st.title("Global Envanter")
    st.info("Veri akışı bekleniyor... Jarvis üzerinden ürün tanımı yapın.")

elif selected_tab == "💰 FINANCES":
    st.title("Finansal Analiz")
    st.metric(label="Yatırım Bedeli", value="1.500 USD", delta="Kurulum Sabit")
