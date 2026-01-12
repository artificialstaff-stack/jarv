import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff - Jarvis", page_icon="🤖")

# API Anahtarını Secrets'tan güvenli bir şekilde çekiyoruz
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Lütfen Streamlit Secrets kısmına GOOGLE_API_KEY ekleyin!")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Model seçimi (Güncel ve hızlı sürüm)
model = genai.GenerativeModel('gemini-1.5-flash')

# Sohbet hafızasını başlat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []
    # Jarvis'in Karşılaması
    intro = ("Merhaba! Ben **Jarvis**, Artificial Staff operasyonel zekasıyım. "
             "Türkiye'deki ürünlerinizi Amerika pazarına taşımak için buradayım. "
             "Lojistikten satışa kadar her adımda yanınızdayım. Hazırsanız başlayalım mı?")
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Mesajları ekrana çiz
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı girişi
if prompt := st.chat_input("Jarvis ile konuşun..."):
    # Kullanıcı mesajını ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Jarvis'in yanıt üretme süreci
    with st.chat_message("assistant"):
        # Karakter ve iş akışı talimatı (System Instruction gibi çalışır)
        context = (
            "Sen Jarvis'sin. Artificial Staff'in beynisin. "
            "Müşteriye Türkiye'den ABD'ye mal gönderme, depo (ev deposu), "
            "Amazon/Etsy satışları ve muhasebe konularında rehberlik ediyorsun. "
            "Samimi, profesyonel ve zeki bir iş ortağı gibi davran. "
            "Müşterinin sorusu: "
        )
        
        try:
            # Yanıtı oluştur
            response = st.session_state.chat.send_message(context + prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Jarvis bir hata ile karşılaştı: {str(e)}")
