import streamlit as st

def render_documents():
    st.title("📂 Dijital Arşiv")
    
    with st.expander("📄 Resmi Belgeler", expanded=True):
        c1, c2 = st.columns(2)
        c1.download_button("Gümrük Beyannamesi.pdf", data="demo", file_name="gumruk.pdf", use_container_width=True)
        c2.download_button("Hizmet Sözleşmesi.pdf", data="demo", file_name="sozlesme.pdf", use_container_width=True)
