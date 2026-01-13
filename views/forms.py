import streamlit as st
import time
import random

# ==============================================================================
# 🎨 1. CSS MOTORU
# ==============================================================================
def inject_forms_css():
    st.markdown("""
    <style>
        /* Wizard (Adım) Göstergesi */
        .wizard-container {
            display: flex;
            justify-content: space-between;
            margin-bottom: 40px;
            position: relative;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        /* Çizgi */
        .wizard-line {
            position: absolute;
            top: 15px; left: 0; right: 0; height: 2px;
            background: #27272A;
            z-index: 0;
        }
        
        /* Adım Kutuları */
        .step-item {
            z-index: 1;
            background: #000000;
            padding: 0 10px;
            display: flex; flex-direction: column; align-items: center; gap: 8px;
        }
        .step-circle {
            width: 32px; height: 32px;
            border-radius: 50%;
            background: #18181B;
            border: 2px solid #3F3F46;
            color: #71717A;
            display: flex; align-items: center; justify-content: center;
            font-weight: 700; font-size: 14px;
            transition: all 0.3s;
        }
        .step-label { font-size: 12px; font-weight: 500; color: #71717A; }

        /* Aktif Adım Stili */
        .step-active .step-circle {
            border-color: #3B82F6;
            background: rgba(59, 130, 246, 0.1);
            color: #3B82F6;
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
        }
        .step-active .step-label { color: #E4E4E7; }

        /* Özet Kartı (Sağ Taraf) */
        .summary-card {
            background: linear-gradient(180deg, rgba(24, 24, 27, 0.6) 0%, rgba(9, 9, 11, 0.8) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 24px;
            position: sticky;
            top: 20px;
        }
        .summary-title { font-size: 11px; color: #71717A; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; margin-bottom: 8px; }
        .summary-total { font-size: 36px; font-weight: 800; color: #FFF; margin-bottom: 20px; letter-spacing: -1px; }
        
        .summary-row {
            display: flex; justify-content: space-between;
            font-size: 14px; color: #A1A1AA;
            margin-bottom: 12px;
            border-bottom: 1px dashed rgba(255,255,255,0.1);
            padding-bottom: 12px;
        }
        .summary-row:last-child { border-bottom: none; }
        .row-val { color: #E4E4E7; font-weight: 500; }
        
        .eta-badge {
            background: rgba(16, 185, 129, 0.1);
            color: #34D399;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            display: inline-block;
            margin-top: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 2. HTML OLUŞTURUCULAR (LIST JOIN YÖNTEMİ - KESİN ÇÖZÜM)
# ==============================================================================
def render_wizard_html(current_step=1):
    steps = [
        {"num": 1, "label": "Kargo Bilgisi"},
        {"num": 2, "label": "Lojistik"},
        {"num": 3, "label": "Onay"}
    ]
    
    html_parts = ['<div class="wizard-container">', '<div class="wizard-line"></div>']
    
    for step in steps:
        active_class = "step-active" if step["num"] <= current_step else ""
        icon = "✓" if step["num"] < current_step else str(step["num"])
        
        html_parts.append(f'<div class="step-item {active_class}">')
        html_parts.append(f'<div class="step-circle">{icon}</div>')
        html_parts.append(f'<div class="step-label">{step["label"]}</div>')
        html_parts.append('</div>')
        
    html_parts.append('</div>')
    return "".join(html_parts)

def render_summary_card(cost, count, service, eta):
    # HTML'i liste elemanları olarak oluşturup birleştiriyoruz. 
    # Bu yöntem indentation hatasını imkansız kılar.
    html_parts = [
        '<div class="summary-card">',
        '<div class="summary-title">TAHMİNİ MALİYET</div>',
        f'<div class="summary-total">${cost:,}</div>',
        
        '<div class="summary-row">',
        '<span>Koli Adedi</span>',
        f'<span class="row-val">{count}</span>',
        '</div>',
        
        '<div class="summary-row">',
        '<span>Servis Tipi</span>',
        f'<span class="row-val">{service}</span>',
        '</div>',
        
        '<div class="summary-row">',
        '<span>Sigorta</span>',
        '<span class="row-val">Dahil</span>',
        '</div>',
        
        '<div style="text-align: center;">',
        f'<div class="eta-badge">🚀 Tahmini Varış: {eta} Gün</div>',
        '</div>',
        '</div>'
    ]
    return "".join(html_parts)

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
        st.markdown("""
        <div style="text-align:right; padding-top:10px;">
            <span style="color:#34D399; font-size:12px; font-weight:600; background:rgba(16,185,129,0.1); padding:6px 12px; border-radius:20px; border:1px solid rgba(16,185,129,0.2);">
                ● Canlı Destek Aktif
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

    # --- TABS ---
    tab_ship, tab_docs, tab_support = st.tabs(["📦 YENİ SEVKİYAT", "📄 DOKÜMAN YÖNETİMİ", "🔧 DESTEK HATTI"])

    # === TAB 1: SEVKİYAT SİHİRBAZI ===
    with tab_ship:
        # Adım Göstergesi
        st.markdown(render_wizard_html(current_step=1), unsafe_allow_html=True)
        
        col_form, col_summary = st.columns([1.8, 1], gap="large")
        
        with col_form:
            st.markdown("##### 🚢 ABD Lojistik Talep Formu")
            with st.container():
                with st.form("shipment_form"):
                    st.caption("1. ADIM: KARGO İÇERİĞİ")
                    c1, c2 = st.columns(2)
                    product_type = c1.selectbox("Ürün Grubu", ["Tekstil (Hazır Giyim)", "Ev Tekstili", "Gıda", "Kozmetik", "Elektronik"])
                    box_count = c2.number_input("Koli Adedi", min_value=1, value=50, step=10)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.caption("2. ADIM: LOJİSTİK TERCİHLERİ")
                    c3, c4 = st.columns(2)
                    origin = c3.selectbox("Çıkış Noktası", ["İstanbul Depo", "İzmir Fabrika", "Mersin Liman"])
                    priority = c4.radio("Servis Tipi", ["Ekonomik (Gemi)", "Standart (Gemi+)", "Ekspres (Uçak)"], horizontal=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.caption("3. ADIM: EKSTRALAR")
                    file = st.file_uploader("Çeki Listesi (Opsiyonel)", type=["pdf", "xlsx"])
                    note = st.text_area("Operasyon Notları", placeholder="Örn: 3. koli hassas içerik barındırıyor.", height=80)

                    st.markdown("---")
                    submitted = st.form_submit_button("🚀 Talebi Oluştur", type="primary", use_container_width=True)

        with col_summary:
            st.markdown("##### 📊 Canlı Tahmin")
            
            # Hesaplama Mantığı
            base_rate = 12 # Gemi
            days = 25
            
            if "Standart" in priority:
                base_rate = 18
                days = 18
            elif "Ekspres" in priority:
                base_rate = 45
                days = 3
                
            total_cost = box_count * base_rate
            
            # HTML Kartı Bas
            st.markdown(render_summary_card(total_cost, box_count, priority.split('(')[0], days), unsafe_allow_html=True)
            
            st.info("💡 **İpucu:** 100 koli üzeri gönderimlerde %15 indirim otomatik uygulanır.")

        # Form Gönderimi
        if submitted:
            with st.status("Talep İşleniyor...", expanded=True) as status:
                st.write("📦 Stok kontrolü yapılıyor...")
                time.sleep(1)
                st.write("🌍 Rota optimizasyonu çalıştırılıyor...")
                time.sleep(1)
                st.write("✅ Referans kodu oluşturuldu.")
                status.update(label="Başarıyla İletildi!", state="complete", expanded=False)
            
            st.success(f"Talebiniz alınmıştır! Takip No: **LOG-{random.randint(10000,99999)}**")
            st.balloons()

    # === TAB 2: BELGELER ===
    with tab_docs:
        st.empty()
        st.info("📂 Tüm belgelerinize sol menüdeki **'Dokümanlar'** sayfasından ulaşabilirsiniz.")
        if st.button("Dokümanlara Git"):
             st.warning("Lütfen sol menüden 'Dokümanlar' sekmesini seçin.")

    # === TAB 3: DESTEK ===
    with tab_support:
        c_sup1, c_sup2 = st.columns([2, 1])
        with c_sup1:
            st.markdown("#### 🆘 Destek Bileti")
            with st.form("ticket_form"):
                topic = st.selectbox("Konu", ["Teknik Sorun", "Fatura", "Gümrük", "Diğer"])
                desc = st.text_area("Sorun Detayı")
                if st.form_submit_button("Gönder", use_container_width=True):
                    st.success("Destek ekibimiz bildirimi aldı.")
        
        with c_sup2:
            st.warning("⚠️ Washington Hub bölgesinde kar fırtınası nedeniyle 1 günlük gecikme bekleniyor.")
