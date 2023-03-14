###################### Manipulando arquivos CSV ##################################
import csv
""" 
1. Ler arquivo de entrada (cadastro)
2. Processamento (retirar o campo ID e junção do campo nome e sobrenome)
3. Gravaçao do arquivo csv de saída
 """


resultados = []

with open('./cap01/arquivos/cadastro.csv', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()[1:]

    for linha in linhas:
        dados = linha.split(',')
        email = dados[3].replace("\n", "")
        resultados.append(f'{dados[1]} {dados[2]}, {email}\n')

with open('./cap01/arquivos/cadastro_saida.csv', 'w') as arquivo_saida:
    for resultado in resultados:
        arquivo_saida.write(resultado)


## Manipulando arquivos CSV
# Escrevendo arquivo.csv
with open('./cap01/arquivos/numeros.csv', 'w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55, 93, 76))
    writer.writerow((62, 14, 86))

# Leitura do arquivo
with open('./cap01/arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)

#Gerando uma lista com dados do arquivo
with open('./cap01/arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)

for linha in dados[1:]:
    print(linha)
