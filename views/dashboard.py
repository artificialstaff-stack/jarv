import streamlit as st
import brain
import time

# --- YARDIMCI FONKSİYON: PRO METRİK KARTI OLUŞTURUCU ---
def render_pro_metric(label, value, delta, icon_class, theme="blue"):
    """HTML ve CSS kullanarak gelişmiş, ikonlu bir metrik kartı çizer."""
    
    # Delta (Değişim) okunu ve rengini belirle
    if "+" in delta:
        delta_html = f"<span class='metric-delta delta-up'><i class='bx bx-trending-up'></i> {delta}</span>"
    elif "-" in delta:
        delta_html = f"<span class='metric-delta delta-down'><i class='bx bx-trending-down'></i> {delta}</span>"
    else:
        delta_html = f"<span class='metric-delta delta-flat'><i class='bx bx-minus'></i> {delta}</span>"

    # Kartın HTML yapısı
    html = f"""
    <div class="pro-metric-card">
        <div class="metric-icon-box theme-{theme}">
            <i class='bx {icon_class}'></i> </div>
        <div class="metric-info">
            <div>{label}</div>
            <div>{value}</div>
            <div>{delta_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_dashboard():
    if "dashboard_mode" not in st.session_state: st.session_state.dashboard_mode = "finance"
    user = st.session_state.user_data

    # --- HEADER ---
    c1, c2 = st.columns([3, 1])
    with c1:
        # Marka ismine özel, ikonlu başlık
        st.markdown(f"### <i class='bx bxs-dashboard' style='color:#3B82F6'></i> {user['brand']} — Komuta Merkezi", unsafe_allow_html=True)
    with c2:
         st.markdown(f"<div style='text-align:right; color:#A1A1AA; padding-top:5px;'><i class='bx bx-user-circle'></i> {user['name']}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # --- ANA YAPI ---
    col_chat, col_visual = st.columns([1.1, 1.9], gap="large")

    # === SOL: YENİLENMİŞ AI ASİSTAN ===
    with col_chat:
        st.markdown("#### <i class='bx bx-bot'></i> ARTIS Copilot", unsafe_allow_html=True)
        
        chat_box = st.container(height=480)
        
        if "messages" not in st.session_state: st.session_state.messages = []
        
        if not st.session_state.messages:
            with chat_box:
                st.markdown("<br>", unsafe_allow_html=True)
                # Daha modern karşılama ikonları
                st.info("👋 Merhaba! Ben ARTIS. Size nasıl yardımcı olabilirim?")
                
                st.markdown("Hızlı Başlangıç:")
                c_b1, c_b2 = st.columns(2)
                if c_b1.button("🚢 Lojistik Durumu", use_container_width=True):
                     st.session_state.messages.append({"role": "user", "content": "Lojistik durumum ne?"})
                     st.rerun()
                if c_b2.button("📈 Finansal Özet", use_container_width=True):
                     st.session_state.messages.append({"role": "user", "content": "Finansal durum?"})
                     st.rerun()
                if st.button("📦 Stok Risk Analizi", use_container_width=True):
                     st.session_state.messages.append({"role": "user", "content": "Stok durumu?"})
                     st.rerun()
        else:
            with chat_box:
                for msg in st.session_state.messages:
                    # Chat ikonlarını da güncelleyelim
                    avatar = "👤" if msg["role"] == "user" else "🤖"
                    with st.chat_message(msg["role"], avatar=avatar):
                        st.write(msg["content"])

        # Input
        if prompt := st.chat_input("Asistana bir talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo", "gemi"]): st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "ürün", "adet"]): st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "para"]): st.session_state.dashboard_mode = "finance"

            # AI Cevabı (Simüle edilmiş)
            full_response = ""
            for chunk in brain.get_streaming_response(st.session_state.messages, st.session_state.user_data):
                full_response += chunk
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            st.rerun()

    # === SAĞ: YENİ NESİL DASHBOARD ===
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        # FİNANS MODU
        if mode == "finance":
            st.markdown("#### 📈 Finansal Genel Bakış")
            
            # --- YENİ PRO KARTLAR ---
            k1, k2, k3 = st.columns(3)
            with k1:
                # Ciro Kartı (Mavi Tema, Dolar İkonu)
                render_pro_metric("Aylık Ciro", "$42,500", "+12%", "bx-dollar-circle", "blue")
            with k2:
                # Kâr Kartı (Yeşil Tema, Yükseliş İkonu)
                render_pro_metric("Net Kâr", "%32", "+4%", "bx-trending-up", "green")
            with k3:
                # Büyüme Kartı (Mor Tema, Roket İkonu)
                render_pro_metric("Büyüme Hızı", "Yüksek", "Stabil", "bx-rocket", "purple")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            with st.container(border=True):
                st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

        # LOJİSTİK MODU
        elif mode == "logistics":
            st.markdown("#### 🚢 Lojistik Operasyon")
            k1, k2 = st.columns(2)
            with k1:
                # Sevkiyat Kartı (Turuncu Tema, Gemi İkonu)
                render_pro_metric("Aktif Sevkiyat", "TR-8821", "Yolda", "bx-ship", "orange")
            with k2:
                # Varış Kartı (Mavi Tema, Zaman İkonu)
                render_pro_metric("Tahmini Varış", "14 Ocak", "2 Gün Kaldı", "bx-time-five", "blue")
            
            st.markdown("<br>", unsafe_allow_html=True)
            with st.container(border=True):
                st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

        # ENVANTER MODU
        elif mode == "inventory":
            st.markdown("#### 📦 Envanter Durumu")
            k1, k2 = st.columns(2)
            with k1:
                # Toplam Ürün (Mor Tema, Kutu İkonu)
                render_pro_metric("Toplam SKU", "48", "+2 Yeni", "bx-package", "purple")
            with k2:
                # Kritik Stok (Kırmızı Delta, Uyarı İkonu)
                render_pro_metric("Kritik Stok", "Çanta", "-50 Adet", "bx-error-circle", "orange")
            
            st.markdown("<br>", unsafe_allow_html=True)
            with st.container(border=True):
                st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
