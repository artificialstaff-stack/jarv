import streamlit as st
import brain
import data

def render_dashboard():
    # --- DURUM YÖNETİMİ ---
    # Eğer daha önce bir mod seçilmediyse varsayılan "finans" olsun
    if "dashboard_mode" not in st.session_state:
        st.session_state.dashboard_mode = "finance"

    # Başlık
    st.title(f"📊 Panel: {st.session_state.user_data['brand']}")
    
    # İki Kolon: Sol (Chat) - Sağ (Değişken Ekran)
    col_chat, col_visual = st.columns([1, 1.5], gap="large")

    # --- SOL: AI CHAT ---
    with col_chat:
        st.subheader("💬 ARTIS Asistan")
        
        # Chat Geçmişi
        if "messages" not in st.session_state: st.session_state.messages = []
        chat_box = st.container(height=400) # Sabit yükseklik
        
        for msg in st.session_state.messages:
            chat_box.chat_message(msg["role"]).write(msg["content"])
            
        # INPUT ALANI & YAKALAYICI
        if prompt := st.chat_input("Bir talimat verin..."):
            # Mesajı ekle
            st.session_state.messages.append({"role": "user", "content": prompt})
            chat_box.chat_message("user").write(prompt)
            
            # --- ZEKİ MOD DEĞİŞTİRİCİ ---
            # Yazılan kelimeye göre sağ tarafı değiştiriyoruz
            prompt_lower = prompt.lower()
            
            if any(x in prompt_lower for x in ["lojistik", "kargo", "gemi", "nerede", "konum", "shipment"]):
                st.session_state.dashboard_mode = "logistics"
            
            elif any(x in prompt_lower for x in ["stok", "envanter", "ürün", "kaç adet", "mal"]):
                st.session_state.dashboard_mode = "inventory"
            
            elif any(x in prompt_lower for x in ["finans", "ciro", "para", "satış", "kar", "gelir"]):
                st.session_state.dashboard_mode = "finance"

            # AI Cevabını Üret
            with chat_box.chat_message("assistant"):
                placeholder = st.empty()
                full_resp = ""
                stream = brain.get_streaming_response(st.session_state.messages, st.session_state.user_data)
                for chunk in stream:
                    full_resp += chunk
                    placeholder.markdown(full_resp + "▌")
                placeholder.markdown(full_resp)
            
            st.session_state.messages.append({"role": "assistant", "content": full_resp})
            
            # SAYFAYI YENİLE (Ki sağ taraf değişsin)
            st.rerun()

    # --- SAĞ: AKILLI GÖRSEL ---
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        # 1. FİNANS MODU
        if mode == "finance":
            st.markdown("### 📈 Finansal Durum")
            c1, c2 = st.columns(2)
            c1.metric("Ciro", "$42,500", "+12%")
            c2.metric("Net Kâr", "%32", "+4%")
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            st.info("💡 İpucu: 'Stok durumum nedir?' yazarak envanteri görebilirsin.")

        # 2. LOJİSTİK MODU
        elif mode == "logistics":
            st.markdown("### 📦 Canlı Sevkiyat Takibi")
            c1, c2 = st.columns(2)
            c1.metric("Aktif Kargo", "TR-8821", "Yolda")
            c2.metric("Tahmini Varış", "2 Gün", "Normal")
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            st.success("✅ Gümrük işlemleri tamamlandı.")

        # 3. ENVANTER MODU
        elif mode == "inventory":
            st.markdown("### 📋 Stok Analizi")
            c1, c2 = st.columns(2)
            c1.metric("Toplam Ürün", "8,400", "Adet")
            c2.metric("Kritik Stok", "Çanta", "-50")
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
            st.warning("⚠️ Deri Çanta stoğu azalıyor. Sipariş verilmeli.")
