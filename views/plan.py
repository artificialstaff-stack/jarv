import streamlit as st
def render_plans():
    st.title("💎 Paketler")
    c1, c2 = st.columns(2)
    with c1: st.info("Başlangıç - $0"); st.button("Seç", key="p1")
    with c2: st.success("VIP - $500"); st.button("Seç", key="p2")
