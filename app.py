import streamlit as st
import time
from instructions import COMPANY_DATA

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Jarvis Neural Interface",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STİLİ (Basit haliyle) ---
st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: white; }
    .stTextInput > div > div > input { background-color: #262730; color: white; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (YAN MENÜ) ---
with st.sidebar:
    st.markdown("### ARTIFICIAL STAFF v4.0")
    st.markdown("---")
    
    # Menü Seçimi
    selected_tab = st.radio(
        "MODÜLLER",
        ["🔴 JARVIS CORE", "📦 GLOBAL ENVANTER", "💰 FİNANSAL ANALİZ", "📈 STRATEJİ"]
    )
    
    st.markdown("---")
    
    # Sistem Durumu Paneli (Görseldeki gibi)
    st.markdown("SİSTEM DURUMU")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="CPU", value="12%", delta="-1%")
    with col2:
        st.metric(label="RAM", value="4.2GB", delta="+0.2")
        
    st.success("🟢 BAĞLANTI: GÜVENLİ (SSL)")
    st.info("📍 KONUM: US-EAST-1")

# --- ANA EKRAN MANTIĞI ---

# 1. JARVIS CORE EKRANI
if selected_tab == "🔴 JARVIS CORE":
    st.title("Jarvis Neural Interface")
    
    # OpenAI Client Kurulumu (Eğer varsa burayı aktif edin)
    # import openai
    # client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # --- SOHBET GEÇMİŞİNİ BAŞLAT ---
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
        # GİZLİ TALİMAT (SİSTEM MESAJI) - Ekranda görünmez, beyne işlenir
        st.session_state.messages.append({
            "role": "system",
            "content": COMPANY_DATA
        })
        
        # AÇILIŞ MESAJI - Ekranda görünür
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Jarvis v4.2 Aktif. Neural arayüze hoş geldiniz. Markanızı tanımlayın."
        })

    # --- MESAJLARI EKRANA BASMA (FİLTRELİ) ---
    for message in st.session_state.messages:
        # EĞER ROL 'SYSTEM' İSE EKRANA BASMA, ATLA!
        if message["role"] == "system":
            continue
            
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --- KULLANICI GİRDİSİ ---
    if prompt := st.chat_input("Talimat verin..."):
        # 1. Kullanıcı mesajını ekrana bas
        with st.chat_message("user"):
            st.markdown(prompt)
        # 2. Geçmişe ekle
        st.session_state.messages.append({"role": "user", "content": prompt})

        # --- YANIT ÜRETME KISMI ---
        # Buraya OpenAI kodunuzu entegre etmelisiniz.
        # Örnek bir şablon bırakıyorum:
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # --- API ÇAĞRISI (Eğer OpenAI kullanıyorsanız aşağıdaki bloğu açın) ---
            # stream = client.chat.completions.create(
            #     model="gpt-4",
            #     messages=st.session_state.messages, # System mesajı dahil tüm geçmiş gidiyor
            #     stream=True,
            # )
            # for chunk in stream:
            #     if chunk.choices[0].delta.content is not None:
            #         full_response += chunk.choices[0].delta.content
            #         message_placeholder.markdown(full_response + "▌")
            
            # --- (Geçici Simülasyon - API Bağlı Değilse Bu Çalışır) ---
            simulated_response = "Bağlantı simülasyonu: Mesajınız alındı. (API Key entegrasyonunu kontrol edin)."
            for chunk in simulated_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            # -----------------------------------------------------------

            message_placeholder.markdown(full_response)
        
        # Asistan cevabını geçmişe ekle
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# 2. DİĞER EKRANLAR (Hata vermemesi için boş şablonlar)
elif selected_tab == "📦 GLOBAL ENVANTER":
    st.title("Global Envanter Yönetimi")
    st.info("Bu modül şu anda bakım aşamasındadır.")

elif selected_tab == "💰 FİNANSAL ANALİZ":
    st.title("Finansal Analiz Modülü")
    st.line_chart([1, 5, 2, 6, 2, 1]) # Örnek grafik

elif selected_tab == "📈 STRATEJİ":
    st.title("Stratejik Planlama")
    st.write("Hedef pazar verileri yükleniyor...")
