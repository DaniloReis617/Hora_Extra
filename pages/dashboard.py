import streamlit as st
from utils.db_utils import carregar_dados_parquet
import pandas as pd

def show():
    st.title(f"Dashboard de Horas Extras - {st.session_state['usuario']}")
    
    # Carregar dados
    dados = carregar_dados_parquet()

    if not dados.empty:
        dados_usuario = dados[dados['Solicitante'] == st.session_state['usuario']]
        if not dados_usuario.empty:
            st.subheader("Indicadores de Horas Extras")
            dados_usuario['Duração'] = pd.to_datetime(dados_usuario['Hora Final']) - pd.to_datetime(dados_usuario['Hora Inicial'])
            total_horas = dados_usuario['Duração'].sum()
            st.metric("Total de Horas Extras", total_horas)
            st.dataframe(dados_usuario)
        else:
            st.warning("Nenhum registro encontrado.")
    else:
        st.warning("Nenhum registro encontrado.")
