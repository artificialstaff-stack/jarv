import streamlit as st
import brain
import time
from typing import Optional, Dict, Any

# ==============================================================================
# 🎨 1. ENTERPRISE CSS & STYLING ENGINE
# ==============================================================================
# Bu bölüm, Streamlit'in varsayılan görünümünü "override" eder ve
# Linear/Vercel tarzı "Derin Karanlık" (Deep Dark) temasını uygular.
# ==============================================================================

def inject_enterprise_css():
    st.markdown("""
    <style>
        /* --- CORE: FONTS & BACKGROUNDS --- */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, .stApp {
            background-color: #050505; /* Absolute Black Base */
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            color: #E4E4E7;
        }

        /* --- UI COMPONENT: GLASS CARDS --- */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 16px;
            padding: 24px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5);
        }
        
        .glass-card:hover {
            border-color: rgba(255, 255, 255, 0.12);
            transform: translateY(-2px);
            box-shadow: 0 12px 30px -4px rgba(0, 0, 0, 0.6);
        }

        /* --- UI COMPONENT: METRIC CARDS --- */
        .metric-container {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        
        .metric-icon-wrapper {
            width: 52px;
            height: 52px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            flex-shrink: 0;
            position: relative;
            overflow: hidden;
        }
        
        /* Icon Glow Effect */
        .metric-icon-wrapper::after {
            content: '';
            position: absolute;
            inset: 0;
            opacity: 0.2;
            background: currentColor;
        }

        /* Themes */
        .theme-blue { color: #3B82F6; background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.2); }
        .theme-green { color: #10B981; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); }
        .theme-purple { color: #8B5CF6; background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.2); }
        .theme-orange { color: #F97316; background: rgba(249, 115, 22, 0.1); border: 1px solid rgba(249, 115, 22, 0.2); }

        .metric-content { display: flex; flex-direction: column; gap: 4px; }
        .metric-label { font-size: 13px; font-weight: 500; color: #A1A1AA; letter-spacing: 0.02em; text-transform: uppercase; }
        .metric-value { font-size: 26px; font-weight: 700; color: #FFFFFF; letter-spacing: -0.03em; line-height: 1.1; }
        
        /* Pill Badge for Delta */
        .metric-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 2px 8px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 600;
            background: rgba(255,255,255,0.05);
        }
        .badge-up { color: #34D399; background: rgba(52, 211, 153, 0.1); }
        .badge-down { color: #F87171; background: rgba(248, 113, 113, 0.1); }
        .badge-flat { color: #94A3B8; background: rgba(148, 163, 184, 0.1); }

        /* --- CHAT INTERFACE --- */
        .stChatMessage { background: transparent !important; border: none !important; }
        
        div[data-testid="stChatMessage"] {
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 0.5rem;
            animation: fadeIn 0.3s ease-out;
        }

        /* User Bubble */
        div[data-testid="stChatMessage"][data-author="user"] {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(37, 99, 235, 0.1) 100%);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-top-right-radius: 2px;
        }

        /* AI Bubble */
        div[data-testid="stChatMessage"][data-author="assistant"] {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-top-left-radius: 2px;
        }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }

        /* --- PULSING DOT ANIMATION --- */
        .status-dot {
            width: 8px; height: 8px;
            background-color: #10B981;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 0 rgba(16, 185, 129, 0.4);
            animation: pulse 2s infinite;
            margin-right: 6px;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
            70% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
            100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }

        /* Clean up Streamlit UI */
        header { visibility: hidden; }
        .stDeployButton { display: none; }
        footer { visibility: hidden; }
        
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 2. COMPONENT LIBRARY (MODULAR UI FUNCTIONS)
# ==============================================================================

def render_pro_metric(
    label: str, 
    value: str, 
    delta: str, 
    icon_class: str, 
    theme: str = "blue"
):
    """
    Renders a high-end metric card using custom HTML/CSS with Flexbox.
    """
    # Determine delta style
    if "+" in delta:
        delta_html = f"<span class='metric-badge badge-up'><i class='bx bx-trending-up'></i> {delta}</span>"
    elif "-" in delta:
        delta_html = f"<span class='metric-badge badge-down'><i class='bx bx-trending-down'></i> {delta}</span>"
    else:
        delta_html = f"<span class='metric-badge badge-flat'>{delta}</span>"

    html_code = f"""
    <div class="glass-card metric-container">
        <div class="metric-icon-wrapper theme-{theme}">
            <i class='bx {icon_class}'></i>
        </div>
        <div class="metric-content">
            <span class="metric-label">{label}</span>
            <div class="metric-value">{value}</div>
            <div>{delta_html}</div>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def render_header(user_data: Dict[str, Any]):
    """
    Renders the sticky header with system status.
    """
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"## {user_data.get('brand', 'Anatolia')}")
        st.markdown(
            "<div style='display:flex; align-items:center; color:#10B981; font-size:12px; font-weight:500;'>"
            "<span class='status-dot'></span>SYSTEM OPERATIONAL • ISTANBUL HQ"
            "</div>", 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"<div style='text-align:right; font-family:\"JetBrains Mono\", monospace; color:#52525B; font-size:12px; padding-top:10px;'>"
            f"AI ENGINE: GEMINI 2.0 • LATENCY: 24ms"
            f"</div>", 
            unsafe_allow_html=True
        )
    st.markdown("---")

# ==============================================================================
# 🧠 3. MAIN DASHBOARD LOGIC
# ==============================================================================

def render_dashboard():
    # 1. Inject Styles
    inject_enterprise_css()
    
    # 2. Session Management
    if "dashboard_mode" not in st.session_state: 
        st.session_state.dashboard_mode = "finance"
    
    user = st.session_state.get('user_data', {'brand': 'Demo Brand', 'name': 'User'})

    # 3. Render Header
    render_header(user)

    # 4. Main Grid Layout
    col_chat, col_visual = st.columns([1.1, 1.9], gap="large")

    # === LEFT COLUMN: AI COPILOT ===
    with col_chat:
        st.markdown("##### <i class='bx bx-bot' style='color:#8B5CF6'></i> Operasyon Asistanı", unsafe_allow_html=True)
        
        # Chat Container (Fixed Height for Stability)
        chat_box = st.container(height=520)
        
        # Initialize Chat History
        if "messages" not in st.session_state: 
            st.session_state.messages = []

        # Empty State (Welcome Screen)
        if not st.session_state.messages:
            with chat_box:
                st.markdown("<br>", unsafe_allow_html=True)
                st.info("👋 Merhaba! Ben ARTIS. Operasyonel verilerinizi canlı izliyorum.")
                
                # Quick Action Buttons
                col_btn1, col_btn2 = st.columns(2)
                if col_btn1.button("📦 Kargo Durumu", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": "Kargo durumum ne?"})
                    st.rerun()
                if col_btn2.button("💰 Finans Özeti", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": "Finansal özet ver."})
                    st.rerun()
        
        # Render Chat History
        else:
            with chat_box:
                for msg in st.session_state.messages:
                    avatar = "👤" if msg["role"] == "user" else "✨"
                    with st.chat_message(msg["role"], avatar=avatar):
                        st.markdown(msg["content"])

        # Chat Input Area
        if prompt := st.chat_input("Bir talimat verin (Örn: Stok riski var mı?)..."):
            # A. Add User Message
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # B. Context Aware Routing (Intelligent Mode Switching)
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo", "gemi", "nerede"]): 
                st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "envanter", "mal", "ürün"]): 
                st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "para", "kazanç"]): 
                st.session_state.dashboard_mode = "finance"
            
            # C. Generate AI Response (Streaming)
            full_response = ""
            try:
                # Streaming Output for Real-time Feel
                for chunk in brain.get_streaming_response(st.session_state.messages, user):
                    full_response += chunk
            except Exception as e:
                full_response = "⚠️ Bağlantı hatası. Lütfen internet bağlantınızı veya API anahtarınızı kontrol edin."
                # Log error silently or to a debug panel
                print(f"Brain Error: {e}")

            # D. Append Assistant Message & Rerun
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            st.rerun()

    # === RIGHT COLUMN: DATA VISUALIZATION CENTER ===
    with col_visual:
        mode = st.session_state.dashboard_mode
        
        # --- SCENARIO 1: FINANCE ---
        if mode == "finance":
            st.markdown("##### 📈 Finansal Performans")
            
            # Metric Grid
            c1, c2, c3 = st.columns(3)
            with c1: render_pro_metric("Aylık Ciro", "$42,500", "+12.5%", "bx-dollar-circle", "blue")
            with c2: render_pro_metric("Net Kâr", "%32", "+4.2%", "bx-line-chart", "green")
            with c3: render_pro_metric("Büyüme Hızı", "Yüksek", "Stabil", "bx-rocket", "purple")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Chart Container
            with st.container():
                st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
                
            st.caption("💡 **AI İçgörüsü:** Reklam harcamaları optimize edildi, organik satışlarda %12 artış gözlemleniyor.")

        # --- SCENARIO 2: LOGISTICS ---
        elif mode == "logistics":
            st.markdown("##### 🌍 Global Lojistik Ağı")
            
            c1, c2 = st.columns(2)
            with c1: render_pro_metric("Aktif Sevkiyat", "TR-8821", "Atlantik", "bx-map-pin", "orange")
            with c2: render_pro_metric("Tahmini Varış", "14 Ocak", "2 Gün", "bx-time-five", "blue")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            with st.container():
                st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

        # --- SCENARIO 3: INVENTORY ---
        elif mode == "inventory":
            st.markdown("##### 📦 Depo ve Envanter Analizi")
            
            c1, c2 = st.columns(2)
            with c1: render_pro_metric("Toplam SKU", "8,550", "+120", "bx-package", "purple")
            with c2: render_pro_metric("Riskli Stok", "Çanta", "Kritik", "bx-error-circle", "orange") # Red yerine Orange daha dengeli
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col_chart, col_details = st.columns([1.5, 1])
            with col_chart:
                st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
            with col_details:
                st.markdown(
                    """
                    <div class='glass-card' style='height: 100%; padding: 16px;'>
                        <div style='font-size:12px; color:#A1A1AA; margin-bottom:10px;'>KRİTİK ÜRÜNLER</div>
                        <div style='margin-bottom:8px; color:#F87171; font-weight:600;'>• Deri Çanta (50 Adet)</div>
                        <div style='color:#FBBF24; font-weight:600;'>• İpek Şal (120 Adet)</div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
