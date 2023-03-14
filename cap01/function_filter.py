def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Chamando a função e passando um número como parâmetro. Retornará 
# Falso de for ímpar e True se for par.
a = verificaPar(34)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
par = list(filter(verificaPar, lista))
print(par)

num_par = list(filter(lambda x: x%2==0, lista))
print(num_par)

num_maior8 = list(filter(lambda num: num > 8, lista))
print(num_maior8)