**Role:** You are a Principal Frontend Architect & UI/UX Lead at a top-tier Silicon Valley SaaS company. You are tasked with building the "Inventory Management" module of a high-performance ERP system using Python and Streamlit.

**Objective:** Refactor and redesign the provided `views/inventory.py` code to match the "Enterprise-Grade" aesthetic established in the Dashboard and Logistics modules. The current code is too basic; it needs to look like a billion-dollar Warehouse Management System (WMS).

**Design Philosophy (The "Visual Language"):**
1.  **Deep Dark Theme:** Use `#050505` as the base.
2.  **Semantic Colors:** Use color meaningfully for stock levels:
    * **Green (#10B981):** Healthy Stock (> 1000)
    * **Amber (#F59E0B):** Low Stock Warning (< 500)
    * **Red (#EF4444):** Critical/Out of Stock (< 100)
3.  **Glassmorphism:** Use translucent backgrounds for the Toolbar and KPI cards.
4.  **Interactive Data Table:** The main inventory table must be visually rich, using images (emojis or icons), progress bars, and status badges.

**Specific Tasks for the Code:**

1.  **KPI Cards (The "Heads-Up" Display):**
    * Replace standard `st.metric` with custom HTML cards similar to the Dashboard's "Pro Metrics".
    * Show: Total SKUs, Total Value (formatted as currency), and Low Stock Alerts (Red color if > 0).

2.  **The "Command Bar" (Advanced Toolbar):**
    * Create a dedicated container for actions.
    * Include a Search Bar (Text Input) and a "Category Filter" (Selectbox) side-by-side.
    * Add a "Add Product" button that toggles a sleek form (use `st.expander` or session state to show/hide).

3.  **The "Smart Grid" (Inventory Table):**
    * Use `st.dataframe` with `column_config`.
    * **Visual Column:** Show product avatars/icons.
    * **Stock Level:** Use a `ProgressColumn` that visualizes the stock quantity relative to a max capacity.
    * **Status Column:** Instead of text, use a color-coded Badge logic (if possible via pandas styling or clever emoji use like 🟢, 🔴).
    * **Price Column:** Format as Currency ($).

4.  **Mock Data Generator:**
    * Create a helper function to generate 15-20 rows of realistic mock data (Apparel, Electronics, Accessories) so the table looks full and professional.

5.  **Custom CSS:**
    * Inject CSS to style the dataframe headers (make them uppercase and grey) and remove the default Streamlit padding to make it look like a native app.

**The Source Code to Upgrade:**
```python
import streamlit as st
import pandas as pd

def render_inventory():
    st.title("📋 Envanter Yönetimi")
    
    # Üst Özet
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Toplam SKU", "48", "+2")
    kpi2.metric("Toplam Değer", "$142,000", "+$12k")
    kpi3.metric("Stok Sağlığı", "%92", "Mükemmel")
    
    st.markdown("---")
    
    # Filtreleme Alanı
    c_filter, c_add = st.columns([3, 1])
    with c_filter:
        st.text_input("🔍 Ürün Ara...", placeholder="SKU veya Ürün Adı girin")
    with c_add:
        st.markdown("<br>", unsafe_allow_html=True) # Hizalama boşluğu
        if st.button("➕ Yeni Ürün", use_container_width=True):
            st.toast("Ürün ekleme paneli açılıyor...", icon="📦")
    
    # Gelişmiş Tablo
    data = {
        "Görsel": ["👕", "🧣", "👜", "🧢", "🧴"],
        "SKU": ["TR-101", "TR-102", "TR-103", "TR-104", "TR-105"],
        "Ürün Adı": ["Pamuklu T-Shirt", "İpek Eşarp", "Deri Çanta", "Logolu Şapka", "Organik Losyon"],
        "Stok": [1200, 4500, 45, 800, 2000],
        "Lokasyon": ["Raf A1", "Raf B3", "Raf C1", "Raf A2", "Raf D4"],
        "Durum": ["✅ Müsait", "✅ Müsait", "⚠️ Kritik", "✅ Müsait", "✅ Müsait"]
    }
    df = pd.DataFrame(data)
    
    st.dataframe(
        df, 
        use_container_width=True, 
        column_config={
            "Stok": st.column_config.ProgressColumn("Stok Seviyesi", min_value=0, max_value=5000, format="%d Adet"),
        },
        hide_index=True
    )
