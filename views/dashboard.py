import streamlit as st
import brain
import data
import time

def render_dashboard():
    if "dashboard_mode" not in st.session_state:
        st.session_state.dashboard_mode = "finance"

    # --- 1. ÜST BİLGİ ---
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown(f"## 👋 Hoşgeldin, {st.session_state.user_data['name']}")
        st.caption(f"Panel: {st.session_state.user_data['brand']} | 🟢 Sistem Online")
    
    with c2:
        # Quick Actions (Daha kompakt)
        if st.button("⚡ Hızlı İşlem Menüsü", use_container_width=True):
            st.toast("Menü açılıyor...", icon="📂")

    st.markdown("---")

    # --- 2. PROGRESS BAR ---
    st.progress(65, text="🚀 Hesap Kurulumu: %65")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. ANA PANEL ---
    col_chat, col_visual = st.columns([1, 1.6], gap="medium")

    # === SOL: AI CHAT (GÜNCELLENDİ: EMPTY STATE EKLENDİ) ===
    with col_chat:
        st.markdown("### 💬 ARTIS Asistan")
        
        chat_container = st.container(height=450, border=True)
        
        # MESAJ YOKSA "HOŞGELDİN" EKRANI GÖSTER
        if "messages" not in st.session_state: st.session_state.messages = []
        
        if not st.session_state.messages:
            with chat_container:
                st.markdown("<br><br>", unsafe_allow_html=True)
                st.markdown("<h3 style='text-align:center;'>👋 Size nasıl yardım edeyim?</h3>", unsafe_allow_html=True)
                st.markdown("<p style='text-align:center; color:#666;'>Aşağıdaki konularda analiz yapabilirim:</p>", unsafe_allow_html=True)
                
                b1, b2 = st.columns(2)
                if b1.button("📦 Lojistik", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": "Lojistik durumum nedir?"})
                    st.rerun()
                if b2.button("💰 Finans", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": "Finansal özet ver."})
                    st.rerun()
        else:
            # Mesaj varsa normal akış
            for msg in st.session_state.messages:
                chat_container.chat_message(msg["role"]).write(msg["content"])

        # INPUT ALANI
        if prompt := st.chat_input("Bir soru sorun..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Mesaj eklendiği için rerun yapıyoruz ki "Boş Ekran" kaybolsun
            st.rerun()

        # CEVAP ÜRETME (Son mesaj kullanıcıdansa)
        if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
            user_msg = st.session_state.messages[-1]["content"]
            
            # Bağlam Yakalama
            p_low = user_msg.lower()
            if any(x in p_low for x in ["lojistik", "kargo"]): st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "ürün"]): st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro"]): st.session_state.dashboard_mode = "finance"

            with chat_container.chat_message("assistant"):
                ph = st.empty()
                full = ""
                for chunk in brain.get_streaming_response(st.session_state.messages, st.session_state.user_data):
                    full += chunk
                    ph.markdown(full + "▌")
                ph.markdown(full)
            st.session_state.messages.append({"role": "assistant", "content": full})
            st.rerun() # Görsel güncellensin diye

    # === SAĞ: AKILLI GÖRSEL (GÜNCELLENDİ: KART GÖRÜNÜMÜ) ===
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        # FİNANS
        if mode == "finance":
            st.markdown("### 📈 Finansal İçgörü")
            
            # Metrikleri Kutuya Al (Card UI)
            with st.container(border=True):
                c1, c2, c3 = st.columns(3)
                c1.metric("Ciro", "$42,500", "+12%")
                c2.metric("Kâr", "%32", "+4%")
                c3.metric("Büyüme", "Yüksek", "Stabil")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            with st.container(border=True):
                st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
                st.info("💡 **AI Analizi:** Reklam maliyetleri sabit kalırken ciro %12 arttı.")

        # LOJİSTİK
        elif mode == "logistics":
            st.markdown("### 📦 Aktif Sevkiyatlar")
            with st.container(border=True):
                c1, c2 = st.columns(2)
                c1.metric("Takip No", "TR-8821", "Yolda")
                c2.metric("Varış", "14 Ocak", "Zamanında")
            
            st.markdown("<br>", unsafe_allow_html=True)
            with st.container(border=True):
                st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
                st.success("✅ **Gümrük:** Belgeler onaylandı.")

        # ENVANTER
        elif mode == "inventory":
            st.markdown("### 📋 Stok Sağlığı")
            with st.container(border=True):
                c1, c2 = st.columns(2)
                c1.metric("Toplam Ürün", "8,550", "+150")
                c2.metric("Riskli Ürün", "Çanta", "Azalıyor", delta_color="inverse")
            
            st.markdown("<br>", unsafe_allow_html=True)
            with st.container(border=True):
                st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
