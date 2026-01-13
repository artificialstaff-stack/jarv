import streamlit as st
import brain
import data
import time

def render_dashboard():
    if "dashboard_mode" not in st.session_state:
        st.session_state.dashboard_mode = "finance"

    # --- 1. ÜST BİLGİ & BİLDİRİMLER ---
    c_title, c_actions = st.columns([2, 1])
    with c_title:
        st.markdown(f"## 👋 Hoşgeldin, {st.session_state.user_data['name']}")
        st.caption(f"Panel: {st.session_state.user_data['brand']} | Server: US-East-1 (Online)")
    
    with c_actions:
        # HIZLI AKSİYONLAR (QUICK ACTIONS) - MÜŞTERİYİ İKNA EDEN KISIM
        st.markdown("##### ⚡ Hızlı İşlemler")
        col_q1, col_q2 = st.columns(2)
        if col_q1.button("📦 Yeni Kargo", use_container_width=True):
            st.toast("Sevkiyat sihirbazı başlatılıyor...", icon="🚢")
        if col_q2.button("📄 Fatura Al", use_container_width=True):
            st.toast("Son ayın ekstresi indiriliyor...", icon="📥")

    st.markdown("---")

    # --- 2. PROGRESS BAR (KURULUM) ---
    st.progress(65, text="🚀 Hesap Kurulumu: %65 (Vergi numaranızı girerek onay sürecini tamamlayın)")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. ANA PANEL (CHAT + GÖRSEL) ---
    col_chat, col_visual = st.columns([1, 1.6], gap="medium")

    # --- SOL: AI CHAT ---
    with col_chat:
        st.markdown("### 💬 ARTIS Asistan")
        chat_box = st.container(height=420, border=True)
        
        if "messages" not in st.session_state: st.session_state.messages = []
        for msg in st.session_state.messages:
            chat_box.chat_message(msg["role"]).write(msg["content"])
            
        if prompt := st.chat_input("Soru sor (Örn: Lojistik durumu)..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            chat_box.chat_message("user").write(prompt)
            
            # Bağlam Yakalama
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo", "konum"]): st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "ürün", "envanter"]): st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "para"]): st.session_state.dashboard_mode = "finance"

            # Cevap (Asla Hata Vermeyen Mod)
            with chat_box.chat_message("assistant"):
                ph = st.empty()
                full = ""
                # Artık brain.py hata verse bile çalışır
                for chunk in brain.get_streaming_response(st.session_state.messages, st.session_state.user_data):
                    full += chunk
                    ph.markdown(full + "▌")
                ph.markdown(full)
            
            st.session_state.messages.append({"role": "assistant", "content": full})
            time.sleep(0.5)
            st.rerun()

    # --- SAĞ: AKILLI GÖRSEL ---
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        # FİNANS MODU
        if mode == "finance":
            st.markdown("### 📈 Finansal İçgörü")
            c1, c2, c3 = st.columns(3)
            c1.metric("Ciro", "$42,500", "+12%")
            c2.metric("Kâr", "%32", "+4%")
            c3.metric("Büyüme", "Yüksek", "Stabil")
            
            with st.container(border=True):
                st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
                st.info("💡 **Yapay Zeka Yorumu:** Geçen aya göre reklam maliyetleriniz sabit kalırken cironuz arttı. Bu çok sağlıklı bir büyüme.")

        # LOJİSTİK MODU
        elif mode == "logistics":
            st.markdown("### 📦 Aktif Sevkiyatlar")
            c1, c2 = st.columns(2)
            c1.metric("Takip No", "TR-8821", "Yolda")
            c2.metric("Tahmini Varış", "14 Ocak", "Zamanında")
            
            with st.container(border=True):
                st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            st.success("✅ **Gümrük Onayı:** Belgeleriniz Washington Limanı tarafından ön onay aldı.")

        # ENVANTER MODU
        elif mode == "inventory":
            st.markdown("### 📋 Stok Sağlığı")
            c1, c2 = st.columns(2)
            c1.metric("Toplam Ürün", "8,550", "+150")
            c2.metric("Riskli Ürün", "Çanta", "Azalıyor", delta_color="inverse")
            
            with st.container(border=True):
                st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
            
            col_act1, col_act2 = st.columns(2)
            if col_act1.button("Tedarikçiyi Ara", use_container_width=True):
                st.toast("Tedarikçi iletişim bilgileri açılıyor...")
            if col_act2.button("Otomatik Sipariş", use_container_width=True):
                st.toast("Sipariş taslağı oluşturuldu.")
