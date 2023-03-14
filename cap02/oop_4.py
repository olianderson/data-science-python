from datetime import datetime

# CLASSE EMPREGADO
# =============================================================================

class Empregado:
    numero_empregados: int = 0

    # Construtor
    def __init__(self, nome_completo: str,
                 email: str,
                 matricula_funcional: str,
                 salario: int):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = salario

    def iniciar_jornada(self):
        print(f'O empregado [{self.matricula_funcional}] {self.nome_completo} '
              f'iniciou sua jornada de trabalho às {datetime.now()}')

    def finalizar_joranda(self):
        print(f'O empregado [{self.matricula_funcional}] {self.nome_completo} '
              f'finalizou sua jornada de trabalho às {datetime.now()}')

    def receber_aumento(self):
        raise NotImplementedError


# CLASSE DESENVOLVEDOR
# =============================================================================

class Desenvolvedor(Empregado):
    porcentagem_aumento: float = 1.05

    def __init__(self, nome_completo: str, email: str,
                 matricula_funcional: str, salario: int,
                 linguagens_programacao: list, litros_cafe: float = 0.0,
                 burnout: bool = False):
        # Chamada ao construtor da classe superior
        super().__init__(nome_completo, email, matricula_funcional, salario)

        # Incrementa o número de empregados, definido na classe superior
        Desenvolvedor.numero_empregados += 1

        self.linguagens_programacao = linguagens_programacao
        self.litros_cafe = litros_cafe
        self.burnout = burnout

    def adicionar_linguagem(self, nova_linguagem: str):
        self.linguagens_programacao.append(nova_linguagem)

        print(f'O Desenvolvedor [{self.matricula_funcional}] '
              f'{self.nome_completo} aprendeu a Linguagem {nova_linguagem}')

    def beber_cafe(self, qtde_cafe: float):
        self.litros_cafe += qtde_cafe

        if self.litros_cafe >= 2:
            print(f'O Desenvolvedor [{self.matricula_funcional}] '
                  f'{self.nome_completo} sofreu um Burnout e terá que '
                  f'finalizar sua Jornada mais cedo.')
            self.finalizar_joranda()
            self.burnout = True

    def receber_aumento(self):
        self.salario *= Desenvolvedor.porcentagem_aumento

        print(f'O Desenvolvedor [{self.matricula_funcional}] '
              f'{self.nome_completo} recebeu um aumento! Parabéns!')


# CLASSE GERENTEPROJETO
# =============================================================================

class GerenteProjeto(Empregado):
    porcentagem_aumento: float = 1.05

    def __init__(self, nome_completo: str, email: str,
                 matricula_funcional: str, salario: int,
                 time: list, projetos_envolvidos: list):
        # Chamada ao construtor da classe superior
        super().__init__(nome_completo, email, matricula_funcional, salario)

        # Incrementa o número de empregados, definido na classe superior
        GerenteProjeto.numero_empregados += 1

        self.time = time
        self.projetos_envolvidos = projetos_envolvidos

    def adicionar_desenvolvedor(self, dev: Desenvolvedor):
        self.time.append(dev)

        print(f'Desenvolvedor [{dev.matricula_funcional}] {dev.nome_completo} '
              f'foi adicionado ao time do Gerente {self.nome_completo}.')

    def remover_desenvolvedor(self, dev: Desenvolvedor):
        self.time.remove(dev)

        print(f'Desenvolvedor [{dev.matricula_funcional}] {dev.nome_completo} '
              f'foi removido do time do Gerente {self.nome_completo}.')

    def participar_projeto(self, novo_projeto: str):
        self.projetos_envolvidos.append(novo_projeto)

        print(f'O Gerente [{self.matricula_funcional}] '
              f'{self.nome_completo} participará do projeto {novo_projeto}!')

    def sair_projeto(self, projeto: str):
        self.projetos_envolvidos.remove(projeto)

        print(f'O Gerente [{self.matricula_funcional}] '
              f'{self.nome_completo} saiu do projeto {projeto}!')

    def receber_aumento(self):
        self.salario *= GerenteProjeto.porcentagem_aumento

        print(f'O Gerente [{self.matricula_funcional}] '
              f'{self.nome_completo} recebeu um aumento! Parabéns!')

