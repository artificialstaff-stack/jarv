import streamlit as st

# --- NAVBAR ---
def render_navbar():
    st.markdown("""
    <nav class="navbar">
        <div class="nav-logo">ARTIFICIAL STAFF</div>
        <div class="nav-links">
            <a href="#">Creative Studio</a>
            <a href="#">API Platform</a>
            <a href="#">About Us</a>
            <a href="#">Blog</a>
        </div>
        <a href="#" class="nav-btn">Start Creating</a>
    </nav>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
def render_hero():
    st.markdown("""
    <div class="hero-container">
        <div class="hero-badge">ARTIFICIAL STAFF v2.0 IS LIVE</div>
        <h1 class="hero-title">
            Artificial Staff v2<br>
            Does It All.
        </h1>
        <p class="hero-sub">
            Input Product. Understand Global Market. Generate US Sales.<br>
            Tek bir panelden Türkiye'den Amerika'ya uçtan uca operasyon.
        </p>
        <a href="#" class="hero-cta">Create Account</a>
    </div>
    """, unsafe_allow_html=True)

# --- BENTO GRID (HİZMETLER) ---
def render_bento_grid():
    # Bu bölüm videodaki kartlı yapının aynısıdır
    st.markdown("""
    <div class="bento-grid">
        <div class="bento-card" style="grid-column: span 2;">
            <div class="card-icon">✈️</div>
            <div class="card-content">
                <div class="card-title">Lojistik & Gümrük</div>
                <div class="card-desc">Kapıdan kapıya 2-4 günde teslimat. Gümrükleme dahil.</div>
            </div>
        </div>

        <div class="bento-card">
            <div class="card-icon">🏛️</div>
            <div class="card-content">
                <div class="card-title">LLC Kurulumu</div>
                <div class="card-desc">Delaware şirket ve banka hesabı açılışı.</div>
            </div>
        </div>

        <div class="bento-card">
            <div class="card-icon">🤖</div>
            <div class="card-content">
                <div class="card-title">AI Sales Agent</div>
                <div class="card-desc">7/24 çalışan B2B satış robotu.</div>
            </div>
        </div>

        <div class="bento-card" style="grid-column: span 2;">
            <div class="card-icon">💳</div>
            <div class="card-content">
                <div class="card-title">Finans & Tahsilat</div>
                <div class="card-desc">Stripe, PayPal ve Mercury Bank entegrasyonu.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
