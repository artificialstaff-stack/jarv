# views.py
import streamlit as st
import time
from brain import get_ai_response
from instructions import COMPANY_DATA

# --- 1. AŞAMA: BİLGİ AL (JARVIS CHAT) ---
def render_step1_consulting():
    st.title("🧠 Jarvis Danışmanlık Hattı")
    st.info("ABD pazarında satış, şirket kurulumu ve lojistik hakkında her şeyi sorun.")

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": COMPANY_DATA}]
        st.session_state.messages.append({"role": "assistant", "content": "Jarvis Online. Amerika operasyonunuz için aklınızdaki soruları yanıtlamaya hazırım."})

    # Geçmişi Göster
    for msg in st.session_state.messages:
        if msg["role"] == "system": continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Yeni Soru
    if prompt := st.chat_input("Örn: Hangi eyalette şirket kurmalıyım?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Cevap Üret
        with st.chat_message("assistant"):
            with st.spinner("Veriler analiz ediliyor..."):
                response_text = get_ai_response(st.session_state.messages)
                st.markdown(response_text)
        
        st.session_state.messages.append({"role": "assistant", "content": response_text})

# --- 2. AŞAMA: İŞE BAŞLA (FORM) ---
def render_step2_action():
    st.title("🚀 Operasyonu Başlat")
    st.write("Strateji tamam. Şimdi şirketinizi resmiyete dökelim.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Şirket Kimliği")
        c_name = st.text_input("Şirket İsmi Seçeneği 1")
        c_name2 = st.text_input("Şirket İsmi Seçeneği 2")
        owner = st.text_input("Kurucu Ad Soyad")
    
    with col2:
        st.subheader("📦 Paket Seçimi")
        plan = st.radio("Hizmet Seviyesi", ["Standart ($1500) - 15 Gün", "Turbo ($2000) - 3 Gün ⚡"], index=0)
        sector = st.selectbox("Sektör", ["E-Ticaret", "Yazılım", "Lojistik", "Diğer"])

    st.markdown("---")
    
    if st.button("BAŞVURUYU GÖNDER VE SÜRECİ BAŞLAT"):
        if c_name and owner:
            # Veriyi "Veritabanına" (Session State) Kaydet
            st.session_state["active_order"] = {
                "company": c_name,
                "owner": owner,
                "plan": plan,
                "status": "Evraklar İnceleniyor",
                "progress": 10
            }
            st.success("✅ Başvuru alındı! 3. Aşamadan durumunuzu takip edebilirsiniz.")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Lütfen şirket ismi ve kurucu adını giriniz.")

# --- 3. AŞAMA: İZLEME (DASHBOARD) ---
def render_step3_tracking():
    st.title("📊 Operasyon Kontrol Merkezi")
    
    if "active_order" not in st.session_state:
        st.warning("⚠️ Henüz aktif bir şirket kurulum süreciniz yok. Lütfen '2. İŞE BAŞLA' sekmesinden başvuru yapın.")
        st.stop()
    
    data = st.session_state["active_order"]
    
    # Üst Bilgi Kartları
    c1, c2, c3 = st.columns(3)
    c1.metric("Şirket Adı", data["company"])
    c2.metric("Paket", "Turbo" if "Turbo" in data["plan"] else "Standart")
    c3.metric("Tahmini Bitiş", "3 Gün" if "Turbo" in data["plan"] else "15 Gün")
    
    st.markdown("---")
    st.subheader("Süreç Durumu")
    
    # İlerleme Çubuğu
    st.progress(data["progress"])
    st.info(f"📍 Güncel Durum: **{data['status']}**")
    
    st.markdown("### 📝 Yapılacaklar Listesi")
    st.checkbox("Başvuru Alındı", value=True, disabled=True)
    st.checkbox("Evrak Kontrolü", value=(data['progress'] > 20), disabled=True)
    st.checkbox("Eyalet Başvurusu (Filing)", value=False, disabled=True)
    st.checkbox("EIN Numarası", value=False, disabled=True)
    st.checkbox("Banka Hesabı Açılışı", value=False, disabled=True)
