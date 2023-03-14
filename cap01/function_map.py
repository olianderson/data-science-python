# Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

# Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius
def celsius(T):
    return (float(5)/9)*(T-32)

temperaturas = [0, 22.5, 40, 100]

# Convertendo para Fahrenheit
temp_fahrenheit = list(map(fahrenheit, temperaturas))
print(temp_fahrenheit)

# Usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
    print(temp)

# Convertendo para Celsius
temp_celsius = list(map(celsius, temperaturas))
print(temp_celsius)

# Usando lambda
temp_lambda = list(map(lambda x: (5.0/9)*(x - 32), temperaturas))
print(temp_lambda)

# Somando os elementos de 3 listas
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

soma3 = list(map(lambda x, y, z: x + y + z, a, b, c))
print(soma3)