import streamlit as st
import brain
import time
from datetime import datetime

# ==============================================================================
# 🎨 DASHBOARD STİLİ
# ==============================================================================
def inject_dashboard_css():
    st.markdown("""
    <style>
        .metric-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🚀 ANA DASHBOARD
# ==============================================================================
def render_dashboard():
    inject_dashboard_css()
    
    # Kullanıcı verisini al (Brain için gerekli!)
    user = st.session_state.get('user_data', {'brand': 'Anatolia Home', 'name': 'User'})
    
    # Header
    st.markdown(f"### 👋 Hoş geldin, {user.get('name')}")
    st.caption(f"{user.get('brand')} Operasyon Merkezi - Sistem Online")

    col1, col2 = st.columns([1.2, 2], gap="medium")

    # --- SOL: CHAT ---
    with col1:
        st.subheader("🧠 Asistan")
        chat_box = st.container(height=450)
        
        if "messages" not in st.session_state: st.session_state.messages = []

        with chat_box:
            if not st.session_state.messages:
                st.info("Merhaba! Finans veya Stok verilerini sorabilirsiniz.")
            
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input("Bir talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_box:
                st.chat_message("user").write(prompt)
                
                with st.chat_message("assistant"):
                    msg_placeholder = st.empty()
                    full_resp = ""
                    try:
                        # !!! İŞTE DÜZELTME BURADA !!!
                        # Hem 'messages' hem 'user' gönderiyoruz.
                        for chunk in brain.get_streaming_response(st.session_state.messages, user):
                            full_resp += chunk
                            msg_placeholder.markdown(full_resp + "▌")
                            time.sleep(0.01)
                        msg_placeholder.markdown(full_resp)
                    except Exception as e:
                        st.error(f"Hata: {e}")
            
            st.session_state.messages.append({"role": "assistant", "content": full_resp})

    # --- SAĞ: GRAFİKLER ---
    with col2:
        st.subheader("📊 Finansal Özet")
        c1, c2 = st.columns(2)
        with c1: 
            st.metric("Ciro", "$42,500", "+12%")
        with c2: 
            st.metric("Kâr", "%32", "+4%")
            
        try:
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
        except:
            st.warning("Grafik yüklenemedi.")
