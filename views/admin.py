import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time
import random
from datetime import datetime, timedelta

# --- GÜVENLİK KATMANI ---
def check_admin_access():
    if st.session_state.user_data.get('role') != 'admin':
        st.error("⛔ YETKİSİZ GİRİŞ TESPİT EDİLDİ (ERROR 403)")
        st.stop()

# --- CORTEX AI BEYNİ (NLP -> ACTION) ---
def cortex_brain(prompt):
    """
    Doğal dil komutlarını sistem aksiyonuna çeviren yönetici zekası.
    """
    prompt = prompt.lower()
    users = st.session_state.users_db # app.py'deki global veritabanı
    
    # 1. BANLAMA / KISITLAMA
    if any(x in prompt for x in ["banla", "kısıtla", "dondur", "blokla"]):
        for user in users:
            if user['name'].lower() in prompt:
                user['status'] = "Suspended"
                return f"🚫 AKSİYON ALINDI: {user['name']} kullanıcısı sistemden banlandı ve oturumu sonlandırıldı."
        return "⚠️ HATA: Kullanıcı veritabanında bulunamadı."

    # 2. AKTİFLEŞTİRME
    elif any(x in prompt for x in ["aç", "aktif et", "yetki ver", "kaldır"]):
        for user in users:
            if user['name'].lower() in prompt:
                user['status'] = "Active"
                return f"✅ ONAYLANDI: {user['name']} kullanıcısının erişim engeli kaldırıldı."
        return "⚠️ HATA: Kullanıcı bulunamadı."

    # 3. YÖNETİCİ YAPMA
    elif any(x in prompt for x in ["admin yap", "yönetici yap", "terfi"]):
        for user in users:
            if user['name'].lower() in prompt:
                user['role'] = "admin"
                return f"🛡️ YETKİ YÜKSELTİLDİ: {user['name']} artık Root/Admin yetkilerine sahip."
        return "⚠️ HATA: Kullanıcı bulunamadı."
    
    # 4. GENEL DURUM
    elif "rapor" in prompt or "durum" in prompt:
        active = sum(1 for u in users if u['status'] == 'Active')
        mrr = sum(u.get('mrr', 0) for u in users)
        return f"📊 SİSTEM DURUMU:\n- Aktif Kullanıcı: {active}\n- Toplam MRR: ${mrr}\n- Sunucu Yükü: %34 (Stabil)"

    else:
        return "🤖 CORTEX: Komut anlaşılamadı. Örn: 'Ahmet'i banla', 'Rapor ver'."

# --- STİL & TASARIM ---
def inject_admin_css():
    st.markdown("""
    <style>
        /* Header Card */
        .admin-header-card {
            background: linear-gradient(135deg, #111 0%, #050505 100%);
            border: 1px solid rgba(239, 68, 68, 0.2);
            padding: 25px;
            border-radius: 16px;
            margin-bottom: 25px;
        }
        .admin-badge {
            background: rgba(220, 38, 38, 0.15);
            color: #EF4444;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 800;
            border: 1px solid rgba(220, 38, 38, 0.3);
        }
        
        /* CORTEX Terminal */
        .cortex-terminal {
            background-color: #0d0d0d;
            border: 1px solid #333;
            border-left: 4px solid #EF4444;
            border-radius: 8px;
            padding: 20px;
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 30px;
        }
        .ai-msg { color: #e0e0e0; margin-top: 5px; }
        .user-msg { color: #EF4444; font-weight: bold; margin-top: 10px; }

        /* Metric Boxes */
        .metric-box {
            background: #0A0A0A;
            border: 1px solid #222;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }
        .metric-val { font-size: 28px; font-weight: 700; color: #FFF; }
        .metric-lbl { font-size: 12px; color: #666; text-transform: uppercase; }
        .delta-pos { color: #10B981; font-size: 11px; }
        .delta-neg { color: #EF4444; font-size: 11px; }
    </style>
    """, unsafe_allow_html=True)

# --- GRAFİKLER ---
def revenue_chart():
    dates = pd.date_range(end=datetime.today(), periods=12, freq='M')
    values = [12000, 14500, 18000, 22000, 21500, 26000, 31000, 38000, 42000, 48000, 55000, 62400]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=values, mode='lines+markers', line=dict(color='#EF4444', width=3), fill='tozeroy', fillcolor='rgba(239, 68, 68, 0.1)'))
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=10,b=10,l=10,r=10), height=250)
    return fig

# --- ANA RENDER ---
def render():
    check_admin_access()
    inject_admin_css()

    # 1. HEADER
    st.markdown("""
        <div class='admin-header-card'>
            <div style='display:flex; justify-content:space-between; align-items:start;'>
                <div>
                    <div class='admin-badge'>CORTEX ENABLED</div>
                    <h1 style='margin:10px 0 5px 0; font-size:2rem;'>ARTIS HQ Komuta Merkezi</h1>
                    <p style='color:#888; margin:0; font-size:14px;'>SaaS Altyapısı ve Yapay Zeka Yönetim Katmanı</p>
                </div>
                <div style='text-align:right;'>
                    <div style='color:#EF4444; font-weight:700; font-size:24px;'>$62,400</div>
                    <div style='color:#666; font-size:11px;'>MRR (AYLIK GELİR)</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. CORTEX AI TERMİNALİ (YENİ EKLEME)
    st.markdown("### 🧠 CORTEX Yönetici Ajanı")
    st.caption("Sistemi doğal dille yönetin. Örn: 'Ahmet Yılmaz'ı banla', 'Sistem raporu ver'.")
    
    with st.container():
        st.markdown("<div class='cortex-terminal'>", unsafe_allow_html=True)
        
        # Geçmişi Göster
        if "cortex_history" not in st.session_state:
            st.session_state.cortex_history = [{"role": "ai", "content": "Sistemler hazır. Komut bekliyorum..."}]
        
        for msg in st.session_state.cortex_history[-3:]: # Son 3 mesajı göster
            if msg['role'] == 'user':
                st.markdown(f"<div class='user-msg'>> {msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='ai-msg'>{msg['content']}</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Komut Girişi
        cortex_input = st.chat_input("CORTEX'e emir ver...")
        if cortex_input:
            st.session_state.cortex_history.append({"role": "user", "content": cortex_input})
            with st.spinner("İşleniyor..."):
                time.sleep(0.5)
                resp = cortex_brain(cortex_input)
                st.session_state.cortex_history.append({"role": "ai", "content": resp})
            st.rerun()

    st.markdown("---")

    # 3. KPI GRID (MEVCUT KOD)
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.markdown("<div class='metric-box'><div class='metric-lbl'>Aktif Müşteri</div><div class='metric-val'>1,240</div><div class='metric-delta delta-pos'>+%12</div></div>", unsafe_allow_html=True)
    with k2: st.markdown("<div class='metric-box'><div class='metric-lbl'>Churn Rate</div><div class='metric-val'>%2.1</div><div class='metric-delta delta-pos'>-%0.4</div></div>", unsafe_allow_html=True)
    with k3: st.markdown("<div class='metric-box'><div class='metric-lbl'>API Maliyeti</div><div class='metric-val'>$4,200</div><div class='metric-delta delta-neg'>+%8</div></div>", unsafe_allow_html=True)
    with k4: st.markdown("<div class='metric-box'><div class='metric-lbl'>Sunucu Sağlığı</div><div class='metric-val'>%98.9</div><div class='metric-delta delta-pos'>Stabil</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. YÖNETİM SEKMELERİ
    tabs = st.tabs(["👥 Canlı Veritabanı (AI Sync)", "🚀 Özellik Kontrolü", "📢 Duyuru", "⚙️ Sistem Logları"])

    # --- TAB 1: CANLI VERİTABANI (APP.PY İLE SENKRONİZE) ---
    with tabs[0]:
        st.subheader("Global Kullanıcı Listesi")
        st.info("Bu tablo CORTEX AI ile senkronizedir. AI üzerinden yapılan banlamalar burada anında görülür.")
        
        # app.py'deki veritabanını DataFrame'e çevir
        current_db = pd.DataFrame(st.session_state.users_db)
        
        edited_df = st.data_editor(
            current_db,
            column_config={
                "status": st.column_config.SelectboxColumn("Statü", options=["Active", "Suspended", "Pending"], width="medium"),
                "role": st.column_config.SelectboxColumn("Yetki", options=["admin", "editor", "viewer"], width="small"),
                "mrr": st.column_config.NumberColumn("Gelir ($)", format="$%d")
            },
            use_container_width=True,
            hide_index=True,
            key="user_editor"
        )
        
        # Manuel değişiklikleri kaydet
        if st.button("💾 Manuel Değişiklikleri Kaydet", type="primary"):
            # DataFrame'i geri dict listesine çevirip session_state'e kaydet
            st.session_state.users_db = edited_df.to_dict('records')
            st.toast("Veritabanı güncellendi.", icon="✅")

    # --- TAB 2: ÖZELLİK ANAHTARLARI ---
    with tabs[1]:
        st.subheader("Modül Yönetimi")
        f1, f2, f3 = st.columns(3)
        with f1:
            st.container(border=True).markdown("#### 🤖 AI Lead Gen")
            st.toggle("Beta Erişim", value=True)
        with f2:
            st.container(border=True).markdown("#### 💳 Stripe Ödeme")
            st.toggle("Sandbox Modu", value=True)
        with f3:
            st.container(border=True).markdown("#### 📱 Mobil API")
            st.toggle("API v2", value=True)

    # --- TAB 3: GLOBAL DUYURU ---
    with tabs[2]:
        col_ann1, col_ann2 = st.columns([1, 1])
        with col_ann1:
            st.subheader("Sistem Duyurusu")
            ann_type = st.selectbox("Tip", ["Bilgi", "Kritik"])
            ann_msg = st.text_area("Mesaj", "Örn: Sistem bakımı...")
            if st.button("Gönder"):
                st.toast("İletildi!", icon="🚀")
        with col_ann2:
            st.subheader("Aktif Duyurular")
            st.warning("⚠️ Planlı Bakım: 20 Ocak")

    # --- TAB 4: FİNANS & LOGLAR ---
    with tabs[3]:
        st.subheader("Finansal Büyüme")
        st.plotly_chart(revenue_chart(), use_container_width=True)
        st.divider()
        st.subheader("Sistem Logları")
        logs = pd.DataFrame({
            "Zaman": ["14:42", "14:40"],
            "Seviye": ["INFO", "WARNING"],
            "Mesaj": ["Admin login successful", "High CPU usage"]
        })
        st.dataframe(logs, use_container_width=True, hide_index=True)

    # Footer
    st.markdown("---")
    st.caption("CORTEX AI Engine v1.0 | Root Access Active")
