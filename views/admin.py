import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time
from datetime import datetime, timedelta

# --- GÜVENLİK KATMANI ---
def check_admin_access():
    if st.session_state.user_data.get('role') != 'admin':
        st.error("⛔ YETKİSİZ GİRİŞ TESPİT EDİLDİ (ERROR 403)")
        st.stop()

# --- STİL & TASARIM ---
def inject_admin_css():
    st.markdown("""
    <style>
        .admin-header-card {
            background: linear-gradient(135deg, #111 0%, #050505 100%);
            border: 1px solid rgba(239, 68, 68, 0.2);
            padding: 25px;
            border-radius: 16px;
            margin-bottom: 25px;
            position: relative;
            overflow: hidden;
        }
        .admin-badge {
            background: rgba(220, 38, 38, 0.15);
            color: #EF4444;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1px;
            border: 1px solid rgba(220, 38, 38, 0.3);
        }
        .metric-box {
            background: #0A0A0A;
            border: 1px solid #222;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }
        .metric-val { font-size: 28px; font-weight: 700; color: #FFF; }
        .metric-lbl { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 1px; }
        .metric-delta { font-size: 11px; font-weight: 600; margin-top: 5px; }
        .delta-pos { color: #10B981; }
        .delta-neg { color: #EF4444; }
    </style>
    """, unsafe_allow_html=True)

# --- GRAFİKLER ---
def revenue_chart():
    # Sahte MRR Verisi
    dates = pd.date_range(end=datetime.today(), periods=12, freq='M')
    values = [12000, 14500, 18000, 22000, 21500, 26000, 31000, 38000, 42000, 48000, 55000, 62400]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates, y=values, mode='lines+markers',
        line=dict(color='#EF4444', width=3),
        fill='tozeroy', fillcolor='rgba(239, 68, 68, 0.1)'
    ))
    fig.update_layout(
        template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=10,b=10,l=10,r=10), height=250,
        xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)')
    )
    return fig

# --- ANA RENDER ---
def render():
    check_admin_access()
    inject_admin_css()

    # 1. HEADER (GOD MODE)
    st.markdown("""
        <div class='admin-header-card'>
            <div style='display:flex; justify-content:space-between; align-items:start;'>
                <div>
                    <div class='admin-badge'>SUPER ADMIN</div>
                    <h1 style='margin:10px 0 5px 0; font-size:2rem;'>ARTIS HQ Komuta Merkezi</h1>
                    <p style='color:#888; margin:0; font-size:14px;'>SaaS Altyapısı, Faturalandırma ve Sistem Sağlığı Yönetimi</p>
                </div>
                <div style='text-align:right;'>
                    <div style='color:#EF4444; font-weight:700; font-size:24px;'>$62,400</div>
                    <div style='color:#666; font-size:11px;'>AYLIK TEKRARLAYAN GELİR (MRR)</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. KPI GRID
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.markdown("<div class='metric-box'><div class='metric-lbl'>Aktif Müşteri</div><div class='metric-val'>1,240</div><div class='metric-delta delta-pos'>+%12 Bu Ay</div></div>", unsafe_allow_html=True)
    with k2: st.markdown("<div class='metric-box'><div class='metric-lbl'>Churn Rate</div><div class='metric-val'>%2.1</div><div class='metric-delta delta-pos'>-%0.4 İyileşme</div></div>", unsafe_allow_html=True)
    with k3: st.markdown("<div class='metric-box'><div class='metric-lbl'>API Maliyeti</div><div class='metric-val'>$4,200</div><div class='metric-delta delta-neg'>+%8 Artış</div></div>", unsafe_allow_html=True)
    with k4: st.markdown("<div class='metric-box'><div class='metric-lbl'>Sunucu Sağlığı</div><div class='metric-val'>%98.9</div><div class='metric-delta delta-pos'>Stabil</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. YÖNETİM SEKMELERİ
    tabs = st.tabs(["👥 Müşteri Yönetimi", "🚀 Özellik Kontrolü (Feature Flags)", "📢 Duyuru & Bildirim", "⚙️ Sistem Ayarları"])

    # --- TAB 1: MÜŞTERİ YÖNETİMİ & GHOSTING ---
    with tabs[0]:
        c_left, c_right = st.columns([2, 1])
        
        with c_left:
            st.subheader("Müşteri Veritabanı")
            users_df = pd.DataFrame([
                {"ID": 101, "Müşteri": "Anatolia Home", "Paket": "Enterprise", "Durum": "Aktif", "Son Giriş": "1 dk önce"},
                {"ID": 102, "Müşteri": "Cyber Systems", "Paket": "Startup", "Durum": "Aktif", "Son Giriş": "2 saat önce"},
                {"ID": 103, "Müşteri": "Global Trade Co", "Paket": "Pro", "Durum": "Ödeme Bekliyor", "Son Giriş": "3 gün önce"},
            ])
            
            edited_df = st.data_editor(
                users_df,
                column_config={
                    "Durum": st.column_config.SelectboxColumn("Statü", options=["Aktif", "Askıya Alındı", "Ödeme Bekliyor"], width="medium"),
                    "Paket": st.column_config.SelectboxColumn("Plan", options=["Startup", "Pro", "Enterprise"], width="small")
                },
                use_container_width=True,
                hide_index=True
            )
            
            if st.button("💾 Değişiklikleri Kaydet", type="primary"):
                st.toast("Müşteri veritabanı güncellendi.", icon="✅")

        with c_right:
            st.container(border=True).markdown("#### 👻 Ghost Mode (Login As)")
            st.info("Kullanıcının şifresini bilmeden, onun paneline giriş yapın ve sorunları yerinde tespit edin.")
            target_user = st.selectbox("Hesap Seçin", ["Anatolia Home", "Cyber Systems"])
            if st.button(f"{target_user} Olarak Giriş Yap"):
                st.warning(f"Simülasyon: {target_user} dashboard'una yönlendiriliyorsunuz... (Demo)")

    # --- TAB 2: ÖZELLİK ANAHTARLARI (FEATURE FLAGS) ---
    with tabs[1]:
        st.subheader("Modül ve Özellik Yönetimi")
        st.caption("Kod deploy etmeden özellikleri anlık olarak açıp kapatın.")
        
        f1, f2, f3 = st.columns(3)
        with f1:
            st.container(border=True).markdown("#### 🤖 AI Lead Gen")
            st.toggle("Beta Erişim (Tüm Müşteriler)", value=True)
            st.toggle("Sadece Enterprise", value=False)
        
        with f2:
            st.container(border=True).markdown("#### 💳 Stripe Ödeme")
            st.toggle("Bakım Modu", value=False)
            st.toggle("Test Modu (Sandbox)", value=True)
            
        with f3:
            st.container(border=True).markdown("#### 📱 Mobil API")
            st.toggle("API v2 Erişimi", value=True)
            st.toggle("Eski API'yi Kapat", value=False)

    # --- TAB 3: GLOBAL DUYURU ---
    with tabs[2]:
        col_ann1, col_ann2 = st.columns([1, 1])
        with col_ann1:
            st.subheader("📢 Sistem Duyurusu Gönder")
            ann_type = st.selectbox("Duyuru Tipi", ["Bilgi (Mavi)", "Başarı (Yeşil)", "Uyarı (Sarı)", "Kritik (Kırmızı)"])
            ann_msg = st.text_area("Mesaj İçeriği", "Örn: Sistem bakımı nedeniyle bu gece 03:00'da kısa süreli kesinti yaşanacaktır.")
            
            if st.button("Tüm Kullanıcılara Gönder", type="primary"):
                st.toast("Duyuru 1,240 kullanıcıya iletildi!", icon="🚀")
        
        with col_ann2:
            st.subheader("Aktif Duyurular")
            st.info("ℹ️ Yeni AI Modülü yayında! (12 Oca - Aktif)")
            st.warning("⚠️ Planlı Bakım: 20 Ocak (Zamanlanmış)")

    # --- TAB 4: SİSTEM SAĞLIĞI & GELİR ---
    with tabs[3]:
        st.subheader("Finansal Büyüme (MRR)")
        st.plotly_chart(revenue_chart(), use_container_width=True)
        
        st.divider()
        st.subheader("Sistem Logları")
        logs = pd.DataFrame({
            "Zaman": ["14:42", "14:40", "14:38", "14:15"],
            "Seviye": ["INFO", "WARNING", "ERROR", "INFO"],
            "Kaynak": ["Auth Service", "Billing API", "AI Engine", "User DB"],
            "Mesaj": ["User ID:102 login successful", "Payment gateway timeout (300ms)", "OpenAI API Rate Limit Exceeded", "Database backup completed"]
        })
        st.dataframe(logs, use_container_width=True, hide_index=True)

    # Footer
    st.markdown("---")
    st.caption("ARTIS SaaS Engine v4.2 | Server: AWS us-east-1 | Latency: 24ms")
