import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

# ==============================================================================
# 🎨 1. BİRLEŞTİRİLMİŞ CSS MOTORU
# ==============================================================================
def inject_operations_css():
    st.markdown("""
    <style>
        /* --- GENEL KART STİLLERİ --- */
        .metric-card-small {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
        }
        .metric-label { font-size: 12px; color: #A1A1AA; text-transform: uppercase; letter-spacing: 1px; }
        .metric-value { font-size: 24px; font-weight: 700; color: #FFF; }

        /* --- GÖREV KARTLARI (TODO) --- */
        .task-card {
            background-color: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-left: 4px solid #52525B;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            display: flex; align-items: center; justify-content: space-between;
            transition: all 0.2s;
        }
        .task-card:hover { transform: translateX(4px); background-color: rgba(255, 255, 255, 0.04); }
        .prio-High { border-left-color: #EF4444 !important; }
        .prio-Medium { border-left-color: #F59E0B !important; }
        .prio-Low { border-left-color: #3B82F6 !important; }
        .task-title { font-weight: 500; font-size: 15px; color: #E4E4E7; }
        .task-meta { font-size: 11px; color: #A1A1AA; display: flex; gap: 10px; margin-top: 4px; }
        .task-tag { background: rgba(255,255,255,0.08); padding: 2px 8px; border-radius: 4px; font-weight: 600; }

        /* --- DOSYA SATIRLARI (DOCS) --- */
        .file-row {
            background-color: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 8px;
            display: flex; align-items: center; justify-content: space-between;
        }
        .file-icon-box {
            width: 40px; height: 40px; border-radius: 8px;
            display: flex; align-items: center; justify-content: center; font-size: 20px;
            margin-right: 15px;
        }
        .icon-pdf { background: rgba(239, 68, 68, 0.15); color: #F87171; }
        .icon-xls { background: rgba(16, 185, 129, 0.15); color: #34D399; }
        .icon-img { background: rgba(59, 130, 246, 0.15); color: #60A5FA; }
        .doc-tag { font-size: 10px; padding: 2px 8px; border-radius: 10px; background: rgba(255,255,255,0.05); color: #A1A1AA; }

        /* --- LOJİSTİK WIZARD (FORMS) --- */
        .wizard-container { display: flex; justify-content: space-between; margin-bottom: 30px; position: relative; max-width: 500px; margin-left: auto; margin-right: auto; }
        .wizard-line { position: absolute; top: 15px; left: 0; right: 0; height: 2px; background: #27272A; z-index: 0; }
        .step-item { z-index: 1; background: #000000; padding: 0 10px; display: flex; flex-direction: column; align-items: center; gap: 5px; }
        .step-circle { width: 30px; height: 30px; border-radius: 50%; background: #18181B; border: 2px solid #3F3F46; color: #71717A; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px; }
        .step-active .step-circle { border-color: #3B82F6; background: rgba(59, 130, 246, 0.1); color: #3B82F6; }
        
        /* Özet Kartı */
        .summary-card { background: #18181B; border: 1px solid #27272A; border-radius: 12px; padding: 20px; }
        .summary-total { font-size: 28px; font-weight: 800; color: #FFF; letter-spacing: -1px; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧠 2. VERİ YÖNETİMİ (STATE)
# ==============================================================================
def init_state():
    # Görevler
    if "todos" not in st.session_state:
        st.session_state.todos = [
            {"id": 1, "task": "Vergileri öde", "tag": "Finans", "prio": "High", "done": False, "date": "2026-01-15"},
            {"id": 2, "task": "Washington stok sayımı", "tag": "Operasyon", "prio": "Medium", "done": False, "date": "2026-01-20"},
        ]
    # Dosyalar (Mock)
    if "documents" not in st.session_state:
        st.session_state.documents = [
            {"name": "2026_Ocak_Gümrük_Beyan.pdf", "type": "pdf", "size": "2.4 MB", "date": "14 Jan", "category": "Gümrük"},
            {"name": "Stok_Listesi_v2.xlsx", "type": "xls", "size": "850 KB", "date": "12 Jan", "category": "Lojistik"},
            {"name": "Hasar_Raporu_001.jpg", "type": "img", "size": "4.2 MB", "date": "08 Jan", "category": "Saha"},
        ]

# --- Yardımcı Fonksiyonlar ---
def add_task(task, tag, prio):
    new_id = int(time.time())
    st.session_state.todos.insert(0, {"id": new_id, "task": task, "tag": tag, "prio": prio, "done": False, "date": datetime.now().strftime("%Y-%m-%d")})

def delete_task(idx):
    st.session_state.todos.pop(idx)

def toggle_task(idx):
    st.session_state.todos[idx]['done'] = not st.session_state.todos[idx]['done']

# ==============================================================================
# 🧩 3. ALT BİLEŞENLER (RENDERERS)
# ==============================================================================

def render_summary_header():
    """Sayfanın en üstündeki özet bant"""
    total_tasks = len(st.session_state.todos)
    pending_tasks = sum(1 for t in st.session_state.todos if not t['done'])
    doc_count = len(st.session_state.documents)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class='metric-card-small'><div class='metric-label'>Bekleyen İş</div><div class='metric-value' style='color:#F59E0B'>{pending_tasks}</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class='metric-card-small'><div class='metric-label'>Tamamlanan</div><div class='metric-value' style='color:#10B981'>{total_tasks - pending_tasks}</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class='metric-card-small'><div class='metric-label'>Aktif Sevkiyat</div><div class='metric-value'>2</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class='metric-card-small'><div class='metric-label'>Arşiv Dosyası</div><div class='metric-value'>{doc_count}</div></div>""", unsafe_allow_html=True)

def render_wizard_html(step):
    steps = [{"n":1,"t":"Kargo"},{"n":2,"t":"Lojistik"},{"n":3,"t":"Onay"}]
    html = ['<div class="wizard-container"><div class="wizard-line"></div>']
    for s in steps:
        active = "step-active" if s["n"] <= step else ""
        icon = "✓" if s["n"] < step else str(s["n"])
        html.append(f'<div class="step-item {active}"><div class="step-circle">{icon}</div><div style="font-size:10px; color:#666">{s["t"]}</div></div>')
    html.append('</div>')
    return "".join(html)

# ==============================================================================
# 🚀 4. ANA EKRAN VE SEKMELER
# ==============================================================================
def render_operations():
    inject_operations_css()
    init_state()
    
    st.title("🛠️ Operasyon Merkezi")
    st.caption("Üretim, sevkiyat ve görevlerinizi tek bir yerden yönetin.")
    
    # 1. ÖZET BANT
    render_summary_header()
    st.markdown("<br>", unsafe_allow_html=True)

    # 2. ANA SEKMELER
    tab_logistics, tab_tasks, tab_docs = st.tabs(["🚢 Yeni Sevkiyat & Talep", "✅ Görev Listesi", "📂 Dijital Arşiv"])

    # --- SEKME 1: LOJİSTİK (FORMS) ---
    with tab_logistics:
        st.markdown(render_wizard_html(1), unsafe_allow_html=True)
        col_form, col_info = st.columns([2, 1])
        
        with col_form:
            with st.form("shipment_form"):
                st.subheader("📦 Sevkiyat Emri Oluştur")
                c1, c2 = st.columns(2)
                product = c1.selectbox("Ürün Tipi", ["Tekstil", "Gıda", "Mobilya", "Yedek Parça"])
                boxes = c2.number_input("Koli Adedi", 1, 1000, 50)
                
                c3, c4 = st.columns(2)
                origin = c3.selectbox("Çıkış Deposu", ["İstanbul", "Bursa", "İzmir"])
                service = c4.radio("Hizmet", ["Ekonomik (Gemi)", "Ekspres (Uçak)"], horizontal=True)
                
                note = st.text_area("Notlar", height=80, placeholder="Özel paketleme isteği vb.")
                
                if st.form_submit_button("🚀 Talebi Gönder", type="primary", use_container_width=True):
                    with st.status("İşleniyor...", expanded=True):
                        time.sleep(1)
                        st.write("✅ Stok kontrol edildi.")
                        time.sleep(0.5)
                        st.write("✅ Lojistik planlamaya iletildi.")
                    st.success(f"Talep alındı! Referans: TR-{random.randint(1000,9999)}")

        with col_info:
            price = boxes * (12 if "Gemi" in service else 45)
            st.markdown(f"""
            <div class="summary-card">
                <div style="font-size:12px; color:#888;">TAHMİNİ MALİYET</div>
                <div class="summary-total">${price:,}</div>
                <div style="margin-top:15px; font-size:14px; color:#AAA;">
                    <div>📦 {boxes} Koli</div>
                    <div>📍 {origin} Çıkışlı</div>
                    <div>🚀 {service}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.info("💡 100 koli üzeri gönderimlerde %10 indirim uygulanır.")

    # --- SEKME 2: GÖREVLER (TODO) ---
    with tab_tasks:
        c_add, c_list = st.columns([1, 2])
        
        with c_add:
            st.markdown("##### ⚡ Hızlı Görev Ekle")
            with st.form("add_task"):
                t_name = st.text_input("Görev Adı", placeholder="Örn: Faturayı kes")
                t_tag = st.selectbox("Etiket", ["Genel", "Finans", "Lojistik", "Üretim"])
                t_prio = st.select_slider("Öncelik", ["Low", "Medium", "High"], value="Medium")
                if st.form_submit_button("Ekle", use_container_width=True):
                    if t_name:
                        add_task(t_name, t_tag, t_prio)
                        st.rerun()

        with c_list:
            st.markdown("##### 📋 Yapılacaklar")
            # Aktif Görevler
            active_tasks = [t for t in st.session_state.todos if not t['done']]
            if not active_tasks:
                st.success("Tüm görevler tamamlandı! 🎉")
            
            for i, task in enumerate(st.session_state.todos):
                if not task['done']:
                    idx = st.session_state.todos.index(task)
                    prio_color = "#EF4444" if task['prio']=="High" else "#F59E0B" if task['prio']=="Medium" else "#3B82F6"
                    
                    c_chk, c_txt, c_del = st.columns([0.5, 4, 0.5])
                    if c_chk.button("⬜", key=f"chk_{task['id']}"):
                        toggle_task(idx)
                        st.rerun()
                    
                    c_txt.markdown(f"""
                        <div class="task-card" style="border-left-color: {prio_color}; margin:0;">
                            <div>
                                <div class="task-title">{task['task']}</div>
                                <div class="task-meta">
                                    <span class="task-tag">{task['tag']}</span> • {task['date']}
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    if c_del.button("🗑️", key=f"del_{task['id']}"):
                        delete_task(idx)
                        st.rerun()

            # Tamamlananları Göster/Gizle
            with st.expander("Tamamlanan Görevler"):
                done_tasks = [t for t in st.session_state.todos if t['done']]
                for t in done_tasks:
                    st.markdown(f"~~{t['task']}~~ <span style='font-size:10px; color:green'>Tamamlandı</span>", unsafe_allow_html=True)

    # --- SEKME 3: DOKÜMANLAR (DOCS) ---
    with tab_docs:
        c_filter, c_upload = st.columns([2, 1])
        
        with c_filter:
            search = st.text_input("🔍 Dosya Ara", placeholder="Dosya adı...")
        
        with c_upload:
            uploaded = st.file_uploader("Yükle", label_visibility="collapsed")
            if uploaded: st.toast("Dosya yüklendi!", icon="cloud")

        st.markdown("##### 📄 Son Dosyalar")
        
        docs = st.session_state.documents
        if search:
            docs = [d for d in docs if search.lower() in d['name'].lower()]
            
        for idx, doc in enumerate(docs):
            icon_cls = "icon-pdf" if "pdf" in doc['type'] else "icon-xls" if "xls" in doc['type'] else "icon-img"
            icon_html = "📄" # Basitlik için
            
            c1, c2, c3 = st.columns([0.5, 3, 1])
            with c1:
                st.markdown(f"<div class='file-icon-box {icon_cls}'><i class='bx bx-file'></i></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"**{doc['name']}**")
                st.caption(f"{doc['size']} • {doc['date']} • {doc['category']}")
            with c3:
                st.button("⬇️ İndir", key=f"dl_{idx}", use_container_width=True)
            
            st.markdown("<hr style='margin:5px 0; border-color:rgba(255,255,255,0.05)'>", unsafe_allow_html=True)

# Test için (sadece bu dosya çalıştırılırsa)
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Operations Hub")
    render_operations()
