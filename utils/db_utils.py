import os
import pandas as pd

PARQUET_FILE = 'data/horas_extras.parquet'

# Função para inicializar o arquivo Parquet
def inicializar_parquet():
    if not os.path.exists(PARQUET_FILE):
        df = pd.DataFrame(columns=['Solicitante', 'Data', 'Hora Inicial', 'Hora Final', 'Atividade', 'Duração'])
        df.to_parquet(PARQUET_FILE, index=False)

# Função para carregar os dados do Parquet
def carregar_dados_parquet():
    inicializar_parquet()
    return pd.read_parquet(PARQUET_FILE)

# Função para salvar os dados no Parquet
def salvar_dados_parquet(df):
    df['Hora Inicial'] = pd.to_datetime(df['Hora Inicial'], format='%H:%M:%S')
    df['Hora Final'] = pd.to_datetime(df['Hora Final'], format='%H:%M:%S')
    df['Duração'] = df['Hora Final'] - df['Hora Inicial']
    df.to_parquet(PARQUET_FILE, index=False)
