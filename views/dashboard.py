import streamlit as st
import brain  # Yapay zeka beyni
import time
from datetime import datetime

# ==============================================================================
# 🎨 DASHBOARD TASARIMI
# ==============================================================================
def inject_dashboard_css():
    st.markdown("""
    <style>
        .dash-header {
            padding: 20px;
            background: linear-gradient(90deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            margin-bottom: 25px;
        }
        .metric-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 20px;
            transition: transform 0.2s;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            border-color: #3B82F6;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 YARDIMCI FONKSİYONLAR
# ==============================================================================
def render_header(user):
    st.markdown(f"""
    <div class="dash-header">
        <h1 style="margin:0; font-size:2.2rem;">{user.get('brand', 'Anatolia Home')}</h1>
        <div style="color:#34D399; font-size:0.9rem; font-weight:bold; margin-top:5px;">
            ● SYSTEM ONLINE <span style="color:#71717A; margin-left:10px;">| Istanbul HQ</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_metric(label, value, delta, color="#3B82F6"):
    st.markdown(f"""
    <div class="metric-card">
        <div style="color:#A1A1AA; font-size:0.8rem; text-transform:uppercase; letter-spacing:1px;">{label}</div>
        <div style="font-size:2rem; font-weight:800; color:white; margin:5px 0;">{value}</div>
        <div style="color:{color}; font-size:0.8rem; font-weight:bold;">{delta}</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🚀 ANA DASHBOARD FONKSİYONU
# ==============================================================================
def render_dashboard():
    inject_dashboard_css()
    user = st.session_state.get('user_data', {'brand': 'Demo'})
    
    # 1. Header
    render_header(user)
    
    # 2. Ana Düzen
    col1, col2 = st.columns([1.2, 2], gap="medium")
    
    # --- SOL: OPERASYON ASİSTANI (AI) ---
    with col1:
        st.subheader("🧠 Operasyon Asistanı")
        chat_container = st.container(height=450)
        
        # Mesaj Geçmişi
        if "messages" not in st.session_state: st.session_state.messages = []
        
        with chat_container:
            if not st.session_state.messages:
                st.info("👋 Merhaba! Finans, Stok veya Lojistik verilerinizi analiz edebilirim.")
            
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        # Yeni Mesaj
        if prompt := st.chat_input("Talimat verin (Örn: Ciro analizi)..."):
            # Kullanıcı mesajını ekle
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_container:
                st.chat_message("user").write(prompt)
                
                # AI Cevabı
                with st.chat_message("assistant"):
                    msg_placeholder = st.empty()
                    full_response = ""
                    
                    try:
                        # Brain modülünden yanıt al (Zeka burada!)
                        for chunk in brain.get_streaming_response(prompt):
                            full_response += chunk
                            msg_placeholder.markdown(full_response + "▌")
                            time.sleep(0.02)
                        msg_placeholder.markdown(full_response)
                        
                    except Exception as e:
                        st.error(f"Brain Hatası: {e}")
                        full_response = "Sistem bağlantısında sorun oluştu."
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    # --- SAĞ: GRAFİKLER VE METRİKLER ---
    with col2:
        st.subheader("📊 Finansal Özet")
        
        # Metrikler
        c1, c2 = st.columns(2)
        with c1: render_metric("Aylık Ciro", "$42,500", "▲ %12.5")
        with c2: render_metric("Net Kâr", "%32", "▲ %4.2", "#10B981")
        
        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
        
        # Grafikler (Brain'den geliyor)
        try:
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
        except Exception as e:
            st.warning(f"Grafik yüklenemedi: {e}")
