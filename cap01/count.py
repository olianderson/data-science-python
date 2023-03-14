# Conte o número de ocorrências de um determinado parâmetro
def count(lista, c):
    total = 0
    for i in range(len(lista)):
        if (lista[i] == c):
            total += 1
    return total

x = count([20, 5, 15, 24, 67, 5, 1, 76, 17, 5], 5)

print(x)