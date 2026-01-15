import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time
import json
import os
from datetime import datetime
from google import genai
from google.genai import types

# --- 1. MODEL VE İSTEMCİ ---
MODEL_NAME = "gemini-3-flash-preview"

def get_ai_client():
    api_key = st.secrets.get("GOOGLE_API_KEY") or os.environ.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY")
    if not api_key: return None
    return genai.Client(api_key=api_key)

# --- 2. GLOBAL STATE (TÜM SİSTEM HAFIZASI) ---
# AI'ın diğer modülleri yönetebilmesi için veritabanlarının burada da erişilebilir olması lazım.
def init_global_memory():
    if "users_db" not in st.session_state:
        st.session_state.users_db = [
            {"id": 101, "name": "Ahmet Yılmaz", "role": "admin", "status": "Active"},
            {"id": 102, "name": "Ayşe Demir", "role": "editor", "status": "Active"}
        ]
    if "forms_db" not in st.session_state:
        st.session_state.forms_db = [
            {"id": 1, "title": "Yıllık Rapor", "desc": "Finans departmanı için", "date": "2024-01-15"}
        ]
    if "inventory_db" not in st.session_state:
        st.session_state.inventory_db = [
            {"item": "Deri Çanta", "qty": 150},
            {"item": "Laptop Kılıfı", "qty": 300}
        ]

# --- 3. CORTEX SUPER BRAIN ---
def cortex_brain(prompt):
    client = get_ai_client()
    init_global_memory() # Hafızayı garantile
    
    # 1. SİSTEMİN RÖNTGENİNİ ÇEK (CONTEXT)
    # AI şu anki veritabanının tam halini görüyor
    system_context = {
        "users": st.session_state.users_db,
        "forms": st.session_state.forms_db,
        "inventory": st.session_state.inventory_db,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    if not client: return "⚠️ API Key Eksik!"

    # 2. SÜPER BEYİN TALİMATI (PROMPT)
    sys_instruction = f"""
    Sen CORTEX. Bu B2B SaaS platformunun "Süper Zekasısın".
    Sadece bir bot değilsin, sistemin veritabanına doğrudan müdahale eden bir yöneticisin.
    
    GÖREVİN:
    1. Kullanıcıyla normal bir insan gibi sohbet et (Açık uçlu soruları yanıtla).
    2. Kullanıcı bir İŞLEM isterse (Form ekle, Kullanıcıyı banla, Stok güncelle), uygun aracı seç.
    
    MEVCUT VERİTABANI DURUMU:
    {json.dumps(system_context)}

    YETENEKLERİN (TOOLS):
    - "create_form": Yeni bir form/görev oluşturur. (Parametreler: title, desc)
    - "ban_user": Kullanıcıyı yasaklar. (Parametre: target_name)
    - "update_inventory": Stok günceller. (Parametreler: item_name, new_qty)
    - "general_chat": Sadece sohbet, analiz veya bilgi verme.
    
    ÇIKTI FORMATI (JSON ZORUNLU):
    {{
        "thought": "Kullanıcının ne istediğini analiz ettiğin iç sesin.",
        "tool": "create_form" | "ban_user" | "update_inventory" | "general_chat",
        "args": {{ "title": "...", "desc": "..." }},  // Eğer tool chat ise burası boş obje {{}} olabilir
        "response_text": "Kullanıcıya vereceğin nihai, profesyonel, Türkçe cevap."
    }}

    ÖRNEK 1:
    User: "Mehmet 500 tane çanta getirecek, formlara ekle."
    JSON: {{
        "thought": "Kullanıcı yeni bir form kaydı istiyor.",
        "tool": "create_form",
        "args": {{ "title": "Lojistik: Çanta Teslimatı", "desc": "Mehmet tarafından 500 adet çanta getirilecek." }},
        "response_text": "Anlaşıldı, Mehmet'in 500 çanta teslimatını formlara işledim."
    }}

    ÖRNEK 2:
    User: "Şu an kaç kullanıcımız var ve durumları ne?"
    JSON: {{
        "thought": "Kullanıcı analiz istiyor, işlem yok.",
        "tool": "general_chat",
        "args": {{}},
        "response_text": "Sistemde toplam 2 kayıtlı kullanıcı var. Ahmet Yılmaz Admin rolünde..."
    }}
    """

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f"User: {prompt}",
            config=types.GenerateContentConfig(
                system_instruction=sys_instruction,
                temperature=0.3, # Biraz yaratıcılık ama kontrollü
                response_mime_type="application/json"
            )
        )
        
        # 3. YANITI İŞLE VE EYLEME DÖK (EXECUTION)
        ai_resp = json.loads(response.text)
        tool = ai_resp.get("tool")
        args = ai_resp.get("args", {})
        reply_text = ai_resp.get("response_text")
        
        # --- TOOL 1: FORM OLUŞTURMA ---
        if tool == "create_form":
            new_form = {
                "id": len(st.session_state.forms_db) + 1,
                "title": args.get("title", "Adsız Form"),
                "desc": args.get("desc", ""),
                "date": datetime.now().strftime("%Y-%m-%d")
            }
            st.session_state.forms_db.append(new_form)
            return f"✅ İŞLEM YAPILDI: {reply_text} (Form ID: {new_form['id']})"

        # --- TOOL 2: KULLANICI BANLAMA ---
        elif tool == "ban_user":
            target = args.get("target_name", "").lower()
            for u in st.session_state.users_db:
                if target in u['name'].lower():
                    u['status'] = 'Suspended'
                    return f"🚫 ERİŞİM KESİLDİ: {reply_text}"
            return f"⚠️ HATA: Kullanıcı bulunamadı ama mesajım şu: {reply_text}"

        # --- TOOL 3: ENVANTER GÜNCELLEME ---
        elif tool == "update_inventory":
            item_name = args.get("item_name")
            qty = args.get("new_qty")
            st.session_state.inventory_db.append({"item": item_name, "qty": qty})
            return f"📦 STOK GİRİLDİ: {reply_text}"

        # --- TOOL 4: GENEL SOHBET ---
        else:
            return f"💬 CORTEX: {reply_text}"

    except Exception as e:
        return f"⚡ KRİTİK HATA: {str(e)}"

# --- GÜVENLİK ---
def check_admin_access():
    if st.session_state.user_data.get('role') != 'admin':
        st.error("⛔ YETKİSİZ GİRİŞ TESPİT EDİLDİ")
        st.stop()

# --- STİL & TASARIM ---
def inject_admin_css():
    st.markdown("""
    <style>
        .admin-header-card { background: linear-gradient(135deg, #000 0%, #1a1a1a 100%); border: 1px solid #333; padding: 25px; border-radius: 16px; margin-bottom: 20px; }
        .cortex-terminal { background-color: #050505; border: 1px solid #333; border-top: 4px solid #7c3aed; border-radius: 8px; padding: 20px; font-family: 'Courier New', monospace; margin-bottom: 30px; }
        .ai-msg { color: #ddd; margin-top: 8px; border-left: 3px solid #7c3aed; padding-left: 12px; }
        .user-msg { color: #a78bfa; font-weight: bold; margin-top: 15px; }
        .success-log { color: #10B981; font-size: 12px; margin-top: 4px; }
    </style>
    """, unsafe_allow_html=True)

# --- ANA RENDER ---
def render():
    check_admin_access()
    inject_admin_css()
    init_global_memory()

    # HEADER
    st.markdown(f"""
        <div class='admin-header-card'>
            <div style='display:flex; justify-content:space-between;'>
                <div>
                    <h1 style='margin:0; font-size:2rem;'>🛡️ ARTIS CORTEX</h1>
                    <p style='color:#888; margin:0;'>Tam Yetkili Otonom Yönetim Sistemi ({MODEL_NAME})</p>
                </div>
                <div style='text-align:right;'>
                    <div style='background:#7c3aed; color:white; padding:5px 15px; border-radius:20px; font-size:12px; font-weight:bold;'>GOD MODE ACTIVE</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # CORTEX TERMİNALİ
    st.markdown("### 🧠 Süper Beyin Terminali")
    st.caption("Sistemdeki her şeyi yönetebilirim. Form oluşturabilir, kullanıcı yasaklayabilir veya analiz yapabilirim.")
    
    with st.container():
        st.markdown("<div class='cortex-terminal'>", unsafe_allow_html=True)
        
        if "cortex_history" not in st.session_state:
            st.session_state.cortex_history = [{"role": "ai", "content": "Sistem veritabanına tam erişim sağlandı. Emrinizi bekliyorum."}]
        
        for msg in st.session_state.cortex_history[-4:]: 
            role_class = "user-msg" if msg['role'] == 'user' else "ai-msg"
            icon = ">" if msg['role'] == 'user' else "⚡"
            st.markdown(f"<div class='{role_class}'>{icon} {msg['content']}</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # INPUT ALANI
        cortex_input = st.chat_input("Emir verin (Örn: 'Mehmet 500 çanta getirecek, forma işle')...")
        if cortex_input:
            st.session_state.cortex_history.append({"role": "user", "content": cortex_input})
            with st.spinner("CORTEX sistemi analiz ediyor ve işlem yapıyor..."):
                resp = cortex_brain(cortex_input)
                st.session_state.cortex_history.append({"role": "ai", "content": resp})
            st.rerun()

    # --- CANLI SİSTEM İZLEME (TABLAR) ---
    st.markdown("### 📡 Canlı Sistem Verileri")
    tabs = st.tabs(["📝 Formlar & Görevler", "👥 Kullanıcılar", "📦 Envanter", "⚙️ Loglar"])

    # TAB 1: FORMLAR (AI BURAYA YAZACAK)
    with tabs[0]:
        st.info("AI'ın oluşturduğu formlar burada görünür.")
        st.dataframe(pd.DataFrame(st.session_state.forms_db), use_container_width=True, hide_index=True)
        
    # TAB 2: KULLANICILAR
    with tabs[1]:
        st.dataframe(pd.DataFrame(st.session_state.users_db), use_container_width=True, hide_index=True)

    # TAB 3: ENVANTER
    with tabs[2]:
        st.dataframe(pd.DataFrame(st.session_state.inventory_db), use_container_width=True, hide_index=True)

    # TAB 4: LOGLAR
    with tabs[3]:
        st.text("System Logs:\n[INFO] Gemini 3 Client Connected.\n[INFO] Global State Loaded.")
