import streamlit as st
from utils.auth import cadastrar_usuario

def show():
    st.title("Cadastro de Usuário")

    usuario = st.text_input("Nome de Usuário")
    senha = st.text_input("Senha", type="password")
    confirmar_senha = st.text_input("Confirme sua Senha", type="password")
    
    if st.button("Cadastrar"):
        if senha == confirmar_senha:
            if cadastrar_usuario(usuario, senha):
                st.success("Usuário cadastrado com sucesso!")
            else:
                st.error("Usuário já existe!")
        else:
            st.error("As senhas não coincidem.")
