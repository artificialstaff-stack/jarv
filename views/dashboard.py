import streamlit as st
import brain
import time
import pandas as pd
from datetime import datetime

def render_dashboard():
    # 1. HATA ÖNLEYİCİ: Session State'i garanti altına al
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {'brand': 'Anatolia Home', 'name': 'Ahmet Yılmaz'}
    
    # 'user' değişkenini burada tanımlıyoruz
    user = st.session_state.user_data
    
    if "dashboard_mode" not in st.session_state:
        st.session_state.dashboard_mode = "finance"

    # Senin orijinal CSS ve Header yapın (Dokunulmadı)
    inject_dashboard_css()
    render_header(user)
    
    col_chat, col_viz = st.columns([1.1, 1.9], gap="large")

    # --- SOL: TAM KAPSAMLI AI ASİSTAN (Gemini 3 Flash Entegre) ---
    with col_chat:
        st.markdown("##### 🧠 Operasyon Asistanı")
        chat_cont = st.container(height=520)
        
        if "messages" not in st.session_state: 
            st.session_state.messages = []
        
        with chat_cont:
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
        
        if prompt := st.chat_input("Talimat verin..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # --- ZEKİ MOD GEÇİŞİ (AI'nın Gözü ve Kulağı) ---
            # Kullanıcı ne yazarsa sağ panel oraya ışınlanır
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo", "harita"]): st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "depo", "envanter"]): st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "para"]): st.session_state.dashboard_mode = "finance"
            elif any(x in p_low for x in ["belge", "doküman"]): st.session_state.dashboard_mode = "documents"
            elif any(x in p_low for x in ["form"]): st.session_state.dashboard_mode = "forms"
            elif any(x in p_low for x in ["yapılacak", "todo"]): st.session_state.dashboard_mode = "todo"
            elif any(x in p_low for x in ["plan"]): st.session_state.dashboard_mode = "plans"
            
            st.rerun()

    # Gemini 3 Flash Motorunu Çalıştıran Kısım
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with chat_cont:
            with st.chat_message("assistant"):
                ph = st.empty()
                full_resp = ""
                # FİX: 'user' parametresini brain.py'ye gönderiyoruz
                try:
                    for chunk in brain.get_streaming_response(st.session_state.messages, user):
                        full_resp += chunk
                        ph.markdown(full_resp + "▌")
                        time.sleep(0.01)
                    ph.markdown(full_resp)
                except Exception as e:
                    st.error(f"Brain Hatası: {e}")
            st.session_state.messages.append({"role": "assistant", "content": full_resp})

    # --- SAĞ: DİNAMİK GÖRSEL PANEL (GELİŞTİRİLDİ) ---
    with col_viz:
        mode = st.session_state.dashboard_mode
        
        if mode == "finance":
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
        elif mode == "logistics":
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
        elif mode == "inventory":
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
        elif mode == "documents":
            st.markdown("##### 📂 Doküman Arşivi")
            # AI dokümanlardan bahsettiğinde burası otomatik tabloya dönüşür
            df = pd.DataFrame({"Dosya": ["Fatura.pdf", "İrsaliye.pdf"], "Tarih": ["12.01", "13.01"]})
            st.dataframe(df, use_container_width=True, hide_index=True)
        elif mode == "plans":
            st.markdown("##### 💎 Stratejik Planlar")
            # Planlar sayfası görseli
            st.progress(70, text="Avrupa Genişlemesi")
