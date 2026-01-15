import streamlit as st

def render():
    st.markdown("## 🤖 Otomasyon & Operasyon Verimliliği")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style='background:rgba(255,255,255,0.03); padding:20px; border-radius:15px; border-left:4px solid #8B5CF6;'>
            <h4>Sipariş İşleme Otopilotu</h4>
            <p>Web sitesinden lojistik deposuna veri akışı %100 otomatize edildi.</p>
            <small>Durum: AKTİF</small>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.metric("Kurtarılan Zaman", "120 Saat/Ay", "+15%")
    
    st.markdown("### Entegrasyonlar")
    st.write("✅ Zapier | ✅ Make | ✅ Shopify Webhooks")
