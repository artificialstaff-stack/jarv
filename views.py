import streamlit as st
import brain
import time

def render_navbar():
    st.markdown("""
        <div class="custom-navbar">
            <div class="nav-logo">ARTIS <span style="color:#D4AF37">STAFF</span></div>
            <div class="nav-links">OPERATIONS // ANALYTICS // NETWORK</div>
            <div class="nav-cta">STATUS: ONLINE</div>
        </div>
    """, unsafe_allow_html=True)

def render_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 3rem;'>ARTIS ACCESS</h1>", unsafe_allow_html=True)
        user = st.text_input("IDENTITY", placeholder="Username")
        password = st.text_input("KEY", placeholder="Password", type="password")
        if st.button("INITIALIZE SYSTEM"):
            if user == "admin" and password == "admin":
                st.session_state['logged_in'] = True
                st.rerun()

def render_command_center():
    st.markdown("<h1 style='font-size:3rem; margin-bottom:10px;'>OPERASYON MERKEZİ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888; margin-bottom:30px;'>Lütfen sol taraftaki adımları tamamlayın. ARTIS size eşlik edecektir.</p>", unsafe_allow_html=True)

    col_form, col_chat = st.columns([1.2, 0.8], gap="large")

    # --- SOL: ADIM ADIM FORM (ACCORDION) ---
    with col_form:
        
        # 1. MARKA & SEKTÖR
        with st.expander("1. MARKA VE SEKTÖR BİLGİLERİ", expanded=True):
            st.session_state.form_data['brand_name'] = st.text_input("Marka Adınız", value=st.session_state.form_data.get('brand_name', ''))
            st.session_state.form_data['sector'] = st.selectbox("Sektör", ["Tekstil", "Gıda", "Kozmetik", "Mobilya", "Diğer"], index=0)
            
            if st.button("Kaydet ve Devam Et", key="btn1"):
                st.toast("Marka bilgileri kaydedildi.", icon="✅")
                # Yapay Zekaya tetikleyici mesaj gönder (Görünmez)
                handle_ai_trigger("Marka adımı girdim: " + st.session_state.form_data['brand_name'], "MARKA GİRİŞİ")

        # 2. ÜRÜN DETAYLARI
        with st.expander("2. ÜRÜN VE ENVANTER", expanded=False):
            st.session_state.form_data['star_product'] = st.text_input("Yıldız Ürününüz (Örn: İpek Eşarp)", value=st.session_state.form_data.get('star_product', ''))
            st.session_state.form_data['dimensions'] = st.text_input("Tahmini Koli Boyutları / Ağırlık", placeholder="Örn: 40x40x60cm, 10kg", value=st.session_state.form_data.get('dimensions', ''))
            
            if st.button("Envanteri İşle", key="btn2"):
                st.toast("Ürün verileri işlendi.", icon="📦")
                handle_ai_trigger("Ürünlerimi girdim: " + st.session_state.form_data['star_product'], "ÜRÜN GİRİŞİ")

        # 3. PAKET SEÇİMİ
        with st.expander("3. ÇALIŞMA MODELİ VE PAKET", expanded=False):
            st.info("Washington DC depomuz ve operasyon ekibimiz için size uygun modeli seçin.")
            package = st.radio("Paket Seçimi", [
                "ORTAKLIK (Sadece Kargo Öde, Kârdan Paylaş)",
                "KURUMSAL ($2000 Kurulum + $250/ay Yönetim)",
                "VIP TAM OTOMASYON ($2000 Kurulum + $500/ay Full Servis)",
                "WEB BAŞLANGIÇ ($500 Web Sitesi)"
            ])
            st.session_state.form_data['selected_package'] = package
            
            if st.button("Paketi Onayla", key="btn3"):
                st.toast("Paket seçimi doğrulandı.", icon="🤝")
                handle_ai_trigger("Paketimi seçtim: " + package, "PAKET SEÇİMİ")

        # 4. GÖNDER VE BİTİR
        st.markdown("---")
        if st.button("🚀 BAŞVURUYU TAMAMLA VE GÖNDER", type="primary"):
            report = brain.generate_final_report(st.session_state.form_data)
            st.session_state['final_report'] = report
            st.session_state['submission_complete'] = True
            st.rerun()

    # --- SAĞ: AI ASİSTAN (COPILOT) ---
    with col_chat:
        st.markdown("### 💬 ARTIS COPILOT")
        
        chat_container = st.container(height=500)
        for msg in st.session_state.chat_history:
            with chat_container.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("Bir soru sorun veya danışın..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with chat_container.chat_message("user"):
                st.write(prompt)
            
            # AI Cevap
            bot = brain.OnboardingBrain()
            # O an hangi input açıksa ona göre context verilebilir, şimdilik genel.
            response = bot.process_message(prompt, "GENEL YARDIM")
            
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            with chat_container.chat_message("assistant"):
                st.write(response)

# Yardımcı Fonksiyon: Butonlara basınca AI'ın otomatik yorum yapması için
def handle_ai_trigger(user_msg, context):
    st.session_state.chat_history.append({"role": "user", "content": user_msg})
    bot = brain.OnboardingBrain()
    response = bot.process_message(user_msg, context)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    # Sayfayı yenilemeye gerek yok, chat bir sonraki etkileşimde güncellenir veya anlık görünmesi için rerun yapılabilir.
    # st.rerun()

def render_dashboard():
    # ... (Mevcut kodlar)
    st.markdown("<h3>FINANSAL PANEL</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1: st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
    with c2: st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

def render_chat_interface():
    # ...
    st.info("Bu modül kurulumdan sonra aktifleşir.")
