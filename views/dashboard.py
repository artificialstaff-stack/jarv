import streamlit as st
import brain
from datetime import datetime
from typing import Dict, Any
import time

# ==============================================================================
# 🎨 DASHBOARD CSS
# ==============================================================================
def inject_dashboard_css():
    st.markdown("""
    <style>
        .dash-header-container {
            padding: 25px;
            background: linear-gradient(90deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            margin-bottom: 25px;
        }
        .metric-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 20px;
            transition: all 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            border-color: rgba(59, 130, 246, 0.5);
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 BİLEŞENLER
# ==============================================================================
def render_header(user_data):
    brand = user_data.get('brand', 'Anatolia Home')
    st.markdown(f"""
    <div class="dash-header-container">
        <h1 style="margin:0; font-size: 2.5rem; background: -webkit-linear-gradient(#eee, #333); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{brand}</h1>
        <div style="color: #34D399; font-size: 0.9rem; margin-top: 5px; font-weight: bold;">● SYSTEM ONLINE</div>
    </div>
    """, unsafe_allow_html=True)

def render_metric(label, value, delta, color="#3B82F6"):
    st.markdown(f"""
    <div class="metric-card">
        <div style="color: #A1A1AA; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">{label}</div>
        <div style="font-size: 2rem; font-weight: 800; color: white; margin: 5px 0;">{value}</div>
        <div style="color: {color}; font-size: 0.8rem; font-weight: 600;">{delta}</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🚀 ANA RENDER FONKSİYONU (AI BURADA)
# ==============================================================================
def render_dashboard():
    inject_dashboard_css()
    
    if "dashboard_mode" not in st.session_state: st.session_state.dashboard_mode = "finance"
    user = st.session_state.get('user_data', {'brand': 'Demo Brand'})
    
    render_header(user)
    
    col1, col2 = st.columns([1.2, 2], gap="medium")
    
    # --- SOL: AI CHAT ---
    with col1:
        st.markdown("### 🧠 Operasyon Asistanı")
        chat_container = st.container(height=500)
        
        if "messages" not in st.session_state: st.session_state.messages = []
        
        # Geçmiş mesajları yazdır
        with chat_container:
            if not st.session_state.messages:
                st.info("👋 Merhaba! Verilerinizi analiz etmeye hazırım.")
            
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        # Yeni mesaj girişi
        if prompt := st.chat_input("Talimat verin (Örn: Ciro analizi)..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_container:
                st.chat_message("user").write(prompt)
                
                # AI DÜŞÜNÜYOR...
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    # Brain.py'den veri çekiliyor (MOCK DEĞİL GERÇEK ÇAĞRI)
                    try:
                        # Modu ayarla
                        if "lojistik" in prompt.lower(): st.session_state.dashboard_mode = "logistics"
                        elif "stok" in prompt.lower(): st.session_state.dashboard_mode = "inventory"
                        else: st.session_state.dashboard_mode = "finance"

                        # Stream Cevap
                        for chunk in brain.get_streaming_response(prompt):
                            full_response += chunk
                            message_placeholder.markdown(full_response + "▌")
                            time.sleep(0.02)
                        message_placeholder.markdown(full_response)
                    except Exception as e:
                        st.error(f"Brain Bağlantı Hatası: {e}")
                        full_response = "Bağlantı hatası."
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            st.rerun()

    # --- SAĞ: GRAFİKLER ---
    with col2:
        mode = st.session_state.dashboard_mode
        
        if mode == "finance":
            st.markdown("### 📈 Finansal Özet")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aylık Ciro", "$42,500", "▲ %12.5")
            with c2: render_metric("Net Kâr", "%32", "▲ %4.2", "#10B981")
            st.markdown("<br>", unsafe_allow_html=True)
            try:
                st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            except:
                st.warning("Grafik yüklenemedi.")

        elif mode == "logistics":
            st.markdown("### 🌍 Lojistik Ağı")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aktif Kargo", "142", "Global Dağıtım", "#F59E0B")
            with c2: render_metric("Teslimat Süresi", "12 Gün", "▼ 2 Gün İyileşme")
            st.markdown("<br>", unsafe_allow_html=True)
            try:
                st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            except:
                st.warning("Harita yüklenemedi.")
        
        elif mode == "inventory":
            st.markdown("### 📦 Depo Durumu")
            render_metric("Kritik Stok", "3 Ürün", "⚠️ Acil Sipariş", "#EF4444")
            st.markdown("<br>", unsafe_allow_html=True)
            try:
                st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
            except:
                st.warning("Stok grafiği yüklenemedi.")
