import streamlit as st
import pandas as pd
from datetime import datetime
from utils import carregar_dados, salvar_dados, calcular_duracao

# Função para exibir a tela de registro
def tela_registro():
    st.title("Registro de Horas Extras")
    
    # Carrega os dados existentes
    df = carregar_dados()

    # Formulário de registro
    with st.form(key='registro_form'):
        data = st.date_input("Data")
        hora_inicial = st.time_input("Hora Inicial")
        hora_final = st.time_input("Hora Final")
        atividade = st.text_area("Atividade")

        # Botão de submissão
        submit_button = st.form_submit_button(label="Registrar")

        if submit_button:
            duracao = calcular_duracao(hora_inicial.strftime('%H:%M'), hora_final.strftime('%H:%M'))

            novo_registro = {
                'Solicitante': st.session_state['usuario_logado'],
                'Data': data,
                'Hora Inicial': hora_inicial.strftime('%H:%M'),
                'Hora Final': hora_final.strftime('%H:%M'),
                'Atividade': atividade,
                'Duração': duracao
            }

            df = df.append(novo_registro, ignore_index=True)
            salvar_dados(df)
            st.success("Registro adicionado com sucesso!")

    # Exibe os registros do usuário logado
    st.subheader("Seus Registros")
    df_usuario = df[df['Solicitante'] == st.session_state['usuario_logado']]
    st.dataframe(df_usuario)
    
    # Botões para editar e excluir os registros podem ser implementados aqui
