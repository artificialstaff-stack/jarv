import streamlit as st
import sys
import os
import time

# Brain modülünü güvenli şekilde içeri aktar
try:
    import brain
except ImportError:
    # Eğer brain.py logic klasöründeyse oraya bak, yoksa ana dizine bak
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))
    try:
        import brain
    except ImportError:
        # Son çare aynı dizine bak
        sys.path.append(os.path.dirname(__file__))
        import brain

# 1. SAYFA AYARLARI (Menüyü zorla açık tutar)
st.set_page_config(
    page_title="ARTIS | Operasyon Merkezi",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# 2. CSS TASARIMI (Menü ve Form Görünümü)
st.markdown("""
<style>
    /* Genel Arkaplan */
    .stApp { background-color: #343541; color: #ECECF1; font-family: 'Inter', sans-serif; }
    
    /* GİRİŞ KUTUSU */
    .login-container {
        background-color: #202123;
        padding: 40px;
        border-radius: 12px;
        border: 1px solid #444;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    
    /* SOL MENÜ (SIDEBAR) */
    section[data-testid="stSidebar"] {
        background-color: #202123;
        border-right: 1px solid #444;
    }
    
    /* Menüdeki Seçim Butonları */
    .stRadio label {
        font-size: 16px !important;
        font-weight: 500;
        padding: 10px;
        border-radius: 5px;
    }
    .stRadio label:hover {
        background-color: #2A2B32;
    }
    
    /* Input Alanları */
    .stTextInput input, .stSelectbox div {
        background-color: #40414F !important;
        color: white !important;
        border: 1px solid #565869;
    }
    
    /* Gizleme */
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. HAFIZA (SESSION STATE) BAŞLATMA
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# BÖLÜM 1: GİRİŞ EKRANI (Kullanıcı henüz giriş yapmadıysa)
# =========================================================
if not st.session_state.setup_complete:
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center; font-size: 3.5rem;'>ARTIS <span style='color:#10A37F'>AI</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#888; margin-bottom: 30px;'>Autonomous Export Operating System v2.5</p>", unsafe_allow_html=True)
        
        # Giriş Formu Kutusu
        with st.container():
            st.markdown('<div class="login-container">', unsafe_allow_html=True)
            st.markdown("### 🚀 SİSTEM KURULUMU")
            st.info("Operasyonu başlatmak için şirket kimliğinizi oluşturun.")
            
            with st.form("setup_form"):
                name = st.text_input("Adınız Soyadınız", placeholder="Örn: Ahmet Yılmaz")
                brand = st.text_input("Marka Adı", placeholder="Örn: Anatolia Textiles")
                sector = st.selectbox("Sektör", ["Tekstil & Moda", "Gıda", "Kozmetik", "Mobilya", "Yazılım", "Diğer"])
                product = st.text_input("Ana Ürünleriniz", placeholder="Örn: İpek Eşarp, Zeytinyağı...")
                
                submitted = st.form_submit_button("SİSTEMİ BAŞLAT", type="primary", use_container_width=True)
                
                if submitted:
                    if len(name) > 2 and len(brand) > 2:
                        # Verileri Kaydet
                        st.session_state.user_data = {
                            "name": name,
                            "brand": brand,
                            "sector": sector,
                            "product": product
                        }
                        # AI İlk Mesajını Hazırla
                        welcome_msg = f"Hoş geldiniz {name} Bey. {brand} markası için analizlerimi tamamladım. Washington DC operasyon merkezindeyim. Sizin için ilk olarak ne yapmamı istersiniz?"
                        st.session_state.messages = [{"role": "assistant", "content": welcome_msg}]
                        
                        # Durumu Güncelle ve Sayfayı Yenile
                        st.session_state.setup_complete = True
                        st.rerun()
                    else:
                        st.error("Lütfen adınızı ve marka isminizi eksiksiz girin.")
            
            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# BÖLÜM 2: ANA UYGULAMA (Giriş yapıldıysa burası çalışır)
# =========================================================
else:
    # --- SOL MENÜ (NAVIGASYON) ---
    with st.sidebar:
        st.markdown(f"## 👤 {st.session_state.user_data['brand']}")
        st.caption("Washington DC: 🟢 Online")
        st.markdown("---")
        
        # Sayfa Seçimi (Radio Buton ile Menü)
        page = st.radio(
            "MENÜ", 
            ["💬 ASİSTAN (CHAT)", "📊 FİNANS PANELİ", "📦 LOJİSTİK TAKİP"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        # Çıkış Butonu
        if st.button("🔴 OTURUMU KAPAT", use_container_width=True):
            st.session_state.setup_complete = False
            st.session_state.messages = []
            st.rerun()

    # --- SAYFA YÖNLENDİRMESİ ---
    
    # 1. CHAT SAYFASI
    if page == "💬 ASİSTAN (CHAT)":
        st.markdown(f"<h2 style='text-align:center;'>ARTIS AI - {st.session_state.user_data['brand']}</h2>", unsafe_allow_html=True)
        
        # Mesaj Geçmişi
        chat_container = st.container(height=600)
        for msg in st.session_state.messages:
            with chat_container.chat_message(msg["role"]):
                st.markdown(msg["content"])
        
        # Input Alanı
        if prompt := st.chat_input("Operasyon hakkında konuşun..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_container.chat_message("user"):
                st.markdown(prompt)
            
            # AI Cevabı
            with chat_container.chat_message("assistant"):
                placeholder = st.empty()
                full_response = ""
                try:
                    stream = brain.get_streaming_response(st.session_state.messages, st.session_state.user_data)
                    for chunk in stream:
                        full_response += chunk
                        placeholder.markdown(full_response + "▌")
                    placeholder.markdown(full_response)
                except Exception:
                    placeholder.error("Bağlantı hatası.")
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 2. FİNANS SAYFASI
    elif page == "📊 FİNANS PANELİ":
        st.title("📊 Finansal Simülasyon")
        st.info("Bu veriler, seçtiğiniz pakete göre tahmini kazancınızı gösterir.")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Tahmini Ciro (Aylık)", "$42,500", "+%15")
        c2.metric("Net Kâr", "$18,200", "+%8")
        c3.metric("Reklam Bütçesi", "$3,000", "Stabil")
        
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

    # 3. LOJİSTİK SAYFASI
    elif page == "📦 LOJİSTİK TAKİP":
        st.title("📦 Global Lojistik Ağı")
        st.success(f"✅ {st.session_state.user_data['product']} ürünleri için Washington DC deposunda yer ayrıldı.")
        
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
