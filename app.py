import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff - Jarvis v2.5", page_icon="🤖")

# API Anahtarı Kontrolü
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Lütfen Secrets kısmına GOOGLE_API_KEY ekleyin!")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# LİSTEDE GÖRDÜĞÜMÜZ TAM MODEL İSMİ (2026 Standartı)
MODEL_NAME = 'models/gemini-2.5-flash'

with st.sidebar:
    st.header("🔧 Sistem Durumu")
    st.success(f"Aktif Model: {MODEL_NAME}")
    st.info("Not: Kota hatası alırsanız 30 saniye bekleyin.")

# Modeli Başlatma
try:
    model = genai.GenerativeModel(MODEL_NAME)
except Exception as e:
    st.error(f"Model yüklenemedi: {e}")

# Sohbet Hafızası (Kota dostu: Sadece son 10 mesajı saklar)
if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = "Merhaba! Ben Jarvis. 2026 operasyonlarınız için hazırım. Lojistik veya pazaryeri hakkında ne işlem yapalım?"
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Mesajları Ekrana Yazdır
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı Girişi
if prompt := st.chat_input("Jarvis v2.5'e talimat ver..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Jarvis'in Kimliği ve Yıl Bilgisi
        context = "Sen Jarvis'sin. Yıl 2026. Artificial Staff operasyon asistanısın. Kısa ve öz cevap ver. "
        
        try:
            # chat.send_message yerine doğrudan generate_content kullanarak kota tasarrufu yapıyoruz
            response = model.generate_content(context + prompt)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            if "429" in str(e):
                st.warning("⚠️ Ücretsiz kullanım kotanız doldu. Lütfen 1 dakika bekleyip tekrar deneyin veya farklı bir API Key kullanın.")
            else:
                st.error(f"Hata: {str(e)}")
