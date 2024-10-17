import streamlit as st
import pandas as pd
from utils import carregar_dados

def tela_admin():
    st.title("Administração Geral")
    
    df = carregar_dados()

    st.subheader("Todos os Registros de Horas Extras")
    st.dataframe(df)
    
    # Funções adicionais de gerenciamento podem ser implementadas aqui
