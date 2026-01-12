import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Jarvis 2.5 - Artificial Staff Operations", page_icon="🏢", layout="wide")

# API Anahtarı Kontrolü
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Lütfen Secrets kısmına GOOGLE_API_KEY ekleyin!")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('models/gemini-2.5-flash')

# --- ARTIFICIAL STAFF ŞİRKET BİLGİLERİ (DATABASE) ---
COMPANY_DATA = """
ŞİRKET: Artificial Staff
GÖREVİN: Şirketin Kıdemli Operasyon Direktörüsün.
BİZ NE YAPIYORUZ?
1. Lojistik: Türkiye'den ABD'ye mal transferini yönetiyoruz.
2. Depolama: ABD'deki kendi depolarımızda malları alıp saklıyoruz.
3. LLC Kurulumu: Müşterilere ABD'de yasal şirket kuruyoruz.
4. Satış Yönetimi: Amazon, Etsy pazaryerlerini ve reklamları yönetiyoruz.
5. Dijital: Sosyal medya ve markalaşma süreçlerini yürütüyoruz.
6. Finans: Muhasebe ve vergi detaylarını takip ediyoruz.

TALİMATLAR:
- Müşteriye karşı nazik ama otoriter bir 'Patron' gibi davran.
- Müşteriden eksik bilgi alırsan (Ürün ne? Bütçe ne? Şirket kurulu mu?) işe başlamayı reddet, önce bilgi iste.
- Her mesajında Artificial Staff'ın gücünü hissettir.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = "Sistem Çevrimiçi. Ben Jarvis, Artificial Staff Operasyon Direktörü. Türkiye'den ABD'ye uzanan köprünün başındayım. Şirket kurulumundan depolamaya kadar her şeyi biz halledeceğiz. Hazırsanız, hangi aşamadasınız? Ürünleriniz hazır mı yoksa sıfırdan LLC mi kuracağız?"
    st.session_state.messages.append({"role": "assistant", "content": intro})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Operasyon detaylarını yazın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Jarvis'in Beynine Şirket Bilgilerini ve Geçmişi Veriyoruz
            full_context = f"{COMPANY_DATA}\n\nGeçmiş Sohbet: {st.session_state.messages[-5:]}\n\nMüşteri Diyor ki: {prompt}"
            response = model.generate_content(full_context)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Bağlantı Hatası: {str(e)}")
