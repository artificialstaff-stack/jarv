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

    # State: Hangi moddayız? (Varsayılan: Finans)
    if "dash_mode" not in st.session_state: st.session_state.dash_mode = "finance"

    user = st.session_state.get('user_data', {'name': 'Yönetici', 'brand': 'Anatolia Home'})
    
    st.markdown(f"### 👋 Hoş geldin, {user['name']}")
    
    col1, col2 = st.columns([1.2, 2], gap="medium")

    # --- SOL: AI ASİSTAN ---
    with col1:
        st.markdown("##### 🧠 Operasyon Asistanı")
        chat_cont = st.container(height=480)
        
        if "messages" not in st.session_state: st.session_state.messages = []
        
        with chat_cont:
            if not st.session_state.messages:
                st.info("💡 İpucu: 'Stok durumu ne?' veya 'Lojistik haritasını aç' diyerek ekranı değiştirebilirsin.")
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        if prompt := st.chat_input("Talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # --- ZEKİ YÖNLENDİRME MODÜLÜ ---
            p_low = prompt.lower()
            if "lojistik" in p_low or "kargo" in p_low or "harita" in p_low:
                st.session_state.dash_mode = "logistics"
            elif "stok" in p_low or "envanter" in p_low or "ürün" in p_low:
                st.session_state.dash_mode = "inventory"
            elif "finans" in p_low or "ciro" in p_low or "satış" in p_low:
                st.session_state.dash_mode = "finance"
            
            # Sayfayı yenile ki grafik anında değişsin
            st.rerun()

    # --- SAĞ: DİNAMİK GRAFİKLER ---
    with col2:
        mode = st.session_state.dash_mode
        
        if mode == "finance":
            st.markdown("##### 📈 Finansal Özet")
            c1, c2 = st.columns(2)
            with c1: st.metric("Ciro", "$125,000", "+%12")
            with c2: st.metric("Kâr", "%32", "+%4")
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            
        elif mode == "logistics":
            st.markdown("##### 🌍 Lojistik ve Sevkiyat")
            c1, c2 = st.columns(2)
            with c1: st.metric("Aktif Kargo", "824", "Yolda")
            with c2: st.metric("Teslimat", "2 Gün", "Normal")
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            
        elif mode == "inventory":
            st.markdown("##### 📦 Depo ve Stok")
            c1, c2 = st.columns(2)
            with c1: st.metric("Toplam Ürün", "14,200", "Adet")
            with c2: st.metric("Kritik Stok", "3", "Riskli")
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)

    # Asistanın cevabını en son üret (Rerun sonrası)
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with chat_cont:
            with st.chat_message("assistant"):
                ph = st.empty()
                full_resp = ""
                for chunk in brain.get_streaming_response(st.session_state.messages, user):
                    full_resp += chunk
                    ph.markdown(full_resp + "▌")
                    time.sleep(0.01)
                ph.markdown(full_resp)
        st.session_state.messages.append({"role": "assistant", "content": full_resp})
