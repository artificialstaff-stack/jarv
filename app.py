import streamlit as st
import time
from instructions import COMPANY_DATA
from styles import apply_tech_style
from ui import render_sidebar, render_inventory_dashboard, render_finance_dashboard
from brain import get_jarvis_response

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="JARVIS 2026",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Stili Uygula
apply_tech_style()

# 3. Sidebar'ı Çiz ve Seçimi Al
selected_tab = render_sidebar()

# --- app.py İçindeki İlgili Kısım ---

if "messages" not in st.session_state:
    # Jarvis'in kimliğini en başa "gizli" mesaj olarak ekliyoruz
    st.session_state.messages = [
        {"role": "system", "content": COMPANY_DATA}
    ]
    
    # Kullanıcının göreceği ilk "Hoş geldin" mesajı
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Jarvis v4.2 Aktif. Neural arayüze hoş geldiniz. Markanızı tanımlayın."
    })
# 5. Ana Ekran Mantığı
if selected_tab == "🤖 JARVIS CORE":
    st.header("Jarvis Neural Interface")
    
    # --- EKRANA MESAJLARI BASAN KISIM ---

for message in st.session_state.messages:
    # BURASI ÇOK ÖNEMLİ: Eğer rol 'system' ise bu turu atla (ekrana basma)
    if message["role"] == "system":
        continue
        
    # Diğer mesajları (user ve assistant) ekrana bas
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    # Kullanıcıdan Girdi Al
    if prompt := st.chat_input("Talimat verin..."):
        # Kullanıcı mesajını ekle
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # AI Cevabını Üret
        with st.chat_message("assistant", avatar="🤖"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Brain dosyasından cevabı al
            ai_response = get_jarvis_response(st.session_state.messages)
            
            # Yazıyor efekti (Typewriter effect)
            for chunk in ai_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})

elif selected_tab == "📦 GLOBAL ENVANTER":
    render_inventory_dashboard()

elif selected_tab == "💰 FİNANSAL ANALİZ":
    render_finance_dashboard()

elif selected_tab == "📊 STRATEJİ":
    st.title("📊 Pazar Stratejisi")
    st.write("Veri madenciliği modülü çalışıyor...")
