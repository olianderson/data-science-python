
###################### Manipulando arquivos JSON ##################################
import json
# Criando um dicionário
dict = {'Nome': 'Guido van Rossum',
        'Linguagem': 'Python',
        'Similar': ['c','Modula-3','lisp'],
        'Users': 1000000}
# Mostrando o dicionário
for k,v in dict.items():
    print (k,v)

# Convertendo o dicionário para um objeto json
json.dumps(dict)

# Criando um arquivo Json
with open('./cap01/arquivos/numeros.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict))

# Leitura de arquivos Json
with open('./cap01/arquivos/dados.json','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print(data)

# Imprimindo um arquivo Json copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]

print ('Título: ', data['title'])
print ('URL: ', data['url'])
print ('Duração: ', data['duration'])
print ('Número de Visualizações: ', data['stats_number_of_plays'])

# Copiando o conteúdo de um arquivo para outro
import os

arquivo_fonte = './cap01/arquivos/dados.json'
arquivo_destino = './cap01/arquivos/json_data.txt'

# Método 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)  

# Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read()) 

# Leitura de arquivos Json
with open('./cap01/arquivos/json_data.txt','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print(data)