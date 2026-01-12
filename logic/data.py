import streamlit as st
from datetime import datetime

# MÜŞTERİLER
USERS = {
    "demo": {"pass": "1234", "name": "Ahmet Yılmaz", "brand": "Anatolia Home", "plan": "Kurumsal"},
    "admin": {"pass": "admin", "name": "Sistem Yöneticisi", "brand": "ARTIS HQ", "plan": "VIP"}
}

def verify_user(u, p):
    if u in USERS and USERS[u]["pass"] == p: return USERS[u]
    return None

def log_activity(action):
    if "activity_log" not in st.session_state: st.session_state.activity_log = []
    st.session_state.activity_log.insert(0, {"time": datetime.now().strftime("%H:%M"), "action": action})
