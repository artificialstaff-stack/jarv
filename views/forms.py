import streamlit as st
import time
import random

# ==============================================================================
# 🎨 1. SAYFAYA ÖZEL STİL (FORMLAR İÇİN)
# ==============================================================================
def inject_forms_css():
    st.markdown("""
    <style>
        /* Form Konteynerı */
        .form-container {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 25px;
        }
        
        /* Adım Göstergesi (Wizard Steps) */
        .step-container {
            display: flex;
            justify-content: space-between;
            margin-bottom: 30px;
            position: relative;
        }
        .step-container::before {
            content: '';
            position: absolute;
            top: 15px;
            left: 0;
            right: 0;
            height: 2px;
            background: #27272A;
            z-index: 0;
        }
        .step-item {
            z-index: 1;
            background: #09090B;
            padding: 0 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
        }
        .step-circle {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #18181B;
            border: 2px solid #27272A;
            color: #71717A;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s;
        }
        .step-active .step-circle {
            border-color: #3B82F6;
            color: #3B82F6;
            background: rgba(59, 130, 246, 0.1);
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
        }
        .step-label {
            font-size: 12px;
            font-weight: 500;
            color: #71717A;
        }
        .step-active .step-label { color: #E4E4E7; }

        /* Özet Kartı */
        .summary-card {
            background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 2. UI BİLEŞENLERİ
# ==============================================================================
def render_wizard_steps(current_step=1):
    """Görsel ilerleme çubuğu"""
    steps = [
        {"num": 1, "label": "Kargo Bilgisi"},
        {"num": 2, "label": "Lojistik"},
        {"num": 3, "label": "Onay"}
    ]
    
    html = '<div class="step-container">'
    for step in steps:
        active_class = "step-active" if step["num"] <= current_step else ""
        icon = "✓" if step["num"] < current_step else str(step["num"])
        
        html += f"""
        <div class="step-item {active_class}">
            <div class="step-circle">{icon}</div>
            <div class="step-label">{step["label"]}</div>
        </div>
        """
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

# ==============================================================================
# 🚀 3. ANA RENDER FONKSİYONU
# ==============================================================================
def render_forms():
    inject_forms_css()
    
    # --- HEADER ---
    c1, c2 = st.columns([3, 1])
    with c1:
        st.title("📝 Operasyon Merkezi")
        st.caption("Yeni sevkiyat talepleri, gümrük belgeleri ve teknik destek.")
    with c2:
        # Sağ üstte canlı destek durumu
        st.markdown("""
        <div style="text-align:right; padding-top:10px;">
            <span style="background:rgba(16, 185, 129, 0.1); color:#34D399; padding:4px 10px; border-radius:20px; font-size:12px; border:1px solid rgba(16, 185, 129, 0.2);">
                ● Canlı Destek Aktif
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

    # --- TAB YAPISI ---
    tab_ship, tab_docs, tab_support = st.tabs(["📦 YENİ SEVKİYAT", "📄 BELGE YÖNETİMİ", "🔧 DESTEK HATTI"])

    # === TAB 1: SEVKİYAT SİHİRBAZI ===
    with tab_ship:
        render_wizard_steps(current_step=1) # Statik görsel (Form içinde adım adım hissi)
        
        col_form, col_summary = st.columns([2, 1], gap="large")
        
        with col_form:
            st.markdown("#### 🚢 ABD Lojistik Talep Formu")
            with st.container(border=True):
                with st.form("shipment_form"):
                    # Bölüm 1
                    st.caption("1. ADIM: KARGO İÇERİĞİ")
                    c1, c2 = st.columns(2)
                    product_type = c1.selectbox("Ürün Grubu", ["Tekstil (Hazır Giyim)", "Ev Tekstili", "Gıda", "Kozmetik", "Elektronik"])
                    box_count = c2.number_input("Koli Adedi", min_value=1, value=50)
                    
                    # Bölüm 2
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.caption("2. ADIM: LOJİSTİK TERCİHLERİ")
                    c3, c4 = st.columns(2)
                    origin = c3.selectbox("Çıkış Noktası", ["İstanbul Depo", "İzmir Fabrika", "Mersin Liman"])
                    priority = c4.radio("Servis Tipi", ["Ekonomik (Gemi - 25 Gün)", "Standart (Gemi - 18 Gün)", "Ekspres (Uçak - 3 Gün)"], horizontal=False)
                    
                    # Bölüm 3
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.caption("3. ADIM: DOKÜMANTASYON")
                    uploaded_file = st.file_uploader("Çeki Listesi (Packing List)", type=["pdf", "xlsx"])
                    note = st.text_area("Operasyon Ekibine Notlar", placeholder="Örn: Kolilerde 'Kırılabilir' etiketi olsun.")

                    st.markdown("---")
                    submitted = st.form_submit_button("🚀 Talebi Oluştur", type="primary", use_container_width=True)

        with col_summary:
            st.markdown("#### 📊 Canlı Tahmin")
            
            # Dinamik Tahmin Kartı
            shipping_cost = box_count * 45 if "Uçak" in priority else box_count * 12
            eta_days = 3 if "Uçak" in priority else (18 if "Standart" in priority else 25)
            
            st.markdown(f"""
            <div class="summary-card">
                <div style="color:#A1A1AA; font-size:12px; margin-bottom:5px;">TAHMİNİ MALİYET</div>
                <div style="color:#FFF; font-size:28px; font-weight:700; margin-bottom:15px;">${shipping_cost:,}</div>
                
                <div style="display:flex; justify-content:space-between; margin-bottom:10px; font-size:14px;">
                    <span style="color:#71717A;">Koli Sayısı:</span>
                    <span style="color:#E4E4E7;">{box_count} Adet</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-bottom:10px; font-size:14px;">
                    <span style="color:#71717A;">Servis:</span>
                    <span style="color:#E4E4E7;">{priority.split('(')[0]}</span>
                </div>
                <div style="border-top:1px solid rgba(255,255,255,0.1); margin:10px 0;"></div>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="color:#71717A;">Tahmini Varış:</span>
                    <span style="color:#34D399; font-weight:600;">{eta_days} Gün Sonra</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.info("💡 **İpucu:** 100 koli ve üzeri gönderimlerde 'Standart' servis %15 daha avantajlıdır.")

        if submitted:
            with st.status("Talep İşleniyor...", expanded=True) as status:
                st.write("Veriler doğrulanıyor...")
                time.sleep(1)
                st.write("Lojistik rotası hesaplanıyor...")
                time.sleep(1)
                st.write("Talep numarası oluşturuluyor...")
                time.sleep(0.5)
                status.update(label="✅ Başarıyla İletildi!", state="complete", expanded=False)
            
            st.success(f"Talebiniz alınmıştır! Takip No: **LOG-{random.randint(1000,9999)}**")
            st.balloons()

    # === TAB 2: BELGELER (Placeholder) ===
    with tab_docs:
        st.empty()
        st.info("Bu modül 'Dokümanlar' sayfasına taşınmıştır.")

    # === TAB 3: DESTEK ===
    with tab_support:
        c_sup1, c_sup2 = st.columns([2, 1])
        with c_sup1:
            st.markdown("#### 🆘 Destek Bileti Oluştur")
            with st.form("support_ticket"):
                c_s1, c_s2 = st.columns(2)
                ticket_type = c_s1.selectbox("Konu", ["Teknik Sorun", "Fatura İtirazı", "Gümrük İşlemleri", "Diğer"])
                urgency = c_s2.select_slider("Aciliyet", options=["Düşük", "Orta", "Yüksek", "KRİTİK"])
                
                desc = st.text_area("Sorunu Açıklayın")
                
                if st.form_submit_button("Bileti Gönder", use_container_width=True):
                    st.success("Destek ekibimiz bildirim aldı. Ortalama yanıt süresi: 15 dk.")

        with c_sup2:
            st.markdown("#### 📞 İletişim Kanalları")
            st.markdown("""
            - **Acil Hat:** +90 (212) 555 00 00
            - **E-posta:** ops@anatolia.com
            - **WhatsApp:** 7/24 Aktif
            """)
            st.warning("⚠️ Washington DC deposunda fırtına uyarısı nedeniyle 1 günlük gecikme beklenmektedir.")
