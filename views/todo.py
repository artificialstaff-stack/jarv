import streamlit as st
import pandas as pd
import time
from datetime import datetime

# ==============================================================================
# 🎨 1. SAYFAYA ÖZEL STİL (LINEAR STYLE)
# ==============================================================================
def inject_todo_css():
    st.markdown("""
    <style>
        /* Görev Kartı */
        .task-card {
            background-color: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-left: 4px solid #52525B;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.2s;
        }
        .task-card:hover {
            background-color: rgba(255, 255, 255, 0.04);
            transform: translateX(4px);
            border-color: rgba(255, 255, 255, 0.1);
        }
        
        /* Öncelik Renkleri */
        .prio-High { border-left-color: #EF4444 !important; }
        .prio-Medium { border-left-color: #F59E0B !important; }
        .prio-Low { border-left-color: #3B82F6 !important; }

        /* Tipografi */
        .task-title { font-weight: 500; font-size: 15px; color: #E4E4E7; }
        .task-meta { font-size: 12px; color: #A1A1AA; display: flex; gap: 10px; margin-top: 6px; }
        
        /* Etiket */
        .task-tag {
            background: rgba(255,255,255,0.08);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🛠️ 2. GÖREV MANTIĞI & VERİ ONARIMI
# ==============================================================================
def init_todo_state():
    # Varsayılan (Modern) Veri Yapısı
    default_todos = [
        {"id": 1, "task": "Vergileri öde", "tag": "Finans", "prio": "High", "done": False, "date": "2026-01-15"},
        {"id": 2, "task": "Washington stok sayımı", "tag": "Operasyon", "prio": "Medium", "done": False, "date": "2026-01-20"},
        {"id": 3, "task": "Yeni tedarikçi görüşmesi", "tag": "Yönetim", "prio": "Low", "done": True, "date": "2026-01-10"},
    ]

    # Durum 1: Hiç veri yoksa oluştur
    if "todos" not in st.session_state:
        st.session_state.todos = default_todos
    
    # Durum 2: Eski tip (bozuk) veri varsa ONAR (Hata burada çözülüyor)
    elif len(st.session_state.todos) > 0:
        # Eğer listedeki ilk eleman bir "sözlük" değilse (yani eskiyse), sıfırla.
        if not isinstance(st.session_state.todos[0], dict):
            st.session_state.todos = default_todos
            st.rerun() # Sayfayı yenile ki hata vermesin

def add_task(task_name, tag, prio):
    new_id = int(time.time()) # Benzersiz ID
    today = datetime.now().strftime("%Y-%m-%d")
    st.session_state.todos.insert(0, {
        "id": new_id, 
        "task": task_name, 
        "tag": tag, 
        "prio": prio, 
        "done": False, 
        "date": today
    })

def delete_task(idx):
    st.session_state.todos.pop(idx)

def toggle_task(idx):
    st.session_state.todos[idx]['done'] = not st.session_state.todos[idx]['done']

# ==============================================================================
# 🧩 3. UI BİLEŞENLERİ
# ==============================================================================
def render_task_row(task, idx):
    prio_class = f"prio-{task.get('prio', 'Low')}"
    opacity = "0.5" if task.get('done', False) else "1.0"
    strike = "text-decoration: line-through; color: #71717A;" if task.get('done', False) else ""
    icon = "✅" if task.get('done', False) else "⬜"
    
    # Grid: Checkbox | Bilgi | Sil Butonu
    c_check, c_info, c_del = st.columns([0.5, 4, 0.5])
    
    with c_check:
        if st.button(icon, key=f"chk_{task['id']}"):
            toggle_task(idx)
            st.rerun()
            
    with c_info:
        st.markdown(f"""
        <div class="task-card {prio_class}" style="opacity: {opacity};">
            <div style="width:100%">
                <div class="task-title" style="{strike}">{task['task']}</div>
                <div class="task-meta">
                    <span class="task-tag">{task['tag']}</span>
                    <span>📅 {task['date']}</span>
                    <span style="color: {'#EF4444' if task['prio']=='High' else '#A1A1AA'}">{task['prio']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with c_del:
        if st.button("🗑️", key=f"del_{task['id']}"):
            delete_task(idx)
            st.rerun()

# ==============================================================================
# 🚀 4. ANA RENDER FONKSİYONU
# ==============================================================================
def render_todo():
    inject_todo_css()
    init_todo_state() # Veriyi kontrol et ve onar
    
    # --- HEADER ---
    c1, c2 = st.columns([3, 1])
    with c1:
        st.title("✅ Görev Yönetimi")
        st.caption("Takım içi görev atamaları ve sprint takibi.")
    with c2:
        # KPI Hesaplama
        todos = st.session_state.todos
        total = len(todos)
        done = sum(1 for t in todos if t.get('done', False))
        percent = int((done / total) * 100) if total > 0 else 0
        st.metric("Tamamlanma", f"%{percent}", f"{total - done} Bekleyen")
        
    st.markdown("---")

    # --- HIZLI EKLEME PANELI ---
    with st.expander("⚡ Hızlı Görev Ekle", expanded=True):
        with st.form("new_task_form", clear_on_submit=True):
            c_input, c_tag, c_prio, c_btn = st.columns([3, 1.2, 1.2, 1])
            with c_input:
                new_task = st.text_input("Görev", placeholder="Örn: Q1 Raporlarını hazırla...")
            with c_tag:
                new_tag = st.selectbox("Etiket", ["Genel", "Finans", "Lojistik", "Yazılım", "İK"])
            with c_prio:
                new_prio = st.selectbox("Öncelik", ["High", "Medium", "Low"])
            with c_btn:
                st.markdown("<br>", unsafe_allow_html=True)
                submitted = st.form_submit_button("Ekle", type="primary", use_container_width=True)
            
            if submitted and new_task:
                add_task(new_task, new_tag, new_prio)
                st.toast("Görev listeye eklendi.", icon="📌")
                st.rerun()

    # --- İLERLEME ---
    if total > 0:
        st.progress(percent / 100)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- LİSTELEME ---
    tab_active, tab_done = st.tabs(["🔥 Yapılacaklar", "✔️ Tamamlananlar"])
    
    with tab_active:
        # Sadece yapılmamışları filtrele
        active_list = [(i, t) for i, t in enumerate(st.session_state.todos) if not t.get('done', False)]
        
        if not active_list:
            st.info("Harika! Tüm görevler tamamlandı.")
        else:
            for i, task in active_list:
                render_task_row(task, i)

    with tab_done:
        # Sadece yapılmışları filtrele
        done_list = [(i, t) for i, t in enumerate(st.session_state.todos) if t.get('done', False)]
        
        if not done_list:
            st.caption("Henüz tamamlanan görev yok.")
        else:
            for i, task in done_list:
                render_task_row(task, i)
