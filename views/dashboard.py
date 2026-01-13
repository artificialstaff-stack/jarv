import streamlit as st
import brain
import data
import time

def render_dashboard():
    # --- STATE YÖNETİMİ (PANEL MODU) ---
    # Sağ panelin hangi modda olduğunu takip ediyoruz
    if "dashboard_mode" not in st.session_state:
        st.session_state.dashboard_mode = "finance" # Varsayılan: Finans

    # --- HEADER ---
    c_title, c_user = st.columns([3, 1])
    with c_title:
        st.markdown(f"## 🚀 Komuta Merkezi: <span style='color:#1F6FEB'>{st.session_state.user_data['brand']}</span>", unsafe_allow_html=True)
    with c_user:
        st.markdown(f"<div style='text-align:right; color:#8B949E;'>👤 {st.session_state.user_data['name']}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # --- ANA YAPI (2 KOLON) ---
    col_chat, col_visual = st.columns([1, 1.5], gap="medium")

    # ---------------------------------------------------------
    # SOL KOLON: AI CHAT (SABİT)
    # ---------------------------------------------------------
    with col_chat:
        st.markdown("### 💬 ARTIS Asistan")
        
        # Chat Geçmişi Konteynerı
        chat_container = st.container(height=500, border=True)
        
        # Mesajları Yazdır
        if "messages" not in st.session_state: st.session_state.messages = []
        for msg in st.session_state.messages:
            chat_container.chat_message(msg["role"]).write(msg["content"])
        
        # --- INPUT ALANI VE BAĞLAM TESPİTİ (CONTEXT DETECTION) ---
        if prompt := st.chat_input("Operasyon, stok veya finans sor..."):
            # 1. Mesajı Kaydet ve Göster
            st.session_state.messages.append({"role": "user", "content": prompt})
            chat_container.chat_message("user").write(prompt)
            
            # 2. BAĞLAM ANALİZİ (Anahtar Kelime Tespiti)
            prompt_lower = prompt.lower()
            if any(x in prompt_lower for x in ["lojistik", "kargo", "gemi", "teslimat", "nerede", "konum", "shipment"]):
                st.session_state.dashboard_mode = "logistics"
            elif any(x in prompt_lower for x in ["stok", "ürün", "adet", "envanter", "mal", "depo"]):
                st.session_state.dashboard_mode = "inventory"
            elif any(x in prompt_lower for x in ["finans", "para", "ciro", "satış", "fatura", "kar", "dolar"]):
                st.session_state.dashboard_mode = "finance"
            
            # 3. AI Cevabını Üret (Streaming)
            with chat_container.chat_message("assistant"):
                placeholder = st.empty()
                full_resp = ""
                # Rerun yapmadan önce görseli güncellemek için burada zorlama yapmıyoruz,
                # Streamlit'in reaktif yapısı input girince sayfayı yeniler.
                
                stream = brain.get_streaming_response(st.session_state.messages, st.session_state.user_data)
                for chunk in stream:
                    full_resp += chunk
                    placeholder.markdown(full_resp + "▌")
                placeholder.markdown(full_resp)
            
            st.session_state.messages.append({"role": "assistant", "content": full_resp})
            # Mod değişimi için sayfayı yenile (Görsel anında değişsin)
            st.rerun()

    # ---------------------------------------------------------
    # SAĞ KOLON: İNTERAKTİF GÖRSEL (DEĞİŞKEN)
    # ---------------------------------------------------------
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        # --- MOD 1: FİNANS (VARSAYILAN) ---
        if mode == "finance":
            st.markdown("### 📈 Finansal Genel Bakış")
            
            # Metrikler
            m1, m2, m3 = st.columns(3)
            m1.metric("Anlık Ciro", "$42,500", "+12%")
            m2.metric("Net Kâr", "%32", "+4%")
            m3.metric("Tahmini Büyüme", "%15", "Stabil")
            
            with st.container(border=True):
                st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
                st.caption("Veriler son 30 günü kapsamaktadır. Tahminler AI tabanlıdır.")

        # --- MOD 2: LOJİSTİK (HARİTA) ---
        elif mode == "logistics":
            st.markdown("### 📦 Canlı Lojistik Takibi")
            
            # Durum Kartı
            st.info("✅ **TR-8821** numaralı konteyner Atlantik Okyanusu üzerinde. Varışa 2 gün.")
            
            with st.container(border=True):
                st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            
            c1, c2 = st.columns(2)
            c1.success("Gümrük: **ONAYLANDI**")
            c2.warning("Son Güncelleme: **10dk önce**")

        # --- MOD 3: ENVANTER (STOK) ---
        elif mode == "inventory":
            st.markdown("### 📋 Depo ve Envanter Analizi")
            
            # Uyarı
            st.warning("⚠️ **Deri Çanta** stokları kritik seviyede (Son 50 adet).")
            
            with st.container(border=True):
                st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
                
            c1, c2 = st.columns(2)
            with c1:
                st.metric("Toplam Stok", "8,553", "Adet")
            with c2:
                if st.button("Sipariş Oluştur", use_container_width=True):
                    st.toast("Tedarikçiye talep gönderildi!", icon="🚀")

        # --- GEÇİŞ EFEKTİ İÇİN ANİMASYON ---
        # Kullanıcıya görselin değiştiğini hissettirmek için minik bir ipucu
        st.toast(f"Görsel Panel Güncellendi: {mode.upper()}", icon="🔄")
