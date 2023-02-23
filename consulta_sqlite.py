import sqlite3

# Cria a conexão com o banco de dados
conexao = sqlite3.connect('banco_exemplo.db')

# Consulta todas as pessoas na tabela
cursor = conexao.execute("SELECT * FROM pessoas")
pessoas = cursor.fetchall()

# Imprime as pessoas encontradas
for pessoa in pessoas:
    print("ID:", pessoa[0])
    print("Nome:", pessoa[1])
    print("Idade:", pessoa[2])

# Fecha a conexão com o banco de dados
conexao.close()
