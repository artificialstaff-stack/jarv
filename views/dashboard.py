import streamlit as st
import brain
from datetime import datetime
from typing import Dict, Any

# ==============================================================================
# 🎨 DASHBOARD ÖZEL STİLİ (Global Header'a Dokunmaz)
# ==============================================================================
def inject_dashboard_css():
    st.markdown("""
    <style>
        /* Sadece Dashboard Container'ı etkiler */
        .dash-header-container {
            padding: 25px 30px;
            background: linear-gradient(90deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
            position: relative;
        }
        
        .brand-title {
            font-size: 42px; font-weight: 800; color: #FFF; letter-spacing: -1px; margin: 0;
            background: linear-gradient(to right, #ffffff, #a1a1aa); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        
        .ai-badge {
            background: rgba(0,0,0,0.4); border: 1px solid #8B5CF6; 
            padding: 8px 12px; border-radius: 8px; color: #C084FC; 
            font-family: monospace; font-size: 12px; font-weight: bold;
        }

        /* Kartlar */
        .glass-card {
            background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06);
            border-radius: 16px; padding: 20px; transition: transform 0.2s;
        }
        .glass-card:hover { transform: translateY(-5px); border-color: rgba(255,255,255,0.2); }
        
        /* Metrikler */
        .metric-val { font-size: 28px; font-weight: 700; color: #FFF; }
        .metric-lbl { font-size: 12px; color: #A1A1AA; text-transform: uppercase; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 UI BİLEŞENLERİ
# ==============================================================================
def render_header(user_data: Dict[str, Any]):
    brand_name = user_data.get('brand', 'Anatolia Home')
    date_str = datetime.now().strftime("%d %B, %A")
    
    st.markdown(f"""
    <div class="dash-header-container">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <div style="color:#71717A; font-size:11px; letter-spacing:1px; font-weight:700; margin-bottom:5px;">OPERASYON MERKEZİ</div>
                <div class="brand-title">{brand_name}</div>
            </div>
            <div class="ai-badge">
                <i class='bx bx-microchip'></i> POWERED BY ARTIFICIAL STAFF
            </div>
        </div>
        <div style="margin-top:20px; display:flex; gap:15px; align-items:center;">
            <span style="background:rgba(16,185,129,0.1); color:#34D399; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:600;">● Sistem Operasyonel</span>
            <span style="background:rgba(59,130,246,0.1); color:#60A5FA; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:600;">İstanbul HQ</span>
            <div style="margin-left:auto; color:#52525B; font-size:12px; font-family:monospace;">{date_str}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_metric(label, value, delta, icon, color="#3B82F6"):
    st.markdown(f"""
    <div class="glass-card" style="display:flex; gap:15px; align-items:center;">
        <div style="width:48px; height:48px; background:{color}20; border-radius:12px; display:flex; align-items:center; justify-content:center; color:{color}; font-size:24px;">
            <i class='bx {icon}'></i>
        </div>
        <div>
            <div class="metric-lbl">{label}</div>
            <div class="metric-val">{value}</div>
            <div style="font-size:11px; color:{color}; font-weight:600;">{delta}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧠 DASHBOARD MAIN
# ==============================================================================
def render_dashboard():
    inject_dashboard_css()
    
    if "dashboard_mode" not in st.session_state: st.session_state.dashboard_mode = "finance"
    user = st.session_state.get('user_data', {'brand': 'Demo Brand'})

    render_header(user)

    col1, col2 = st.columns([1.2, 2], gap="large")

    # SOL: CHAT
    with col1:
        st.markdown("##### 🤖 Operasyon Asistanı")
        chat_cont = st.container(height=450)
        
        # Chat Logic (Basitleştirilmiş)
        if "messages" not in st.session_state: st.session_state.messages = []
        if not st.session_state.messages:
            chat_cont.info("👋 Merhaba! Size nasıl yardımcı olabilirim?")
        
        for msg in st.session_state.messages:
            with chat_cont.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("Talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Basit Yönlendirme Mantığı
            if "lojistik" in prompt.lower(): st.session_state.dashboard_mode = "logistics"
            elif "stok" in prompt.lower(): st.session_state.dashboard_mode = "inventory"
            else: st.session_state.dashboard_mode = "finance"
            
            response_chunks = brain.get_streaming_response(st.session_state.messages, user)
            full_res = ""
            # Stream simülasyonu
            placeholder = chat_cont.empty()
            for chunk in response_chunks:
                full_res += chunk
                placeholder.markdown(full_res + "▌")
            placeholder.markdown(full_res)
            
            st.session_state.messages.append({"role": "assistant", "content": full_res})
            st.rerun()

    # SAĞ: GRAFİKLER
    with col2:
        mode = st.session_state.dashboard_mode
        
        if mode == "finance":
            st.markdown("##### 📈 Finansal Özet")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aylık Ciro", "$42,500", "▲ %12.5", "bx-dollar-circle", "#3B82F6")
            with c2: render_metric("Net Kâr", "%32", "▲ %4.2", "bx-trending-up", "#10B981")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

        elif mode == "logistics":
            st.markdown("##### 🌍 Lojistik Durumu")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aktif Kargo", "142", "Global", "bx-map-pin", "#F59E0B")
            with c2: render_metric("Ort. Teslimat", "12 Gün", "▼ 2 Gün", "bx-time", "#3B82F6")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

        elif mode == "inventory":
            st.markdown("##### 📦 Depo Analizi")
            render_metric("Kritik Stok", "3 Ürün", "⚠️ Acil Sipariş", "bx-error", "#EF4444")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
