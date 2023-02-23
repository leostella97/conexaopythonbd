# conexaopythonbd
Exemplos de conexão Python usando o SQLite e MongoDB
Como conectar ao SQLite em Python
Este é um tutorial simples sobre como conectar ao SQLite em Python usando a biblioteca padrão sqlite3.

Requisitos
Antes de começar, você precisa ter o Python instalado em seu computador. Se você ainda não tem o Python instalado, baixe-o em https://www.python.org/downloads/.

Além disso, você precisa ter a biblioteca padrão sqlite3 instalada. A boa notícia é que a biblioteca já vem com o Python, então você não precisa instalá-la separadamente.

Conectando ao banco de dados
Para se conectar ao banco de dados SQLite em Python, você precisa criar uma conexão usando o método connect(), que está disponível na biblioteca sqlite3. Você precisa passar o nome do arquivo de banco de dados como parâmetro para o método connect(). Se o arquivo não existir, ele será criado automaticamente.

Aqui está um exemplo:


import sqlite3

# Cria a conexão com o banco de dados
conexao = sqlite3.connect('exemplo.db')
Este exemplo cria uma conexão com um banco de dados chamado "exemplo.db". Se o arquivo não existir, ele será criado automaticamente.

Executando consultas SQL
Uma vez conectado ao banco de dados, você pode executar consultas SQL usando o método execute(). É possível criar, atualizar e excluir tabelas e registros usando SQL.

Aqui está um exemplo de como criar uma tabela de exemplo:

# Cria uma tabela de exemplo
conexao.execute('''CREATE TABLE exemplo
                    (id INT PRIMARY KEY NOT NULL,
                    nome TEXT NOT NULL,
                    idade INT NOT NULL);''')
Este exemplo cria uma tabela chamada "exemplo" com três colunas: "id", "nome" e "idade".

Agora, vamos inserir alguns dados na tabela:

# Insere alguns dados na tabela
conexao.execute("INSERT INTO exemplo (id, nome, idade) VALUES (1, 'João', 20)")
conexao.execute("INSERT INTO exemplo (id, nome, idade) VALUES (2, 'Maria', 25)")
conexao.execute("INSERT INTO exemplo (id, nome, idade) VALUES (3, 'Pedro', 30)")
Este exemplo insere três registros na tabela "exemplo".

Recuperando resultados
Para obter os resultados de uma consulta, você precisa usar o método fetchall() para recuperar todos os registros encontrados ou o método fetchone() para recuperar apenas um registro por vez. Em seguida, você pode iterar pelos resultados e exibi-los na tela ou manipulá-los de outras maneiras.

Aqui está um exemplo de como recuperar todos os registros da tabela "exemplo" e exibi-los na tela:

# Recupera todos os registros da tabela
resultados = conexao.execute("SELECT * FROM exemplo").fetchall()

# Itera pelos resultados e exibe na tela
for resultado in resultados:
    print(resultado)
Este exemplo recupera todos os registros da tabela "exemplo" usando uma consulta SQL e os armazena na variável "resultados". Em seguida, itera pelos resultados e exibe cada um deles na tela.

Fechando a conexão
Por fim, quando terminar de trabalhar com o banco de dados, é importante fechar a conexão usando o método close(). Aqui está um exemplo:

# Fecha a conexão com o banco de dados
conexao.close()
Este exemplo fecha a conexão com o banco de dados "exemplo.db".

Conclusão
Este foi um tutorial simples sobre como conectar ao SQLite em Python usando a biblioteca sqlite3. Lembre-se de que este é apenas um exemplo básico e que você pode fazer muito mais com o SQLite em Python, como executar transações, usar o método executemany() para executar várias consultas em uma única chamada e muito mais. Consulte a documentação da biblioteca sqlite3 para obter mais informações.