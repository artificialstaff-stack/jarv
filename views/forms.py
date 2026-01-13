import streamlit as st
import time

def render_forms():
    st.title("📝 Operasyon Merkezi")
    st.markdown("Yeni bir sevkiyat başlatın veya teknik destek talebi oluşturun.")
    
    tab_shipment, tab_support = st.tabs(["📦 YENİ SEVKİYAT BAŞLAT", "🔧 TEKNİK DESTEK"])
    
    # --- SEKME 1: SEVKİYAT SİHİRBAZI ---
    with tab_shipment:
        st.markdown("### 🚢 ABD Lojistik Talep Formu")
        st.info("Bu form ile İstanbul depomuzdan Washington DC Hub'ına gönderim planlayabilirsiniz.")
        
        with st.form("shipment_wizard"):
            # Bölüm 1: Ürün Bilgisi
            st.markdown("#### 1. Kargo İçeriği")
            c1, c2 = st.columns(2)
            product_type = c1.selectbox("Ürün Tipi", ["Tekstil (Hazır Giyim)", "Ev Tekstili", "Gıda (Paketli)", "Kozmetik", "Diğer"])
            box_count = c2.number_input("Koli Adedi", min_value=1, value=10)
            
            # Bölüm 2: Lojistik Detayları
            st.markdown("#### 2. Lojistik Tercihleri")
            c3, c4 = st.columns(2)
            ship_date = c3.date_input("Tahmini Teslim Tarihi (Depomuza)")
            priority = c4.radio("Gönderim Hızı", ["Standart (Gemi - 20 Gün)", "Ekspres (Uçak - 3 Gün)"], horizontal=True)
            
            # Bölüm 3: Belgeler
            st.markdown("#### 3. Dokümantasyon")
            st.file_uploader("Çeki Listesi (Packing List) Yükle", type=["pdf", "excel"])
            
            notes = st.text_area("Varsa Ek Notlar (Örn: Kırılabilir ürün)")
            
            # Onay
            submitted = st.form_submit_button("🚀 SEVKİYAT TALEBİNİ OLUŞTUR", type="primary", use_container_width=True)
            
            if submitted:
                with st.spinner("Talep sisteme işleniyor..."):
                    time.sleep(1.5) # İşlem yapıyormuş hissi
                st.success(f"✅ Talep Başarıyla Alındı! Referans Kodunuz: #LOG-{int(time.time())}")
                st.balloons()
                st.info("Lojistik uzmanımız 2 saat içinde belgelerinizi onaylayıp size dönecektir.")

    # --- SEKME 2: DESTEK ---
    with tab_support:
        st.markdown("### 🔧 Teknik Destek Bileti")
        with st.form("support_ticket"):
            issue_type = st.selectbox("Konu", ["Entegrasyon Sorunu", "Fatura/Ödeme", "Panel Hatası", "Diğer"])
            description = st.text_area("Sorunu detaylı açıklayın")
            
            if st.form_submit_button("Bilet Oluştur"):
                st.success("Destek ekibimiz talebinizi aldı.")
