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

        /* --- GÖREV KARTLARI --- */
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

        /* --- DOSYA SATIRLARI --- */
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
        
        /* --- PRO FORM STİLLERİ --- */
        .form-section-title {
            color: #C5A059;
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 20px;
            margin-bottom: 10px;
            border-bottom: 1px solid rgba(197, 160, 89, 0.2);
            padding-bottom: 5px;
        }
        .summary-card { background: #18181B; border: 1px solid #27272A; border-radius: 12px; padding: 20px; position: sticky; top: 20px; }
        .summary-total { font-size: 28px; font-weight: 800; color: #FFF; letter-spacing: -1px; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🧠 2. VERİ YÖNETİMİ (STATE)
# ==============================================================================
def init_state():
    if "todos" not in st.session_state:
        st.session_state.todos = [
            {"id": 1, "task": "Vergileri öde", "tag": "Finans", "prio": "High", "done": False, "date": "2026-01-15"},
            {"id": 2, "task": "Washington stok sayımı", "tag": "Operasyon", "prio": "Medium", "done": False, "date": "2026-01-20"},
        ]
    # Arşiv veritabanını başlat
    if "documents" not in st.session_state:
        st.session_state.documents = [
            {"name": "2026_Ocak_Gümrük_Beyan.pdf", "type": "pdf", "size": "2.4 MB", "date": "14 Jan", "category": "Gümrük"},
            {"name": "Stok_Listesi_v2.xlsx", "type": "xls", "size": "850 KB", "date": "12 Jan", "category": "Lojistik"},
        ]

# --- Yardımcı Fonksiyonlar ---
def add_task(task, tag, prio):
    new_id = int(time.time())
    st.session_state.todos.insert(0, {"id": new_id, "task": task, "tag": tag, "prio": prio, "done": False, "date": datetime.now().strftime("%Y-%m-%d")})

def delete_task(idx):
    st.session_state.todos.pop(idx)

def toggle_task(idx):
    st.session_state.todos[idx]['done'] = not st.session_state.todos[idx]['done']

def save_uploaded_file(uploaded_file, category="Genel"):
    """Dosyayı hafızaya kaydeder ve Arşiv sekmesinde gösterir."""
    if uploaded_file is not None:
        # Dosya tipini belirle
        if "pdf" in uploaded_file.type: file_type = "pdf"
        elif "sheet" in uploaded_file.type or "excel" in uploaded_file.type: file_type = "xls"
        else: file_type = "img"
        
        file_size = f"{uploaded_file.size / 1024:.1f} KB"
        
        # Yeni dosya objesi
        new_doc = {
            "name": uploaded_file.name,
            "type": file_type,
            "size": file_size,
            "date": datetime.now().strftime("%d %b"),
            "category": category
        }
        
        # Listeye en başa ekle (Session State'e yazar)
        st.session_state.documents.insert(0, new_doc)
        return True
    return False

# ==============================================================================
# 🧩 3. ALT BİLEŞENLER
# ==============================================================================
def render_summary_header():
    total_tasks = len(st.session_state.todos)
    pending_tasks = sum(1 for t in st.session_state.todos if not t['done'])
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(f"""<div class='metric-card-small'><div class='metric-label'>Bekleyen İş</div><div class='metric-value' style='color:#F59E0B'>{pending_tasks}</div></div>""", unsafe_allow_html=True)
    with c2: st.markdown(f"""<div class='metric-card-small'><div class='metric-label'>Tamamlanan</div><div class='metric-value' style='color:#10B981'>{total_tasks - pending_tasks}</div></div>""", unsafe_allow_html=True)
    with c3: st.markdown(f"""<div class='metric-card-small'><div class='metric-label'>Aktif Sevkiyat</div><div class='metric-value'>2</div></div>""", unsafe_allow_html=True)
    with c4: st.markdown(f"""<div class='metric-card-small'><div class='metric-label'>Arşiv</div><div class='metric-value'>{len(st.session_state.documents)}</div></div>""", unsafe_allow_html=True)

# ==============================================================================
# 🚀 4. ANA EKRAN
# ==============================================================================
def render_operations():
    inject_operations_css()
    init_state()
    
    st.title("🛠️ Operasyon Merkezi")
    st.caption("Üretim, sevkiyat ve görevlerinizi tek bir yerden yönetin.")
    
    render_summary_header()
    st.markdown("<br>", unsafe_allow_html=True)

    tab_logistics, tab_tasks, tab_docs = st.tabs(["🚢 Yeni İhracat Talebi (ABD)", "✅ Görev Listesi", "📂 Dijital Arşiv"])

    # --- SEKME 1: PROFESYONEL İHRACAT FORMU ---
    with tab_logistics:
        col_form, col_summary = st.columns([2, 1], gap="large")
        
        with col_form:
            with st.form("export_form"):
                st.markdown("### 🇹🇷 ➔ 🇺🇸 ABD İhracat & Lojistik Formu")
                st.caption("Lütfen gümrükleme ve lojistik işlemleri için tüm alanları eksiksiz doldurun.")
                
                # 1. ÜRÜN VE GÜMRÜK DETAYLARI
                st.markdown('<div class="form-section-title">1. ÜRÜN & GÜMRÜK DETAYLARI</div>', unsafe_allow_html=True)
                c1, c2 = st.columns(2)
                product_name = c1.text_input("Ürün Tanımı (İngilizce)", placeholder="Örn: 100% Cotton Towels")
                hs_code = c2.text_input("GTİP Kodu (HS Code)", placeholder="Örn: 6302.60.00.00.00", help="Gümrük Tarife İstatistik Pozisyonu (12 Hane)")
                
                c3, c4 = st.columns(2)
                material_origin = c3.selectbox("Menşei", ["Türkiye (TR)", "Diğer"])
                incoterms = c4.selectbox("Teslim Şekli (Incoterms)", ["EXW - İşyerinde Teslim", "FOB - Gemi Güvertesinde", "CIF - Mal Bedeli, Sigorta, Navlun", "DDP - Gümrük Vergileri Ödenmiş"], index=3)

                # 2. PAKETLEME VE HACİM
                st.markdown('<div class="form-section-title">2. PAKETLEME & HACİM (PL)</div>', unsafe_allow_html=True)
                cc1, cc2 = st.columns(2)
                total_cartons = cc1.number_input("Toplam Koli Adedi", min_value=1, value=50)
                total_weight = cc2.number_input("Toplam Brüt Ağırlık (kg)", min_value=1.0, value=500.0)
                
                st.caption("Koli Ebatları (cm) - Hacimsel ağırlık hesabı için gereklidir.")
                d1, d2, d3 = st.columns(3)
                dim_l = d1.number_input("Boy (L)", value=60)
                dim_w = d2.number_input("En (W)", value=40)
                dim_h = d3.number_input("Yükseklik (H)", value=40)

                # 3. ALICI VE SEVKİYAT BİLGİLERİ
                st.markdown('<div class="form-section-title">3. SEVKİYAT & ALICI (CONSIGNEE)</div>', unsafe_allow_html=True)
                s1, s2 = st.columns(2)
                ship_method = s1.radio("Taşıma Modu", ["Deniz Yolu (LCL - Parsiyel)", "Deniz Yolu (FCL - Full Konteyner)", "Hava Kargo (Express)"], index=0)
                pickup_loc = s2.selectbox("Yükleme Adresi", ["İstanbul (Depo)", "İzmir (Fabrika)", "Bursa (Fabrika)", "Gaziantep (Fabrika)"])
                
                consignee = st.text_area("Alıcı (Consignee) Adres & Vergi No (EIN)", placeholder="Örn: Amazon FBA Warehouse TEB3\n123 Logistics Way, NJ 08000\nTax ID: XX-XXXXXXX", height=80)
                
                # 4. DOKÜMAN YÜKLEME
                st.markdown('<div class="form-section-title">4. ZORUNLU BELGELER</div>', unsafe_allow_html=True)
                st.info("Buraya yüklenen belgeler otomatik olarak **Dijital Arşiv** sekmesine kaydedilir.")
                doc1 = st.file_uploader("Çeki Listesi (Packing List)", type=["pdf", "xlsx"], key="pl_up")
                doc2 = st.file_uploader("Ticari Fatura (Commercial Invoice)", type=["pdf", "xlsx"], key="ci_up")

                st.markdown("---")
                submitted = st.form_submit_button("🚀 Teklif Al ve Operasyonu Başlat", type="primary", use_container_width=True)

        with col_summary:
            volumetric_weight = (dim_l * dim_w * dim_h / 5000) * total_cartons
            chargeable_weight = max(total_weight, volumetric_weight)
            cbm = (dim_l * dim_w * dim_h * total_cartons) / 1000000
            
            rate = 4.5 if "Hava" in ship_method else 0.8
            est_cost = chargeable_weight * rate
            
            st.markdown(f"""
            <div class="summary-card">
                <div style="font-size:12px; color:#888;">TAHMİNİ NAVLUN BEDELİ</div>
                <div class="summary-total">${est_cost:,.2f}</div>
                <div style="margin-top:15px; font-size:13px; color:#AAA; line-height: 1.6;">
                    <div style="display:flex; justify-content:space-between;"><span>📦 Koli:</span> <span style="color:#FFF">{total_cartons} Adet</span></div>
                    <div style="display:flex; justify-content:space-between;"><span>⚖️ Hacim:</span> <span style="color:#FFF">{cbm:.2f} CBM</span></div>
                    <div style="display:flex; justify-content:space-between;"><span>📏 Hacimsel Kg:</span> <span style="color:#FFF">{volumetric_weight:.1f} kg</span></div>
                    <div style="display:flex; justify-content:space-between;"><span>💰 Ücretlendirilen:</span> <span style="color:#C5A059; font-weight:bold;">{chargeable_weight:.1f} kg</span></div>
                    <hr style="border-color:#333;">
                    <div style="color:#3B82F6;">ℹ️ {incoterms.split('-')[0]} seçildi.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        if submitted:
            if not product_name or not hs_code:
                st.error("Lütfen Ürün Tanımı ve GTİP Kodunu giriniz.")
            else:
                # --- DOSYALARI KAYDETME İŞLEMİ ---
                files_saved = 0
                if doc1:
                    save_uploaded_file(doc1, category="Lojistik")
                    files_saved += 1
                if doc2:
                    save_uploaded_file(doc2, category="Finans")
                    files_saved += 1
                
                with st.status("Operasyon Başlatılıyor...", expanded=True):
                    st.write("📦 Hacimsel ağırlık kontrol ediliyor...")
                    time.sleep(0.5)
                    if files_saved > 0:
                        st.write(f"📂 {files_saved} adet belge Dijital Arşiv'e kaydedildi.")
                        time.sleep(0.5)
                    st.write(f"🌍 {incoterms} kurallarına göre rota oluşturuluyor...")
                    time.sleep(0.5)
                    st.write("📄 Gümrük müşavirine bildirim gönderildi.")
                    time.sleep(0.5)
                
                st.success(f"Talebiniz Alındı! Operasyon Kodu: **US-EXP-{random.randint(10000,99999)}**")
                
                # [DÜZELTME] Emoji hatası giderildi: "cloud" yerine "✅"
                if files_saved > 0:
                    st.toast(f"{files_saved} dosya arşivlendi.", icon="✅")
                st.balloons()

    # --- SEKME 2: GÖREVLER (TODO) ---
    with tab_tasks:
        c_add, c_list = st.columns([1, 2])
        with c_add:
            st.markdown("##### ⚡ Hızlı Görev Ekle")
            with st.form("add_task"):
                t_name = st.text_input("Görev Adı")
                t_tag = st.selectbox("Etiket", ["Genel", "Lojistik", "Üretim", "Gümrük"])
                t_prio = st.select_slider("Öncelik", ["Low", "Medium", "High"], value="Medium")
                if st.form_submit_button("Ekle", use_container_width=True):
                    if t_name:
                        add_task(t_name, t_tag, t_prio)
                        st.rerun()
        with c_list:
            st.markdown("##### 📋 Yapılacaklar")
            for i, task in enumerate(st.session_state.todos):
                if not task['done']:
                    idx = st.session_state.todos.index(task)
                    prio_color = "#EF4444" if task['prio']=="High" else "#F59E0B" if task['prio']=="Medium" else "#3B82F6"
                    c_chk, c_txt, c_del = st.columns([0.5, 4, 0.5])
                    if c_chk.button("⬜", key=f"chk_{task['id']}"): toggle_task(idx); st.rerun()
                    c_txt.markdown(f"""<div class="task-card" style="border-left-color: {prio_color}; margin:0;"><div><div class="task-title">{task['task']}</div><div class="task-meta"><span class="task-tag">{task['tag']}</span> • {task['date']}</div></div></div>""", unsafe_allow_html=True)
                    if c_del.button("🗑️", key=f"del_{task['id']}"): delete_task(idx); st.rerun()

    # --- SEKME 3: DOKÜMANLAR ---
    with tab_docs:
        c_filter, c_upload = st.columns([2, 1])
        with c_filter: search = st.text_input("🔍 Dosya Ara")
        with c_upload: 
            # DİREKT YÜKLEME İÇİN
            uploaded_doc = st.file_uploader("Hızlı Yükle", label_visibility="collapsed")
            if uploaded_doc:
                if save_uploaded_file(uploaded_doc, category="Genel"):
                    # [DÜZELTME] Emoji hatası giderildi
                    st.toast("Dosya arşivlendi!", icon="✅")
        
        st.markdown("##### 📄 Son Dosyalar")
        docs = st.session_state.documents
        if search: docs = [d for d in docs if search.lower() in d['name'].lower()]
        
        for idx, doc in enumerate(docs):
            icon_cls = "icon-pdf" if "pdf" in doc['type'] else "icon-xls" if "xls" in doc['type'] else "icon-img"
            c1, c2, c3 = st.columns([0.5, 3, 1])
            with c1: st.markdown(f"<div class='file-icon-box {icon_cls}'><i class='bx bx-file'></i></div>", unsafe_allow_html=True)
            with c2: st.markdown(f"**{doc['name']}**"); st.caption(f"{doc['size']} • {doc['date']} • {doc['category']}")
            with c3: st.button("⬇️ İndir", key=f"dl_{idx}", use_container_width=True)
            st.markdown("<hr style='margin:5px 0; border-color:rgba(255,255,255,0.05)'>", unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Operations Hub")
    render_operations()
