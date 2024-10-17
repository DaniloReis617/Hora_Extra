import pandas as pd
import os
from datetime import datetime

# Caminho do arquivo Parquet
CAMINHO_PARQUET = 'data/registros.parquet'

# Função para calcular a duração entre Hora Inicial e Hora Final
def calcular_duracao(hora_inicial, hora_final):
    formato = "%H:%M"
    hora_inicial_dt = datetime.strptime(hora_inicial, formato)
    hora_final_dt = datetime.strptime(hora_final, formato)
    duracao = hora_final_dt - hora_inicial_dt
    return duracao

# Função para carregar dados do arquivo Parquet
def carregar_dados():
    if os.path.exists(CAMINHO_PARQUET):
        return pd.read_parquet(CAMINHO_PARQUET)
    else:
        return pd.DataFrame(columns=['Solicitante', 'Data', 'Hora Inicial', 'Hora Final', 'Atividade', 'Duração'])

# Função para salvar dados no arquivo Parquet
def salvar_dados(df):
    df.to_parquet(CAMINHO_PARQUET, engine='pyarrow')
