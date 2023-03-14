# Retornar cada caracter em uma sequência de caracteres
lst = [x for x in 'python']

# Variável x elevada ao quadrado para um range de números e retornar uma lista
lst = [x**2 for x in range(0, 11)]

# Verificar os números pares em um range de números
lst = [x for x in range(11) if x % 2 == 0]

# Converter Celsius para Fahrenheit
temp_celsius = [0,10,20.1,34.5]
fahrenheit = [((float(9) / 5) * temp + 32) for temp in temp_celsius]
print(fahrenheit)

# Operações aninhadas
lista_alinhada = [ x**2 for x in [x**2 for x in range(11)]]
print(lista_alinhada)