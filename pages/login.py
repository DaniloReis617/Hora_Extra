import streamlit as st
from utils.auth import autenticar_usuario

def show():
    st.title("Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if autenticar_usuario(usuario, senha):
            st.session_state.logged_in = True
            st.session_state.usuario = usuario
            st.success(f"Bem-vindo {usuario}!")
        else:
            st.error("Usuário ou senha incorretos.")


