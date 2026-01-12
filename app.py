import streamlit as st
import sys
import os
import time

# Brain modülünü güvenli import et
try:
    import brain
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))
    import brain

# 1. SAYFA AYARLARI
st.set_page_config(
    page_title="ARTIS | Operasyon Merkezi",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS (ChatGPT Dark Mode + Türkçe Fontlar)
st.markdown("""
<style>
    /* Ana Arkaplan */
    .stApp { background-color: #343541; color: #ECECF1; font-family: 'Inter', sans-serif; }
    
    /* Sidebar */
    section[data-testid="stSidebar"] { background-color: #202123; }
    
    /* Input Alanı */
    .stChatInput { position: fixed; bottom: 30px; width: 70% !important; left: 50%; transform: translateX(-40%); z-index: 1000; }
    
    /* Mesaj Balonları */
    .stChatMessage { background-color: transparent; border: none; }
    div[data-testid="chatAvatarIcon-user"] { background-color: #5436DA !important; }
    div[data-testid="chatAvatarIcon-assistant"] { background-color: #10A37F !important; }
    
    /* Gizleme */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* Metrikler */
    div[data-testid="stMetricValue"] { color: #10A37F !important; }
</style>
""", unsafe_allow_html=True)

# 3. HAFIZA BAŞLATMA
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Merhaba 👋 Ben ARTIS. Washington DC operasyon merkezine hoş geldiniz. Size nasıl yardımcı olabilirim? (Örn: Marka analizi yapalım)"}]

# 4. SOL MENÜ (NAVIGASYON)
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#fff;'>ARTIS v2.5</h2>", unsafe_allow_html=True)
    st.caption("🚀 Autonomous Export OS")
    st.markdown("---")
    
    page = st.radio("MENÜ", ["💬 ASİSTAN (CHAT)", "📊 FİNANS PANELİ", "📦 LOJİSTİK TAKİP"], label_visibility="collapsed")
    
    st.markdown("---")
    if page == "💬 ASİSTAN (CHAT)":
        if st.button("🗑️ Sohbeti Temizle", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
            
    st.markdown("<div style='position:fixed; bottom:20px; font-size:12px; color:#666;'>Server: US-EAST-1 (Online)</div>", unsafe_allow_html=True)

# 5. SAYFA İÇERİKLERİ

# --- CHAT EKRANI ---
if page == "💬 ASİSTAN (CHAT)":
    st.markdown("<h1 style='text-align: center; color: #ECECF1; margin-bottom: 50px;'>ARTIS AI</h1>", unsafe_allow_html=True)
    
    # Sohbet Geçmişi
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        st.markdown("<br><br><br>", unsafe_allow_html=True) # Input altına boşluk

    # Input
    if prompt := st.chat_input("İşletmeniz hakkında konuşalım..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container.chat_message("user"):
            st.markdown(prompt)

        with chat_container.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ""
            
            # Brain'den Streaming Cevap
            try:
                stream = brain.get_streaming_response(st.session_state.messages)
                for chunk in stream:
                    full_response += chunk
                    placeholder.markdown(full_response + "▌")
                placeholder.markdown(full_response)
            except Exception:
                placeholder.markdown("⚠️ Bağlantı kurulamadı.")
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- FİNANS EKRANI ---
elif page == "📊 FİNANS PANELİ":
    st.title("📊 Finansal Simülasyon")
    st.info("Bu veriler, seçtiğiniz pakete göre tahmini kazancınızı gösterir.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Tahmini Ciro (Aylık)", "$42,500", "+%15")
    col2.metric("Net Kâr", "$18,200", "+%8")
    col3.metric("Reklam Bütçesi", "$3,000", "Stabil")
    
    st.markdown("### 📈 Gelir Projeksiyonu")
    st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

# --- LOJİSTİK EKRANI ---
elif page == "📦 LOJİSTİK TAKİP":
    st.title("📦 Global Lojistik Ağı")
    st.success("✅ Washington DC Depomuzda (US-IAD) kapasite mevcut.")
    
    st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
    
    with st.expander("Gümrük ve Depo Durumu", expanded=True):
        st.write("""
        * **Konum:** Washington DC (Beyaz Saray'a 15dk)
        * **Gümrük Durumu:** Yeşil Hat (Hızlı Geçiş)
        * **Son Sevkiyat:** İstanbul'dan 2 saat önce çıktı.
        """)
