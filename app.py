import streamlit as st
import sys
import os
import time

# Brain import
try:
    import brain
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))
    import brain

# 1. SAYFA AYARLARI
st.set_page_config(
    page_title="ARTIS | Global OS",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded" # Menüyü zorla aç
)

# 2. CSS TASARIMI (Görünürlüğü Artırılmış Menü)
st.markdown("""
<style>
    /* Genel */
    .stApp { background-color: #343541; color: #ECECF1; }
    
    /* Input Alanları */
    .stTextInput input, .stSelectbox div {
        background-color: #40414F !important;
        color: white !important;
        border: 1px solid #565869;
    }
    
    /* GİRİŞ EKRANI KUTUSU */
    .login-box {
        background-color: #202123;
        padding: 40px;
        border-radius: 10px;
        border: 1px solid #565869;
        margin-top: 50px;
    }

    /* SOL MENÜ (SIDEBAR) GÖRÜNÜRLÜK AYARI */
    section[data-testid="stSidebar"] {
        background-color: #202123;
        border-right: 1px solid #444;
    }
    
    /* Menü Yazıları */
    .stRadio label {
        color: white !important;
        font-size: 18px !important;
        font-weight: bold;
    }

    /* Başlık */
    h1, h2, h3 { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. HAFIZA (SESSION STATE)
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# DURUM 1: KURULUM YAPILMADIYSA -> GİRİŞ FORMUNU GÖSTER
# =========================================================
if not st.session_state.setup_complete:
    
    # Giriş Ekranı Tasarımı
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center; font-size: 4rem;'>ARTIS <span style='color:#D4AF37'>AI</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#888;'>Autonomous Export Operating System</p>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="login-box">
            <h3 style="text-align:center;">SİSTEM KURULUMU</h3>
            <p style="text-align:center; color:#aaa;">Operasyonu başlatmak için şirket bilgilerinizi giriniz.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Form
        with st.form("setup_form"):
            name = st.text_input("Adınız Soyadınız", placeholder="Örn: Ahmet Yılmaz")
            brand = st.text_input("Marka Adı", placeholder="Örn: Anatolia Home")
            sector = st.selectbox("Sektör", ["Tekstil", "Gıda", "Kozmetik", "Mobilya", "Otomotiv", "Diğer"])
            product = st.text_input("Ana Ürünleriniz", placeholder="Örn: İpek Eşarp, Zeytinyağı...")
            
            submit = st.form_submit_button("🚀 SİSTEMİ BAŞLAT", type="primary", use_container_width=True)
            
            if submit:
                if name and brand and product:
                    # Verileri Kaydet
                    st.session_state.user_data = {
                        "name": name,
                        "brand": brand,
                        "sector": sector,
                        "product": product
                    }
                    # AI'ın ilk mesajını kişiye özel hazırla
                    st.session_state.messages = [{
                        "role": "assistant", 
                        "content": f"Hoş geldiniz {name} Bey. {brand} markası için analizlerimi tamamladım. Washington DC operasyon merkezindeyim. Sizin için ilk olarak ne yapmamı istersiniz?"
                    }]
                    
                    st.session_state.setup_complete = True
                    st.rerun() # Sayfayı yenile ve ana ekrana geç
                else:
                    st.error("Lütfen tüm alanları doldurunuz.")

# =========================================================
# DURUM 2: KURULUM TAMAM -> ANA UYGULAMAYI GÖSTER
# =========================================================
else:
    # --- SOL MENÜ (NAVIGASYON) ---
    with st.sidebar:
        st.markdown("## 🧭 NAVİGASYON")
        st.info(f"👤 {st.session_state.user_data['brand']}")
        
        # Sayfa Seçimi
        page = st.radio("MODÜLLER", ["💬 ASİSTAN", "📊 FİNANS", "📦 LOJİSTİK"], label_visibility="collapsed")
        
        st.markdown("---")
        if st.button("🔴 OTURUMU KAPAT", use_container_width=True):
            st.session_state.setup_complete = False
            st.rerun()

    # --- SAYFA İÇERİKLERİ ---
    
    # 1. ASİSTAN SAYFASI
    if page == "💬 ASİSTAN":
        st.markdown(f"## ARTIS AI - {st.session_state.user_data['brand']} Operasyonu")
        
        # Chat Alanı
        chat_container = st.container(height=600)
        for msg in st.session_state.messages:
            with chat_container.chat_message(msg["role"]):
                st.markdown(msg["content"])
                
        # Input Alanı
        if prompt := st.chat_input("Operasyon hakkında konuşun..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_container.chat_message("user"):
                st.markdown(prompt)
            
            with chat_container.chat_message("assistant"):
                placeholder = st.empty()
                full_response = ""
                try:
                    # Brain'e kullanıcı verisini de gönderiyoruz
                    stream = brain.get_streaming_response(st.session_state.messages, st.session_state.user_data)
                    for chunk in stream:
                        full_response += chunk
                        placeholder.markdown(full_response + "▌")
                    placeholder.markdown(full_response)
                except Exception as e:
                    placeholder.error("Bağlantı hatası.")
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 2. FİNANS SAYFASI
    elif page == "📊 FİNANS":
        st.title("📊 Finansal Simülasyon")
        c1, c2, c3 = st.columns(3)
        c1.metric("Tahmini Ciro", "$42,500")
        c2.metric("Net Kâr", "$18,200")
        c3.metric("Lojistik Maliyeti", "$3,500")
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

    # 3. LOJİSTİK SAYFASI
    elif page == "📦 LOJİSTİK":
        st.title("📦 Lojistik Takip")
        st.success(f"✅ {st.session_state.user_data['product']} ürünleri için Washington DC deposunda yer ayrıldı.")
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
