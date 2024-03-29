# Módulo PyMongo
import pymongo

# Conexão com o MongoDB (neste caso, conexão padrão)
client_con = pymongo.MongoClient()

# Listando os bancos de dados disponíveis
# client_con.database_names()
client_con.list_database_names()

# Definindo o objeto db
db = client_con.cadastrodb

# Listando as coleções disponíveis
# db.collection_names()
db.list_collection_names()

# Criando uma coleção
db.create_collection("mycollection")

# Listando as coleções disponíveis
# db.collection_names()
db.list_collection_names()

# Inserindo um documento na coleção criada
db.mycollection.insert_one({
   'titulo': 'MongoDB com Python', 
   'descricao': 'MongoDB é um Banco de Dados NoSQL',
   'by': 'Data Science Academy',
   'url': 'http://www.datascienceacademy.com.br',
   'tags': ['mongodb', 'database', 'NoSQL'],
   'likes': 100
})

# Retornando o documento criado
db.mycollection.find_one()

# Preparando um documento
doc1 = {"Nome":"Donald","sobrenome":"Trump","twitter":"@POTUS"}

# Inserindo um documento
db.mycollection.insert_one(doc1)

# Preparando um documento
doc2 = {"Site":"http://www.datascienceacademy.com.br",
        "facebook":"facebook.com/dsacademybr"}

# Inserindo um documento
db.mycollection.insert_one(doc2)

# Retornando os documentos na coleção
for rec in db.mycollection.find():
    print(rec)

# Conectando a uma coleção
col = db["mycollection"]

# Contando os documentos em uma coleção
col.count()
col.estimated_document_count()

# Encontrando um único documento
redoc = col.find_one()