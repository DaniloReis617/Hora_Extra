.
├── app.py                 # Arquivo principal do Streamlit
├── auth.py                # Gerenciamento de autenticação (login e cadastro)
├── dashboard.py           # Dashboard com indicadores
├── extras.py              # Tela para registro de horas extras
├── admin.py               # Tela de administração geral
├── utils.py               # Funções auxiliares (gerenciamento do arquivo Parquet, etc)
├── data/                  # Pasta para armazenar o arquivo Parquet
│   └── registros.parquet   # Arquivo Parquet com os registros de horas extras
└── requirements.txt       # Bibliotecas e dependências



1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run app.py
   ```
