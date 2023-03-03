import sqlite3
import hashlib

def hash_password(password):
    """Retorna o hash da senha usando SHA-256"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Conectar ao banco de dados
conn = sqlite3.connect('banco_de_dados.db')

# Cria uma tabela 'usuarios' com duas colunas: 'usuario' e 'senha'
cursor = conn.cursor()
cursor.execute('''CREATE TABLE usuarios
                (usuario text primary key, senha text)''')

# Insere um novo usuário com a senha 'minha_senha'
usuario = 'joao'
senha = hash_password('minha_senha')
cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (usuario, senha))

# Confirma a operação e fecha a conexão com o banco de dados
conn.commit()
conn.close()
