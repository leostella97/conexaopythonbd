import pymongo

# Cria a conexão com o MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleciona o banco de dados
db = client["meu_banco_de_dados"]

# Seleciona a coleção
colecao = db["minha_colecao"]

# Consulta os documentos na coleção
resultados = colecao.find()

# Imprime os documentos encontrados
for documento in resultados:
    print(documento)

# Fecha a conexão com o MongoDB
client.close()
