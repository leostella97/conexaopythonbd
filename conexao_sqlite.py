import sqlite3

# Cria a conexão com o banco de dados
conexao = sqlite3.connect('exemplo.db')

# Cria uma tabela chamada 'pessoas'
conexao.execute('''CREATE TABLE pessoas
                (id INT PRIMARY KEY NOT NULL,
                nome TEXT NOT NULL,
                idade INT NOT NULL);''')

# Insere algumas pessoas na tabela
conexao.execute("INSERT INTO pessoas (id, nome, idade) VALUES (1, 'Leonardo', 26)")
conexao.execute("INSERT INTO pessoas (id, nome, idade) VALUES (2, 'Anakin', 25)")
conexao.execute("INSERT INTO pessoas (id, nome, idade) VALUES (3, 'Yoda', 30)")

# Salva as mudanças no banco de dados
conexao.commit()

# Fecha a conexão com o banco de dados
conexao.close()