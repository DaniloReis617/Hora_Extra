import streamlit as st
from utils.db_utils import carregar_dados_parquet, salvar_dados_parquet
import pandas as pd
import datetime

def tela_registro():
    st.title(f"Registro de Horas Extras - {st.session_state['usuario']}")
    
    # Carregar dados existentes
    dados = carregar_dados_parquet()

    # Tabela de registros do usuário
    dados_usuario = dados[dados['Solicitante'] == st.session_state['usuario']]
    st.subheader("Registros")
    st.dataframe(dados_usuario)

    # Formulário para novo registro
    with st.form("novo_registro"):
        data = st.date_input("Data", datetime.date.today())
        hora_inicial = st.time_input("Hora Inicial")
        hora_final = st.time_input("Hora Final")
        atividade = st.text_input("Atividade")
        if st.form_submit_button("Registrar"):
            novo_registro = {
                'Solicitante': st.session_state['usuario'],
                'Data': str(data),
                'Hora Inicial': str(hora_inicial),
                'Hora Final': str(hora_final),
                'Atividade': atividade
            }
            # Adiciona novo registro e salva
            dados = dados.append(novo_registro, ignore_index=True)
            salvar_dados_parquet(dados)
            st.success("Registro adicionado com sucesso!")
