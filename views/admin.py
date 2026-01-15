import streamlit as st
import pandas as pd
import time

def inject_admin_css():
    st.markdown("""
    <style>
        .admin-card {
            background: rgba(20, 20, 22, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
        }
        .status-dot {
            height: 10px; width: 10px; 
            border-radius: 50%; display: inline-block; margin-right: 8px;
        }
        .dot-green { background-color: #10B981; box-shadow: 0 0 10px #10B981; }
        .dot-red { background-color: #EF4444; box-shadow: 0 0 10px #EF4444; }
        
        /* Toggle Switch Stili */
        .stToggle label { color: #E4E4E7 !important; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

def render():
    inject_admin_css()
    
    st.markdown("""
        <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:30px;'>
            <div>
                <h1 style='margin:0; font-size: 2.5rem; font-weight: 800; color:white;'>🛡️ Yönetici Paneli</h1>
                <p style='color:#888; margin:0;'>Sistem konfigürasyonu, kullanıcı yönetimi ve modül ayarları.</p>
            </div>
            <div style='text-align:right;'>
                <div style='background:rgba(239, 68, 68, 0.1); border:1px solid rgba(239, 68, 68, 0.3); color:#EF4444; padding:5px 15px; border-radius:20px; font-size:12px; font-weight:700;'>
                    ADMIN YETKİSİ AKTİF
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Sekmeli Yapı
    tab1, tab2, tab3, tab4 = st.tabs(["⚙️ Genel Ayarlar", "👥 Kullanıcılar", "🔌 Modül Yönetimi", "📡 Sistem Logları"])

    # --- TAB 1: GENEL AYARLAR ---
    with tab1:
        st.markdown("### 🏢 Marka ve Sistem Kimliği")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("#### Marka Bilgileri")
                
                # Session State'den mevcut markayı al
                current_brand = st.session_state.user_data.get('brand', 'Anatolia Home')
                new_brand = st.text_input("Şirket İsmi", value=current_brand)
                
                if st.button("Marka İsmini Güncelle", type="primary"):
                    st.session_state.user_data['brand'] = new_brand
                    st.success(f"Marka ismi '{new_brand}' olarak güncellendi! (Sayfayı yenileyince sol menüde değişir)")
                    time.sleep(1)
                    st.rerun()

        with col2:
            with st.container(border=True):
                st.markdown("#### API Yapılandırması")
                api_key = st.text_input("Google Gemini API Key", value="********************", type="password")
                st.info("API Anahtarı 'st.secrets' üzerinden güvenli şekilde çekilmektedir.")
                
                model_secimi = st.selectbox("Aktif AI Modeli", ["gemini-2.5-flash", "gemini-pro-1.5", "gemini-ultra"])
                st.caption("Şu anki aktif model: **gemini-2.5-flash**")

    # --- TAB 2: KULLANICI YÖNETİMİ ---
    with tab2:
        st.markdown("### 👥 Personel ve Yetkilendirme")
        
        # Sahte Veri
        users_data = pd.DataFrame({
            "ID": [101, 102, 103, 104],
            "Ad Soyad": ["Ahmet Yılmaz", "Ayşe Demir", "Mehmet Kaya", "Elif Şahin"],
            "Departman": ["Yönetim", "Lojistik", "Finans", "Pazarlama"],
            "Rol": ["Admin", "Editör", "İzleyici", "Editör"],
            "Durum": [True, True, True, False]
        })

        edited_df = st.data_editor(
            users_data,
            column_config={
                "Durum": st.column_config.CheckboxColumn("Aktif", help="Kullanıcı sisteme girebilir mi?", default=True),
                "Rol": st.column_config.SelectboxColumn("Yetki", options=["Admin", "Editör", "İzleyici"])
            },
            use_container_width=True,
            num_rows="dynamic",
            hide_index=True
        )
        
        col_act1, col_act2 = st.columns([1, 4])
        with col_act1:
            if st.button("Değişiklikleri Kaydet"):
                st.success("Kullanıcı veritabanı güncellendi.")

    # --- TAB 3: MODÜL YÖNETİMİ ---
    with tab3:
        st.markdown("### 🔌 Modül Görünürlük Ayarları")
        st.warning("Buradan kapattığınız modüller sol menüden gizlenir (Simülasyon).")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<div class='admin-card'>", unsafe_allow_html=True)
            st.markdown("#### 📦 Operasyon")
            st.toggle("Lojistik Modülü", value=True)
            st.toggle("Envanter Modülü", value=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with c2:
            st.markdown("<div class='admin-card'>", unsafe_allow_html=True)
            st.markdown("#### 📢 Pazarlama")
            st.toggle("Sosyal Medya", value=True)
            st.toggle("Reklam Yönetimi", value=False) # Varsayılan kapalı örnek
            st.markdown("</div>", unsafe_allow_html=True)
            
        with c3:
            st.markdown("<div class='admin-card'>", unsafe_allow_html=True)
            st.markdown("#### ⚙️ Araçlar")
            st.toggle("AI Asistan", value=True)
            st.toggle("Bakım Modu (Tüm Site)", value=False)
            st.markdown("</div>", unsafe_allow_html=True)

    # --- TAB 4: SİSTEM LOGLARI ---
    with tab4:
        st.markdown("### 📡 Canlı Sistem İzleme")
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("CPU Kullanımı", "%12", "-2%")
        m2.metric("RAM Kullanımı", "4.2 GB", "+120MB")
        m3.metric("API Gecikmesi", "240ms", "Normal")
        m4.metric("Aktif Kullanıcı", "4", "+1")
        
        st.markdown("#### Son İşlem Kayıtları")
        logs = pd.DataFrame({
            "Zaman": ["14:02", "14:00", "13:45", "13:30"],
            "Kullanıcı": ["Ahmet Y.", "Sistem", "Ayşe D.", "Mehmet K."],
            "İşlem": ["Lojistik Haritası Görüntülendi", "Otomatik Yedekleme", "Yeni Görev Eklendi", "Fatura Onaylandı"],
            "IP": ["192.168.1.1", "localhost", "192.168.1.14", "192.168.1.20"]
        })
        st.dataframe(logs, use_container_width=True, hide_index=True)

        if st.button("🗑️ Logları Temizle", type="primary"):
            st.toast("Sistem logları temizlendi.", icon="🧹")
