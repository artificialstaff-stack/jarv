import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- GÜVENLİK KATMANI ---
def check_admin_access():
    """
    RBAC (Role-Based Access Control) Kontrolü
    Kullanıcı 'admin' yetkisine sahip değilse erişimi engeller.
    """
    user_role = st.session_state.user_data.get('role', 'user')
    if user_role != 'admin':
        st.error("⛔ YETKİSİZ ERİŞİM TESPİT EDİLDİ")
        st.warning("Bu alana erişim yetkiniz yok. Olay güvenlik loglarına işlendi.")
        st.stop() # Kodun geri kalanını durdur

def inject_admin_css():
    st.markdown("""
    <style>
        /* Admin Paneli Özel Kırmızı/Gri Tema */
        .admin-header {
            border-bottom: 1px solid rgba(239, 68, 68, 0.3);
            padding-bottom: 20px;
            margin-bottom: 20px;
        }
        .security-badge {
            background: rgba(239, 68, 68, 0.1);
            color: #EF4444;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 700;
            border: 1px solid rgba(239, 68, 68, 0.2);
            letter-spacing: 1px;
        }
        .stat-card {
            background: #111;
            border: 1px solid #333;
            padding: 20px;
            border-radius: 12px;
        }
    </style>
    """, unsafe_allow_html=True)

def render():
    # 1. Güvenlik Kontrolü
    check_admin_access()
    inject_admin_css()
    
    # Header
    st.markdown("""
        <div class='admin-header'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div>
                    <h1 style='font-size: 2rem; margin:0;'>🛡️ Sistem Yönetim Paneli</h1>
                    <p style='color:#666; font-size:14px;'>SaaS Altyapısı ve Kullanıcı Yönetimi</p>
                </div>
                <div class='security-badge'>ROOT PRIVILEGES ACTIVE</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. KPI Metrikleri (SaaS Durumu)
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Toplam Kullanıcı", "1,240", "+12")
    k2.metric("Aktif Oturumlar", "85", "Canlı")
    k3.metric("Sunucu Yükü", "%34", "Stabil")
    k4.metric("Güvenlik Tehdidi", "0", "Temiz")

    # 3. Yönetim Sekmeleri
    tab_users, tab_security, tab_settings = st.tabs(["👥 Kullanıcı Yönetimi", "🚨 Güvenlik & Loglar", "⚙️ Sistem Ayarları"])

    # --- SEKME 1: KULLANICI YÖNETİMİ (CRUD) ---
    with tab_users:
        st.markdown("### 🧬 Kullanıcı Veritabanı")
        
        # Mock Veritabanı (Gerçekte SQL'den gelir)
        user_db = pd.DataFrame([
            {"ID": 1001, "Ad Soyad": "Ahmet Yılmaz", "Email": "ahmet@anatolia.com", "Rol": "admin", "Durum": True, "Son Giriş": "14:02"},
            {"ID": 1002, "Ad Soyad": "Ayşe Demir", "Email": "ayse@anatolia.com", "Rol": "editor", "Durum": True, "Son Giriş": "13:45"},
            {"ID": 1003, "Ad Soyad": "Mehmet Kaya", "Email": "mehmet@anatolia.com", "Rol": "viewer", "Durum": True, "Son Giriş": "11:20"},
            {"ID": 1004, "Ad Soyad": "John Doe", "Email": "john@us-branch.com", "Rol": "viewer", "Durum": False, "Son Giriş": "Dün"},
        ])

        # Data Editor (Excel gibi düzenleme)
        edited_users = st.data_editor(
            user_db,
            column_config={
                "Durum": st.column_config.CheckboxColumn("Hesap Aktif", help="Kullanıcıyı banlamak için tiki kaldırın"),
                "Rol": st.column_config.SelectboxColumn("Yetki Seviyesi", options=["admin", "editor", "viewer", "restricted"]),
                "ID": st.column_config.NumberColumn(disabled=True)
            },
            use_container_width=True,
            num_rows="dynamic",
            hide_index=True
        )

        col_btn, _ = st.columns([1, 4])
        with col_btn:
            if st.button("💾 Değişiklikleri Veritabanına İşle", type="primary"):
                st.toast("Kullanıcı yetkileri güncellendi ve erişim tokenları yenilendi.", icon="✅")

    # --- SEKME 2: SİBER GÜVENLİK ---
    with tab_security:
        c1, c2 = st.columns([2, 1])
        
        with c1:
            st.markdown("### 📡 Audit Logs (Denetim İzleri)")
            logs = pd.DataFrame({
                "Zaman": ["14:05:12", "14:02:10", "13:55:00", "13:12:44"],
                "IP Adresi": ["192.168.1.10", "85.102.xx.xx", "10.0.0.5", "192.168.1.12"],
                "Kullanıcı": ["Ahmet Y.", "Sistem", "Ayşe D.", "Mehmet K."],
                "Eylem": ["Admin paneline giriş", "Otomatik yedekleme", "Veri ihracı (Export)", "Hatalı şifre denemesi (3x)"],
                "Risk": ["Düşük", "Bilgi", "Orta", "Yüksek"]
            })
            
            # Risk Renklendirmesi
            def highlight_risk(val):
                color = '#EF4444' if val == 'Yüksek' else '#F59E0B' if val == 'Orta' else '#10B981'
                return f'color: {color}; font-weight: bold'
            
            st.dataframe(logs.style.map(highlight_risk, subset=['Risk']), use_container_width=True, hide_index=True)

        with c2:
            st.markdown("### 🛡️ Acil Durum")
            st.warning("Bu işlemler geri alınamaz.")
            
            if st.button("🚫 Tüm Oturumları Zorla Kapat"):
                st.error("Tüm kullanıcılar sistemden atılıyor...")
            
            st.markdown("---")
            toggle_maint = st.toggle("Bakım Modu (Maintenance)", value=False)
            if toggle_maint:
                st.info("Sistem bakım modunda. Sadece Adminler girebilir.")

    # --- SEKME 3: SİSTEM AYARLARI ---
    with tab_settings:
        st.markdown("### ⚙️ Global Konfigürasyon")
        
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            current_brand = st.session_state.user_data.get('brand', 'Anatolia Home')
            new_brand = st.text_input("SaaS Marka İsmi (White Label)", value=current_brand)
            if st.button("Markayı Güncelle"):
                st.session_state.user_data['brand'] = new_brand
                st.rerun()
                
        with col_s2:
            st.markdown("**Veri Saklama Politikası**")
            st.selectbox("Log Tutma Süresi", ["30 Gün", "90 Gün", "1 Yıl (GDPR Uyumu)"])
            st.checkbox("İki Faktörlü Doğrulamayı (2FA) Zorunlu Tut", value=True)
