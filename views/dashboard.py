import streamlit as st
import brain
import data
import time

def render_dashboard():
    # Mod kontrolü
    if "dashboard_mode" not in st.session_state: st.session_state.dashboard_mode = "finance"

    # --- ÜST BAŞLIK (Daha sade) ---
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown(f"### 👋 Hoşgeldin, {st.session_state.user_data['name']}")
    with c2:
        st.markdown(f"<div style='text-align:right; color:#666; font-size:12px; padding-top:10px;'>{st.session_state.user_data['brand']}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # --- İKİ KOLONLU YAPI ---
    col_chat, col_visual = st.columns([1, 1.6], gap="large")

    # === SOL: AI ASİSTAN (Artık boş değil!) ===
    with col_chat:
        st.markdown("#### 🤖 Asistan")
        
        chat_box = st.container(height=450)
        
        # Eğer hiç mesaj yoksa -> KARŞILAMA EKRANI GÖSTER
        if "messages" not in st.session_state: st.session_state.messages = []
        
        if not st.session_state.messages:
            with chat_box:
                st.markdown("<br>", unsafe_allow_html=True)
                st.info("👋 Merhaba! Ben ARTIS. Size nasıl yardımcı olabilirim?")
                
                # Hazır Sorular (Butonlar)
                b1 = st.button("📦 Lojistik durumum ne?", use_container_width=True)
                b2 = st.button("💰 Bu ay ne kadar kazandık?", use_container_width=True)
                b3 = st.button("📋 Stoklarda risk var mı?", use_container_width=True)
                
                if b1:
                    st.session_state.messages.append({"role": "user", "content": "Lojistik durumum ne?"})
                    st.rerun()
                if b2:
                    st.session_state.messages.append({"role": "user", "content": "Finansal durum?"})
                    st.rerun()
                if b3:
                    st.session_state.messages.append({"role": "user", "content": "Stok durumu?"})
                    st.rerun()
        else:
            # Mesaj varsa normal sohbeti göster
            with chat_box:
                for msg in st.session_state.messages:
                    with st.chat_message(msg["role"]):
                        st.write(msg["content"])

        # Input Alanı
        if prompt := st.chat_input("Bir şeyler yazın..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Mod Değiştirme Mantığı
            p_low = prompt.lower()
            if "lojistik" in p_low or "kargo" in p_low: st.session_state.dashboard_mode = "logistics"
            elif "stok" in p_low or "ürün" in p_low: st.session_state.dashboard_mode = "inventory"
            elif "finans" in p_low or "ciro" in p_low: st.session_state.dashboard_mode = "finance"

            # AI Cevabı
            full_response = ""
            for chunk in brain.get_streaming_response(st.session_state.messages, st.session_state.user_data):
                full_response += chunk
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            st.rerun()

    # === SAĞ: İÇERİK ===
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        if mode == "finance":
            st.markdown("#### 📈 Finansal Özet")
            c1, c2, c3 = st.columns(3)
            c1.metric("Ciro", "$42,500", "+12%")
            c2.metric("Kâr", "%32", "+4%")
            c3.metric("Büyüme", "Stabil", "Normal")
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

        elif mode == "logistics":
            st.markdown("#### 🚢 Aktif Lojistik")
            c1, c2 = st.columns(2)
            c1.metric("Konteyner", "TR-8821", "Yolda")
            c2.metric("Varış", "2 Gün", "Zamanında")
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

        elif mode == "inventory":
            st.markdown("#### 📦 Envanter")
            c1, c2 = st.columns(2)
            c1.metric("Toplam Ürün", "8,550", "+150")
            c2.metric("Kritik", "Çanta", "-50")
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
