import streamlit as st
import brain, data

def render_dashboard():
    st.title(f"📊 Panel: {st.session_state.user_data['brand']}")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Ciro", "$42,500", "+12%")
    c2.metric("Sipariş", "148", "+5")
    c3.metric("Depo", "%64", "-2%")
    c4.metric("Kâr", "%32", "+4%")
    
    col_chat, col_stats = st.columns([1, 1.5])
    with col_chat:
        st.subheader("💬 AI Asistan")
        if "messages" not in st.session_state: st.session_state.messages = []
        chat = st.container(height=350)
        for msg in st.session_state.messages: chat.chat_message(msg["role"]).write(msg["content"])
        
        if p := st.chat_input("Sor..."):
            st.session_state.messages.append({"role": "user", "content": p})
            chat.chat_message("user").write(p)
            with chat.chat_message("assistant"):
                ph = st.empty()
                full = ""
                for chunk in brain.get_streaming_response(st.session_state.messages, st.session_state.user_data):
                    full += chunk
                    ph.markdown(full + "▌")
                ph.markdown(full)
            st.session_state.messages.append({"role": "assistant", "content": full})

    with col_stats:
        st.subheader("📈 Gelir")
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
