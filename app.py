import streamlit as st
import sys
import os
import time
import textwrap

# ==============================================================================
# 🔧 1. SİSTEM VE DOSYA YOLLARI (CRITICAL FIX)
# ==============================================================================
# Python'un ana klasörü görmesini garantiye alıyoruz
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# ==============================================================================
# ⚙️ SAYFA AYARLARI
# ==============================================================================
st.set_page_config(
    page_title="ARTIS | Intelligent Operations",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': "Powered by Artificial Staff"}
)

# ==============================================================================
# 📦 2. MODÜLLERİ ÇAĞIRMA (SENİN KLASÖR YAPINA GÖRE)
# ==============================================================================
try:
    # 1. Ana dizindeki stil dosyası
    import styles 
    
    # 2. 'views' klasöründeki dosyalar (BUNLARI ARTIK BULACAK)
    from views import login
    from views import dashboard
    from views import logistics
    from views import inventory
    from views import plan
    from views import documents
    from views import todo
    from views import forms
    
    # 3. 'logic' klasörü (Gerekirse)
    # from logic import brain 

except ImportError as e:
    st.error(f"""
    🚨 **BAĞLANTI HATASI**
    
    Dosyalar var ama Python bağlayamadı.
    Hata detayı: `{e}`
    
    **Çözüm:** Lütfen `views` klasörünün içinde `__init__.py` adında (içi boş olabilir) bir dosya olduğundan emin ol. Yoksa bile aşağıdaki kod çalışmalı.
    """)
    st.stop()

# ==============================================================================
# 🛠️ 3. CSS İLE SIDEBAR BUTONUNU ZORLA GÖSTERME
# ==============================================================================
st.markdown("""
<style>
    /* Header'ı Şeffaf ve Pasif Yap */
    header[data-testid="stHeader"] {
        background: transparent !important;
        pointer-events: none !important;
    }

    /* Sidebar Açma Butonunu (OK İŞARETİ) Zorla Ekrana Çivile */
    button[data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        z-index: 9999999 !important; /* En üst katman */
        
        /* Görünüm */
        background-color: #3B82F6 !important; /* Mavi */
        color: white !important;
        width: 42px !important;
        height: 42px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
        
        /* Etkileşim */
        pointer-events: auto !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
    }

    /* İkon Rengi */
    button[data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
    }

    /* Hover */
    button[data-testid="stSidebarCollapsedControl"]:hover {
        background-color: #2563EB !important;
        transform: scale(1.1) !important;
    }

    /* Sağ Üst Menü */
    div[data-testid="stToolbar"] {
        top: 15px !important;
        right: 15px !important;
        pointer-events: auto !important;
        z-index: 999999 !important;
    }

    /* Gereksizleri Gizle */
    div[data-testid="stDecoration"] { display: none !important; }
    div[data-testid="stSidebarNav"] { display: none !important; }
    
    /* Sidebar Rengi */
    section[data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 🚀 4. UYGULAMA MANTIĞI
# ==============================================================================
styles.load_css()

if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_data" not in st.session_state: st.session_state.user_data = {}

def render_sidebar():
    with st.sidebar:
        # MARKA BAŞLIĞI
        user_brand = st.session_state.user_data.get('brand', 'ARTIS AI')
        user_plan = st.session_state.user_data.get('plan', 'Enterprise')
        
        st.markdown(textwrap.dedent(f"""
            <div style="margin-top:20px; margin-bottom:25px; padding:12px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid rgba(255,255,255,0.05);">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div style="width:36px; height:36px; background:linear-gradient(135deg, #8B5CF6, #3B82F6); border-radius:8px; display:flex; justify-content:center; align-items:center; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.25);">
                        <i class='bx bxs-command' style="color:white; font-size:20px;"></i>
                    </div>
                    <div>
                        <div style="font-weight:800; font-size:15px; color:#FFF; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:170px;">
                            {user_brand}
                        </div>
                        <div style="font-size:10px; color:#34D399; font-weight:600; text-transform:uppercase; margin-top:2px;">
                            ● {user_plan} Edition
                        </div>
                    </div>
                </div>
            </div>
        """), unsafe_allow_html=True)

        # MENÜ
        opts = {
            "Dashboard": "📊  Dashboard",
            "Lojistik": "📦  Lojistik",
            "Envanter": "📋  Envanter",
            "Formlar": "📝  Formlar",
            "Dokümanlar": "📂  Dokümanlar",
            "Yapılacaklar": "✅  Yapılacaklar",
            "Planlar": "💎  Planlar"
        }
        
        sel = st.radio("NAV", list(opts.keys()), format_func=lambda x: opts[x], label_visibility="collapsed")
        
        # PROFIL KARTI
        st.markdown("<div style='flex-grow:1; min-height:100px;'></div>", unsafe_allow_html=True)
        
        user_name = st.session_state.user_data.get('name', 'Kullanıcı')
        user_init = user_name[0] if user_name else "U"
        
        st.markdown(textwrap.dedent(f"""
            <div style="
                background: linear-gradient(180deg, rgba(255,255,255,0.02) 0%, rgba(255,255,255,0.04) 100%); 
                border-top: 1px solid rgba(255,255,255,0.08); 
                padding: 12px; 
                border-radius: 12px; 
                display: flex; 
                align-items: center; 
                gap: 12px;
                margin-bottom: 10px;">
                <div style="width:34px; height:34px; background:#27272A; border:1px solid #3F3F46; border-radius:50%; display:flex; justify-content:center; align-items:center; font-weight:700; color:#E4E4E7;">
                    {user_init}
                </div>
                <div>
                    <div style="font-size:13px; font-weight:600; color:#E4E4E7;">{user_name}</div>
                    <div style="font-size:10px; color:#71717A;">Çevrimiçi</div>
                </div>
            </div>
        """), unsafe_allow_html=True)
        
        if st.button("Güvenli Çıkış", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
        return sel

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
