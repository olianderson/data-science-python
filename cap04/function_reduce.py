# Importando a função reduce do módulo functools
from functools import reduce

lista = [47,11,42,13]

def soma(a,b):
    x = a + b
    return x

# Usando reduce com uma função e uma lista. A função vai retornar o maior valor
soma_valores = reduce(soma, lista)
#print(soma_valores)

lst = [47, 11, 42, 13]

# Usando a função reduce() com lambda retorna a soma dos valores da lista
soma = reduce(lambda x, y: x + y, lst)
#print(soma)

# Atribuindo a expressão lambda a uma variável, neste caso retorna a > b
max_find2 = lambda a,b: a if (a > b) else b

# Reduzindo a lista até o maior valor, através da função criada com a expressão lambda
a = reduce(max_find2, lst)
print(a)