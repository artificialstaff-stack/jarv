import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff - Jarvis", page_icon="🤖")

# Secrets kontrolü
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Lütfen Secrets kısmına GOOGLE_API_KEY ekleyin!")
    st.stop()

# API Yapılandırması
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# HATAYI ÇÖZEN KRİTİK DEĞİŞİKLİK: 
# Eğer 1.5-flash hata veriyorsa 'gemini-pro' en stabil çalışan alternatiftir.
MODEL_NAME = 'gemini-1.5-flash' 

try:
    model = genai.GenerativeModel(MODEL_NAME)
except Exception:
    model = genai.GenerativeModel('gemini-pro')

# Sohbet hafızasını başlat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []
    intro = ("Merhaba! Ben **Jarvis**, Artificial Staff operasyonel zekasıyım. "
             "Türkiye'deki ürünlerinizi Amerika pazarına taşımak için buradayım. "
             "Hazırsanız başlayalım mı?")
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Mesajları ekrana çiz
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı girişi
if prompt := st.chat_input("Jarvis ile konuşun..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Jarvis'in kimlik tanımı
        context = "Sen Jarvis'sin, Artificial Staff şirketinin zeki asistanısın. Kısa, profesyonel ve çözüm odaklı cevaplar ver. "
        
        try:
            # Model yanıtı üret
            response = st.session_state.chat.send_message(context + prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # Eğer hala model bulunamadı hatası alırsak alternatif modele geçiş uyarısı
            st.error(f"Jarvis bir bağlantı hatası aldı. Lütfen tekrar deneyin. (Hata: {str(e)})")
