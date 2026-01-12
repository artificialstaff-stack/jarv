import streamlit as st
from ui import apply_luxury_theme, render_sidebar
from brain import get_jarvis_response

apply_luxury_theme()
selected_tab = render_sidebar()

# --- 1. SEKME: JARVIS AI (SOHBET) ---
if selected_tab == "🤖 Jarvis AI":
    st.markdown("<h2 style='color:#B89B5E;'>Operasyonel Zeka: Jarvis</h2>", unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hoş geldiniz. Amerika operasyonunuz için sistemler hazır. Kiminle tanışıyorum?"}]

    # Mesaj geçmişini göster
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Jarvis'e talimat verin..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

# --- 2. SEKME: ENVANTER ---
elif selected_tab == "📦 Envanter Takip":
    st.header("Envanter Yönetimi")
    st.info("Henüz ürün girişi yapılmadı. Jarvis üzerinden ürünlerinizi tanımlayabilirsiniz.")

# --- 3. SEKME: LOJİSTİK ---
elif selected_tab == "🚢 Lojistik Durumu":
    st.header("Global Sevkiyat Hattı")
    st.markdown("""
    <div class="premium-card">
        <h4>Aktif Sevkiyat: Yok</h4>
        <p>Türkiye -> ABD hattını başlatmak için Jarvis'e 'Turbo Akış' onayı verin.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 4. SEKME: MUHASEBE ---
elif selected_tab == "💰 Muhasebe & Vergi":
    st.header("Finansal Raporlar")
    col1, col2 = st.columns(2)
    col1.metric("Toplam Ciro", "0.00 $", "0%")
    col2.metric("LLC Giderleri", "1500 $", "Sabit")

# --- 5. SEKME: STRATEJİ ---
elif selected_tab == "📈 Strateji Geliştirme":
    st.header("Gelişim Önerileri")
    st.write("Markanızın Amerika'daki pazar payını artırmak için Jarvis analiz yapıyor...")

# AI Cevap Motoru (Sadece Jarvis sekmesindeyse çalışır)
if selected_tab == "🤖 Jarvis AI" and len(st.session_state.messages) > 0 and st.session_state.messages[-1]["role"] == "user":
    response = get_jarvis_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
