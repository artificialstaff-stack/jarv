import streamlit as st
import time

# Sayfa tasarımı
st.set_page_config(page_title="Artificial Staff - Jarvis", page_icon="🤖")

# CSS ile Jarvis havası katalım (Opsiyonel: Koyu tema ve güzel fontlar)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
    # Jarvis'in Karşılaması
    jarvis_intro = (
        "Sisteme hoş geldiniz. Ben **Jarvis**, Artificial Staff operasyonel zekasıyım. "
        "Türkiye'deki operasyonunuzu Amerika pazarına taşımak, lojistik süreçlerinizi yönetmek "
        "ve envanterinizi otonom olarak takip etmek için buradayım.\n\n"
        "**Amerika pazarına açılmaya hazır mısınız?**"
    )
    st.session_state.messages.append({"role": "assistant", "content": jarvis_intro})

# Mesajları göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Müşteri girişi
if prompt := st.chat_input("Jarvis ile konuşun..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if "evet" in prompt.lower() or "hazırım" in prompt.lower():
            response = (
                "Mükemmel bir karar! Başarı yolculuğunuz başlıyor. 🚀\n\n"
                "Süreci hemen başlatabilmem için bana birkaç detay vermeniz gerekiyor:\n"
                "1. Hangi tür ürünler satmayı planlıyorsunuz? (Örn: Tekstil, Ev Gereçleri)\n"
                "2. İlk etapta tahmini kaç adet ürün yollayacaksınız?\n"
                "3. Ürünler İstanbul'da hangi bölgeden teslim alınacak?"
            )
        else:
            response = "Anlaşıldı. Hazır olduğunuzda 'hazırım' demeniz yeterli, sizi bekliyor olacağım."
        
        # Yazıyor efekti
        placeholder = st.empty()
        full_res = ""
        for chunk in response.split():
            full_res += chunk + " "
            time.sleep(0.05)
            placeholder.markdown(full_res + "▌")
        placeholder.markdown(full_res)
    
    st.session_state.messages.append({"role": "assistant", "content": full_res})
