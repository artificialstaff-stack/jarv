import streamlit as st
import sys
import os

# Yolları ekle (Views ve Logic'i bulması için)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

# Modülleri çağır
import login, dashboard, logistics, inventory, plan, documents, todo, forms
import styles

# 1. AYARLAR
st.set_page_config(page_title="ARTIS | SaaS", page_icon="🌍", layout="wide")
styles.load_css()

# 2. STATE
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

# 3. YÖNLENDİRME (ROUTER)
if not st.session_state.logged_in:
    login.render_login_page()
else:
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.user_data.get('brand', 'Marka')}")
        menu = st.radio(
            "MENÜ", 
            ["📊 Dashboard", "📦 Lojistik", "📋 Envanter", "📝 Formlar", "📂 Dokümanlar", "✅ Yapılacaklar", "💎 Planlar"],
            label_visibility="collapsed"
        )
        st.markdown("---")
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()

    # Sayfa Seçimi
    if menu == "📊 Dashboard": dashboard.render_dashboard()
    elif menu == "📦 Lojistik": logistics.render_logistics()
    elif menu == "📋 Envanter": inventory.render_inventory()
    elif menu == "📝 Formlar": forms.render_forms()
    elif menu == "📂 Dokümanlar": documents.render_documents()
    elif menu == "✅ Yapılacaklar": todo.render_todo()
    elif menu == "💎 Planlar": plan.render_plans()
