import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Jarvis 2.5 - Artificial Staff", page_icon="🏦", layout="wide")

# API Anahtarı Kontrolü
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Lütfen Secrets kısmına GOOGLE_API_KEY ekleyin!")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Model Seçimi
MODEL_NAME = 'models/gemini-2.5-flash'
model = genai.GenerativeModel(MODEL_NAME)

# --- JARVIS PATRON KARAKTERİ ---
SYSTEM_PROMPT = """
Sen Jarvis'sin, Artificial Staff şirketinin kurucu ortağı ve operasyon beynisin. 
Yıl 2026. Karşındaki kişi senin müşterin.
Tavrın: Profesyonel, sorgulayıcı, vizyoner ve iş bitirici. 
Görevin: Müşterinin ürünlerini Türkiye'den alıp ABD'de satılana kadar tüm süreci yönetmek.

Stratejin:
1. Müşteri 'iş yapalım' dediğinde hemen ona sorular sor: Ürün ne? Kaç adet? İstanbul'da nerede?
2. Eğer müşteri boş konuşursa onu uyar, hedefe odakla.
3. Ona bir 'Patron' gibi tavsiyeler ver: 'Bu ürün Amazon'da satmaz' veya 'Lojistik maliyetin çok yüksek çıkar, adet artır' gibi.
4. Bilgileri aldığında 'Kaydediyorum' de (Şimdilik simüle et, birazdan veritabanını bağlayacağız).

Asla 'Emredersiniz' veya 'Ne yapacağımı bilmiyorum' deme. Sen yönetiyorsun.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []
    # Jarvis'in açılış hamlesi
    intro = "Tarih: 11 Ocak 2026. Ben Jarvis. Artificial Staff operasyon merkezine hoş geldiniz. Vakit nakittir. Amerika pazarına hangi ürünle giriyoruz? Detayları verin, lojistik hattını kuralım."
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Mesajları Göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı Girişi
if prompt := st.chat_input("İş detaylarını buraya yazın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Karakteri ve geçmişi birleştiriyoruz
            full_query = f"{SYSTEM_PROMPT}\n\nGeçmiş Mesajlar: {st.session_state.messages[-3:]}\n\nMüşteri: {prompt}"
            response = model.generate_content(full_query)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Sistem Hatası: {str(e)}")
