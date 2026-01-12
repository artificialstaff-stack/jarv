import streamlit as st
import sys
import os

# Yolları ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

import login, dashboard, logistics, inventory, forms, documents, settings
import styles

# 1. CONFIG
st.set_page_config(page_title="ARTIS | Enterprise OS", page_icon="🌍", layout="wide")
styles.load_css()

# 2. STATE
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

# 3. ROUTER
if not st.session_state.logged_in:
    login.render_login_page()
else:
    # SIDEBAR
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.user_data['brand']}")
        menu = st.radio(
            "MENÜ", 
            ["📊 Dashboard", "📦 Lojistik", "📋 Envanter", "📝 Formlar", "📂 Belgeler", "⚙️ Ayarlar"],
            label_visibility="collapsed"
        )
        st.markdown("---")
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()

    # PAGES
    if menu == "📊 Dashboard": dashboard.render_dashboard()
    elif menu == "📦 Lojistik": logistics.render_logistics()
    elif menu == "📋 Envanter": inventory.render_inventory()
    elif menu == "📝 Formlar": forms.render_forms()
    elif menu == "📂 Belgeler": documents.render_documents()
    elif menu == "⚙️ Ayarlar": settings.render_settings()
