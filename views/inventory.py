import streamlit as st
import pandas as pd
import random

# ==============================================================================
# 🎨 1. SAYFAYA ÖZEL STİL (ENVANTER İÇİN)
# ==============================================================================
def inject_inventory_css():
    st.markdown("""
    <style>
        /* KPI Kartları için Özel Tasarım */
        .inv-kpi-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 5px;
            transition: transform 0.2s, border-color 0.2s;
        }
        .inv-kpi-card:hover {
            transform: translateY(-2px);
            border-color: rgba(255, 255, 255, 0.15);
            background: rgba(255, 255, 255, 0.05);
        }
        .kpi-label { color: #A1A1AA; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 500; }
        .kpi-value { color: #FFF; font-size: 24px; font-weight: 700; }
        .kpi-badge { 
            align-self: flex-start;
            font-size: 11px; 
            padding: 3px 8px; 
            border-radius: 20px; 
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }
        .badge-green { background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.2); }
        .badge-red { background: rgba(239, 68, 68, 0.15); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.2); }
        .badge-blue { background: rgba(59, 130, 246, 0.15); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.2); }

        /* Filtre Alanı */
        .toolbar-container {
            background-color: #0E0E10;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            border: 1px solid #1F1F23;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🛠️ 2. YARDIMCI FONKSİYONLAR
# ==============================================================================
def render_kpi(label, value, badge_text, badge_type="green", icon="bx-stats"):
    st.markdown(f"""
    <div class="inv-kpi-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div class="kpi-label">{label}</div>
            <i class='bx {icon}' style="color:#52525B; font-size:18px;"></i>
        </div>
        <div class="kpi-value">{value}</div>
        <span class="kpi-badge badge-{badge_type}">{badge_text}</span>
    </div>
    """, unsafe_allow_html=True)

def get_inventory_data():
    """Gerçekçi envanter verisi üretir."""
    products = [
        {"icon": "🧥", "name": "Kaşmir Palto", "sku": "TR-881", "cat": "Giyim", "stock": 120, "price": 4500, "status": "✅ Yüksek"},
        {"icon": "👜", "name": "Deri Çanta", "sku": "TR-902", "cat": "Aksesuar", "stock": 45, "price": 2800, "status": "⚠️ Kritik"},
        {"icon": "🧣", "name": "İpek Şal", "sku": "TR-334", "cat": "Aksesuar", "stock": 850, "price": 1200, "status": "⚡ Normal"},
        {"icon": "👞", "name": "Oxford Ayakkabı", "sku": "TR-112", "cat": "Ayakkabı", "stock": 320, "price": 3500, "status": "⚡ Normal"},
        {"icon": "⌚", "name": "Akıllı Saat", "sku": "EL-551", "cat": "Elektronik", "stock": 15, "price": 8900, "status": "🚨 Tükeniyor"},
        {"icon": "🎧", "name": "Kablosuz Kulaklık", "sku": "EL-229", "cat": "Elektronik", "stock": 210, "price": 1500, "status": "⚡ Normal"},
        {"icon": "🧢", "name": "Logolu Şapka", "sku": "TR-005", "cat": "Aksesuar", "stock": 1500, "price": 450, "status": "✅ Yüksek"},
        {"icon": "🧴", "name": "Organik Losyon", "sku": "KZ-101", "cat": "Kozmetik", "stock": 2000, "price": 320, "status": "✅ Yüksek"},
        {"icon": "🕶️", "name": "Güneş Gözlüğü", "sku": "TR-404", "cat": "Aksesuar", "stock": 90, "price": 1850, "status": "⚠️ Kritik"},
    ]
    return pd.DataFrame(products)

# ==============================================================================
# 🚀 3. ANA RENDER FONKSİYONU
# ==============================================================================
def render_inventory():
    inject_inventory_css()
    
    # --- HEADER ---
    c1, c2 = st.columns([3, 1])
    with c1:
        st.title("📦 Envanter Yönetimi")
        st.caption("Depo stok durumu, ürün değerlemeleri ve kritik seviye takibi.")
    with c2:
         # Butonu sağa yaslamak için boşluk
         st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
         if st.button("➕ Yeni Ürün Ekle", type="primary", use_container_width=True):
             st.toast("Ekleme modülü açılıyor...", icon="⚡")

    st.markdown("---")

    # --- KPI GRİD (4 SÜTUN) ---
    k1, k2, k3, k4 = st.columns(4)
    with k1: render_kpi("Toplam SKU", "1,240", "+12 Yeni", "blue", "bx-package")
    with k2: render_kpi("Depo Değeri", "₺4.2M", "+%5.4", "green", "bx-money")
    with k3: render_kpi("Kritik Stok", "24 Ürün", "⚠️ Aksiyon Al", "red", "bx-error-circle")
    with k4: render_kpi("Stok Devir", "4.8", "🚀 Yüksek", "green", "bx-refresh")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- GELİŞMİŞ FİLTRE & TABLO ALANI ---
    # Toolbar
    col_search, col_filter, col_sort = st.columns([2, 1, 1])
    with col_search:
        search_term = st.text_input("🔍 Ürün Ara", placeholder="SKU, İsim veya Barkod...", label_visibility="collapsed")
    with col_filter:
        cat_filter = st.selectbox("Kategori", ["Tümü", "Giyim", "Aksesuar", "Elektronik", "Kozmetik"], label_visibility="collapsed")
    with col_sort:
        sort_by = st.selectbox("Sıralama", ["Stok (Azalan)", "Stok (Artan)", "Fiyat (Yüksek)"], label_visibility="collapsed")

    # Veriyi Hazırla
    df = get_inventory_data()
    
    # Filtreleme Mantığı
    if search_term:
        df = df[df['name'].str.contains(search_term, case=False) | df['sku'].str.contains(search_term, case=False)]
    if cat_filter != "Tümü":
        df = df[df['cat'] == cat_filter]

    # --- AKILLI TABLO (SMART TABLE) ---
    st.dataframe(
        df,
        column_config={
            "icon": st.column_config.TextColumn("Görsel", width="small"),
            "name": st.column_config.TextColumn("Ürün Adı", width="medium"),
            "sku": st.column_config.TextColumn("SKU", help="Stok Kodu"),
            "cat": st.column_config.TextColumn("Kategori"),
            "price": st.column_config.NumberColumn("Birim Fiyat", format="₺%d"),
            "stock": st.column_config.ProgressColumn(
                "Stok Seviyesi",
                format="%d Adet",
                min_value=0,
                max_value=2000,
            ),
            "status": st.column_config.TextColumn("Durum")
        },
        use_container_width=True,
        hide_index=True,
        height=500
    )
