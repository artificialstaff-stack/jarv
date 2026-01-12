import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("<h2 style='text-align: center;'>ARTIFICIAL<br><span style='font-size:14px; letter-spacing: 3px; color: #aaa;'>STAFF v4.0</span></h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Navigasyon
        selected = st.radio(
            "MODÜLLER",
            ["🤖 JARVIS CORE", "📦 GLOBAL ENVANTER", "💰 FİNANSAL ANALİZ", "📊 STRATEJİ"],
            index=0
        )
        
        st.markdown("---")
        
        # Sistem Durumu (Sanki canlıymış gibi)
        st.caption("SİSTEM DURUMU")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("CPU", "12%", "-1%")
        with col2:
            st.metric("RAM", "4.2GB", "+0.2")
            
        st.success("🟢 BAĞLANTI: GÜVENLİ (SSL)")
        st.info("📍 KONUM: US-EAST-1")
        
        return selected

def render_inventory_dashboard():
    st.title("📦 Global Envanter")
    
    # Üst Bilgi Kartları
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Toplam Ürün", "1,204", "12")
    c2.metric("Kritik Stok", "8", "-2", delta_color="inverse")
    c3.metric("Tahmini Değer", "$420K", "+5%")
    c4.metric("Aktif Sipariş", "34", "4")
    
    st.markdown("### 🔍 Hızlı İşlem Menüsü")
    st.info("Veri akışı bekleniyor... Jarvis üzerinden manuel giriş yapabilirsiniz.")

def render_finance_dashboard():
    st.title("💰 Finansal Kokpit")
    c1, c2 = st.columns(2)
    c1.metric("Aylık Ciro", "$54,000", "+%12")
    c2.metric("Reklam Harcaması", "$4,200", "-%3")
    st.warning("Detaylı grafikler yükleniyor...")
