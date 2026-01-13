import streamlit as st
import brain
import data
import time

def render_dashboard():
    # --- DURUM YÖNETİMİ ---
    if "dashboard_mode" not in st.session_state:
        st.session_state.dashboard_mode = "finance"

    # =========================================================
    # 🆕 1. ONBOARDING PROGRESS BAR (OYUNLAŞTIRMA)
    # =========================================================
    # Müşteri hesabının ne kadarının tamamlandığını hissettiriyoruz
    progress_cols = st.columns([0.8, 0.2])
    with progress_cols[0]:
        st.markdown("##### 🚀 Hesap Kurulumu")
        st.progress(65, text="Profiliniz %65 oranında tamamlandı. Lütfen vergi numaranızı girin.")
    with progress_cols[1]:
        if st.button("Tamamla ➔", key="complete_profile", help="Profil ayarlarına git"):
            st.toast("Ayarlar sayfasına yönlendiriliyorsunuz...", icon="⚙️")

    st.markdown("---")

    # Başlık ve Kullanıcı
    c_title, c_user = st.columns([3, 1])
    with c_title:
        st.markdown(f"## Panel: <span style='color:#1F6FEB'>{st.session_state.user_data['brand']}</span>", unsafe_allow_html=True)
    with c_user:
        st.markdown(f"<div style='text-align:right; color:#8B949E; font-size:14px;'>👤 {st.session_state.user_data['name']}<br><span style='color:#238636'>● Online</span></div>", unsafe_allow_html=True)

    # İki Kolon Yapısı
    col_chat, col_visual = st.columns([1, 1.5], gap="large")

    # --- SOL: AI CHAT ---
    with col_chat:
        st.subheader("💬 ARTIS Asistan")
        
        # Chat Geçmişi
        chat_box = st.container(height=450, border=True)
        if "messages" not in st.session_state: st.session_state.messages = []
        
        for msg in st.session_state.messages:
            chat_box.chat_message(msg["role"]).write(msg["content"])
            
        # INPUT
        if prompt := st.chat_input("Talimat verin (Örn: Stok durumu)..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            chat_box.chat_message("user").write(prompt)
            
            # BAĞLAM TESPİTİ (Context-Aware)
            prompt_lower = prompt.lower()
            if any(x in prompt_lower for x in ["lojistik", "kargo", "konum", "shipment"]):
                st.session_state.dashboard_mode = "logistics"
            elif any(x in prompt_lower for x in ["stok", "envanter", "ürün"]):
                st.session_state.dashboard_mode = "inventory"
            elif any(x in prompt_lower for x in ["finans", "ciro", "para", "satış"]):
                st.session_state.dashboard_mode = "finance"

            # AI Cevabı
            with chat_box.chat_message("assistant"):
                placeholder = st.empty()
                full_resp = ""
                stream = brain.get_streaming_response(st.session_state.messages, st.session_state.user_data)
                for chunk in stream:
                    full_resp += chunk
                    placeholder.markdown(full_resp + "▌")
                placeholder.markdown(full_resp)
            
            st.session_state.messages.append({"role": "assistant", "content": full_resp})
            time.sleep(0.5)
            st.rerun()

    # --- SAĞ: AKILLI GÖRSEL ---
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        # MOD 1: FİNANS
        if mode == "finance":
            st.markdown("### 📈 Finansal Özet")
            c1, c2, c3 = st.columns(3)
            c1.metric("Aylık Ciro", "$42,500", "+12%")
            c2.metric("Net Kâr", "%32", "+4%")
            c3.metric("Büyüme", "Stabil", "Normal")
            
            with st.container(border=True):
                st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

        # MOD 2: LOJİSTİK
        elif mode == "logistics":
            st.markdown("### 📦 Canlı Sevkiyat")
            st.info("🚢 **TR-8821** numaralı gemi Atlantik rotasında. Tahmini varış: 2 Gün.")
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            
            # Hızlı Aksiyon Butonu
            if st.button("📍 Detaylı Konum Raporu İndir", use_container_width=True):
                st.toast("Rapor hazırlanıyor...", icon="📄")

        # MOD 3: ENVANTER
        elif mode == "inventory":
            st.markdown("### 📋 Stok Durumu")
            c1, c2 = st.columns(2)
            c1.metric("Toplam Ürün", "8,550", "+150")
            c2.metric("Kritik Ürün", "Çanta", "-50 Adet", delta_color="inverse")
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
            
            st.warning("⚠️ **Deri Çanta** stoğu bitmek üzere. Tedarikçi siparişi oluşturulmalı.")
