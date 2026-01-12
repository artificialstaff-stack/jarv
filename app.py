import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff - Jarvis", page_icon="🤖")

# API Anahtarını Streamlit Secrets'dan çekiyoruz
# (Streamlit panelinde Settings > Secrets kısmına GOOGLE_API_KEY eklemelisin)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
except:
    st.error("Lütfen Google API Key'i ayarlara ekleyin.")

# Jarvis'in Karakter Tanımı (System Prompt)
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    # Jarvis'e kim olduğunu öğretiyoruz
    st.session_state.messages = []
    intro_text = ("Merhaba! Ben **Jarvis**, Artificial Staff'in operasyonel zekasıyım. "
                  "Türkiye'deki işinizi Amerika'ya taşımak için buradayım. "
                  "Lojistik, depo ve satış süreçlerinizi birlikte yöneteceğiz. "
                  "Hazırsanız başlayalım mı?")
    st.session_state.messages.append({"role": "assistant", "content": intro_text})

# Sohbeti Ekrana Yazdır
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Müşteri Yazdığında
if prompt := st.chat_input("Jarvis'e bir şey sorun..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Jarvis'in Düşünme Süreci
    with st.chat_message("assistant"):
        # Jarvis'e arka planda kim olduğunu hatırlatıyoruz ki karakterden çıkmasın
        full_prompt = f"Sen Jarvis'sin, Artificial Staff operasyon asistanısın. Müşterinin şu mesajına bir iş ortağı gibi mantıklı ve samimi cevap ver: {prompt}"
        
        response = st.session_state.chat.send_message(full_prompt)
        st.markdown(response.text)
        
    st.session_state.messages.append({"role": "assistant", "content": response.text})
