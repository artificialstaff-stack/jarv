import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time
import json
import os
from datetime import datetime
from google import genai
from google.genai import types

# --- 1. MODEL YAPILANDIRMASI (PRO ERİŞİMİ) ---
# Google AI Studio'daki tam model adınız farklıysa buradan değiştirin.
# Genellikle: "gemini-3.0-flash-preview" veya "gemini-3.0-flash-001"
MODEL_NAME = "gemini-3.0-flash-preview" 

def get_ai_client():
    # API Key'i secrets veya environment'tan çeker
    api_key = st.secrets.get("GOOGLE_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

# --- 2. CORTEX ZEKASI (GEMINI 3.0 FLASH AGENT) ---
def cortex_brain(prompt):
    """
    Doğal dil komutlarını sistem aksiyonuna çeviren yönetici zekası.
    Google Gemini 3.0 Flash (Pro) modelini kullanır.
    """
    client = get_ai_client()
    users = st.session_state.users_db # Global veritabanını okur
    
    # AI'a Sistemin Anlık Durumunu Veriyoruz (Context)
    system_stats = {
        "active_users_count": sum(1 for u in users if u['status'] == 'Active'),
        "total_mrr": sum(u.get('mrr', 0) for u in users),
        "user_database": users, # Tüm kullanıcı listesini AI görüyor
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    if not client:
        return "⚠️ API Key Eksik! Lütfen .streamlit/secrets.toml dosyasına GOOGLE_API_KEY ekleyin."

    # --- SYSTEM PROMPT (KARAKTER & KURALLAR) ---
    sys_instruction = f"""
    Sen CORTEX. Bu SaaS platformunun "God Mode" yetkilerine sahip Yönetici Yapay Zekasısın.
    
    GÖREVİN:
    Kullanıcının doğal dilde verdiği emirleri analiz et ve aşağıdaki JSON formatında cevap ver.
    SADECE JSON DÖNDÜR. Yorum yapma.
    
    MEVCUT SİSTEM VERİLERİ:
    {json.dumps(system_stats)}

    EYLEM TİPLERİ (action):
    - "ban_user": Kullanıcıyı yasaklar (Status -> Suspended).
    - "activate_user": Kullanıcıyı açar (Status -> Active).
    - "promote_admin": Kullanıcıyı yönetici yapar (Role -> admin).
    - "report_status": Genel durum raporu verir.
    - "unknown": Komut anlaşılamadıysa.

    JSON FORMATI:
    {{
        "action": "eylem_tipi",
        "target_name": "Hedef Kullanıcı Adı (Veritabanından en yakın eşleşme)",
        "message": "Kullanıcıya gösterilecek otoriter, Türkçe sistem mesajı."
    }}
    """

    try:
        # GEMINI 3.0 FLASH ÇAĞRISI
        response = client.models.generate_content(
            model=MODEL_NAME, # En tepedeki değişkeni kullanır
            contents=f"User Command: {prompt}",
            config=types.GenerateContentConfig(
                system_instruction=sys_instruction,
                temperature=0.1, # Kesinlik için düşük yaratıcılık
                response_mime_type="application/json" # JSON zorunluluğu
            )
        )
        
        # AI Yanıtını İşle
        cmd = json.loads(response.text)
        action = cmd.get("action")
        target = cmd.get("target_name")
        message = cmd.get("message")

        # --- EYLEM KATMANI (EXECUTION LAYER) ---
        # AI sadece karar verir, Python uygular.
        
        if action == "report_status" or action == "unknown":
            return message

        # Kullanıcıyı bul ve işlemi yap
        user_found = False
        for user in st.session_state.users_db:
            if target and target.lower() in user['name'].lower():
                user_found = True
                
                if action == "ban_user":
                    user['status'] = "Suspended"
                elif action == "activate_user":
                    user['status'] = "Active"
                elif action == "promote_admin":
                    user['role'] = "admin"
                
                return message # Başarılı mesajı döndür

        if not user_found and target:
            return f"⚠️ Veritabanında '{target}' bulunamadı, ancak AI işlem yapmaya çalıştı."
        
        return message

    except Exception as e:
        return f"⚡ CORTEX HATASI ({MODEL_NAME}): {str(e)}"

# --- GÜVENLİK ---
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
        .cortex-terminal {
            background-color: #0d0d0d;
            border: 1px solid #333;
            border-left: 4px solid #EF4444;
            border-radius: 8px;
            padding: 20px;
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 30px;
        }
        .ai-msg { color: #e0e0e0; margin-top: 5px; border-left: 2px solid #EF4444; padding-left: 10px; }
        .user-msg { color: #EF4444; font-weight: bold; margin-top: 10px; }
        .metric-box { background: #0A0A0A; border: 1px solid #222; padding: 20px; border-radius: 12px; text-align: center; }
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
    st.markdown(f"""
        <div class='admin-header-card'>
            <div style='display:flex; justify-content:space-between; align-items:start;'>
                <div>
                    <div class='admin-badge'>GEMINI 3.0 FLASH ENABLED</div>
                    <h1 style='margin:10px 0 5px 0; font-size:2rem;'>ARTIS HQ Komuta Merkezi</h1>
                    <p style='color:#888; margin:0; font-size:14px;'>Google GenAI Tabanlı Otonom Yönetim Katmanı</p>
                </div>
                <div style='text-align:right;'>
                    <div style='color:#EF4444; font-weight:700; font-size:24px;'>$62,400</div>
                    <div style='color:#666; font-size:11px;'>MRR (AYLIK GELİR)</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. CORTEX AI TERMİNALİ
    st.markdown("### 🧠 CORTEX Yönetici Ajanı")
    st.caption("Sistemi doğal dille yönetin. Örn: 'Ahmet Yılmaz çok sorun çıkarıyor, sistemden at'.")
    
    with st.container():
        st.markdown("<div class='cortex-terminal'>", unsafe_allow_html=True)
        
        if "cortex_history" not in st.session_state:
            st.session_state.cortex_history = [{"role": "ai", "content": f"Cortex v3.0 ({MODEL_NAME}) devrede. Veritabanına bağlıyım."}]
        
        for msg in st.session_state.cortex_history[-3:]: 
            if msg['role'] == 'user':
                st.markdown(f"<div class='user-msg'>> {msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='ai-msg'>{msg['content']}</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        cortex_input = st.chat_input("CORTEX'e emir ver...")
        if cortex_input:
            st.session_state.cortex_history.append({"role": "user", "content": cortex_input})
            with st.spinner("Gemini 3 Flash analiz ediyor..."):
                resp = cortex_brain(cortex_input)
                st.session_state.cortex_history.append({"role": "ai", "content": resp})
            st.rerun()

    st.markdown("---")

    # 3. KPI WIDGETS
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.markdown("<div class='metric-box'><div class='metric-lbl'>Aktif Müşteri</div><div class='metric-val'>1,240</div><div class='metric-delta delta-pos'>+%12</div></div>", unsafe_allow_html=True)
    with k2: st.markdown("<div class='metric-box'><div class='metric-lbl'>Churn Rate</div><div class='metric-val'>%2.1</div><div class='metric-delta delta-pos'>-%0.4</div></div>", unsafe_allow_html=True)
    with k3: st.markdown("<div class='metric-box'><div class='metric-lbl'>API Maliyeti</div><div class='metric-val'>$4,200</div><div class='metric-delta delta-neg'>+%8</div></div>", unsafe_allow_html=True)
    with k4: st.markdown("<div class='metric-box'><div class='metric-lbl'>Sunucu Sağlığı</div><div class='metric-val'>%98.9</div><div class='metric-delta delta-pos'>Stabil</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. YÖNETİM SEKMELERİ
    tabs = st.tabs(["👥 Canlı Veritabanı (AI Sync)", "🚀 Özellik Kontrolü", "📢 Duyuru", "⚙️ Sistem Logları"])

    # --- TAB 1: CANLI VERİTABANI ---
    with tabs[0]:
        st.subheader("Global Kullanıcı Listesi")
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
        
        if st.button("💾 Değişiklikleri Kaydet", type="primary"):
            st.session_state.users_db = edited_df.to_dict('records')
            st.toast("Veritabanı güncellendi.", icon="✅")

    # --- TAB 2, 3, 4 (Görsel Öğeler) ---
    with tabs[1]:
        f1, f2, f3 = st.columns(3)
        with f1: st.toggle("AI Lead Gen (Beta)", value=True)
        with f2: st.toggle("Stripe Sandbox", value=True)
        with f3: st.toggle("API v2", value=True)
    with tabs[2]:
        if st.button("Duyuru Gönder"): st.toast("İletildi!", icon="🚀")
    with tabs[3]:
        st.plotly_chart(revenue_chart(), use_container_width=True)
        st.dataframe(pd.DataFrame({"Zaman": ["14:02"], "Log": ["Cortex Agent Started"]}), use_container_width=True)

    st.markdown("---")
    st.caption(f"Powered by Google {MODEL_NAME} | Enterprise License")
