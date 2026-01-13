import streamlit as st
import brain
import time
from datetime import datetime
from typing import Optional, Dict, Any

# ==============================================================================
# 🎨 1. ENTERPRISE CSS & STYLING ENGINE
# ==============================================================================
def inject_enterprise_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

        /* --- DASHBOARD HEADER ÖZEL STİLİ --- */
        .dash-header-container {
            padding: 10px 0 30px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            margin-bottom: 30px;
        }
        
        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 15px;
        }
        
        /* Marka Başlığı */
        .brand-eyebrow {
            font-size: 11px;
            color: #71717A;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 600;
            margin-bottom: 4px;
        }
        .brand-title {
            font-size: 38px;
            font-weight: 800;
            color: #FFF;
            letter-spacing: -1.2px;
            line-height: 1;
            background: linear-gradient(to right, #FFFFFF 0%, #A1A1AA 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Teknik Rozetler (Sağ Üst) */
        .tech-badge-group { display: flex; gap: 10px; }
        .tech-badge {
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: #71717A;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            padding: 6px 10px;
            border-radius: 6px;
            display: flex; align-items: center; gap: 6px;
            transition: all 0.2s;
        }
        .tech-badge:hover { border-color: rgba(255,255,255,0.2); color: #E4E4E7; }
        
        /* Alt Statü Satırı */
        .header-bottom {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .status-pill {
            display: inline-flex; align-items: center; gap: 8px;
            padding: 6px 12px;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.2);
            border-radius: 20px;
            color: #34D399;
            font-size: 12px; font-weight: 600;
        }
        
        .location-pill {
            display: inline-flex; align-items: center; gap: 6px;
            padding: 6px 12px;
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 20px;
            color: #60A5FA;
            font-size: 12px; font-weight: 600;
        }
        
        .live-dot {
            width: 6px; height: 6px;
            background: #10B981;
            border-radius: 50%;
            box-shadow: 0 0 8px rgba(16, 185, 129, 0.6);
            animation: pulse-dot 2s infinite;
        }
        
        @keyframes pulse-dot {
            0% { opacity: 0.6; box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
            70% { opacity: 1; box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
            100% { opacity: 0.6; box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }

        /* --- KARTLAR & GENEL --- */
        .glass-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 16px;
            padding: 24px;
        }
        
        /* Metric Cards */
        .metric-container { display: flex; align-items: center; gap: 16px; }
        .metric-icon-wrapper {
            width: 52px; height: 52px; border-radius: 14px;
            display: flex; align-items: center; justify-content: center;
            font-size: 24px; flex-shrink: 0;
        }
        .metric-value { font-size: 26px; font-weight: 700; color: #FFF; line-height: 1.1; }
        .metric-label { font-size: 13px; font-weight: 500; color: #A1A1AA; text-transform: uppercase; }
        
        .theme-blue { color: #3B82F6; background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.2); }
        .theme-green { color: #10B981; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); }
        .theme-purple { color: #8B5CF6; background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.2); }
        .theme-orange { color: #F97316; background: rgba(249, 115, 22, 0.1); border: 1px solid rgba(249, 115, 22, 0.2); }
        
        /* Badge */
        .metric-badge { padding: 2px 8px; border-radius: 99px; font-size: 11px; font-weight: 600; display: inline-flex; align-items: center; gap: 4px; }
        .badge-up { color: #34D399; background: rgba(52, 211, 153, 0.1); }
        .badge-down { color: #F87171; background: rgba(248, 113, 113, 0.1); }
        .badge-flat { color: #94A3B8; background: rgba(148, 163, 184, 0.1); }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 2. UI COMPONENTS (SAFE HTML GENERATION)
# ==============================================================================

def render_header(user_data: Dict[str, Any]):
    """
    Renders the ULTRA-PREMIUM header using List Join method to prevent indentation bugs.
    """
    brand_name = user_data.get('brand', 'Anatolia')
    current_date = datetime.now().strftime("%d %B, %A")
    
    # HTML parçalarını liste olarak oluşturup birleştiriyoruz.
    # Bu yöntem indentation (girinti) hatasını %100 engeller.
    html_parts = [
        '<div class="dash-header-container">',
        '<div class="header-top">',
        '<div>',
        '<div class="brand-eyebrow">Operasyon Merkezi</div>',
        f'<div class="brand-title">{brand_name}</div>',
        '</div>',
        '<div class="tech-badge-group">',
        '<div class="tech-badge"><i class="bx bx-cpu"></i> GEMINI 2.0 FLASH</div>',
        '<div class="tech-badge"><i class="bx bx-wifi"></i> 24ms LATENCY</div>',
        '</div>',
        '</div>', # End header-top
        
        '<div class="header-bottom">',
        '<div class="status-pill"><div class="live-dot"></div>Sistem Operasyonel</div>',
        '<div class="location-pill"><i class="bx bx-map"></i> İstanbul HQ</div>',
        f'<div style="margin-left: auto; font-size: 13px; color: #52525B; font-family: \'JetBrains Mono\', monospace;">{current_date}</div>',
        '</div>', # End header-bottom
        '</div>'
    ]
    
    st.markdown("".join(html_parts), unsafe_allow_html=True)

def render_pro_metric(label, value, delta, icon_class, theme="blue"):
    if "+" in delta:
        delta_html = f"<span class='metric-badge badge-up'><i class='bx bx-trending-up'></i> {delta}</span>"
    elif "-" in delta:
        delta_html = f"<span class='metric-badge badge-down'><i class='bx bx-trending-down'></i> {delta}</span>"
    else:
        delta_html = f"<span class='metric-badge badge-flat'>{delta}</span>"

    html_parts = [
        '<div class="glass-card metric-container">',
        f'<div class="metric-icon-wrapper theme-{theme}">',
        f'<i class="bx {icon_class}"></i>',
        '</div>',
        '<div class="metric-content">',
        f'<div class="metric-label">{label}</div>',
        f'<div class="metric-value">{value}</div>',
        f'<div>{delta_html}</div>',
        '</div>',
        '</div>'
    ]
    
    st.markdown("".join(html_parts), unsafe_allow_html=True)

# ==============================================================================
# 🧠 3. MAIN DASHBOARD
# ==============================================================================

def render_dashboard():
    inject_enterprise_css()
    
    if "dashboard_mode" not in st.session_state: 
        st.session_state.dashboard_mode = "finance"
    
    user = st.session_state.get('user_data', {'brand': 'Demo Brand'})

    # 1. RENDER HEADER (FIXED)
    render_header(user)

    # 2. MAIN LAYOUT
    col_chat, col_visual = st.columns([1.1, 1.9], gap="large")

    # === LEFT: AI COPILOT ===
    with col_chat:
        st.markdown("##### <i class='bx bx-bot' style='color:#8B5CF6'></i> Operasyon Asistanı", unsafe_allow_html=True)
        chat_box = st.container(height=520)
        
        if "messages" not in st.session_state: st.session_state.messages = []

        if not st.session_state.messages:
            with chat_box:
                st.markdown("<br>", unsafe_allow_html=True)
                st.info("👋 Merhaba! Ben ARTIS. Bugün hangi operasyonu yönetmek istersiniz?")
                c1, c2 = st.columns(2)
                if c1.button("📦 Kargo Durumu", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": "Kargo durumum ne?"})
                    st.rerun()
                if c2.button("💰 Finans Özeti", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": "Finansal özet ver."})
                    st.rerun()
        else:
            with chat_box:
                for msg in st.session_state.messages:
                    avatar = "👤" if msg["role"] == "user" else "✨"
                    with st.chat_message(msg["role"], avatar=avatar):
                        st.markdown(msg["content"])

        if prompt := st.chat_input("Bir talimat verin (Örn: Stok analizi)..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Mode Switching
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo", "gemi"]): st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "envanter", "mal"]): st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "para"]): st.session_state.dashboard_mode = "finance"
            
            # AI Response
            full_response = ""
            try:
                for chunk in brain.get_streaming_response(st.session_state.messages, user):
                    full_response += chunk
            except Exception as e:
                full_response = "⚠️ Bağlantı hatası."
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            st.rerun()

    # === RIGHT: DATA CENTER ===
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        if mode == "finance":
            st.markdown("##### 📈 Finansal Performans")
            c1, c2, c3 = st.columns(3)
            with c1: render_pro_metric("Aylık Ciro", "$42,500", "+12.5%", "bx-dollar-circle", "blue")
            with c2: render_pro_metric("Net Kâr", "%32", "+4.2%", "bx-line-chart", "green")
            with c3: render_pro_metric("Büyüme", "Yüksek", "Stabil", "bx-rocket", "purple")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            st.caption("💡 **AI Notu:** Reklam harcamaları optimize edildi.")

        elif mode == "logistics":
            st.markdown("##### 🌍 Lojistik Ağı")
            c1, c2 = st.columns(2)
            with c1: render_pro_metric("Aktif Sevkiyat", "TR-8821", "Atlantik", "bx-map-pin", "orange")
            with c2: render_pro_metric("Tahmini Varış", "14 Ocak", "2 Gün", "bx-time-five", "blue")
            st.markdown("<br>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

        elif mode == "inventory":
            st.markdown("##### 📦 Depo Durumu")
            c1, c2 = st.columns(2)
            with c1: render_pro_metric("Toplam SKU", "8,550", "+120", "bx-package", "purple")
            with c2: render_pro_metric("Riskli Stok", "Çanta", "Kritik", "bx-error-circle", "orange")
            st.markdown("<br>", unsafe_allow_html=True)
            c_chart, c_det = st.columns([1.5, 1])
            with c_chart: st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
            with c_det:
                st.markdown("""
                <div class='glass-card'>
                    <div style='font-size:12px; color:#A1A1AA; margin-bottom:10px;'>KRİTİK ÜRÜNLER</div>
                    <div style='color:#F87171; font-weight:600; margin-bottom:5px;'>• Deri Çanta (50)</div>
                    <div style='color:#FBBF24; font-weight:600;'>• İpek Şal (120)</div>
                </div>""", unsafe_allow_html=True)
