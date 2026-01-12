import streamlit as st
import brain
import data

def render_dashboard():
    # Üst Bar (Başlık ve Bildirimler)
    c_title, c_notif = st.columns([3, 1])
    with c_title:
        st.title(f"📊 Yönetim Paneli: {st.session_state.user_data['brand']}")
    with c_notif:
        with st.expander("🔔 Bildirimler (3)"):
            for notif in data.get_notifications():
                st.caption(notif)
                st.markdown("---")

    # 1. KPI Kartları
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Toplam Ciro", "$42,500", "+%12")
    c2.metric("Aktif Sipariş", "148", "+5")
    c3.metric("Depo Doluluk", "%64", "-%2")
    c4.metric("Kârlılık", "%32", "+%4")

    st.markdown("---")

    # 2. AI & Grafik
    col_chat, col_stats = st.columns([1, 1.5])
    
    with col_chat:
        st.subheader("💬 Hızlı Asistan")
        # Chat geçmişi başlat
        if "messages" not in st.session_state: st.session_state.messages = []
        
        chat_box = st.container(height=350)
        for msg in st.session_state.messages:
            chat_box.chat_message(msg["role"]).write(msg["content"])
            
        if prompt := st.chat_input("Soru sor..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            chat_box.chat_message("user").write(prompt)
            data.log_activity(f"AI Sohbet: {prompt[:20]}...")
            
            # Cevap
            with chat_box.chat_message("assistant"):
                placeholder = st.empty()
                full_resp = ""
                stream = brain.get_streaming_response(st.session_state.messages, st.session_state.user_data)
                for chunk in stream:
                    full_resp += chunk
                    placeholder.markdown(full_resp + "▌")
                placeholder.markdown(full_resp)
            st.session_state.messages.append({"role": "assistant", "content": full_resp})

    with col_stats:
        st.subheader("📈 Gelir Analizi")
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
        
        st.subheader("📝 Son Aktiviteler")
        if "activity_log" not in st.session_state: st.session_state.activity_log = []
        
        # Logları göster
        if not st.session_state.activity_log:
            st.caption("Henüz aktivite yok.")
        else:
            for log in st.session_state.activity_log[:5]: # Son 5 işlem
                st.text(f"🕒 {log['time']} - {log['action']}")
