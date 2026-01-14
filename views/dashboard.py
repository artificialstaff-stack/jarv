import streamlit as st
import brain
import time
import pandas as pd
from datetime import datetime
from typing import Dict, Any

# ==============================================================================
# 🎨 1. MODERN CSS TASARIM SİSTEMİ
# ==============================================================================
def inject_dashboard_css():
    st.markdown("""
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <style>
        /* FONTLAR */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap');
        
        :root {
            --bg-glass: rgba(20, 20, 22, 0.7);
            --border-glass: rgba(255, 255, 255, 0.08);
            --text-primary: #FFFFFF;
            --text-secondary: #A1A1AA;
            --accent-blue: #3B82F6;
            --accent-green: #10B981;
            --accent-purple: #8B5CF6;
            --accent-orange: #F59E0B;
        }

        /* HEADER (Glow & Glass Efektli) */
        .dash-header-container {
            padding: 24px 32px;
            background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid var(--border-glass);
            border-radius: 24px;
            margin-bottom: 32px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 20px 40px -10px rgba(0,0,0,0.5);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* METRİK KARTLARI (Bento Style) */
        .metric-card {
            background: var(--bg-glass);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 24px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            gap: 12px;
            height: 100%; /* Aynı yükseklikte olmaları için */
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 255, 255, 0.2);
            box-shadow: 0 15px 30px rgba(0,0,0,0.4), inset 0 0 20px rgba(255,255,255,0.02);
        }

        /* İkon Kutusu */
        .icon-box {
            width: 48px; height: 48px;
            border-radius: 14px;
            display: flex; align-items: center; justify-content: center;
            font-size: 24px;
        }

        /* Renk Temaları */
        .theme-blue { background: rgba(59, 130, 246, 0.15); color: var(--accent-blue); border: 1px solid rgba(59, 130, 246, 0.2); }
        .theme-green { background: rgba(16, 185, 129, 0.15); color: var(--accent-green); border: 1px solid rgba(16, 185, 129, 0.2); }
        .theme-purple { background: rgba(139, 92, 246, 0.15); color: var(--accent-purple); border: 1px solid rgba(139, 92, 246, 0.2); }
        .theme-orange { background: rgba(245, 158, 11, 0.15); color: var(--accent-orange); border: 1px solid rgba(245, 158, 11, 0.2); }

        /* Yazı Stilleri */
        .metric-label { font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 600; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px; }
        .metric-value { font-family: 'Inter', sans-serif; font-size: 32px; font-weight: 800; color: var(--text-primary); letter-spacing: -0.5px; line-height: 1; }
        
        /* Delta (Değişim) Rozeti */
        .delta-badge {
            display: inline-flex; align-items: center; gap: 6px;
            font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700;
            padding: 6px 12px; border-radius: 30px;
            width: fit-content;
        }
        .delta-pos { background: rgba(16, 185, 129, 0.1); color: var(--accent-green); border: 1px solid rgba(16, 185, 129, 0.2); }
        .delta-neg { background: rgba(239, 68, 68, 0.1); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.2); }
        .delta-neu { background: rgba(255, 255, 255, 0.05); color: var(--text-secondary); border: 1px solid rgba(255, 255, 255, 0.1); }
        
        /* Chat Başlığı */
        .chat-header {
            display: flex; align-items: center; gap: 12px; margin-bottom: 20px;
            padding-bottom: 15px; border-bottom: 1px solid var(--border-glass);
        }
        .chat-icon {
             width: 36px; height: 36px; background: linear-gradient(135deg, var(--accent-purple), var(--accent-blue));
             border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 18px;
             box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
        }

        /* Canlı Durum Noktası */
        .live-dot {
            width: 8px; height: 8px; background: var(--accent-green); border-radius: 50%;
            box-shadow: 0 0 10px var(--accent-green); animation: pulse 2s infinite;
        }
        @keyframes pulse { 0% { opacity: 0.6; } 50% { opacity: 1; box-shadow: 0 0 15px var(--accent-green); } 100% { opacity: 0.6; } }

    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧩 2. BİLEŞENLER
# ==============================================================================

def render_header(user_data):
    brand = user_data.get('brand', 'Anatolia Home')
    date_str = datetime.now().strftime("%d %B, %A")
    
    st.markdown(f"""
    <div class="dash-header-container">
        <div>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
                <span style="color:var(--accent-purple); font-size:14px;"><i class='bx bx-command'></i></span>
                <span style="color:var(--text-secondary); font-size:11px; font-weight:700; letter-spacing:2px; text-transform:uppercase;">Operasyon Merkezi</span>
            </div>
            <h1 style="margin:0; font-family:'Inter', sans-serif; font-size: 3rem; font-weight:800; background: linear-gradient(to right, #fff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{brand}</h1>
        </div>
        <div style="text-align:right; display:flex; flex-direction:column; align-items:flex-end; gap:10px;">
             <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.2); padding:6px 16px; border-radius:30px;">
                <div class="live-dot"></div>
                <span style="color:var(--accent-green); font-family:'JetBrains Mono'; font-size:12px; font-weight:700;">SYSTEM ONLINE</span>
             </div>
             <div style="color:var(--text-secondary); font-family:'Inter'; font-size:13px; font-weight:500; display:flex; align-items:center; gap:6px;">
                <i class='bx bx-calendar'></i> {date_str}
             </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_metric(label, value, delta, icon="bx-stats", theme="blue"):
    
    if any(x in delta for x in ["+", "Yolda", "Normal", "Yeni", "Bu Hafta"]): delta_class = "delta-pos"
    elif any(x in delta for x in ["-", "Risk", "Kritik", "Acil"]): delta_class = "delta-neg"
    else: delta_class = "delta-neu"
    
    delta_icon = ""
    if "+" in delta: delta_icon = "<i class='bx bx-trending-up'></i>"
    elif "-" in delta: delta_icon = "<i class='bx bx-trending-down'></i>"

    st.markdown(f"""
    <div class="metric-card">
        <div style="display:flex; justify-content:space-between; align-items:start;">
            <div class="icon-box theme-{theme}">
                <i class='bx {icon}'></i>
            </div>
            <div class="delta-badge {delta_class}">
                {delta_icon} {delta}
            </div>
        </div>
        <div style="margin-top:auto;"> <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🚀 3. ANA DASHBOARD (LOGIC + LAYOUT)
# ==============================================================================
def render_dashboard():
    inject_dashboard_css()
    
    # 1. KULLANICI BİLGİSİ
    user = st.session_state.get('user_data', {'brand': 'Demo Brand', 'name': 'User'})
    
    # 2. HEADER
    render_header(user)
    
    # 3. MOD YÖNETİMİ
    if "dashboard_mode" not in st.session_state: st.session_state.dashboard_mode = "finance"
    current_mode = st.session_state.dashboard_mode

    # 4. İKİ KOLONLU YAPI
    col_chat, col_viz = st.columns([1.1, 1.9], gap="large")

    # --- SOL: AI ASİSTAN (MODERN GÖRÜNÜM) ---
    with col_chat:
        st.markdown("""
        <div class="chat-header">
            <div class="chat-icon"><i class='bx bx-bot'></i></div>
            <div>
                <h4 style="margin:0; font-family:'Inter'; font-weight:700; color:var(--text-primary);">Operasyon Asistanı</h4>
                <p style="margin:0; font-size:12px; color:var(--text-secondary);">Gerçek zamanlı veri analizi</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        chat_cont = st.container(height=520)
        
        # Mesaj Geçmişi
        if "messages" not in st.session_state: st.session_state.messages = []
        
        with chat_cont:
            if not st.session_state.messages:
                st.info("👋 Merhaba! Tüm operasyonel verilerinize hakimim. Bana bir talimat verin.")
            
            for msg in st.session_state.messages:
                avatar = "👤" if msg["role"] == "user" else "🤖"
                st.chat_message(msg["role"], avatar=avatar).write(msg["content"])
        
        # Yeni Mesaj Girişi
        if prompt := st.chat_input("Talimat verin (Örn: Lojistik durumu)..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # --- ZEKİ MOD DEĞİŞTİRİCİ (BACKEND MANTIĞI AYNI) ---
            p_low = prompt.lower()
            if any(x in p_low for x in ["lojistik", "kargo", "harita"]): st.session_state.dashboard_mode = "logistics"
            elif any(x in p_low for x in ["stok", "depo", "ürün"]): st.session_state.dashboard_mode = "inventory"
            elif any(x in p_low for x in ["finans", "ciro", "satış"]): st.session_state.dashboard_mode = "finance"
            elif any(x in p_low for x in ["belge", "doküman"]): st.session_state.dashboard_mode = "documents"
            elif any(x in p_low for x in ["form"]): st.session_state.dashboard_mode = "forms"
            elif any(x in p_low for x in ["yapılacak", "görev"]): st.session_state.dashboard_mode = "todo"
            elif any(x in p_low for x in ["plan"]): st.session_state.dashboard_mode = "plans"
            
            st.rerun()

    # Asistan Cevabı
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with chat_cont:
            with st.chat_message("assistant", avatar="🤖"):
                ph = st.empty()
                full_resp = ""
                # BACKEND ÇAĞRISI (DEĞİŞMEDİ)
                for chunk in brain.get_streaming_response(st.session_state.messages, user):
                    full_resp += chunk
                    ph.markdown(full_resp + "▌")
                    time.sleep(0.01)
                ph.markdown(full_resp)
        st.session_state.messages.append({"role": "assistant", "content": full_resp})

    # --- SAĞ: DİNAMİK GÖRSELLER (YENİLENMİŞ TASARIM) ---
    with col_viz:
        mode = st.session_state.dashboard_mode
        
        # 1. FİNANS
        if mode == "finance":
            st.markdown("##### 📈 Finansal Performans")
            c1, c2, c3 = st.columns(3)
            with c1: render_metric("Aylık Ciro", "$42,500", "+%12.5", "bx-dollar-circle", "blue")
            with c2: render_metric("Net Kâr", "%32", "+%4.2", "bx-trending-up", "green")
            with c3: render_metric("Büyüme", "Stabil", "Normal", "bx-pulse", "purple")
            
            st.markdown("<br>", unsafe_allow_html=True)
            # Grafik Container (Glass Efektli Kutu İçine Aldık)
            st.markdown("<div class='metric-card' style='padding:10px;'>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        # 2. LOJİSTİK
        elif mode == "logistics":
            st.markdown("##### 🌍 Lojistik Ağı")
            c1, c2 = st.columns(2)
            with c1: render_metric("Aktif Kargo", "TR-8821", "Yolda", "bx-map-pin", "orange")
            with c2: render_metric("Tahmini Varış", "2 Gün", "Zamanında", "bx-time", "blue")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<div class='metric-card' style='padding:10px;'>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_logistics_map(), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        # 3. ENVANTER
        elif mode == "inventory":
            st.markdown("##### 📦 Depo Durumu")
            c1, c2 = st.columns(2)
            with c1: render_metric("Toplam Ürün", "8,500", "Adet", "bx-package", "purple")
            with c2: render_metric("Riskli Stok", "Çanta", "Kritik", "bx-error", "orange")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<div class='metric-card' style='padding:10px;'>", unsafe_allow_html=True)
            st.plotly_chart(brain.get_inventory_chart(), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        # 4. DOKÜMANLAR (Modern Tablo)
        elif mode == "documents":
            st.markdown("##### 📂 Dijital Arşiv")
            c1, c2 = st.columns(2)
            with c1: render_metric("Toplam Dosya", "1,240", "+5 Yeni", "bx-folder", "blue")
            with c2: render_metric("Son Yükleme", "Bugün", "İrsaliye", "bx-cloud-upload", "green")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("**📁 Son Yüklenen Evraklar**")
            
            data = {
                "Dosya Adı": ["Fatura_Ocak_2026.pdf", "Gümrük_Beyan_TR88.pdf", "Stok_Raporu_V2.xlsx", "İade_Prosedürü.docx"],
                "Tarih": ["14.01.2026", "13.01.2026", "12.01.2026", "10.01.2026"],
                "Boyut": ["1.2 MB", "450 KB", "2.1 MB", "800 KB"],
                "Durum": ["Onaylandı", "İşleniyor", "Hazır", "Taslak"]
            }
            # Tabloyu bir kartın içine koyalım
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
            st.markdown("</div>", unsafe_allow_html=True)

        # 5. FORMLAR
        elif mode == "forms":
            st.markdown("##### 📝 Onay Bekleyenler")
            c1, c2 = st.columns(2)
            with c1: render_metric("Bekleyen", "3", "Acil", "bx-edit", "orange")
            with c2: render_metric("Onaylanan", "12", "Bu Hafta", "bx-check-circle", "green")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Formları da kart içine alalım
            with st.container():
                st.markdown("""
                <div class='metric-card' style='flex-direction:row; align-items:center; justify-content:space-between;'>
                    <div>
                        <h4 style='margin:0; color:white;'>📌 Personel İzin Formu - Ahmet Y.</h4>
                        <p style='margin:5px 0 0 0; color:var(--text-secondary); font-size:13px;'>Tarih: 15-20 Ocak | Departman: Lojistik</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.button("Onayla", key="f1", use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            with st.container():
                st.markdown("""
                <div class='metric-card' style='flex-direction:row; align-items:center; justify-content:space-between;'>
                    <div>
                        <h4 style='margin:0; color:white;'>📌 Satın Alma Talebi - #9921</h4>
                        <p style='margin:5px 0 0 0; color:var(--text-secondary); font-size:13px;'>Ürün: Ambalaj Malzemesi | Tutar: 5.000 TL</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.button("Onayla", key="f2", use_container_width=True)

        # 6. PLANLAR (Kartlar)
        elif mode == "plans":
            st.markdown("##### 💎 Stratejik Planlar")
            st.info("🎯 **Q1 Hedefi:** Lojistik maliyetlerini %10 düşür.")
            
            c_a, c_b = st.columns(2)
            with c_a:
                st.markdown("""
                <div class="metric-card" style="border-left: 4px solid var(--accent-blue);">
                    <h4 style='margin:0; color:white;'>🇪🇺 Avrupa Genişlemesi</h4>
                    <p style="color:var(--text-secondary); font-size:12px; margin-top:5px;">Berlin deposu açılış süreci.</p>
                    <div style="background:rgba(255,255,255,0.1); height:6px; width:100%; border-radius:3px; margin-top:15px;">
                        <div style="background:var(--accent-blue); height:6px; width:70%; border-radius:3px; box-shadow: 0 0 10px var(--accent-blue);"></div>
                    </div>
                    <p style="text-align:right; font-family:'JetBrains Mono'; font-size:11px; font-weight:700; margin-top:8px; color:var(--accent-blue);">%70 TAMAMLANDI</p>
                </div>
                """, unsafe_allow_html=True)
            
            with c_b:
                st.markdown("""
                <div class="metric-card" style="border-left: 4px solid var(--accent-green);">
                    <h4 style='margin:0; color:white;'>🤖 AI Entegrasyonu</h4>
                    <p style="color:var(--text-secondary); font-size:12px; margin-top:5px;">Otomatik sipariş botu.</p>
                    <div style="background:rgba(255,255,255,0.1); height:6px; width:100%; border-radius:3px; margin-top:15px;">
                        <div style="background:var(--accent-green); height:6px; width:40%; border-radius:3px; box-shadow: 0 0 10px var(--accent-green);"></div>
                    </div>
                    <p style="text-align:right; font-family:'JetBrains Mono'; font-size:11px; font-weight:700; margin-top:8px; color:var(--accent-green);">%40 TAMAMLANDI</p>
                </div>
                """, unsafe_allow_html=True)
