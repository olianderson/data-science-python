import csv
""" 
1. Ler arquivo de entrada (cadastro)
2. Processamento (retirar o campo ID e junção do campo nome e sobrenome)
3. Gravaçao do arquivo csv de saída
"""


""" resultados = []

with open('./cap04/arquivos/cadastro.csv', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()[1:]

    for linha in linhas:
        dados = linha.split(',')
        email = dados[3].replace("\n", "")
        resultados.append(f'{dados[1]} {dados[2]}, {email}\n')

with open('./cap04/arquivos/cadastro_saida.csv', 'w') as arquivo_saida:
    for resultado in resultados:
        arquivo_saida.write(resultado) """



## Manipulando arquivos CSV

# Escrevendo arquivo.csv
""" with open('./cap04/arquivos/numeros.csv', 'w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55, 93, 76))
    writer.writerow((62, 14, 86))

# Leitura do arquivo
with open('./cap04/arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)

#Gerando uma lista com dados do arquivo
with open('./cap04/arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)

for linha in dados[1:]:
    print(linha) """



## Manipulando arquivos JSON
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
with open('./cap04/arquivos/numeros.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict))

# Leitura de arquivos Json
with open('./cap04/arquivos/dados.json','r') as arquivo:
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

arquivo_fonte = './cap04/arquivos/dados.json'
arquivo_destino = './cap04/arquivos/json_data.txt'

""" # Método 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)   """

# Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read()) 

# Leitura de arquivos Json
with open('./cap04/arquivos/json_data.txt','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print(data)