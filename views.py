import streamlit as st
import time
from brain import get_dashboard_metrics, get_sales_chart, get_map_chart, get_marketing_chart, get_artis_response

# --- YARDIMCI: BAŞLIK ---
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
                    st.error("Erişim Reddedildi.")

# --- 2. KARŞILAMA ANİMASYONU ---
def render_welcome_animation():
    placeholder = st.empty()
    messages = [
        "Sisteme hoş geldiniz...",
        "Artificial Staff, yerel sınırları kaldırmak için tasarlandı.",
        "Siz üretiminize odaklanın, global operasyonu bize bırakın.",
        "Panel hazırlanıyor..."
    ]
    with placeholder.container():
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        for msg in messages:
            text_area = st.empty()
            full_text = ""
            for char in msg:
                full_text += char
                text_area.markdown(f"<div class='welcome-text'>{full_text}</div>", unsafe_allow_html=True)
                time.sleep(0.03)
            time.sleep(1.5)
            text_area.empty()
            
    st.session_state.show_welcome = False
    st.rerun()

# --- 3. ANA MERKEZ (HUB) - EKSİK OLAN FONKSİYON ---
def render_main_hub():
    render_header("Global Kontrol Paneli", "Merkezi Yönetim Ekranı")

    col1, col2 = st.columns(2)

    # SOL MODÜL: Şirket Bilgisi
    with col1:
        st.markdown("""
        <div class="hub-card">
            <div class="hub-icon"><i class="fa-solid fa-building"></i></div>
            <div class="hub-title">ŞİRKET PROFİLİ</div>
            <div class="hub-desc">Vizyon, Misyon & Strateji</div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Şirket Hakkında"):
            st.info("Artificial Staff, Türk üreticileri ABD pazarına taşıyan uçtan uca ihracat ortağıdır. 'Üretim Türkiye'de, Kazanç Amerika'da' mottosuyla çalışırız.")

    # SAĞ MODÜL: Hizmetler (Tıklayınca açılır)
    with col2:
        st.markdown("""
        <div class="hub-card" style="border-color:rgba(212, 175, 55, 0.4);">
            <div class="hub-icon"><i class="fa-solid fa-layer-group"></i></div>
            <div class="hub-title">HİZMET MODÜLLERİ</div>
            <div class="hub-desc">Aktif 9 Hizmet Entegrasyonu</div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Tüm Hizmetleri Görüntüle", expanded=True):
            render_services_catalog() # Hizmetleri burada çağırıyoruz

# --- 4. HİZMET KATALOĞU (DETAY) ---
def render_services_catalog():
    services = [
        ("💻", "Web & Teknoloji", "ABD odaklı e-ticaret altyapısı."),
        ("🏛️", "LLC Kurulumu", "Delaware şirket ve Banka hesabı."),
        ("✈️", "Lojistik", "Kapıdan kapıya 2-4 günde teslimat."),
        ("🏭", "3PL Depolama", "NJ ve CA eyaletlerinde stratejik depolar."),
        ("🛒", "Pazaryeri", "Amazon & Walmart hesap yönetimi."),
        ("📱", "Sosyal Medya", "Global marka yönetimi."),
        ("📢", "Reklamlar", "Meta & Google Ads performansı."),
        ("🤖", "Otomasyon", "CRM ve fatura otomasyonu."),
        ("🤝", "B2B Satış", "Yapay zeka ile toptan müşteri bulma.")
    ]
    for icon, title, desc in services:
        st.markdown(f"<div class='service-mini-card'><strong>{icon} {title}</strong><br><span style='font-size:11px; color:#888;'>{desc}</span></div>", unsafe_allow_html=True)

# --- 5. DİĞER SAYFALAR ---
def render_dashboard():
    render_header("Finansal Veriler", "Anlık Ciro ve Trafik")
    metrics = get_dashboard_metrics()
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric(metrics["revenue"]["label"], metrics["revenue"]["value"], metrics["revenue"]["delta"])
    with c2: st.metric(metrics["region"]["label"], metrics["region"]["value"], metrics["region"]["delta"])
    with c3: st.metric(metrics["visitors"]["label"], metrics["visitors"]["value"], metrics["visitors"]["delta"])
    with c4: st.metric(metrics["conversion"]["label"], metrics["conversion"]["value"], metrics["conversion"]["delta"])
    st.markdown("### 📈 Satış Trendi")
    st.plotly_chart(get_sales_chart(), width="stretch")

def render_artis_ai():
    render_header("ARTIS AI", "Yapay Zeka Asistanı")
    if "messages" not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Merhaba! Ben ARTIS. Size nasıl yardımcı olabilirim?"}]
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.write(msg["content"])
    if prompt := st.chat_input("Sorunuzu yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        response = get_artis_response(prompt)
        time.sleep(0.5)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"): st.write(response)

def render_logistics():
    render_header("Lojistik", "Kargo Takip")
    st.plotly_chart(get_map_chart(), width="stretch")

def render_marketing():
    render_header("Pazarlama", "Reklam Performansı")
    st.plotly_chart(get_marketing_chart(), width="stretch")
