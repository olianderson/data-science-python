x = [1,2]
y = [4,5,6]

d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

# Perceba que zip retorna tuplas. Neste caso, uma lista de tuplas
a = list(zip(x,y))

# Atenção quando as sequências tiverem número diferente de elementos
b = list(zip('ABCD', 'xy'))

# Zip vai unir as chaves
c = list(zip(d1,d2))

# Zip pode unir os valores (itens) que que retorna uma lista com tuplas e equivale a função trocaValores abaixo
d = dict(zip(d1, d2.values()))

# Criando uma função para trocar valores entre 2 dicionários e retorna um terceiro dicionário
def trocaValores(d1, d2):
    dicTemp = {}    
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
    return dicTemp

tv = trocaValores(d1, d2)

print(c, d, tv)
