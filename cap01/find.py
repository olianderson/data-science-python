def find(lista, c):
    for i in range(len(lista)):
        if (lista[i] == c):
            return True
    return False

x = find([20, 5, 15, 24, 67, 5, 1, 76, 17, 5], 5)

print(x)