import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

# ==============================================================================
# 🎨 1. SAYFAYA ÖZEL STİL (DOKÜMANLAR İÇİN)
# ==============================================================================
def inject_docs_css():
    st.markdown("""
    <style>
        /* Dosya Kartı (Liste Görünümü) */
        .file-row {
            background-color: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.2s;
        }
        .file-row:hover {
            background-color: rgba(255, 255, 255, 0.04);
            border-color: rgba(255, 255, 255, 0.1);
            transform: translateX(4px);
        }
        
        /* Dosya İkonu Kutusu */
        .file-icon-box {
            width: 44px; height: 44px;
            border-radius: 10px;
            display: flex; align-items: center; justify-content: center;
            font-size: 22px;
            margin-right: 15px;
        }
        .icon-pdf { background: rgba(239, 68, 68, 0.15); color: #F87171; }
        .icon-xls { background: rgba(16, 185, 129, 0.15); color: #34D399; }
        .icon-img { background: rgba(59, 130, 246, 0.15); color: #60A5FA; }
        .icon-doc { background: rgba(59, 130, 246, 0.15); color: #93C5FD; }

        /* Etiketler */
        .doc-tag {
            font-size: 11px;
            padding: 4px 10px;
            border-radius: 20px;
            background: rgba(255,255,255,0.05);
            color: #A1A1AA;
            border: 1px solid rgba(255,255,255,0.05);
        }

        /* Upload Alanı */
        .upload-zone {
            border: 2px dashed #27272A;
            border-radius: 16px;
            padding: 30px;
            text-align: center;
            background: rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🛠️ 2. MOCK DATA GENERATOR
# ==============================================================================
def get_documents():
    return [
        {"name": "2026_Ocak_Gümrük_Beyannamesi.pdf", "type": "pdf", "size": "2.4 MB", "date": "14 Jan 2026", "category": "Gümrük", "owner": "Ahmet Y."},
        {"name": "Washington_Hub_Stok_Sayim.xlsx", "type": "xls", "size": "850 KB", "date": "12 Jan 2026", "category": "Lojistik", "owner": "Sistem"},
        {"name": "Fatura_INV-2026-001.pdf", "type": "pdf", "size": "1.1 MB", "date": "10 Jan 2026", "category": "Finans", "owner": "Fatma K."},
        {"name": "Konteyner_Hasar_Raporu.jpg", "type": "img", "size": "4.2 MB", "date": "08 Jan 2026", "category": "Operasyon", "owner": "Saha Ekibi"},
        {"name": "Müşteri_Sözleşmesi_V2.docx", "type": "doc", "size": "1.8 MB", "date": "05 Jan 2026", "category": "Hukuk", "owner": "Mehmet B."},
        {"name": "Q1_Lojistik_Projeksiyonu.pdf", "type": "pdf", "size": "5.6 MB", "date": "02 Jan 2026", "category": "Yönetim", "owner": "Ahmet Y."},
    ]

# ==============================================================================
# 🧩 3. UI BİLEŞENLERİ
# ==============================================================================
def render_file_row(file, idx):
    """HTML tabanlı özel dosya satırı"""
    
    # İkon Tipi Belirle
    icon_map = {
        "pdf": ("bx-file-pdf", "icon-pdf"),
        "xls": ("bx-table", "icon-xls"),
        "img": ("bx-image", "icon-img"),
        "doc": ("bx-file", "icon-doc")
    }
    icon_cls, theme_cls = icon_map.get(file['type'], ("bx-file", "icon-doc"))
    
    # HTML Satırı
    c1, c2, c3, c4, c5 = st.columns([0.6, 2, 1, 1, 1])
    
    with c1:
        st.markdown(f"""
        <div class="file-icon-box {theme_cls}">
            <i class='bx {icon_cls}'></i>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown(f"**{file['name']}**")
        st.caption(f"{file['size']} • {file['owner']}")
        
    with c3:
        st.markdown(f"<span class='doc-tag'>{file['category']}</span>", unsafe_allow_html=True)
        
    with c4:
        st.caption(file['date'])
        
    with c5:
        # Streamlit butonu (Unique key önemli)
        if st.button("⬇️ İndir", key=f"dl_{idx}", use_container_width=True):
            st.toast(f"Dosya indiriliyor: {file['name']}", icon="cloud")

    st.markdown("---") # Ayırıcı çizgi

# ==============================================================================
# 🚀 4. ANA RENDER FONKSİYONU
# ==============================================================================
def render_documents():
    inject_docs_css()
    
    # --- HEADER ---
    c1, c2 = st.columns([3, 1])
    with c1:
        st.title("📂 Doküman Arşivi")
        st.caption("Operasyonel belgeler, faturalar ve raporlar.")
    with c2:
        st.metric("Toplam Alan", "45 GB / 1 TB", delta="12%")
    
    st.markdown("---")

    # --- UPLOAD ZONE (Görsel Olarak) ---
    with st.expander("☁️ Yeni Dosya Yükle", expanded=False):
        st.markdown("""
        <div class="upload-zone">
            <i class='bx bx-cloud-upload' style='font-size: 48px; color: #52525B;'></i>
            <p>Dosyaları buraya sürükleyin veya seçin</p>
            <span style="font-size:12px; color:#52525B;">PDF, XLSX, DOCX, JPG (Max 25MB)</span>
        </div>
        """, unsafe_allow_html=True)
        uploaded = st.file_uploader("", label_visibility="collapsed")
        if uploaded:
            st.success("Dosya başarıyla şifrelendi ve buluta yüklendi!")

    # --- FİLTRELEME ---
    c_search, c_type, c_sort = st.columns([2, 1, 1])
    with c_search:
        search = st.text_input("🔍 Dosya Ara", placeholder="Dosya adı veya etiket...")
    with c_type:
        f_type = st.selectbox("Dosya Tipi", ["Tümü", "PDF", "Excel", "Resim", "Word"])
    with c_sort:
        sort = st.selectbox("Sıralama", ["Yeniden Eskiye", "Eskiden Yeniye", "Boyut"])

    st.markdown("<br>", unsafe_allow_html=True)

    # --- DOSYA LİSTESİ ---
    docs = get_documents()
    
    # Basit Filtreleme Mantığı (Simüle Edilmiş)
    if search:
        docs = [d for d in docs if search.lower() in d['name'].lower()]
    if f_type != "Tümü":
        mapping = {"PDF": "pdf", "Excel": "xls", "Resim": "img", "Word": "doc"}
        docs = [d for d in docs if d['type'] == mapping[f_type]]

    # Listeleme
    st.markdown("##### 📄 Son Dosyalar")
    if not docs:
        st.warning("Kriterlere uygun dosya bulunamadı.")
    else:
        for idx, doc in enumerate(docs):
            render_file_row(doc, idx)
