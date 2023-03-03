import sqlite3
nome = 'Rafael Reis de Godoy'
idade = 39

def registro(nome, idade):
    # Conectando ao banco de dados
    conexao = sqlite3.connect('contas.db')

        # Executando um comando SQL para inserir um novo registro na tabela
    cursor = conexao.cursor()
    comando_sql = "INSERT INTO usuarios (username, password) VALUES (?, ?)"
    dados_registro = (nome, idade)
    cursor.execute(comando_sql, dados_registro)

    # Confirmar a operação
    conexao.commit()

    # Fechando a conexão com o banco de dados
    conexao.close()

def cadastro():
    nome=input('Qual seu nome: ')
    idade = input ('Qual sua idade: ')
    registro(nome,idade)

cadastro()
