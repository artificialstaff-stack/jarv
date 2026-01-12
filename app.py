import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff - Jarvis", page_icon="🤖")

# Secrets kontrolü
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Lütfen Secrets kısmına GOOGLE_API_KEY ekleyin!")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# SENİN İSTEDİĞİN MODEL (Ekran görüntüsündeki en yeni sürüm)
# Eğer 2.0 hata verirse 1.5'i deneyecek akıllı bir yapı kurdum.
try:
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
except:
    model = genai.GenerativeModel('gemini-1.5-flash')

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
        context = "Sen Jarvis'sin. Artificial Staff şirketinin zeki asistanısın. Kısa, net ve çözüm odaklı cevap ver. "
        
        try:
            response = st.session_state.chat.send_message(context + prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Hata: {str(e)}. Lütfen sayfayı yenileyin.")
