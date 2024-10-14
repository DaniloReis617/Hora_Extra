import json
import os

USER_DB = 'users.json'

# Função para verificar login
def autenticar_usuario(usuario, senha):
    if os.path.exists(USER_DB):
        with open(USER_DB, 'r') as f:
            usuarios = json.load(f)
        if usuario in usuarios and usuarios[usuario]['senha'] == senha:
            return True
    return False

# Função para cadastrar novo usuário
def cadastrar_usuario(usuario, senha):
    if not os.path.exists(USER_DB):
        usuarios = {}
    else:
        with open(USER_DB, 'r') as f:
            usuarios = json.load(f)
    
    if usuario in usuarios:
        return False  # Usuário já existe
    else:
        usuarios[usuario] = {'senha': senha}
        with open(USER_DB, 'w') as f:
            json.dump(usuarios, f)
        return True  # Cadastro bem-sucedido
