# Conexão Python ao Banco de Dados
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


##############################################################################################################################################################


Como conectar ao MongoDB em Python
Este é um tutorial simples sobre como conectar ao MongoDB em Python usando a biblioteca pymongo.

Requisitos
Antes de começar, você precisa ter o Python instalado em seu computador. Se você ainda não tem o Python instalado, baixe-o em https://www.python.org/downloads/.

Além disso, você precisa ter a biblioteca pymongo instalada. Você pode instalá-la usando o pip, o gerenciador de pacotes do Python. Abra o terminal ou prompt de comando e digite o seguinte comando:


pip install pymongo
Conectando ao banco de dados
Para se conectar ao banco de dados MongoDB em Python, você precisa criar uma conexão usando a classe MongoClient(), que está disponível na biblioteca pymongo. Você precisa passar o URI do banco de dados como parâmetro para a classe MongoClient().

Aqui está um exemplo:


import pymongo

# Cria a conexão com o banco de dados
cliente = pymongo.MongoClient("mongodb+srv://<username>:<password>@<cluster>/<database>?retryWrites=true&w=majority")

# Seleciona o banco de dados
banco_de_dados = cliente.<nome_do_banco_de_dados>
Este exemplo cria uma conexão com um banco de dados MongoDB usando uma URI. Você precisa substituir <username> pelo nome de usuário do seu banco de dados, <password> pela senha do seu banco de dados, <cluster> pelo nome do cluster do seu banco de dados, <database> pelo nome do banco de dados e <nome_do_banco_de_dados> pelo nome do banco de dados que você deseja usar.

Executando operações CRUD
Uma vez conectado ao banco de dados, você pode executar operações CRUD usando os métodos disponíveis na classe Collection(), que está disponível na biblioteca pymongo. É possível criar, atualizar e excluir documentos usando a sintaxe do MongoDB.

Aqui está um exemplo de como criar um documento na coleção "exemplo":


# Seleciona a coleção
colecao = banco_de_dados.exemplo

# Cria um documento
documento = {"nome": "João", "idade": 30}

# Insere o documento na coleção
resultado = colecao.insert_one(documento)

# Imprime o ID do documento inserido
print(resultado.inserted_id)
Este exemplo cria um documento com dois campos ("nome" e "idade") e o insere na coleção "exemplo". O método insert_one() retorna um objeto InsertOneResult que contém o ID do documento inserido.

Agora, vamos atualizar o documento que acabamos de criar:

# Atualiza o documento
filtro = {"nome": "João"}
novo_valor = {"$set": {"idade": 35}}
resultado = colecao.update_one(filtro, novo_valor)

# Imprime o número de documentos atualizados
print(resultado.modified_count)
Este exemplo atualiza o campo "idade" do documento que possui o nome "João" na coleção "exemplo". O método update_one() retorna um objeto UpdateResult que contém o número de documentos atualizados.

Para recuperar documentos da coleção, você pode usar o método find() ou find_one(). Aqui está um exemplo de como recuperar todos os documentos da coleção "exemplo" e exibi-los na tela:


# Recupera todos os documentos da coleção
documentos = colecao.find()

# Exibe os documentos na tela
for documento in documentos:
    print(documento)
Este exemplo recupera todos os documentos da coleção "exemplo" usando o método find() e exibe cada documento na tela usando um loop for.

Por fim, vamos excluir o documento que criamos anteriormente:


# Exclui o documento
filtro = {"_id": resultado.inserted_id}
resultado = colecao.delete_one(filtro)

# Imprime o número de documentos excluídos
print(resultado.deleted_count)
Este exemplo exclui o documento que criamos anteriormente usando o método delete_one(). O método delete_one() retorna um objeto DeleteResult que contém o número de documentos excluídos.

Fechando a conexão
Quando terminar de usar o banco de dados, é uma boa prática fechar a conexão com o banco de dados usando o método close().


# Fecha a conexão com o banco de dados
cliente.close()
Este exemplo fecha a conexão com o banco de dados MongoDB.

Conclusão
Este foi um tutorial simples sobre como conectar ao MongoDB em Python usando a biblioteca pymongo. Lembre-se de que este é apenas um exemplo básico e que você pode fazer muito mais com o MongoDB em Python, como usar o método find_many(), usar o método aggregate() para executar consultas de agregação e muito mais. Consulte a documentação da biblioteca pymongo para obter mais informações.