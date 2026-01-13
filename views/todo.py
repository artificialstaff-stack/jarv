import streamlit as st
import pandas as pd
import time
from datetime import datetime

# ==============================================================================
# 🎨 1. SAYFAYA ÖZEL STİL (GÖREV YÖNETİMİ)
# ==============================================================================
def inject_todo_css():
    st.markdown("""
    <style>
        /* Görev Kartı */
        .task-card {
            background-color: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-left: 4px solid #52525B; /* Varsayılan border */
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
        }
        
        /* Öncelik Renkleri (Sol Border) */
        .prio-High { border-left-color: #EF4444 !important; }
        .prio-Medium { border-left-color: #F59E0B !important; }
        .prio-Low { border-left-color: #3B82F6 !important; }

        /* Metin Stilleri */
        .task-title { font-weight: 500; font-size: 15px; color: #E4E4E7; }
        .task-meta { font-size: 12px; color: #A1A1AA; display: flex; gap: 10px; margin-top: 4px; }
        
        /* Etiket (Tag) */
        .task-tag {
            background: rgba(255,255,255,0.1);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 11px;
        }

        /* İlerleme Çubuğu Konteynerı */
        .progress-container {
            background: #18181B;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 25px;
            border: 1px solid #27272A;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🛠️ 2. GÖREV MANTIĞI (SESSION STATE)
# ==============================================================================
def init_todo_state():
    if "todos" not in st.session_state:
        st.session_state.todos = [
            {"id": 1, "task": "Vergileri öde", "tag": "Finans", "prio": "High", "done": False, "date": "2026-01-15"},
            {"id": 2, "task": "Washington stok sayımı", "tag": "Operasyon", "prio": "Medium", "done": False, "date": "2026-01-20"},
            {"id": 3, "task": "Yeni tedarikçi görüşmesi", "tag": "Yönetim", "prio": "Low", "done": True, "date": "2026-01-10"},
        ]

def add_task(task_name, tag, prio):
    new_id = len(st.session_state.todos) + 1
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
    # Kart Tasarımı
    prio_class = f"prio-{task['prio']}"
    opacity = "0.5" if task['done'] else "1.0"
    strike = "text-decoration: line-through;" if task['done'] else ""
    icon = "✅" if task['done'] else "⬜"
    
    # Grid Yapısı
    c_check, c_info, c_action = st.columns([0.5, 3, 0.5])
    
    with c_check:
        # Checkbox yerine buton kullanıyoruz daha şık durması için
        if st.button(icon, key=f"chk_{idx}_{task['id']}"):
            toggle_task(idx)
            st.rerun()
            
    with c_info:
        st.markdown(f"""
        <div class="task-card {prio_class}" style="opacity: {opacity}; margin-bottom:0;">
            <div>
                <div class="task-title" style="{strike}">{task['task']}</div>
                <div class="task-meta">
                    <span class="task-tag">{task['tag']}</span>
                    <span>📅 {task['date']}</span>
                    <span style="color: {'#EF4444' if task['prio']=='High' else '#A1A1AA'}">{task['prio']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with c_action:
        if st.button("🗑️", key=f"del_{idx}_{task['id']}"):
            delete_task(idx)
            st.rerun()

# ==============================================================================
# 🚀 4. ANA RENDER FONKSİYONU
# ==============================================================================
def render_todo():
    inject_todo_css()
    init_todo_state()
    
    # --- HEADER ---
    c1, c2 = st.columns([3, 1])
    with c1:
        st.title("✅ Görev Yönetimi")
        st.caption("Takım içi görev atamaları ve takip listesi.")
    with c2:
        # KPI Hesaplama
        total = len(st.session_state.todos)
        done = sum(1 for t in st.session_state.todos if t['done'])
        pending = total - done
        percent = int((done / total) * 100) if total > 0 else 0
        
        st.metric("Tamamlanan", f"{percent}%", f"{pending} Bekleyen", delta_color="normal")
        
    st.markdown("---")

    # --- YENİ GÖREV EKLEME (ADD BAR) ---
    with st.expander("➕ Yeni Görev Ekle", expanded=True):
        with st.form("add_task_form", clear_on_submit=True):
            c_input, c_tag, c_prio, c_btn = st.columns([3, 1.5, 1.5, 1])
            
            with c_input:
                new_task = st.text_input("Görev Adı", placeholder="Örn: Aylık raporu hazırla...")
            with c_tag:
                new_tag = st.selectbox("Etiket", ["Genel", "Finans", "Lojistik", "Yönetim", "Teknik"])
            with c_prio:
                new_prio = st.selectbox("Öncelik", ["High", "Medium", "Low"])
            with c_btn:
                st.markdown("<br>", unsafe_allow_html=True)
                submitted = st.form_submit_button("Ekle", type="primary", use_container_width=True)
                
            if submitted and new_task:
                add_task(new_task, new_tag, new_prio)
                st.toast("Görev eklendi!", icon="✅")
                st.rerun()

    # --- İLERLEME ÇUBUĞU ---
    st.progress(percent / 100)

    # --- GÖREV LİSTESİ ---
    tab_active, tab_completed = st.tabs(["🔥 Aktif Görevler", "✔️ Tamamlananlar"])
    
    with tab_active:
        active_tasks = [(i, t) for i, t in enumerate(st.session_state.todos) if not t['done']]
        if not active_tasks:
            st.info("Harika! Tüm aktif görevleri tamamladınız.")
        else:
            for idx, task in active_tasks:
                render_task_row(task, idx)
                
    with tab_completed:
        done_tasks = [(i, t) for i, t in enumerate(st.session_state.todos) if t['done']]
        if not done_tasks:
            st.caption("Henüz tamamlanmış görev yok.")
        else:
            for idx, task in done_tasks:
                render_task_row(task, idx)
