
from random import randint
from time import sleep
#Criando uma locadora de automóveis:

VALOR_PEDAGIO_CARRO = 3.5
VALOR_PEDAGIO_MOTO = 2.75

VALOR_KM_RODADO_CARRO = 1.5
VALOR_KM_RODADO_MOTO = 1.0

class Automovel:
    numero_total_locacoes = 0

    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        
        self.valor_fatura = 0
        self.nome_cliente = ""
        print(f'Automóvel {self.montadora} {self.modelo} adquirido pela Locadora')

    def alugar(self, nome_cliente):
        Automovel.numero_total_locacoes += 1
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f'O automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}')
    
    def devolver_automovel(self):
        self.alugado = False
        print(f'O automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}')

    def valor_fatura(self, numero_pedagios, km_rodados):
        raise NotImplementedError

    @classmethod
    def mostrar_numero_total_locacoes(cls):
        print(f'O número total de locações de Automóveis é de: {cls.numero_total_locacoes} locações')


class Carro(Automovel):
    numero_total_locacoes_carro = 0
    valor_total_locacoes = 0.0

    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)
        print('O automóvel adquirido foi um Carro')

    def alugar(self, nome_cliente):
        super(Carro, self).alugar(nome_cliente)
        Carro.numero_total_locacoes_carro +=1

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios *VALOR_PEDAGIO_CARRO + km_rodados * VALOR_KM_RODADO_CARRO
        print(f'Fatura do carro {self.montadora} {self.modelo} gerada no valor de R$ {self.valor_fatura:.2f}')
        Carro.valor_total_locacoes += self.valor_fatura

    @classmethod
    def calcular_media_locacoes(cls):
        if cls.numero_total_locacoes_carro != 0:
            media_locacoes = cls.valor_total_locacoes/cls.numero_total_locacoes_carro
            print(f'O valor médio de locação de Carros está em R$ {media_locacoes:.2f}/locação')
        else:
            print('Número total de locação de Carros igual a zero')

class Moto(Automovel):
    numero_total_locacoes_moto = 0
    valor_total_locacoes = 0.0

    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print('O automóvel adquirido foi uma Moto')
    
    def alugar(self, nome_cliente):
        super(Moto, self).alugar(nome_cliente)
        Moto.numero_total_locacoes_moto +=1

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios *VALOR_PEDAGIO_MOTO + km_rodados * VALOR_KM_RODADO_MOTO
        print(f'Fatura da moto {self.montadora} {self.modelo} gerada no valor de R$ {self.valor_fatura:.2f}')
        Moto.valor_total_locacoes += self.valor_fatura

    @classmethod
    def calcular_media_locacoes(cls):
        if cls.numero_total_locacoes_moto != 0:
            media_locacoes = cls.valor_total_locacoes/cls.numero_total_locacoes_moto
            print(f'O valor médio de locação de Motos está em R$ {media_locacoes:.2f}/locação')
        else:
            print('Número total de locação de Motos igual a zero')


def mostrar_fatura(automovel):
    print(f'O valor da Fatura do Automóvel {automovel.montadora} {automovel.modelo} '
    f'alugado por {automovel.nome_cliente} ficou no valor de R$ {automovel.valor_fatura:.2f}')


# instanciando objetos e atributos
fiesta = Carro('Ford', 'Fiesta', False)
fiesta.alugar('Anderson')
sleep(randint(7, 10))
fiesta.devolver_automovel()
fiesta.gerar_valor_fatura(numero_pedagios=5, km_rodados=750)
mostrar_fatura(fiesta)

honda_cb = Moto('Honda', 'CB500', False)
honda_cb.alugar('Ana')
sleep(randint(7, 10))
honda_cb.gerar_valor_fatura(numero_pedagios=3, km_rodados=500)
mostrar_fatura(honda_cb)