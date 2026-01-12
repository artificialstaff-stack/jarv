import streamlit as st
import sys
import os
import time

# Brain modülünü güvenli import et
try:
    import brain
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))
    try:
        import brain
    except ImportError:
        sys.path.append(os.path.dirname(__file__))
        import brain

# 1. SAYFA YAPILANDIRMASI (PRO AYARLAR)
st.set_page_config(
    page_title="ARTIS | Global OS",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. PREMIUM CSS ENJEKSİYONU
st.markdown("""
<style>
    /* FONTLAR VE GENEL ARKAPLAN */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #0E1117; /* Derin Siyah/Mavi */
        color: #E0E0E0;
    }

    /* SIDEBAR TASARIMI */
    section[data-testid="stSidebar"] {
        background-color: #161B22; /* Koyu Github Grisi */
        border-right: 1px solid #30363D;
    }

    /* MENÜ (RADIO) BUTONLARINI GİZLE, KART GİBİ YAP */
    .stRadio > div {
        background-color: transparent;
    }
    .stRadio div[role="radiogroup"] > label {
        background-color: #21262D;
        padding: 12px 20px;
        margin-bottom: 8px;
        border-radius: 8px;
        border: 1px solid #30363D;
        transition: all 0.3s ease;
        cursor: pointer;
        display: flex; /* İçeriği hizala */
        align-items: center;
    }
    .stRadio div[role="radiogroup"] > label:hover {
        background-color: #2F81F7; /* Hover Rengi: Mavi */
        color: white !important;
        border-color: #2F81F7;
    }
    /* Seçili olanı mavi yap */
    .stRadio div[role="radiogroup"] > label[data-checked="true"] {
        background-color: #1F6FEB;
        color: white !important;
        border-color: #1F6FEB;
        box-shadow: 0 0 10px rgba(31, 111, 235, 0.4);
    }
    /* Radio yuvarlaklarını gizle */
    .stRadio div[role="radiogroup"] > label > div:first-child {
        display: none;
    }

    /* INPUT ALANI */
    .stChatInput {
        position: fixed;
        bottom: 30px;
        width: 70% !important;
        left: 55%; /* Ortalamak için */
        transform: translateX(-50%);
        z-index: 999;
    }
    .stTextInput input {
        background-color: #0D1117 !important;
        border: 1px solid #30363D;
        color: white;
    }

    /* GİRİŞ EKRANI */
    .login-box {
        background: linear-gradient(145deg, #161B22, #0D1117);
        padding: 50px;
        border-radius: 16px;
        border: 1px solid #30363D;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* ÖNERİ KARTLARI (CHAT BAŞLANGICI) */
    .suggestion-card {
        background-color: #21262D;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363D;
        text-align: center;
        transition: 0.3s;
        cursor: pointer;
        height: 100%;
    }
    .suggestion-card:hover {
        border-color: #1F6FEB;
        background-color: #1F6FEB;
        color: white;
    }
    
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. HAFIZA BAŞLATMA
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# DURUM 1: GİRİŞ EKRANI (LANDING PAGE)
# =========================================================
if not st.session_state.setup_complete:
    
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        # Logo ve Başlık
        st.markdown("<h1 style='text-align:center; font-size: 4rem; letter-spacing: -2px;'>ARTIS <span style='color:#1F6FEB'>.OS</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8B949E; font-size: 1.2rem;'>Next-Gen Lojistik Operasyon Sistemi</p>", unsafe_allow_html=True)
        
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        
        with st.form("setup_form"):
            st.markdown("### 🚀 Hesap Oluşturun")
            col_a, col_b = st.columns(2)
            with col_a:
                name_in = st.text_input("Ad Soyad", placeholder="Örn: Burak Yılmaz")
                sector_in = st.selectbox("Sektör", ["E-Ticaret", "Tekstil", "Gıda", "Yazılım", "Diğer"])
            with col_b:
                brand_in = st.text_input("Marka Adı", placeholder="Örn: Modanisa")
                product_in = st.text_input("Ana Ürün", placeholder="Örn: Kadın Giyim")
            
            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("PANELİ BAŞLAT →", type="primary", use_container_width=True)
            
            if submitted:
                if len(name_in) > 1 and len(brand_in) > 1:
                    st.session_state.user_data = {
                        "name": name_in,
                        "brand": brand_in,
                        "sector": sector_in,
                        "product": product_in
                    }
                    # İlk mesajı buraya eklemiyoruz, chat ekranında dinamik göstereceğiz
                    st.session_state.setup_complete = True
                    st.rerun()
                else:
                    st.error("Lütfen zorunlu alanları doldurunuz.")
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# DURUM 2: ANA UYGULAMA (DASHBOARD)
# =========================================================
else:
    # --- SIDEBAR (PROFESYONEL MENÜ) ---
    with st.sidebar:
        # Marka Logosu Simülasyonu
        st.markdown(f"""
        <div style="background:#21262D; padding:15px; border-radius:10px; text-align:center; border:1px solid #30363D;">
            <h2 style="margin:0; color:white;">{st.session_state.user_data['brand'][0:2].upper()}</h2>
            <small style="color:#8B949E;">{st.session_state.user_data['brand']}</small>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Menü
        page = st.radio(
            "NAVIGASYON", 
            ["💬 AI ASİSTAN", "📊 FİNANSAL TABLO", "📦 LOJİSTİK AĞI"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        # Alt Bilgi
        st.caption("Server: **US-EAST-1** (4ms)")
        st.caption("Versiyon: **2.5.0 Pro**")
        
        if st.button("Çıkış Yap", use_container_width=True):
            st.session_state.setup_complete = False
            st.session_state.messages = []
            st.rerun()

    # --- SAYFA İÇERİKLERİ ---
    
    # 1. AI ASİSTAN SAYFASI
    if page == "💬 AI ASİSTAN":
        
        # Eğer mesaj geçmişi boşsa "Öneri Kartlarını" göster
        if not st.session_state.messages:
            st.markdown(f"<h1 style='text-align:center; margin-top: 50px;'>Merhaba, {st.session_state.user_data['name']} 👋</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; color:#8B949E;'>Washington DC operasyon merkezi hazır. Nereden başlayalım?</p>", unsafe_allow_html=True)
            
            # Öneri Kartları (Grid Yapısı)
            col1, col2, col3 = st.columns(3)
            
            # Kartlara basınca session state'e mesaj ekleyip rerun yapıyoruz
            if col1.button("💰 Maliyet Analizi", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": "Ürünlerimin ABD lojistik ve depolama maliyetini hesaplar mısın?"})
                st.rerun()
                
            if col2.button("🚀 Şirket Kurulumu", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": "Amerika'da şirket kurmak ve vergi süreçleri nasıl işliyor?"})
                st.rerun()
                
            if col3.button("📦 Kargo Süreci", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": "Türkiye'den ürünleri depoya gönderme süreci nasıl?"})
                st.rerun()
                
        else:
            # Mesajlar varsa göster
            chat_container = st.container(height=600)
            for msg in st.session_state.messages:
                with chat_container.chat_message(msg["role"]):
                    st.markdown(msg["content"])

        # Input Alanı
        if prompt := st.chat_input("Bir şeyler sorun..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.rerun() # Ekranı hemen güncellemek için

        # Son mesaj kullanıcıdansa cevap üret (Rerun sonrası burası çalışır)
        if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
            with st.chat_message("user"):
                st.markdown(st.session_state.messages[-1]["content"])
            
            with st.chat_message("assistant"):
                placeholder = st.empty()
                full_response = ""
                try:
                    # Brain Streaming
                    stream = brain.get_streaming_response(st.session_state.messages, st.session_state.user_data)
                    for chunk in stream:
                        full_response += chunk
                        placeholder.markdown(full_response + "▌")
                    placeholder.markdown(full_response)
                except Exception:
                    placeholder.error("Bağlantı hatası.")
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})


    # 2. FİNANS SAYFASI
    elif page == "📊 FİNANSAL TABLO":
        st.markdown("## 📊 Gelir Projeksiyonu")
        st.markdown("Sektör ortalamalarına göre tahmini büyüme.")
        
        # Metrikler
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Aylık Ciro", "$42,500", "+12%")
        m2.metric("Net Kâr", "$15,200", "+8%")
        m3.metric("ROI", "%320", "+5%")
        m4.metric("CAC (Maliyet)", "$12", "-2%")
        
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

    # 3. LOJİSTİK SAYFASI
    elif page == "📦 LOJİSTİK AĞI":
        st.markdown("## 📦 Global Sevkiyat Ağı")
        
        row1_1, row1_2 = st.columns([3, 1])
        with row1_1:
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
        with row1_2:
            st.success("Depo Durumu: MÜSAİT")
            st.info("Son Sevkiyat: Yolda")
            st.warning("Gümrük: İşleniyor")
            
            with st.expander("Depo Detayları"):
                st.write("Adres: 1200 Pennsylvania Ave, Washington DC")
                st.write("Yönetici: ARTIS AI")
