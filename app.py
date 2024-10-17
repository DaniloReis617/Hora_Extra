import streamlit as st
from auth import login, cadastro, autenticar_usuario
from extras import tela_registro
from dashboard import tela_dashboard
from admin import tela_admin

# Configuração inicial
st.set_page_config(page_title="Registro de Horas Extras", layout="wide")

# Função principal para controlar a navegação
def main():
    if 'usuario_logado' not in st.session_state:
        st.session_state['usuario_logado'] = None

    menu = ["Login", "Cadastro", "Registro de Horas Extras", "Dashboard", "Admin"]
    
    # Controle da navegação
    if st.session_state['usuario_logado']:
        escolha = st.sidebar.selectbox("Menu", menu[2:])
        
        if escolha == "Registro de Horas Extras":
            tela_registro()
        elif escolha == "Dashboard":
            tela_dashboard()
        elif escolha == "Admin":
            tela_admin()
    else:
        escolha = st.sidebar.selectbox("Menu", menu[:2])
        
        if escolha == "Login":
            login()
        elif escolha == "Cadastro":
            cadastro()

if __name__ == '__main__':
    main()
