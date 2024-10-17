import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import carregar_dados

def tela_dashboard():
    st.title("Dashboard de Horas Extras")
    
    df = carregar_dados()
    df_usuario = df[df['Solicitante'] == st.session_state['usuario_logado']]

    if not df_usuario.empty:
        total_horas = df_usuario['Duração'].sum()
        st.metric("Total de Horas Extras", total_horas)

        # Exemplo de gráfico com Matplotlib
        df_usuario['Data'] = pd.to_datetime(df_usuario['Data'])
        horas_por_dia = df_usuario.groupby('Data')['Duração'].sum()

        st.subheader("Horas por Dia")
        fig, ax = plt.subplots()
        horas_por_dia.plot(kind='bar', ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Nenhum registro encontrado.")
