import streamlit as st
import brain
import pandas as pd
import random
from datetime import datetime, timedelta

# ==============================================================================
# 🎨 1. SAYFAYA ÖZEL STİL (LOJİSTİK İÇİN)
# ==============================================================================
def inject_logistics_css():
    st.markdown("""
    <style>
        /* Tablo Başlıkları */
        th { color: #A1A1AA !important; font-weight: 600 !important; }
        
        /* Gelişmiş Filtre Alanı */
        .filter-container {
            background-color: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.05);
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🛠️ 2. YARDIMCI VERİ OLUŞTURUCU (MOCK DATA)
# ==============================================================================
def get_shipment_data():
    """
    Sanki veritabanından geliyormuş gibi zengin bir lojistik tablosu oluşturur.
    """
    data = [
        {"ID": "TR-8821", "Rota": "Istanbul ➝ New York", "Tip": "Deniz", "Durum": "Yolda", "İlerleme": 65, "ETA": "14 Jan"},
        {"ID": "TR-9942", "Rota": "Ankara ➝ Berlin", "Tip": "Hava", "Durum": "Gümrükte", "İlerleme": 80, "ETA": "12 Jan"},
        {"ID": "CN-1102", "Rota": "Shanghai ➝ Istanbul", "Tip": "Deniz", "Durum": "Gecikmeli", "İlerleme": 40, "ETA": "22 Jan"},
        {"ID": "US-3321", "Rota": "Miami ➝ London", "Tip": "Hava", "Durum": "Teslim Edildi", "İlerleme": 100, "ETA": "10 Jan"},
        {"ID": "TR-7714", "Rota": "Izmir ➝ Tokyo", "Tip": "Deniz", "Durum": "Hazırlanıyor", "İlerleme": 10, "ETA": "02 Feb"},
    ]
    return pd.DataFrame(data)

# ==============================================================================
# 🧩 3. UI BİLEŞENLERİ
# ==============================================================================
def render_kpi_card(title, value, icon, color):
    """Lojistik KPI Kartı"""
    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.03); 
        border: 1px solid rgba(255,255,255,0.05); 
        padding: 20px; 
        border-radius: 16px; 
        display: flex; 
        align-items: center; 
        gap: 15px;">
        <div style="
            width: 48px; height: 48px; 
            background: {color}20; 
            color: {color}; 
            border-radius: 12px; 
            display: flex; align-items: center; justify-content: center; font-size: 24px;">
            <i class='bx {icon}'></i>
        </div>
        <div>
            <div style="color: #A1A1AA; font-size: 13px; text-transform: uppercase; font-weight: 500;">{title}</div>
            <div style="color: #FFF; font-size: 24px; font-weight: 700;">{value}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🚀 4. ANA RENDER FONKSİYONU
# ==============================================================================
def render_logistics():
    inject_logistics_css()
    
    # --- ÜST BAŞLIK ---
    c1, c2 = st.columns([3, 1])
    with c1:
        st.title("🌍 Global Lojistik Ağı")
        st.caption("Gerçek zamanlı sevkiyat takibi ve rota optimizasyonu.")
    with c2:
        # Sağ üste aksiyon butonu
        st.button("➕ Yeni Sevkiyat", use_container_width=True, type="primary")

    st.markdown("---")

    # --- KPI KARTLARI (3'lü Grid) ---
    k1, k2, k3, k4 = st.columns(4)
    with k1: render_kpi_card("Aktif Sevkiyat", "12", "bx-map-pin", "#3B82F6")
    with k2: render_kpi_card("Yoldaki Yük", "840 Ton", "bx-package", "#8B5CF6")
    with k3: render_kpi_card("Gecikmeler", "1", "bx-error-circle", "#F59E0B")
    with k4: render_kpi_card("Teslimat %", "%98.2", "bx-check-circle", "#10B981")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ANA İÇERİK: HARİTA VE LİSTE ---
    col_map, col_list = st.columns([1.5, 1], gap="medium")

    # SOL: HOLOGRAFİK HARİTA
    with col_map:
        st.markdown("##### 📍 Canlı Rota Haritası")
        with st.container(border=True):
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            
        # Alt Bilgi (AI Insight)
        st.info("🤖 **AI Optimizasyonu:** Süveyş Kanalı rotasında yoğunluk tespit edildi. 'TR-7714' nolu sevkiyat için alternatif rota hesaplanıyor.")

    # SAĞ: AKILLI SEVKİYAT LİSTESİ
    with col_list:
        st.markdown("##### 📋 Sevkiyat Listesi")
        
        # Filtreleme (Görünmez kutu içinde)
        search = st.text_input("Sevkiyat Ara (ID veya Şehir)", placeholder="Örn: Istanbul...")
        
        df = get_shipment_data()
        
        # Arama mantığı
        if search:
            df = df[df['Rota'].str.contains(search, case=False) | df['ID'].str.contains(search, case=False)]

        # --- NEXT-GEN TABLE CONFIGURATION ---
        st.dataframe(
            df,
            column_config={
                "ID": st.column_config.TextColumn("Kargo ID", help="Takip Numarası"),
                "Rota": st.column_config.TextColumn("Güzergah", width="medium"),
                "Tip": st.column_config.TextColumn("Mod"),
                "Durum": st.column_config.Column(
                    "Statü",
                    width="small",
                    help="Güncel Durum"
                ),
                "İlerleme": st.column_config.ProgressColumn(
                    "Tahmini Varış",
                    format="%d%%",
                    min_value=0,
                    max_value=100,
                ),
                "ETA": "Varış"
            },
            hide_index=True,
            use_container_width=True,
            height=400
        )
