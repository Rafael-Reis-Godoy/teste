import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('contas.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Executa uma consulta SQL para recuperar todos os registros da tabela 'clientes'
cursor.execute('SELECT * FROM usuarios')

# Lê todos os registros retornados pela consulta
registros = cursor.fetchall()


# Imprime os registros na tela
for registro in registros:
    print(registro)
    

# Fecha a conexão com o banco de dados
conn.close()
