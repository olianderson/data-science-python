# Operações com datasets
import pandas as pd

f = open('./cap04/salarios.csv', 'r')

dados = f.read()

linhas = dados.split('\n')

fullDados = []

for linha in linhas:
    splitLinhas = linha.split(',')
    fullDados.append(splitLinhas)
    primeiraLinha = fullDados[0]

contLinhas = 0
for linha in linhas:
    contLinhas += 1


contColunas = 0
for coluna in primeiraLinha:
    contColunas += 1

#print(f'Dados completos do arquivo salários.csv \n{fullDados}')
print(f'Cabeçado do arquivo salarios.csv \n{fullDados[0]}\n')
print(f'Quantidade de linhas: {contLinhas}')
print(f'Quantidade de colunas: {contColunas}')


file_name = "./cap04/salarios.csv"

def Arq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()

arquivo = Arq(file_name)
print(arquivo)
