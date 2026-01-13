import streamlit as st
import time

# ==============================================================================
# 🎨 1. SAYFAYA ÖZEL CSS (PREMIUM GÖRÜNÜM)
# ==============================================================================
def inject_pricing_css():
    st.markdown("""
    <style>
        /* Genel Kart Yapısı */
        .pricing-card {
            background-color: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            height: 100%;
            transition: all 0.3s ease;
            position: relative;
        }
        .pricing-card:hover {
            transform: translateY(-8px);
            background-color: rgba(255, 255, 255, 0.04);
            box-shadow: 0 20px 40px -10px rgba(0,0,0,0.5);
        }

        /* Öne Çıkan Kart (PRO) */
        .card-highlight {
            background: linear-gradient(145deg, rgba(59, 130, 246, 0.05) 0%, rgba(139, 92, 246, 0.05) 100%);
            border: 1px solid rgba(139, 92, 246, 0.3);
            box-shadow: 0 0 30px rgba(139, 92, 246, 0.1);
        }
        .card-highlight:hover {
            border-color: rgba(139, 92, 246, 0.6);
            box-shadow: 0 0 50px rgba(139, 92, 246, 0.2);
        }

        /* Başlıklar ve Fiyat */
        .plan-name { font-size: 14px; font-weight: 600; color: #A1A1AA; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }
        .plan-price { font-size: 42px; font-weight: 800; color: #FFF; margin-bottom: 5px; }
        .plan-period { font-size: 14px; color: #71717A; font-weight: 400; }
        .plan-desc { font-size: 14px; color: #A1A1AA; margin: 15px 0 25px 0; line-height: 1.5; }

        /* Özellik Listesi */
        .feature-list { list-style: none; padding: 0; margin: 0; }
        .feature-item { 
            display: flex; align-items: center; gap: 10px; 
            font-size: 14px; color: #E4E4E7; margin-bottom: 12px; 
        }
        .check-icon { color: #10B981; font-weight: bold; }
        .check-icon-gray { color: #52525B; }
        
        /* En Popüler Etiketi */
        .popular-badge {
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(90deg, #8B5CF6 0%, #3B82F6 100%);
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 2. UI KART OLUŞTURUCU
# ==============================================================================
def render_plan_content(title, price, desc, features, is_highlight=False):
    """
    Kartın HTML içeriğini oluşturur (Buton hariç).
    Buton Streamlit native olmalı ki tıklamayı yakalayalım.
    """
    card_class = "pricing-card card-highlight" if is_highlight else "pricing-card"
    badge_html = '<div class="popular-badge">✨ EN POPÜLER</div>' if is_highlight else ""
    
    feature_html = ""
    for feat in features:
        icon = "✓" if feat['active'] else "•"
        style_cls = "check-icon" if feat['active'] else "check-icon-gray"
        text_style = "color: #E4E4E7;" if feat['active'] else "color: #52525B; text-decoration: line-through;"
        
        feature_html += f"""
        <li class="feature-item">
            <span class="{style_cls}">{icon}</span>
            <span style="{text_style}">{feat['text']}</span>
        </li>
        """

    html = f"""
    <div class="{card_class}">
        {badge_html}
        <div class="plan-name">{title}</div>
        <div class="plan-price">{price}<span class="plan-period">/ay</span></div>
        <div class="plan-desc">{desc}</div>
        <hr style="border-color: rgba(255,255,255,0.1); margin-bottom: 20px;">
        <ul class="feature-list">
            {feature_html}
        </ul>
    </div>
    """
    return html

# ==============================================================================
# 🚀 3. ANA RENDER FONKSİYONU
# ==============================================================================
def render_plan():
    inject_pricing_css()
    
    # --- BAŞLIK ---
    st.markdown("<div style='text-align: center; margin-bottom: 40px;'>", unsafe_allow_html=True)
    st.title("💎 Planını Seç")
    st.markdown("<p style='color: #A1A1AA; font-size: 16px;'>İşletmenizin ölçeğine uygun, şeffaf fiyatlandırma.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- KARTLAR (3 KOLON) ---
    # Ortadaki kolon (Pro) biraz daha geniş olsun diye oran veriyoruz
    c1, c2, c3 = st.columns([1, 1.1, 1], gap="medium")

    # === PLAN 1: BAŞLANGIÇ ===
    with c1:
        st.markdown(render_plan_content(
            title="BAŞLANGIÇ",
            price="$0",
            desc="Küçük işletmeler ve bireysel satıcılar için temel özellikler.",
            features=[
                {"text": "Aylık 50 Sevkiyat", "active": True},
                {"text": "Temel Stok Takibi", "active": True},
                {"text": "AI Asistan (Sınırlı)", "active": True},
                {"text": "Gelişmiş Raporlar", "active": False},
                {"text": "7/24 Canlı Destek", "active": False},
            ]
        ), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True) # Boşluk
        if st.button("Mevcut Plan", key="btn_free", use_container_width=True, disabled=True):
            pass

    # === PLAN 2: PRO (HIGHLIGHT) ===
    with c2:
        st.markdown(render_plan_content(
            title="PROFESYONEL",
            price="$49",
            desc="Büyüyen e-ticaret operasyonları için tam kapsamlı çözüm.",
            features=[
                {"text": "Sınırsız Sevkiyat", "active": True},
                {"text": "Gelişmiş AI Analizleri", "active": True},
                {"text": "Çoklu Depo Yönetimi", "active": True},
                {"text": "Lojistik Rota Optimizasyonu", "active": True},
                {"text": "Öncelıklı E-posta Desteği", "active": True},
            ],
            is_highlight=True
        ), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Parlayan Buton
        if st.button("🔥 PRO'ya Yükselt", key="btn_pro", type="primary", use_container_width=True):
            with st.spinner("Ödeme altyapısına bağlanılıyor..."):
                time.sleep(1.5)
            st.toast("Tebrikler! Hesabınız PRO seviyesine yükseltildi.", icon="🚀")
            st.balloons()

    # === PLAN 3: ENTERPRISE ===
    with c3:
        st.markdown(render_plan_content(
            title="ENTERPRISE",
            price="ÖZEL",
            desc="Global markalar ve büyük hacimli operasyonlar için.",
            features=[
                {"text": "Özel Sunucu & API", "active": True},
                {"text": "Sınırsız Kullanıcı", "active": True},
                {"text": "Özel AI Model Eğitimi", "active": True},
                {"text": "SLA & 7/24 Dedike Destek", "active": True},
                {"text": "Yerinde Kurulum", "active": True},
            ]
        ), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Satış ile Görüş", key="btn_ent", use_container_width=True):
            st.info("Kurumsal satış ekibimiz sizinle iletişime geçecektir.")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- GÜVENLİK ROZETLERİ ---
    st.markdown("""
    <div style="text-align: center; color: #52525B; font-size: 12px; margin-top: 20px;">
        <i class='bx bx-shield-quarter'></i> 256-bit SSL Güvenli Ödeme • İstediğiniz Zaman İptal Edin
    </div>
    """, unsafe_allow_html=True)
