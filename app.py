import streamlit as st
from ui import apply_luxury_theme, render_dashboard
from brain import get_jarvis_response

# Başlangıç
apply_luxury_theme()
st.markdown('<h1 class="brand-text">ARTIFICIAL STAFF</h1>', unsafe_allow_html=True)

# Session State Yönetimi
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hoş geldiniz. Ben Jarvis. Markanızı dünyaya taşımaya hazır mısınız? İsminizi nasıl kaydedelim?"}]
    st.session_state.progress = 10

# Arayüzü İkiye Böl (Chat ve Dashboard)
chat_col, dash_col = st.columns([0.6, 0.4])

with dash_col:
    render_dashboard(st.session_state.progress)

with chat_col:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Jarvis ile konuşun..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            response = get_jarvis_response(st.session_state.messages)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.progress = min(st.session_state.progress + 15, 100)
            st.rerun() # Paneli güncellemek için
