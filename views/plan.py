import streamlit as st
import time

# ==============================================================================
# 🎨 1. CSS MOTORU (GLASSMORPHISM & GLOW)
# ==============================================================================
def inject_pricing_css():
    st.markdown("""
    <style>
        /* Kartın Kendisi */
        .pricing-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 24px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            height: 100%;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: visible;
        }
        
        .pricing-card:hover {
            transform: translateY(-10px);
            background: rgba(255, 255, 255, 0.05);
            border-color: rgba(255, 255, 255, 0.2);
            box-shadow: 0 20px 50px -10px rgba(0,0,0,0.6);
        }

        /* PRO Kart Özelleştirmesi (Neon Glow) */
        .card-highlight {
            background: linear-gradient(180deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
            border: 1px solid rgba(139, 92, 246, 0.5);
            box-shadow: 0 0 40px rgba(139, 92, 246, 0.15);
        }
        .card-highlight:hover {
            border-color: #8B5CF6;
            box-shadow: 0 0 60px rgba(139, 92, 246, 0.3);
        }

        /* Tipografi */
        .plan-name { 
            font-size: 13px; font-weight: 700; color: #94A3B8; 
            text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 15px; 
        }
        .plan-price { 
            font-size: 48px; font-weight: 800; color: #F8FAFC; 
            letter-spacing: -1px; margin-bottom: 5px; line-height: 1;
        }
        .plan-period { font-size: 16px; color: #64748B; font-weight: 500; margin-left: 2px; }
        .plan-desc { 
            font-size: 15px; color: #CBD5E1; margin: 20px 0 30px 0; 
            line-height: 1.6; min-height: 50px; font-weight: 400;
        }

        /* Liste Elemanları */
        .feature-list { list-style: none; padding: 0; margin: 0; }
        .feature-item { 
            display: flex; align-items: center; gap: 12px; 
            font-size: 14px; color: #E2E8F0; margin-bottom: 16px; 
        }
        
        /* İkonlar */
        .icon-box {
            width: 20px; height: 20px;
            display: flex; align-items: center; justify-content: center;
            border-radius: 50%;
        }
        .icon-check { background: rgba(16, 185, 129, 0.2); color: #34D399; }
        .icon-cross { background: rgba(255, 255, 255, 0.05); color: #64748B; }

        /* Badge (En Popüler) */
        .popular-badge {
            position: absolute;
            top: -14px; left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(90deg, #7C3AED 0%, #2563EB 100%);
            color: #FFF;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 11px; font-weight: 800;
            text-transform: uppercase; letter-spacing: 1px;
            box-shadow: 0 4px 15px rgba(124, 58, 237, 0.5);
            z-index: 10;
            border: 2px solid #0F172A; 
        }
        
        /* Ayırıcı Çizgi */
        .divider {
            height: 1px; background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.1) 50%, rgba(255,255,255,0) 100%);
            border: none; margin-bottom: 25px;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 2. HTML OLUŞTURUCU (GİRİNTİSİZ - KESİN ÇÖZÜM)
# ==============================================================================
def render_plan_content(title, price, desc, features, is_highlight=False):
    """
    HTML'i parça parça birleştirerek oluşturur. 
    Bu yöntem, 'indentation' (girinti) hatalarını %100 engeller.
    """
    card_class = "pricing-card card-highlight" if is_highlight else "pricing-card"
    badge_html = '<div class="popular-badge">✨ EN POPÜLER</div>' if is_highlight else ""
    
    # HTML String'ini satır satır birleştiriyoruz (Hata riskini sıfırlar)
    html = f'<div class="{card_class}">'
    html += f'{badge_html}'
    html += f'<div class="plan-name">{title}</div>'
    html += f'<div class="plan-price">{price}<span class="plan-period">/ay</span></div>'
    html += f'<div class="plan-desc">{desc}</div>'
    html += f'<hr class="divider">'
    html += f'<ul class="feature-list">'
    
    for feat in features:
        if feat['active']:
            icon_html = '<div class="icon-box icon-check"><i class="bx bx-check"></i></div>'
            text_style = "color: #E2E8F0;"
        else:
            icon_html = '<div class="icon-box icon-cross"><i class="bx bx-x"></i></div>'
            text_style = "color: #64748B; text-decoration: line-through;"
            
        html += f'<li class="feature-item">{icon_html}<span style="{text_style}">{feat["text"]}</span></li>'
    
    html += '</ul></div>'
    
    return html

# ==============================================================================
# 🚀 3. ANA RENDER FONKSİYONU
# ==============================================================================
def render_plans():
    inject_pricing_css()
    
    # --- BAŞLIK ---
    st.markdown("<div style='text-align: center; margin-bottom: 60px;'>", unsafe_allow_html=True)
    st.title("💎 Ölçeklenebilir Fiyatlandırma")
    st.markdown("<p style='color: #94A3B8; font-size: 18px; max-width: 600px; margin: 0 auto;'>İşletmeniz büyüdükçe sizinle birlikte büyüyen, şeffaf ve esnek planlar.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- KARTLAR ---
    c1, c2, c3 = st.columns([1, 1.1, 1], gap="medium")

    # === PLAN 1: STARTUP ===
    with c1:
        html_content = render_plan_content(
            title="BAŞLANGIÇ",
            price="$0",
            desc="Bireysel satıcılar ve yeni başlayanlar için ideal.",
            features=[
                {"text": "Aylık 50 Sevkiyat", "active": True},
                {"text": "Temel Stok Takibi", "active": True},
                {"text": "AI Chatbot (Limitli)", "active": True},
                {"text": "API Erişimi", "active": False},
                {"text": "Öncelikli Destek", "active": False},
            ]
        )
        st.markdown(html_content, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("Ücretsiz Başla", key="p_free", use_container_width=True)

    # === PLAN 2: SCALE (HIGHLIGHT) ===
    with c2:
        html_content = render_plan_content(
            title="PROFESYONEL",
            price="$49",
            desc="Hızlı büyüyen markalar için tam güç otomasyon.",
            features=[
                {"text": "Sınırsız Sevkiyat", "active": True},
                {"text": "Gelişmiş AI Analizleri", "active": True},
                {"text": "Lojistik Rota Optimizasyonu", "active": True},
                {"text": "Çoklu Depo Yönetimi", "active": True},
                {"text": "E-posta Destek Hattı", "active": True},
            ],
            is_highlight=True
        )
        st.markdown(html_content, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔥 Pro'ya Geçiş Yap", key="p_pro", type="primary", use_container_width=True):
            with st.spinner("Ödeme paneli hazırlanıyor..."):
                time.sleep(1)
            st.balloons()
            st.success("Yönlendiriliyorsunuz!")

    # === PLAN 3: ENTERPRISE ===
    with c3:
        html_content = render_plan_content(
            title="ENTERPRISE",
            price="ÖZEL",
            desc="Global operasyonlar için özelleştirilmiş altyapı.",
            features=[
                {"text": "Size Özel Sunucu", "active": True},
                {"text": "Sınırsız Kullanıcı", "active": True},
                {"text": "Özel AI Model Eğitimi", "active": True},
                {"text": "SLA Garantisi (%99.9)", "active": True},
                {"text": "7/24 Dedike Müşteri Temsilcisi", "active": True},
            ]
        )
        st.markdown(html_content, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("Satış Ekibiyle Görüş", key="p_ent", use_container_width=True)

    # --- ALT BİLGİ ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: #52525B; font-size: 13px; display: flex; justify-content: center; gap: 30px;">
        <span><i class='bx bx-check-shield'></i> 30 Gün Para İade Garantisi</span>
        <span><i class='bx bx-credit-card'></i> Gizli Ücret Yok</span>
        <span><i class='bx bx-support'></i> Kurulum Desteği</span>
    </div>
    """, unsafe_allow_html=True)
