# Localize o número de ocorrências de um determinado parâmetro
def locate(lista, c):
    res = []
    for i in range(len(lista)):
        if(lista[i] == c):
            res.append(i)
    return False if len(res) == 0 else res

x = locate([20, 5, 15, 24, 67, 5, 1, 76, 17, 5], 5)
print(x)
