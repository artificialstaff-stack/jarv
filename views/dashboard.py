import streamlit as st
import brain
import time

def render_dashboard():
    # CSS
    st.markdown("""
    <style>
        .metric-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

    # Veri Al
    user = st.session_state.get('user_data', {'name': 'Yönetici', 'brand': 'Anatolia Home'})
    
    st.markdown(f"### 👋 Hoş geldin, {user['name']}")
    st.caption(f"{user['brand']} Operasyon Paneli")

    col1, col2 = st.columns([1.2, 2], gap="medium")

    # --- CHAT ---
    with col1:
        st.markdown("##### 🧠 Asistan")
        chat_cont = st.container(height=450)
        
        if "messages" not in st.session_state: st.session_state.messages = []
        
        with chat_cont:
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        if prompt := st.chat_input("Bir talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_cont:
                st.chat_message("user").write(prompt)
                with st.chat_message("assistant"):
                    ph = st.empty()
                    full_resp = ""
                    # DÜZELTME: brain'e hem mesajları hem user'ı gönderiyoruz
                    for chunk in brain.get_streaming_response(st.session_state.messages, user):
                        full_resp += chunk
                        ph.markdown(full_resp + "▌")
                        time.sleep(0.01)
                    ph.markdown(full_resp)
            st.session_state.messages.append({"role": "assistant", "content": full_resp})

    # --- GRAFİK ---
    with col2:
        st.markdown("##### 📊 Özet Tablo")
        c1, c2 = st.columns(2)
        with c1: st.metric("Ciro", "$125,000", "+12%")
        with c2: st.metric("Aktif Sipariş", "142", "Normal")
        
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
