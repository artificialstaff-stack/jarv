import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Artificial Staff - Jarvis (2026 Edition)", page_icon="🤖")

# API Anahtarı Kontrolü
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Lütfen Secrets kısmına GOOGLE_API_KEY ekleyin!")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# --- 2026 MODEL SEÇİMİ ---
# Senin belirttiğin sürümü hedefliyoruz
MODEL_NAME = 'gemini-2.5-flash'

# Yan Menü (Sidebar): Mevcut Modelleri Kontrol Etme Paneli
with st.sidebar:
    st.header("🔧 Sistem Durumu")
    st.write(f"Hedeflenen Model: `{MODEL_NAME}`")
    
    # 2026'da hangi modellerin aktif olduğunu listeleme
    try:
        st.write("📡 Aktif Modeller Listeleniyor...")
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
                st.code(m.name) # Mevcut modelleri buraya yazdırır
    except Exception as e:
        st.error(f"Model listesi alınamadı: {e}")

# Modeli Başlatma
try:
    model = genai.GenerativeModel(MODEL_NAME)
except:
    # Eğer 2.5-flash bulunamazsa, listedeki ilk uygun modeli seçmeye çalış (Fallback)
    st.warning(f"{MODEL_NAME} bulunamadı, alternatif aranıyor...")
    model = genai.GenerativeModel('models/gemini-2.0-flash-exp') # Yedek

# Sohbet Başlatma
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []
    intro = ("Sistem Tarihi: 11 Ocak 2026\n"
             "Merhaba! Ben **Jarvis v2.5**. Artificial Staff operasyonel zekasıyım. "
             "Amerika pazarındaki operasyonlarınızı yönetmek için hazırım. Başlayalım mı?")
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Mesajları Göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı Girişi
if prompt := st.chat_input("Jarvis (v2.5) ile konuşun..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        context = "Sen Jarvis'sin. Yıl 2026. Artificial Staff şirketinin gelişmiş yapay zeka asistanısın. Profesyonel, vizyoner ve çözüm odaklısın. "
        try:
            response = st.session_state.chat.send_message(context + prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Hata oluştu: {str(e)}")
