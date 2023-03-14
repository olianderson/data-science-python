# Criando uma classe chamada Circulo
class Circulo():
    
    # O valor de pi é constante
    pi = 3.14

    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5.
    def __init__(self, raio = 8):
        self.raio = raio 

    # Esse método calcula a área. Self utiliza os atributos deste mesmo objeto
    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio


# Criando o objeto circ uma instância da classe Circulo()
circ = Circulo()
# Executando um método da classe Circulo
circ.getRaio()
# Criando outro objeto chamado circ1 uma instância da classe Circulo() sobrescrevendo o valor do atributo default
circ1 = Circulo(4)
# Executando um método da classe Circulo
circ1.getRaio()
# Imprimindo o raio
print ('O raio é: ', circ.getRaio())
# Imprimindo a area
print('Area igual a: ', circ.area())
# Gerando um novo valor para o raio do círculo
circ.setRaio(3)
# Imprimindo o novo raio
print ('Novo raio igual a: ', circ.getRaio())