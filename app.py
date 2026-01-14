import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. SİSTEM KONFİGÜRASYONU
# ==============================================================================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'logic')))

st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': "# ARTIS OS v4.2\nPowered by Artificial Staff"}
)

# ==============================================================================
# 🛠️ 2. CSS PATCH (SIDEBAR BUTONUNU ZORLA GÖRÜNÜR YAPMA)
# ==============================================================================
# Bu kod, sidebar kapandığında açma butonunu header'dan bağımsızlaştırır
# ve sol üste "Floating Action Button" (Yüzen Buton) olarak çiviler.
st.markdown("""
<style>
    /* 1. Header'ı Görünmez Yap ama Varlığını Koru (Tıklamaları engellememesi için) */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
    }

    /* 2. Sidebar AÇMA/KAPAMA Butonunu Özelleştir ve Sabitle */
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        visibility: visible !important;
        
        /* KONUMLANDIRMA (SAYFAYA ÇİVİLE) */
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        z-index: 999999 !important; /* Her şeyin en üstünde */
        pointer-events: auto !important; /* Tıklanabilir */
        
        /* GÖRÜNÜM (GÖRÜNMEMESİ İMKANSIZ OLSUN) */
        width: 44px !important;
        height: 44px !important;
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%) !important; /* PARLAK MAVİ */
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.6) !important; /* NEON GLOW */
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    /* Butonun İçindeki Ok İşaretini Beyaz Yap */
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
        width: 24px !important;
        height: 24px !important;
    }

    /* Hover Efekti (Üzerine gelince büyüsün) */
    [data-testid="stSidebarCollapsedControl"]:hover {
        transform: scale(1.1) !important;
        box-shadow: 0 0 30px rgba(59, 130, 246, 0.9) !important;
        background: linear-gradient(135deg, #60A5FA 0%, #3B82F6 100%) !important;
    }

    /* 3. Sağ Üst Menü (3 Nokta) Ayarı */
    div[data-testid="stToolbar"] {
        right: 1.5rem;
        top: 1rem;
        pointer-events: auto;
    }

    /* 4. Native Sidebar Menüyü Gizle */
    div[data-testid="stSidebarNav"] { display: none; }
    
    /* 5. Sidebar Arka Planı */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 📦 3. MODÜL YÜKLEME
# ==============================================================================
try:
    import styles
    import login
    import dashboard
    import logistics
    import inventory
    import plan
    import documents
    import todo
    import forms
except ImportError as e:
    st.error(f"⚠️ Kritik Hata: Modüller yüklenemedi.\nDetay: {e}")
    st.stop()

# ==============================================================================
# 🚀 4. UI ENJEKSİYONU & LOGIC
# ==============================================================================
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

def render_sidebar():
    with st.sidebar:
        # --- A. MARKA BAŞLIĞI ---
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        user_plan = st.session_state.user_data.get('plan', 'Enterprise')
        
        st.markdown(textwrap.dedent(f"""
            <div style="margin-top: 15px; margin-bottom: 25px; padding: 12px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #8B5CF6 0%, #3B82F6 100%); border-radius: 8px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.25);">
                        <i class='bx bxs-command' style="color: white; font-size: 20px;"></i>
                    </div>
                    <div>
                        <div style="font-weight: 800; font-size: 15px; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 170px;">
                            {user_brand}
                        </div>
                        <div style="font-size: 10px; color: #34D399; font-weight: 600; text-transform: uppercase;">
                            ● {user_plan} Edition
                        </div>
                    </div>
                </div>
            </div>
        """), unsafe_allow_html=True)

        # --- B. MENÜ ---
        opts = {
            "Dashboard": "📊 Dashboard",
            "Lojistik": "📦 Lojistik",
            "Envanter": "📋 Envanter",
            "Formlar": "📝 Formlar",
            "Dokümanlar": "📂 Dokümanlar",
            "Yapılacaklar": "✅ Yapılacaklar",
            "Planlar": "💎 Planlar"
        }
        selection = st.radio("NAV", list(opts.keys()), format_func=lambda x: opts[x], label_visibility="collapsed")
        
        # --- C. PROFİL ---
        st.markdown("<div style='flex-grow: 1; min-height: 150px;'></div>", unsafe_allow_html=True)
        user_name = st.session_state.user_data.get('name', 'Kullanıcı')
        
        st.markdown(textwrap.dedent(f"""
            <div style="padding: 15px; background: rgba(255,255,255,0.03); border-radius: 12px; display: flex; align-items: center; gap: 12px; border-top: 1px solid rgba(255,255,255,0.08);">
                <div style="width: 34px; height: 34px; background: #27272A; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #FFF; font-weight: 700;">
                    {user_name[0]}
                </div>
                <div>
                    <div style="font-size: 13px; font-weight: 600; color: #E4E4E7;">{user_name}</div>
                    <div style="font-size: 10px; color: #71717A;">Çevrimiçi</div>
                </div>
            </div>
        """), unsafe_allow_html=True)
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        if st.button("Güvenli Çıkış", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
        return selection

def main():
    if not st.session_state.logged_in:
        login.render_login_page()
    else:
        sel = render_sidebar()
        if sel == "Dashboard": dashboard.render_dashboard()
        elif sel == "Lojistik": logistics.render_logistics()
        elif sel == "Envanter": inventory.render_inventory()
        elif sel == "Formlar": forms.render_forms()
        elif sel == "Dokümanlar": documents.render_documents()
        elif sel == "Yapılacaklar": todo.render_todo()
        elif sel == "Planlar": plan.render_plans()

if __name__ == "__main__":
    main()
