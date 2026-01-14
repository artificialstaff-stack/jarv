import streamlit as st
import brain
import time
from datetime import datetime
from typing import Optional, Dict, Any

# ==============================================================================
# 🎨 1. ENTERPRISE CSS & STYLING ENGINE (ULTRA PREMIUM)
# ==============================================================================
def inject_enterprise_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap');

        /* --- DASHBOARD HEADER CONTAINER --- */
        .dash-header-container {
            padding: 20px 25px;
            background: linear-gradient(90deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            margin-bottom: 35px;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        /* Arka Plan Efekti (Aurora Glow) */
        .dash-header-container::before {
            content: '';
            position: absolute;
            top: -50%; left: -50%; width: 200%; height: 200%;
            background: radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.08) 0%, transparent 50%);
            z-index: 0;
            pointer-events: none;
        }
        
        .header-content { position: relative; z-index: 1; }
        
        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 20px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            padding-bottom: 15px;
        }
        
        /* Sol Taraf: Marka İsmi */
        .brand-eyebrow {
            font-size: 10px;
            color: #A1A1AA;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 700;
            margin-bottom: 6px;
            display: flex; align-items: center; gap: 6px;
        }
        .brand-title {
            font-size: 42px;
            font-weight: 800;
            color: #FFF;
            letter-spacing: -1.5px;
            line-height: 1;
            text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }

        /* Sağ Taraf: AI Engine Badge */
        .ai-badge {
            font-family: 'JetBrains Mono', monospace;
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(139, 92, 246, 0.3); /* Mor Çerçeve */
            padding: 8px 12px;
            border-radius: 8px;
            display: flex; flex-direction: column; align-items: flex-end;
            gap: 2px;
            box-shadow: 0 0 15px rgba(139, 92, 246, 0.1);
        }
        .ai-label { font-size: 9px; color: #71717A; text-transform: uppercase; letter-spacing: 1px; }
        .ai-name { 
            font-size: 13px; color: #C084FC; font-weight: 700; letter-spacing: 0.5px; 
            display: flex; align-items: center; gap: 8px;
        }
        
        /* Alt Statü Satırı */
        .header-bottom {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .status-pill {
            display: inline-flex; align-items: center; gap: 8px;
            padding: 5px 12px;
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.15);
            border-radius: 99px;
            color: #34D399;
            font-size: 11px; font-weight: 600; letter-spacing: 0.3px;
        }
        
        .location-pill {
            display: inline-flex; align-items: center; gap: 6px;
            padding: 5px 12px;
            background: rgba(59, 130, 246, 0.08);
            border: 1px solid rgba(59, 130, 246, 0.15);
            border-radius: 99px;
            color: #60A5FA;
            font-size: 11px; font-weight: 600;
        }
        
        .live-dot {
            width: 6px; height: 6px;
            background: #10B981;
            border-radius: 50%;
            box-shadow: 0 0 8px rgba(16, 185, 129, 0.8);
            animation: pulse-dot 2s infinite;
        }
        
        @keyframes pulse-dot {
            0% { opacity: 0.6; box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
            50% { opacity: 1; box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
            100% { opacity: 0.6; box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }

        /* --- KARTLAR & METRİKLER --- */
        .glass-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 16px;
            padding: 24px;
            transition: transform 0.2s;
        }
        .glass-card:hover { transform: translateY(-2px); border-color: rgba(255,255,255,0.1); }
        
        .metric-container { display: flex; align-items: center; gap: 16px; }
        .metric-icon-wrapper {
            width: 52px; height: 52px; border-radius: 14px;
            display: flex; align-items: center; justify-content: center;
            font-size: 24px; flex-shrink: 0;
        }
        .metric-value { font-size: 26px; font-weight: 700; color: #FFF; line-height: 1.1; margin: 4px 0;}
        .metric-label { font-size: 12px; font-weight: 600; color: #71717A; text-transform: uppercase; letter-spacing: 0.5px; }
        
        .theme-blue { color: #3B82F6; background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.2); }
        .theme-green { color: #10B981; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); }
        .theme-purple { color: #8B5CF6; background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.2); }
        .theme-orange { color: #F97316; background: rgba(249, 115, 22, 0.1); border: 1px solid rgba(249, 115, 22, 0.2); }
        
        /* Badge */
        .metric-badge { padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center; gap: 4px; }
        .badge-up { color: #34D399; background: rgba(52, 211, 153, 0.1); border: 1px solid rgba(52, 211, 153, 0.2); }
        .badge-down { color: #F87171; background: rgba(248, 113, 113, 0.1); border: 1px solid rgba(248, 113, 113, 0.2); }
        .badge-flat { color: #A1A1AA; background: rgba(148, 163, 184, 0.1); border: 1px solid rgba(148, 163, 184, 0.2); }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 2. UI COMPONENTS (SAFE HTML LIST-JOIN)
# ==============================================================================

def render_header(user_data: Dict[str, Any]):
    """
    Renders the DASHBOARD HEADER.
    - Sol: Kullanıcının Marka İsmi (Dinamik)
    - Sağ: 'ARTIFICIAL STAFF' (Bizim AI Motorumuz)
    """
    # 1. Kullanıcının Marka İsmini Dinamik Alıyoruz
    brand_name = user_data.get('brand', 'Anatolia Home')
    
    current_date = datetime.now().strftime("%d %B, %A")
    
    # HTML Parçaları (Indentation hatasını önlemek için liste birleştirme)
    html_parts = [
        '<div class="dash-header-container">',
        '<div class="header-content">',
        
        # --- TOP ROW ---
        '<div class="header-top">',
            # SOL: MARKA İSMİ
            '<div>',
                '<div class="brand-eyebrow"><i class="bx bx-command"></i> OPERASYON MERKEZİ</div>',
                f'<div class="brand-title">{brand_name}</div>',
            '</div>',
            
            # SAĞ: BİZİM MOTORUMUZ (ARTIFICIAL STAFF)
            '<div class="ai-badge">',
                '<div class="ai-label">POWERED BY</div>',
                '<div class="ai-name"><i class="bx bx-microchip"></i> ARTIFICIAL STAFF</div>',
            '</div>',
        '</div>',
        
        # --- BOTTOM ROW ---
        '<div class="header-bottom">',
            '<div class="status-pill"><div class="live-dot"></div>Sistem Operasyonel</div>',
            '<div class="location-pill"><i class="bx bx-globe"></i> İstanbul HQ</div>',
            f'<div style="margin-left: auto; font-size: 12px; color: #52525B; font-family: \'JetBrains Mono\';">{current_date}</div>',
        '</div>',
        
        '</div>', # End header-content
        '</div>'  # End container
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
# 🧠 3. MAIN DASHBOARD LOGIC
# ==============================================================================

def render_dashboard():
    inject_enterprise_css()
    
    if "dashboard_mode" not in st.session_state: 
        st.session_state.dashboard_mode = "finance"
    
    # Kullanıcı verisini session'dan çekiyoruz
    user = st.session_state.get('user_data', {'brand': 'Demo Brand'})

    # 1. RENDER HEADER (Artık Dinamik Marka + Artificial Staff Badge)
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
            st.caption("💡 **Artificial Staff Notu:** Reklam harcamaları optimize edildi.")

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
