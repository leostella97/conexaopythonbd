import pymongo 

# Cria a conexão com o MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleciona o banco de dados
db = client["meu_banco_de_dados"]

# Seleciona a coleção
colecao = db["minha_colecao"]

# Insere um documento na coleção
documento = {"nome": "Leonardo", "idade": 26}
colecao.insert_one(documento)

# Fecha a conexão com o MongoDB
client.close() 
