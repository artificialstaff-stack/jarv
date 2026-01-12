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

# 1. SAYFA AYARLARI
st.set_page_config(
    page_title="ARTIS | Global OS",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS TASARIMI
st.markdown("""
<style>
    .stApp { background-color: #343541; color: #ECECF1; font-family: 'Inter', sans-serif; }
    .login-box { background-color: #202123; padding: 40px; border-radius: 12px; border: 1px solid #444; }
    section[data-testid="stSidebar"] { background-color: #202123; border-right: 1px solid #444; }
    .stTextInput input, .stSelectbox div { background-color: #40414F !important; color: white !important; border: 1px solid #565869; }
    header {visibility: hidden;}
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
# AKIŞ KONTROLÜ (GİRİŞ EKRANI vs ANA UYGULAMA)
# =========================================================

if not st.session_state.setup_complete:
    # --- GİRİŞ EKRANI ---
    # Sütunları burada tanımlıyoruz (Sadece bu blokta geçerli)
    login_col1, login_col2, login_col3 = st.columns([1, 2, 1])
    
    with login_col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center;'>ARTIS <span style='color:#10A37F'>AI</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#888;'>Autonomous Export Operating System v2.5</p>", unsafe_allow_html=True)
        
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown("### 🚀 SİSTEM KURULUMU")
        
        with st.form("setup_form"):
            name_in = st.text_input("Adınız Soyadınız", placeholder="Örn: Ahmet Yılmaz")
            brand_in = st.text_input("Marka Adı", placeholder="Örn: Anatolia")
            sector_in = st.selectbox("Sektör", ["Tekstil", "Gıda", "Kozmetik", "Diğer"])
            product_in = st.text_input("Ana Ürünler", placeholder="Örn: İpek Eşarp")
            
            submitted = st.form_submit_button("SİSTEMİ BAŞLAT", type="primary", use_container_width=True)
            
            if submitted:
                if len(name_in) > 1 and len(brand_in) > 1:
                    # Verileri Kaydet
                    st.session_state.user_data = {
                        "name": name_in,
                        "brand": brand_in,
                        "sector": sector_in,
                        "product": product_in
                    }
                    # İlk Mesajı Hazırla
                    first_msg = f"Hoş geldiniz {name_in} Bey. {brand_in} markası için analizlerimi tamamladım. Washington DC operasyon merkezindeyim. İlk olarak ne yapmamı istersiniz?"
                    st.session_state.messages = [{"role": "assistant", "content": first_msg}]
                    
                    st.session_state.setup_complete = True
                    st.rerun()
                else:
                    st.error("Lütfen bilgileri eksiksiz giriniz.")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- ANA UYGULAMA ---
    # Burada artık login_col2 kullanmıyoruz, hata vermez.
    
    # SOL MENÜ
    with st.sidebar:
        st.markdown(f"## 👤 {st.session_state.user_data.get('brand', 'Marka')}")
        st.caption("Washington DC: 🟢 Online")
        st.markdown("---")
        
        page = st.radio("MENÜ", ["💬 ASİSTAN", "📊 FİNANS", "📦 LOJİSTİK"], label_visibility="collapsed")
        
        st.markdown("---")
        if st.button("🔴 ÇIKIŞ", use_container_width=True):
            st.session_state.setup_complete = False
            st.session_state.messages = []
            st.rerun()

    # SAYFALAR
    if page == "💬 ASİSTAN":
        st.title(f"ARTIS AI - {st.session_state.user_data.get('name', 'Kullanıcı')}")
        
        chat_container = st.container(height=600)
        for msg in st.session_state.messages:
            with chat_container.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Mesaj yazın..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_container.chat_message("user"):
                st.markdown(prompt)
            
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

    elif page == "📊 FİNANS":
        st.title("📊 Finansal Simülasyon")
        c1, c2, c3 = st.columns(3)
        c1.metric("Tahmini Ciro", "$42,500")
        c2.metric("Net Kâr", "$18,200")
        c3.metric("Maliyet", "$3,500")
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)

    elif page == "📦 LOJİSTİK":
        st.title("📦 Lojistik Takip")
        st.success("Washington DC Deposu: Müsait")
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
