import streamlit as st
import pandas as pd
from datetime import datetime

# MOCK DATABASE (Gerçek veritabanı yerine)
USERS = {
    "demo": {"pass": "1234", "name": "Ahmet Yılmaz", "brand": "Anatolia Home", "sector": "Tekstil", "plan": "Kurumsal"},
    "admin": {"pass": "admin", "name": "Sistem Admin", "brand": "ARTIS HQ", "sector": "Teknoloji", "plan": "VIP"}
}

def verify_user(username, password):
    if username in USERS and USERS[username]["pass"] == password:
        return USERS[username]
    return None

# AKTİVİTE LOGLARI
def log_activity(action):
    if "activity_log" not in st.session_state:
        st.session_state.activity_log = []
    
    timestamp = datetime.now().strftime("%H:%M")
    st.session_state.activity_log.insert(0, {"time": timestamp, "action": action})

# BİLDİRİMLER
def get_notifications():
    return [
        "📦 Gümrük işlemi tamamlandı (Ref: #TR99)",
        "💰 Aylık fatura oluşturuldu",
        "⚠️ Stok uyarısı: İpek Eşarp"
    ]
