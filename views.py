import streamlit as st
import brain

def render_navbar():
    st.markdown("""
        <div class="custom-navbar">
            <div class="nav-logo">ARTIS <span style="color:#D4AF37">STAFF</span></div>
            <div class="nav-links">
                OPERATIONS // ANALYTICS // NETWORK
            </div>
            <div class="nav-cta">
                STATUS: ONLINE
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 3rem;'>ARTIS ACCESS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666; font-family: Share Tech Mono;'>ENTER CREDENTIALS TO INITIALIZE KERNEL</p>", unsafe_allow_html=True)
        
        user = st.text_input("IDENTITY", placeholder="Username")
        password = st.text_input("KEY", placeholder="Password", type="password")
        
        if st.button("INITIALIZE SYSTEM"):
            if user == "admin" and password == "admin":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("ACCESS DENIED. INVALID CREDENTIALS.")

def render_hero():
    st.markdown("""
        <div class="animate-text">
            <h1 style="font-size: 4rem; margin-bottom: 0;">ARTIFICIAL STAFF <span style="font-size:1rem; vertical-align:top; color:#D4AF37">v2.0</span></h1>
            <p style="font-size: 1.2rem; color: #AAA; max-width: 600px;">
                The autonomous operating system for Turkish enterprises expanding into the Americas. 
                Logistics. Legal. Sales. Synchronized.
            </p>
        </div>
        <hr style="border-color: #333; margin: 30px 0;">
    """, unsafe_allow_html=True)

def render_bento_menu():
    st.markdown("<h3>SYSTEM MODULES</h3>", unsafe_allow_html=True)
    
    # Row 1
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="hub-card">
            <div class="card-title">LLC SETUP</div>
            <div class="card-desc">Delaware/Wyoming Incorporation & EIN Procurement</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="hub-card">
            <div class="card-title">LOGISTICS</div>
            <div class="card-desc">Real-time FBA Tracking & Customs Clearance</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="hub-card">
            <div class="card-title">AI SALES</div>
            <div class="card-desc">Cold Email Automation & CRM Integration</div>
        </div>
        """, unsafe_allow_html=True)

    # Row 2 (Wider cards)
    st.markdown("<br>", unsafe_allow_html=True)
    c4, c5 = st.columns([2, 1])
    
    with c4:
        st.markdown("""
        <div class="hub-card" style="height: 150px; align-items: flex-start; text-align: left;">
            <div class="card-title">MARKETING INTELLIGENCE</div>
            <div class="card-desc">Competitor Ad Analysis & ROAS Optimization Algorithms active.</div>
        </div>
        """, unsafe_allow_html=True)
    
    with c5:
        st.markdown("""
        <div class="hub-card" style="height: 150px;">
            <div class="card-title" style="color: #D4AF37;">$42,890</div>
            <div class="card-desc">Forecasted Monthly Revenue</div>
        </div>
        """, unsafe_allow_html=True)

def render_dashboard():
    st.markdown("<h3>FINANCIAL TELEMETRY</h3>", unsafe_allow_html=True)
    
    # Top Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("TOTAL REVENUE", "$124,500", "+12%")
    m2.metric("NET PROFIT", "$56,200", "+8%")
    m3.metric("AD SPEND", "$12,400", "-2%")
    m4.metric("ACTIVE SHIPMENTS", "14", "On Time")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.markdown("<p style='font-family: Share Tech Mono; color: #888;'>REVENUE TRAJECTORY (30D)</p>", unsafe_allow_html=True)
        st.plotly_chart(brain.get_sales_chart(), use_container_width=True)
        
    with c2:
        st.markdown("<p style='font-family: Share Tech Mono; color: #888;'>SUPPLY CHAIN VISUALIZER</p>", unsafe_allow_html=True)
        st.plotly_chart(brain.get_logistics_map(), use_container_width=True)

def render_chat_interface():
    st.markdown("<h3>ARTIS INTELLIGENCE CORE</h3>", unsafe_allow_html=True)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask Artis about Logistics, Taxes, or Ads..."):
        # User message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Response
        with st.chat_message("assistant"):
            response_text = brain.get_artis_response(prompt)
            st.markdown(response_text)
            
        st.session_state.messages.append({"role": "assistant", "content": response_text})
