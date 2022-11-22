# Criando um novo tipo de objeto chamado Carro
class Carro(object):
    pass

# Instância do Carro
sandero = Carro()

print(type(sandero))

# Criando uma classe Estudantes
class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Estudante1 = Estudantes("Pele", 12, 9.5)
# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
Estudante1.nome
# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
Estudante1.idade
# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
Estudante1.nota

# Criando uma classe Funcionários
class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def listFunc(self):
        print("O nome do funcionário é " + self.nome + " e o salário é R$" + str(self.salario))

# Criando um objeto chamado Func1 a partir da classe Funcionarios
Func1 = Funcionarios("Obama", 20000)
# Usando o método da classe
Func1.listFunc()

# Verificando atributos
hasattr(Func1, "nome")
hasattr(Func1, "salario")
setattr(Func1, "salario", 4500)
hasattr(Func1, "salario")
getattr(Func1, "salario")
delattr(Func1, "salario")
hasattr(Func1, "salario")