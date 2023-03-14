# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
lista = [2, 3, 4]
pot = list(map(lambda x: x**3, lista))
print(pot)


# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)

res = map(lambda w: [w.upper(), w.lower(), len(w)], palavras)
for i in res:
    print (i)


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
transposta = [[linha[i] for linha in matrix] for i in range(2)]
print(transposta)


# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos de uma lista. Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 2, 4, 5, 6]

def quad(num):
        return (num**2)
def cubo(num):
        return (num**3)

funcs = [quad, cubo]

for i in lista:
    valor = map(lambda x: x(i), funcs)
    print(list((valor)))


# Exercício 5 - Faça com que cada elemento da listaA seja elevado ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [5, 4, 2]
list(map(pow, listaA, listaB))


# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
a = range(-6, 4)
list(filter((lambda x: x < 0), a))


# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(filter(lambda x: x in a, b)))


# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
import datetime
print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
import time
print (time.strftime("%d/%m/%Y %H:%M"))


# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}
dict3 = dict(zip(dict1, dict2.values()))
print(dict3)


# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
indice_maior_5 = [v for i, v in enumerate(lista) if i > 5 ]
for x in indice_maior_5:
    print(x)


# Exercício 11 - Escreva uma função que retorne se um numero é primo
nums = range(1, 200)
def Primo(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

num_primo = list(filter(Primo, nums))
print(f'Números primos: {num_primo}')


# Exercício 12 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe() Arquivo: "binary.csv"
import pandas as pd
file_name = "./cap04/arquivos/binary.csv"
def Read(file):
    df = pd.read_csv(file)
    return df.describe()

arquivo = Read(file_name)
print(arquivo)


# Exercício 13 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função que converta cada temperatura para Fahrenheit
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = list(map(lambda x: (float(9)/5)*x + 32, Celsius))
print (Fahrenheit)


# Exercício 14 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print (f"Dentro da função a variável 'TOTAL' é: {total}")
    return total

soma( 10, 20 )
print (f"Fora da função a variável 'TOTAL' é: {total}")


# Exercício 15 - Crie uma função e atribua seu retorno a uma variável chamada soma. 
# A expressão vai receber 2 números como parâmetro e retornar a soma deles
soma = lambda arg1, arg2: arg1 + arg2
print ("A soma é : ", soma( 452, 298 ))


# Exercício - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
def printNum( arg1, *lista ):
    print (arg1)
    for i in lista:
        print (i)
    return

printNum( 100 )
printNum( 'A', 'B', 'C' )


# Exercício - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e imprima a lista
lista = [1, 2, 3, 4]
def Adiciona(numberList):
    numberList.append(5)
    numberList.append(6)

Adiciona(lista)
print(lista)


# Exercício - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
t = 'Bebam 2,5L de água todos os dias'
def Upper(texto):
    return texto.upper()

upper_text = Upper(t)
print(upper_text)


# Exercício - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números  
nums = range(1, 20)
def Par(num):
    for x in nums:
        if num % 2 == 0:
            return True
    return False

num_par = list(filter(Par, nums))

print(num_par)



## Exercícios soltos
import string, random

tamanho_senha = int(input('Tamanho da senha: '))
senha = list()
for i in range(0, tamanho_senha):
    senha.append(random.choice(string.ascii_letters))

print(''.join(senha))

# A maneira certa de acessar diciocnarios:
raridade = {
    'Great Sword': 98,
    'Golden Bow': 97,
    'Iron Sword': 80,
    'Axe': 34,
    'Stick': 1
}

x = raridade.get('Iron Sword')
y = raridade.get('Anderson')
print(x, y, raridade)

y = raridade.setdefault('Anderson', 43)
print(x, y, raridade)

# Combinando listas:
loot = ['bow', 'helmet']
chest = ['ruby', 'gold']
curr_inv = ['sword', 'sheild']

new = [*loot, *chest, *curr_inv]
print(new)

# ORDENAÇÃO
inventario = ['Axe', 'Great Sword', 'Stick']

raridade = {
    'Great Sword': 98,
    'Golden Bow': 97,
    'Iron Sword': 80,
    'Axe': 34,
    'Stick': 1}

sort_inven = sorted(inventario, \
    key=raridade.__getitem__, reverse = True)

print(sort_inven)

# Soma das coordenadas de um vetor:
class Vetor(object):
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'X: {self.x}, Y: {self.y}'

v1 = Vetor(10, 20)    
v2 = Vetor(50, 60)
v3 = v1 + v2

print(v3)

#Deseja escolher habilidades em grupo de 3:
import math

skills = [
    'Farming',
    'Mining',
    'Crafting',
    'Healing',
    'Melee',
    'Archery',
    'Alchemy',
    'Stealth',
    'Persuasion',
    'Mobility'
]

num_skills = len(skills)
variations = math.comb(num_skills, 3)
print(variations)

# Expressões BuiltIn: lambda

quadrado = lambda x: x**2
print(quadrado(4))


# Função com número variável de argumentos
def printVarInfo( arg1, *vartuple ):
   # Imprimindo o valor do primeiro argumento
    print (f"O parâmetro passado foi: {arg1}")
   
   # Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print (f"O parâmetro passado foi: {item}")
    return

printVarInfo(1972)
printVarInfo('Amarelo', 'Azul celeste', 'Rosas vermelhas', 'Cachorro caramelo')

# Fazendo split:
def splitString(texto):
    return texto.split(" ")

texto = "Está é uma função bastante útil para separar grandes volumes de dados."

print(splitString(texto))

