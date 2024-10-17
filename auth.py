import streamlit as st
import bcrypt
import pandas as pd
import os

# Funções de manipulação de autenticação
usuarios = {}  # Dicionário para armazenar usuários (pode ser substituído por um banco de dados real)

# Simula um arquivo para salvar os usuários cadastrados
USUARIOS_PARQUET = 'data/usuarios.parquet'

# Função para carregar usuários salvos
def carregar_usuarios():
    if os.path.exists(USUARIOS_PARQUET):
        return pd.read_parquet(USUARIOS_PARQUET).set_index('usuario').T.to_dict()
    return {}

# Função para salvar os usuários
def salvar_usuarios():
    df = pd.DataFrame(usuarios).T.reset_index().rename(columns={'index': 'usuario'})
    df.to_parquet(USUARIOS_PARQUET, engine='pyarrow')

# Carrega os usuários na inicialização
usuarios = carregar_usuarios()

def autenticar_usuario(usuario, senha):
    if usuario in usuarios:
        return bcrypt.checkpw(senha.encode(), usuarios[usuario]['senha'])
    return False

def login():
    st.title("Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        if autenticar_usuario(usuario, senha):
            st.session_state['usuario_logado'] = usuario
            st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha inválidos.")

def cadastro():
    st.title("Cadastro de Usuário")

    usuario = st.text_input("Escolha um nome de usuário")
    senha = st.text_input("Escolha uma senha", type="password")
    confirm_senha = st.text_input("Confirme sua senha", type="password")

    if st.button("Cadastrar"):
        if usuario in usuarios:
            st.error("Usuário já existe!")
        elif senha != confirm_senha:
            st.error("As senhas não conferem!")
        else:
            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            usuarios[usuario] = {'senha': senha_hash}
            salvar_usuarios()
            st.success("Usuário cadastrado com sucesso!")
