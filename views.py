import streamlit as st
import time
from brain import get_dashboard_metrics, get_sales_chart, get_map_chart, get_marketing_chart, get_artis_response

# --- HEADER FONKSİYONU ---
def render_header(title, subtitle):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### {title}")
        st.caption(subtitle)
    with col2:
        st.markdown("<div style='text-align:right; color:#D4AF37; font-size:12px;'>● SYSTEM ONLINE</div>", unsafe_allow_html=True)
    st.markdown("---")

# --- 1. LOGIN EKRANI ---
def render_login_screen():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center; color:#D4AF37; font-family:Cinzel; font-size:60px; margin-bottom:0;'>AS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#666; letter-spacing:4px; font-size:12px;'>ENTERPRISE SYSTEM</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("Kullanıcı Adı", placeholder="admin")
            password = st.text_input("Şifre", type="password", placeholder="••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("SİSTEME GİRİŞ YAP")
            
            if submit:
                if username == "admin" and password == "admin":
                    st.session_state.authenticated = True
                    st.session_state.show_welcome = True
                    st.rerun()
                else:
                    st.error("Erişim Reddedildi. Bilgileri kontrol edin.")

# --- 2. KARŞILAMA ANİMASYONU (SAMİMİ) ---
def render_welcome_animation():
    placeholder = st.empty()
    
    # Samimi ve profesyonel mesajlar
    messages = [
        "Sisteme hoş geldiniz...",
        "Artificial Staff, yerel sınırları kaldırmak için tasarlandı.",
        "Siz üretiminize odaklanın, global operasyonu bize bırakın.",
        "Panel hazırlanıyor..."
    ]
    
    with placeholder.container():
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        for msg in messages:
            # Yazı efekti
            text_area = st.empty()
            full_text = ""
            for char in msg:
                full_text += char
                text_area.markdown(f"<div class='welcome-text'>{full_text}</div>", unsafe_allow_html=True)
                time.sleep(0.03) # Yazma hızı
            time.sleep(1.5) # Bekleme süresi
            text_area.empty()
            
    st.session_state.show_welcome = False
    st.rerun()

# --- 3. HİZMET KATALOĞU (ANA MERKEZ) ---
def render_services_catalog():
    render_header("Hizmetler & Çözümler", "Artificial Staff Enterprise Ekosistemi")
    
    st.info("Global bir marka olmanız için gereken 9 temel yapı taşı.")

    # Hizmet Verileri
    services = [
        ("💻", "Web & Teknoloji", "ABD odaklı, yüksek dönüşümlü e-ticaret altyapısı."),
        ("🏛️", "LLC Kurulumu", "Delaware şirket, EIN ve Banka hesabı."),
        ("✈️", "Lojistik & Gümrük", "Kapıdan kapıya 2-4 günde teslimat."),
        ("🏭", "3PL Depolama", "NJ ve CA eyaletlerinde stratejik depolar."),
        ("🛒", "Pazaryeri Yönetimi", "Amazon, Etsy, Walmart hesap yönetimi."),
        ("📱", "Sosyal Medya", "Global marka algısı ve Influencer yönetimi."),
        ("📢", "Reklam (Ads)", "Yüksek ROAS hedefli Meta/Google reklamları."),
        ("🤖", "Otomasyon", "Sipariş ve fatura süreçlerinde sıfır hata."),
        ("🤝", "B2B AI Satış", "Yapay zeka ile toptan müşteri bulma.")
    ]

    # Grid Yapısı (3'lü Kartlar)
    for i in range(0, len(services), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(services):
                icon, title, desc = services[i+j]
                with cols[j]:
                    # Styles.py'daki 'hub-card' sınıfını kullanıyoruz
                    st.markdown(f"""
                    <div class="hub-card" style="height:200px; padding:20px;">
                        <div style="font-size:30px; margin-bottom:10px;">{icon}</div>
                        <h4 style="color:#fff; margin:0; font-family:'Cinzel', serif; font-size:16px;">{title}</h4>
                        <p style="color:#888; font-size:12px; margin-top:10px;">{desc}</p>
                    </div>
                    """, unsafe_allow_html=True)
        st.write("") # Boşluk

# --- 4. DASHBOARD ---
def render_dashboard():
    render_header("Global Operasyon Merkezi", "Anlık Veri Akışı")
    
    metrics = get_dashboard_metrics()
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric(metrics["revenue"]["label"], metrics["revenue"]["value"], metrics["revenue"]["delta"])
    with c2: st.metric(metrics["region"]["label"], metrics["region"]["value"], metrics["region"]["delta"])
    with c3: st.metric(metrics["visitors"]["label"], metrics["visitors"]["value"], metrics["visitors"]["delta"])
    with c4: st.metric(metrics["conversion"]["label"], metrics["conversion"]["value"], metrics["conversion"]["delta"])

    st.markdown("### 📈 Büyüme Projeksiyonu")
    # Log uyarısını düzeltmek için width="stretch" kullanıldı
    st.plotly_chart(get_sales_chart(), width="stretch")

# --- 5. ARTIS AI ---
def render_artis_ai():
    render_header("ARTIS AI", "Yapay Zeka Operasyon Asistanı")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Merhaba! Ben ARTIS. Global operasyonlarınız için buradayım."}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Sorunuzu yazın (Örn: Lojistik süresi nedir?)..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        response = get_artis_response(prompt)
        time.sleep(0.5)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

# --- 6. LOJİSTİK & PAZARLAMA ---
def render_logistics():
    render_header("Lojistik Ağı", "Canlı Takip")
    c1, c2 = st.columns([3, 1])
    with c1: st.plotly_chart(get_map_chart(), width="stretch")
    with c2: 
        st.info("📦 **TR-8821**: İstanbul -> NY (Gümrükte)")
        st.success("✅ **EU-1029**: İstanbul -> Berlin (Teslim Edildi)")

def render_marketing():
    render_header("Pazarlama 360°", "Kanal Performansı")
    c1, c2 = st.columns(2)
    with c1: st.plotly_chart(get_marketing_chart(), width="stretch")
    with c2:
        st.metric("Google ROAS", "4.2x", "+0.3x")
        st.metric("Meta ROAS", "3.1x", "-0.1x")
