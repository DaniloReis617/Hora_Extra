projeto_horas_extras/
│
├── app.py               # Arquivo principal que inicia o app e controla a navegação
├── pages/               # Diretório para as páginas individuais
│   ├── login.py         # Página de login
│   ├── dashboard.py     # Página de dashboard
│   ├── registro.py      # Página de registro de horas
├── requirements.txt     # Lista de dependências
├── utils/               # Funções auxiliares como autenticação e manipulação de dados
│   ├── __init__.py
│   └── auth.py          # Funções de autenticação
│   └── db_utils.py      # Funções para manipular o arquivo Parquet
└── users.json           # Arquivo JSON para armazenamento de usuários


1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run app.py
   ```
