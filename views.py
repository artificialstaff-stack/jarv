import streamlit as st
import time
from brain import get_artis_response, get_sales_chart, get_map_chart

# [VIEW-01] LOGIN
def render_login_screen():
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center; font-family:Cinzel; font-size:50px; color:#D4AF37;'>AS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#666; letter-spacing:4px; font-size:10px;'>ENTERPRISE ACCESS</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            user = st.text_input("ID", placeholder="admin")
            pw = st.text_input("PASS", type="password", placeholder="••••")
            if st.form_submit_button("LOGIN"):
                if user == "admin" and pw == "admin":
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("ACCESS DENIED")

# [VIEW-02] JARVIS CORE (HOME / SEARCH)
def render_jarvis_core():
    # Perplexity Tarzı Merkez
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-family:Cinzel; font-size:40px; color:white;'>ARTIFICIAL STAFF</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666;'>Global operasyonlarınız için neyi bilmek istersiniz?</p>", unsafe_allow_html=True)
    
    # Arama Çubuğu
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        user_input = st.chat_input("Bir talimat verin...")
    
    # Örnek Butonlar
    b1, b2, b3, b4 = st.columns(4)
    with b1: st.button("📦 Lojistik Durumu", use_container_width=True)
    with b2: st.button("💰 Maliyet Analizi", use_container_width=True)
    with b3: st.button("📈 Pazar Trendi", use_container_width=True)
    with b4: st.button("🏛️ Şirket Kurulumu", use_container_width=True)

    if user_input:
        st.markdown("---")
        with st.chat_message("user"): st.write(user_input)
        response = get_artis_response(user_input)
        time.sleep(0.5)
        with st.chat_message("assistant"): 
            st.markdown(f"<span style='color:#D4AF37'>ARTIS:</span> {response}", unsafe_allow_html=True)

# [VIEW-03] GLOBAL HUB (SERVICES)
def render_global_hub():
    st.markdown("### 💠 HİZMET PROTOKOLLERİ")
    st.markdown("---")
    services = [
        ("💻", "WEB & TECH", "ABD uyumlu e-ticaret altyapısı."),
        ("🏛️", "LLC & LEGAL", "Şirket ve Banka kurulumu."),
        ("✈️", "LOGISTICS", "Kapıdan kapıya 2-4 gün teslimat."),
        ("🏭", "WAREHOUSE", "NJ/CA 3PL depolama."),
        ("📢", "MARKETING", "Meta & Google Ads yönetimi."),
        ("🤝", "B2B SALES", "Yapay zeka ile toptan satış.")
    ]
    # Grid
    rows = [services[i:i+3] for i in range(0, len(services), 3)]
    for row in rows:
        cols = st.columns(3)
        for idx, (icon, title, desc) in enumerate(row):
            with cols[idx]:
                st.markdown(f"""
                <div class="glass-card">
                    <div style="font-size:24px; color:#D4AF37;">{icon}</div>
                    <div style="font-family:'Cinzel'; color:white; margin-top:10px;">{title}</div>
                    <div style="font-size:12px; color:#888;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)
        st.write("")

# [VIEW-04] FINANCES (DASHBOARD)
def render_finances():
    st.markdown("### 💰 FİNANSAL GÖSTERGELER")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Ciro", "$124,500", "+12%")
    with c2: st.metric("Kâr Marjı", "%32", "+2%")
    with c3: st.metric("Reklam Harcaması", "$12,000", "-5%")
    with c4: st.metric("ROI", "4.2x", "+0.3")
    
    st.markdown("### Nakit Akışı")
    st.plotly_chart(get_sales_chart(), use_container_width=True)

# [VIEW-05] LOGISTICS
def render_logistics_view():
    st.markdown("### ✈️ LOJİSTİK AĞI")
    c1, c2 = st.columns([2, 1])
    with c1: st.plotly_chart(get_map_chart(), use_container_width=True)
    with c2:
        st.info("TR-8291: Gümrükte (NY)")
        st.success("EU-1029: Teslim Edildi (Berlin)")
