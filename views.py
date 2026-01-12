import streamlit as st
import brain
import time

def render_navbar():
    st.markdown("""
        <div class="custom-navbar">
            <div class="nav-logo">ARTIS <span style="color:#D4AF37">STAFF</span></div>
            <div class="nav-links">
                OPERATIONS // ANALYTICS // NETWORK
            </div>
            <div class="nav-cta">
                STATUS: ONLINE
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 3rem;'>ARTIS ACCESS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666; font-family: Share Tech Mono;'>ENTER CREDENTIALS TO INITIALIZE KERNEL</p>", unsafe_allow_html=True)
        
        user = st.text_input("IDENTITY", placeholder="Username")
        password = st.text_input("KEY", placeholder="Password", type="password")
        
        if st.button("INITIALIZE SYSTEM"):
            if user == "admin" and password == "admin":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("ACCESS DENIED. INVALID CREDENTIALS.")

def render_checklist_item(title, subtitle, is_completed):
    """
    Sol taraftaki maddeleri çizen fonksiyon.
    """
    # Renkler
    border_color = "#D4AF37" if is_completed else "#333333" # Gold veya Koyu Gri
    bg_color = "rgba(212, 175, 55, 0.1)" if is_completed else "rgba(20,20,20,0.5)"
    icon = "✅ TAMAMLANDI" if is_completed else "⏳ BEKLİYOR"
    text_color = "#FFF" if is_completed else "#666"
    
    # Animasyonlu glow efekti
    glow = "box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);" if is_completed else ""

    html = f"""
    <div style="
        border: 1px solid {border_color};
        background-color: {bg_color};
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 12px;
        transition: all 0.5s ease;
        {glow}
    ">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; font-size:1rem; color:{text_color}; font-family:'Cinzel'">{title}</h3>
            <span style="font-family:'Share Tech Mono'; font-size:0.7rem; color:{border_color}">{icon}</span>
        </div>
        <p style="margin:5px 0 0 0; font-size:0.8rem; color:#888; font-family:'Inter'">{subtitle}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_command_center():
    """
    Yeni Ana Sayfa: Split Screen (Checklist + Chat)
    """
    st.markdown("<h1 style='font-size:3rem; margin-bottom:10px;'>OPERASYON MERKEZİ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#888; margin-bottom:30px;'>Yapay Zeka Asistanı ile kuruluş adımlarını tamamlayın.</p>", unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    # --- SOL SÜTUN: GÜNCELLENMİŞ CHECKLIST ---
    with col_left:
        st.markdown("### 📋 KURULUM ADIMLARI")
        
        status = st.session_state.checklist
        
        # 1. ADIM
        render_checklist_item(
            "1. MARKA & SEKTÖR ANALİZİ", 
            "Marka kimliği ve genel sektör tanımı.", 
            status.get('brand', False)
        )
        
        # 2. ADIM
        render_checklist_item(
            "2. ÜRÜN ENVANTERİ", 
            "Spesifik ürünler ve yıldız parçalar.", 
            status.get('product', False)
        )
        
        # 3. ADIM (GİZLİ VERİ TOPLAMA SONUCU)
        render_checklist_item(
            "3. MALİYET & LOJİSTİK VERİSİ", 
            "Washington DC depo planlaması ve boyut analizi.", 
            status.get('data', False)
        )
        
        # 4. ADIM
        render_checklist_item(
            "4. İŞ MODELİ SEÇİMİ", 
            "Ortaklık, Kurumsal veya Tam Paket onayı.", 
            status.get('offer', False)
        )

        if all(status.values()):
            st.markdown("""
            <div style="background:#D4AF37; color:black; padding:20px; border-radius:10px; text-align:center; font-weight:bold; margin-top:20px;">
                🚀 OPERASYON BAŞLATILIYOR...
            </div>
            """, unsafe_allow_html=True)

    # --- SAĞ SÜTUN: SOHBET (AI AGENT) ---
    with col_right:
        st.markdown("### 💬 ARTIS AI")
        
        # Sohbet için container
        chat_container = st.container(height=500)
        
        # Geçmişi göster
        for msg in st.session_state.onboarding_history:
            with chat_container.chat_message(msg["role"]):
                st.write(msg["content"])

        # Input
        if prompt := st.chat_input("Cevabınızı buraya yazın...", key="onboarding_input"):
            # Kullanıcı mesajını ekle
            st.session_state.onboarding_history.append({"role": "user", "content": prompt})
            with chat_container.chat_message("user"):
                st.write(prompt)

            # Beyni çalıştır
            onboarding_bot = brain.OnboardingBrain()
            bot_response, next_step, new_checklist = onboarding_bot.process_message(
                prompt, 
                st.session_state.onboarding_step, 
                st.session_state.checklist
            )

            # State güncelle
            st.session_state.onboarding_step = next_step
            st.session_state.checklist = new_checklist
            
            # Bot cevabını ekle
            st.session_state.onboarding_history.append({"role": "assistant", "content": bot_response})
            with chat_container.chat_message("assistant"):
                st.write(bot_response)
            
            # Ekranı yenile (Sol tarafın güncellenmesi için)
            time.sleep(0.5)
            st.rerun()

def render_dashboard():
    st.markdown("<h3>FINANSAL PANEL</h3>", unsafe_allow_html=True)
    
    # Top Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("TOTAL REVENUE", "$0.00", "Start")
    m2.metric("NET PROFIT", "$0.00", "Start")
    m3.metric("AD SPEND", "$0.00", "Start")
    m4.metric("ACTIVE SHIPMENTS", "0", "Ready")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("<p style='font-family: Share Tech Mono; color: #888;'>TAHMİNİ GELİR SİMÜLASYONU</p>", unsafe_allow_html=True)
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
    with c2:
        st.markdown("<p style='font-family: Share Tech Mono; color: #888;'>TEDARİK ZİNCİRİ</p>", unsafe_allow_html=True)
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

def render_chat_interface():
    st.markdown("<h3>GENEL ZEKA (ARTIS AI)</h3>", unsafe_allow_html=True)
    
    # Genel chat için ayrı history tutabiliriz veya aynı kalabilir.
    # Burada basitlik adına genel bir mesaj gösteriyoruz.
    st.info("Bu modül, kurulum tamamlandıktan sonra operasyonel sorularınız için aktif olacaktır.")
