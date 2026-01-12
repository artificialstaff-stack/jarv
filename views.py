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
    # (Eski kod ile aynı - yer kaplamasın diye kısalttım)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br><h1 style='text-align:center'>ARTIS ACCESS</h1>", unsafe_allow_html=True)
        user = st.text_input("IDENTITY", "admin")
        password = st.text_input("KEY", "admin", type="password")
        if st.button("INITIALIZE"):
            if user=="admin" and password=="admin":
                st.session_state['logged_in']=True
                st.rerun()

def render_hero():
    # Hero artık command center'ın içinde küçük başlık olarak kullanılıyor
    pass 

# --- YENİ CHEKLIST GÖRSELLEŞTİRME FONKSİYONU ---
def render_checklist_item(title, subtitle, is_completed):
    """
    Sol taraftaki maddeleri çizen fonksiyon.
    is_completed=True ise Yeşil/Altın yanar. False ise Sönük/Kırmızı kalır.
    """
    # Renkler
    border_color = "#00FF41" if is_completed else "#333333" # Neon Yeşil veya Koyu Gri
    bg_color = "rgba(0, 255, 65, 0.1)" if is_completed else "rgba(20,20,20,0.5)"
    icon = "✅ HAZIR" if is_completed else "⏳ BEKLİYOR"
    text_color = "#FFF" if is_completed else "#666"
    glow = "box-shadow: 0 0 15px rgba(0, 255, 65, 0.3);" if is_completed else ""

    html = f"""
    <div style="
        border: 1px solid {border_color};
        background-color: {bg_color};
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        transition: all 0.5s ease;
        {glow}
    ">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; font-size:1.1rem; color:{text_color}; font-family:'Cinzel'">{title}</h3>
            <span style="font-family:'Share Tech Mono'; font-size:0.8rem; color:{border_color}">{icon}</span>
        </div>
        <p style="margin:5px 0 0 0; font-size:0.8rem; color:#888; font-family:'Inter'">{subtitle}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_command_center():
    st.markdown("<h1 style='font-size:3rem; margin-bottom:10px;'>OPERASYON MERKEZİ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888; margin-bottom:30px;'>Yapay Zeka Asistanı ile kuruluş adımlarını tamamlayın.</p>", unsafe_allow_html=True)

    # EKRANI İKİYE BÖLÜYORUZ
    col_left, col_right = st.columns([1, 1], gap="large")

    # --- SOL SÜTUN: YAPILACAKLAR LİSTESİ ---
    with col_left:
        st.markdown("### 📋 KURULUM PROTOKOLÜ")
        
        # Session state'den durumları alıp çizdiriyoruz
        status = st.session_state.checklist
        
        render_checklist_item(
            "1. KURUMSAL KİMLİK", 
            "Marka analizi ve veritabanı kaydı.", 
            status['profile']
        )
        
        render_checklist_item(
            "2. YASAL ALTYAPI (LLC)", 
            "ABD Şirket kurulumu ve EIN Vergi numarası.", 
            status['legal']
        )
        
        render_checklist_item(
            "3. LOJİSTİK AĞI", 
            "Fulfillment ve Gümrük operasyon entegrasyonu.", 
            status['logistics']
        )
        
        render_checklist_item(
            "4. PAZAR GİRİŞİ", 
            "Reklam bütçesi ve hedef kitle tanımlaması.", 
            status['marketing']
        )

        # Eğer hepsi tamamsa büyük bir onay kutusu göster
        if all(status.values()):
            st.markdown("""
            <div style="background:#D4AF37; color:black; padding:20px; border-radius:10px; text-align:center; font-weight:bold; margin-top:20px;">
                🚀 SİSTEM TAMAMEN HAZIR. SATIŞA BAŞLAYABİLİRSİNİZ.
            </div>
            """, unsafe_allow_html=True)

    # --- SAĞ SÜTUN: AI SOHBET ---
    with col_right:
        st.markdown("### 💬 ASİSTAN ARAYÜZÜ")
        
        # Sohbet Geçmişi Konteynerı
        chat_container = st.container(height=400)
        
        # Geçmiş mesajları yazdır
        for msg in st.session_state.onboarding_history:
            with chat_container.chat_message(msg["role"]):
                st.write(msg["content"])

        # Yeni Giriş
        if prompt := st.chat_input("Cevabınızı buraya yazın...", key="onboarding_input"):
            # 1. Kullanıcı mesajını ekle
            st.session_state.onboarding_history.append({"role": "user", "content": prompt})
            with chat_container.chat_message("user"):
                st.write(prompt)

            # 2. Beyni çalıştır (Cevabı ve yeni durumu al)
            onboarding_bot = brain.OnboardingBrain()
            bot_response, next_step, new_checklist = onboarding_bot.process_message(
                prompt, 
                st.session_state.onboarding_step, 
                st.session_state.checklist
            )

            # 3. State güncelle
            st.session_state.onboarding_step = next_step
            st.session_state.checklist = new_checklist
            
            # 4. Bot cevabını ekle
            st.session_state.onboarding_history.append({"role": "assistant", "content": bot_response})
            with chat_container.chat_message("assistant"):
                st.write(bot_response)
            
            # 5. Sol tarafı güncellemek için sayfayı yenile
            time.sleep(0.5)
            st.rerun()

# Diğer fonksiyonlar (Dashboard, Chat Interface vb.) aynen kalıyor...
def render_dashboard():
    # (Mevcut kodunuzdaki dashboard içeriği)
    st.markdown("<h3>FINANSAL PANEL</h3>", unsafe_allow_html=True)
    st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

def render_chat_interface():
    st.markdown("<h3>GENEL ZEKA (ARTIS AI)</h3>", unsafe_allow_html=True)
    # (Genel chat kodlarınız)
