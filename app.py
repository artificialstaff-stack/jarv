import streamlit as st
import sys
import os

# Brain modülünü import etmek için yol ayarı
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))
import brain

# 1. SAYFA AYARLARI
st.set_page_config(
    page_title="ARTIS | AI Chat",
    page_icon="🤖",
    layout="centered", # ChatGPT gibi ortalı
    initial_sidebar_state="expanded"
)

# 2. CHATGPT TARZI CSS (STYLES)
st.markdown("""
<style>
    /* Genel Arkaplan */
    .stApp {
        background-color: #343541; /* ChatGPT Koyu Gri */
        color: #ECECF1;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #202123;
    }
    
    /* Chat Input Alanı */
    .stChatInput {
        position: fixed;
        bottom: 20px;
    }
    
    /* Mesaj Kutuları */
    .stChatMessage {
        background-color: transparent;
        border: none;
    }
    div[data-testid="chatAvatarIcon-user"] {
        background-color: #5436DA !important; /* Kullanıcı Mor */
    }
    div[data-testid="chatAvatarIcon-assistant"] {
        background-color: #10A37F !important; /* GPT Yeşil */
    }
    
    /* Başlık Gizle */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# 3. SESSION STATE (HAFIZA)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Merhaba. Ben ARTIS. Washington DC operasyon merkezine hoş geldiniz. Markanızın adı nedir?"}
    ]

# 4. SIDEBAR (MENÜ)
with st.sidebar:
    st.title("ARTIS v2.5")
    st.markdown("---")
    st.info("Washington DC Hub: **ONLINE** 🟢")
    
    if st.button("🗑️ Sohbeti Temizle", type="primary"):
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("---")
    st.caption("© 2026 Artificial Staff OS")

# 5. CHAT ARAYÜZÜ (ANA AKIŞ)

# Başlık
st.markdown("<h1 style='text-align: center; color: #ECECF1;'>ARTIS AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ACACBE;'>Global Operations Expert</p>", unsafe_allow_html=True)

# Mesajları Göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Yeni Mesaj Girişi
if prompt := st.chat_input("Bir şeyler yazın..."):
    # 1. Kullanıcı mesajını ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Asistan Cevabı (Streaming)
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Brain'den stream al
        stream_generator = brain.get_streaming_response(st.session_state.messages)
        
        for chunk in stream_generator:
            full_response += chunk
            response_placeholder.markdown(full_response + "▌") # İmleç efekti
            
        response_placeholder.markdown(full_response)
    
    # 3. Cevabı kaydet
    st.session_state.messages.append({"role": "assistant", "content": full_response})
