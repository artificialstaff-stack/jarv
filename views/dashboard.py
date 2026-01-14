import streamlit as st
import brain
import time
import pandas as pd
from datetime import datetime
from typing import Dict, Any

# ==============================================================================
# 🎨 1. MODERN DESIGN SYSTEM (KORUNDU)
# ==============================================================================
def inject_dashboard_css():
    st.markdown("""
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        .dash-header-container {
            padding: 30px;
            background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            margin-bottom: 30px;
            backdrop-filter: blur(20px);
            box-shadow: 0 20px 40px -10px rgba(0,0,0,0.5);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .metric-card {
            background: rgba(20, 20, 22, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 24px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 255, 255, 0.2);
            box-shadow: 0 15px 30px rgba(0,0,0,0.4);
        }

        .icon-box {
            width: 48px; height: 48px;
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            font-size: 24px;
            margin-bottom: 5px;
        }

        .theme-blue { background: rgba(59, 130, 246, 0.15); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.2); }
        .theme-green { background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.2); }
        .theme-purple { background: rgba(139, 92, 246, 0.15); color: #A78BFA; border: 1px solid rgba(139, 92, 246, 0.2); }
        .theme-orange { background: rgba(245, 158, 11, 0.15); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.2); }

        .metric-label { font-size: 13px; font-weight: 600; color: #A1A1AA; text-transform: uppercase; letter-spacing: 1px; }
        .metric-value { font-size: 32px; font-weight: 800; color: #FFFFFF; letter-spacing: -1px; line-height: 1; }
        
        .delta-badge {
            display: inline-flex; align-items: center; gap: 4px;
            font-size: 12px; font-weight: 700;
            padding: 4px 10px; border-radius: 20px;
            width: fit-content;
        }
        .delta-pos { background: rgba(16, 185, 129, 0.1); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.2); }
        .delta-neg { background: rgba(239, 68, 68, 0.1); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.2); }
        .delta-neu { background: rgba(255, 255, 255, 0.05); color: #A1A1AA; border: 1px solid rgba(255, 255, 255, 0.1); }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 2. YARDIMCI BİLEŞENLER (KORUNDU)
# ==============================================================================
def render_header(user_data):
    brand = user_data.get('brand', 'Anatolia Home')
    date_str = datetime.now().strftime("%d %B, %A")
    st.markdown(f"""
    <div class="dash-header-container">
        <div>
            <div style="color:#A1A1AA; font-size:11px; font-weight:700; letter-spacing:2px; margin-bottom:5px;">OPERASYON MERKEZİ</div>
            <h1 style="margin:0; font-size: 3rem; font-weight:800; background: linear-gradient(to right, #fff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{brand}</h1>
        </div>
        <div style="text-align:right;">
             <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.2); padding:6px 16px; border-radius:30px; margin-bottom:8px;">
                <div style="width:8px; height:8px; background:#10B981; border-radius:50%; box-shadow:0 0 10px #10B981;"></div>
                <span style="color:#34D399; font-size:12px; font-weight:700;">SYSTEM ONLINE</span>
             </div>
             <div style="color:#52525B; font-family:'Inter'; font-size:13px; font-weight:500;">{date_str}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_metric(label, value, delta, icon="bx-stats", theme="blue"):
    if "+" in delta or "Yolda" in delta or "Normal" in delta: d_class = "delta-pos"
    elif "-" in delta or "Risk" in delta or "Kritik" in delta: d_class = "delta-neg"
    else: d_class = "delta-neu"
    st.markdown(f"""
    <div class="metric-card">
        <div style="display:flex; justify-content:space-between; align-items:start;">
            <div class="icon-box theme-{theme}"><i class='bx {icon}'></i></div>
            <div class="delta-badge {d_class}">{delta}</div>
        </div>
        <div style="margin-top:10px;">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🚀 3. ANA DASHBOARD (HATA ONARILDI)
# ==============================================================================
def render_dashboard():
    inject_dashboard_css()
    
    # 1. GÜVENLİK: Session State Onarımı
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {'brand': 'Anatolia Home', 'name': 'Ahmet Yılmaz'}
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "dashboard_mode" not in st.session_state:
        st.session_state.dashboard_mode = "finance"
    
    user = st.session_state.user_data
    render_header(user)
    
    col_chat, col_viz = st.columns([1.1, 1.9], gap="large")

    # --- SOL: AI ASİSTAN ---
    with col_chat:
        st.markdown("<h4 style='color:white;'><i class='bx bx-bot'></i> Operasyon Asistanı</h4>", unsafe_allow_html=True)
        chat_cont = st.container(height=520)
        
        with chat_cont:
            if not st.session_state.messages:
                st.info("👋 Merhaba! Tüm operasyonel verilerinize hakimim. Bana bir talimat verin.")
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        if prompt := st.chat_input("Talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Zeki Mod Değiştirici
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo", "harita"]): st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "depo", "envanter"]): st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "para"]): st.session_state.dashboard_mode = "finance"
            elif any(x in p_low for x in ["belge", "doküman"]): st.session_state.dashboard_mode = "documents"
            elif any(x in p_low for x in ["form"]): st.session_state.dashboard_mode = "forms"
            elif any(x in p_low for x in ["yapılacak", "todo"]): st.session_state.dashboard_mode = "todo"
            elif any(x in p_low for x in ["plan"]): st.session_state.dashboard_mode = "plans"
            
            st.rerun()

    # AI Cevap Motoru (Hata Onarılan Kısım)
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with chat_cont:
            with st.chat_message("assistant"):
                ph = st.empty()
                full_resp = ""
                try:
                    # DÜZELTME: Hem mesajlar hem user_data gönderiliyor
                    for chunk in brain.get_streaming_response(st.session_state.messages, user):
                        full_resp += chunk
                        ph.markdown(full_resp + "▌")
                        time.sleep(0.01)
                    ph.markdown(full_resp)
                except Exception as e:
                    st.error(f"Brain Bağlantı Hatası: {e}")
            st.session_state.messages.append({"role": "assistant", "content": full_resp})

    # --- SAĞ: DİNAMİK GÖRSELLER (KORUNDU) ---
    with col_viz:
        mode = st.session_state.dashboard_mode
        if mode == "finance":
            st.markdown("##### 📈 Finansal Performans")
            c1, c2, c3 = st.columns(3)
            with c1: render_metric("Aylık Ciro", "$42,500", "+%12.5", "bx-dollar-circle", "blue")
            with c2: render_metric("Net Kâr", "%32", "+%4.2", "bx-trending-up", "green")
            with c3: render_metric("Büyüme", "Stabil", "Normal", "bx-pulse", "purple")
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            
        elif mode == "logistics":
            st.markdown("##### 🌍 Lojistik Ağı")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aktif Kargo", "TR-8821", "Yolda", "bx-map-pin", "orange")
            with c2: render_metric("Tahmini Varış", "2 Gün", "Zamanında", "bx-time", "blue")
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            
        elif mode == "inventory":
            st.markdown("##### 📦 Depo Durumu")
            c1, c2 = st.columns(2)
            with c1: render_metric("Toplam SKU", "8,500", "Adet", "bx-package", "purple")
            with c2: render_metric("Riskli Stok", "Çanta", "Kritik", "bx-error", "orange")
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)

        elif mode == "documents":
            st.markdown("##### 📂 Dijital Arşiv")
            data = {"Dosya": ["Fatura_Ocak.pdf", "Stok_V2.xlsx"], "Tarih": ["14.01", "12.01"], "Durum": ["Onaylı", "Hazır"]}
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

        elif mode == "forms":
            st.markdown("##### 📝 Onay Bekleyenler")
            st.info("📌 Personel İzin Formu - Ahmet Y. (Onay Bekliyor)")
            st.button("Onayla", key="dash_f1")

        elif mode == "plans":
            st.markdown("##### 💎 Stratejik Planlar")
            st.progress(70, text="Avrupa Genişlemesi (%70)")
            st.progress(40, text="AI Entegrasyonu (%40)")
