import streamlit as st

def render_todo():
    st.title("✅ Yapılacaklar")
    if "todos" not in st.session_state: st.session_state.todos = ["Vergileri öde", "Stok sayımı"]
    
    new = st.text_input("Görev Ekle")
    if new and st.button("Ekle"): 
        st.session_state.todos.append(new)
        st.rerun()
        
    for i, t in enumerate(st.session_state.todos):
        c1, c2 = st.columns([0.9, 0.1])
        c1.write(f"- {t}")
        if c2.button("X", key=i):
            st.session_state.todos.pop(i)
            st.rerun()
