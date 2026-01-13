import streamlit as st
import brain
import time

# --- YENİ NESİL KART OLUŞTURUCU ---
def render_pro_metric(label, value, delta, icon_class, theme="blue"):
    
    # Delta Stilini Belirle (Badge Style)
    if "+" in delta:
        delta_html = f"<span class='metric-delta delta-up'><i class='bx bx-up-arrow-alt'></i> {delta}</span>"
    elif "-" in delta:
        delta_html = f"<span class='metric-delta delta-down'><i class='bx bx-down-arrow-alt'></i> {delta}</span>"
    else:
        delta_html = f"<span class='metric-delta delta-flat'>{delta}</span>"

    html = f"""
    <div class="pro-metric-card">
        <div class="metric-icon-box theme-{theme}">
            <i class='bx {icon_class}'></i>
        </div>
        <div class="metric-info">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div>{delta_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_dashboard():
    if "dashboard_mode" not in st.session_state: st.session_state.dashboard_mode = "finance"
    user = st.session_state.user_data

    # --- HEADER (LIVE STATUS) ---
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown(f"## {user['brand']}")
        # Canlılık hissi veren yanıp sönen nokta simülasyonu
        st.caption("🟢 Sistem Operasyonel • İstanbul HQ Bağlı")
    with c2:
        # Tarih ve Saat (Statik Demo)
        st.markdown(f"<div style='text-align:right; font-family:monospace; color:#52525B;'>14 JAN 2026 • 10:42 PM</div>", unsafe_allow_html=True)

    st.markdown("---")

    # --- ANA YAPI ---
    col_chat, col_visual = st.columns([1.2, 2], gap="large")

    # === SOL: NEXT-GEN COPILOT ===
    with col_chat:
        st.markdown("##### <i class='bx bx-sparkles' style='color:#8B5CF6'></i> AI Operasyon Asistanı", unsafe_allow_html=True)
        
        chat_container = st.container(height=520)
        
        # CHAT ARAYÜZÜ
        if not st.session_state.get("messages"):
             with chat_container:
                st.markdown("<br>", unsafe_allow_html=True)
                st.info("👋 Merhaba! Ben ARTIS. Bugün hangi operasyonu yönetmek istersiniz?")
                
                # Modern Kısayol Butonları
                c_a, c_b = st.columns(2)
                if c_a.button("📦 Kargo Takibi", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": "Kargo durumum ne?"})
                    st.rerun()
                if c_b.button("📊 Finans Raporu", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": "Finansal özet ver."})
                    st.rerun()
        else:
            with chat_container:
                for msg in st.session_state.messages:
                    if msg["role"] == "user":
                        with st.chat_message("user", avatar="👤"):
                            st.write(msg["content"])
                    else:
                        # AI Avatarı yerine şık bir ikon
                        with st.chat_message("assistant", avatar="✨"):
                            st.write(msg["content"])

        # INPUT (Sticky Bottom Effect)
        if prompt := st.chat_input("Bir talimat verin (Örn: Stok analizi)..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Smart Routing
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo"]): st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "envanter"]): st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro"]): st.session_state.dashboard_mode = "finance"

            # Fake Streaming
            full_response = "Simülasyon Modu: Veriler analiz ediliyor..."
            # (Burada brain.get_streaming_response çağırılacak)
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            st.rerun()

    # === SAĞ: DATA COMMAND CENTER ===
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        # --- MOD 1: FİNANS ---
        if mode == "finance":
            st.markdown("##### 📈 Finansal Performans")
            
            # Pro Kartlar (3'lü Grid)
            k1, k2, k3 = st.columns(3)
            with k1: render_pro_metric("Aylık Ciro", "$42,500", "+12.5%", "bx-dollar", "blue")
            with k2: render_pro_metric("Net Kâr", "%32", "+4.2%", "bx-trending-up", "green")
            with k3: render_pro_metric("Büyüme", "Yüksek", "Stabil", "bx-rocket", "purple")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Grafik Alanı
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            
            # AI Insight (Alt Bilgi)
            st.info("💡 **AI Analizi:** Geçen çeyreğe göre reklam harcamaları %5 düşerken, organik satışlar %12 arttı.")

        # --- MOD 2: LOJİSTİK ---
        elif mode == "logistics":
            st.markdown("##### 🌍 Canlı Lojistik Ağı")
            
            k1, k2 = st.columns(2)
            with k1: render_pro_metric("Aktif Kargo", "TR-8821", "Atlantik", "bx-map-pin", "orange")
            with k2: render_pro_metric("Tahmini Varış", "14 Ocak", "2 Gün", "bx-time", "blue")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

        # --- MOD 3: ENVANTER ---
        elif mode == "inventory":
            st.markdown("##### 📦 Depo ve Stok")
            
            k1, k2 = st.columns(2)
            with k1: render_pro_metric("Toplam Ürün", "8,550", "+120", "bx-box", "purple")
            with k2: render_pro_metric("Riskli Stok", "Çanta", "Kritik", "bx-error", "red")
            
            st.markdown("<br>", unsafe_allow_html=True)
            c_chart, c_list = st.columns([1.5, 1])
            with c_chart:
                st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
            with c_list:
                st.markdown("**Kritik Ürünler**")
                st.error("Deri Çanta (Son 50)")
                st.warning("İpek Şal (Son 120)")
