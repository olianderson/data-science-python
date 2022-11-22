from oop_4 import Desenvolvedor, GerenteProjeto

joao_dev = Desenvolvedor(
    nome_completo='João Carlos da Silva',
    matricula_funcional='F4787962',
    email='joao.carlos@empresa.br',
    salario=4500,
    linguagens_programacao=['C', 'Python']
)

adam_gerente = GerenteProjeto(
    nome_completo='Adam Muller',
    matricula_funcional='G5489625',
    email='adam.muller@empresa.br',
    salario=12000,
    time=[joao_dev],
    projetos_envolvidos=['Polícia Federal', 'Ministério da Economia']
)

# João e Adam iniciam sua Jornada de Trabalho
joao_dev.iniciar_jornada()
adam_gerente.iniciar_jornada()

# João toma aquele cafézinho pra iniciar mais um dia de trabalho
joao_dev.beber_cafe(0.5)

# Adam começa a participar de mais um projeto...
adam_gerente.participar_projeto(novo_projeto='Ministério do Turismo')

# E por isso, recebe um aumento...
adam_gerente.receber_aumento()

# E João também, que desempenhou um ótimo trabalho...
joao_dev.receber_aumento()

# Mas Adam fica sobrecarregado e pede pra sair do projeto da Polícia Federal
adam_gerente.sair_projeto('Polícia Federal')

# João deu um UPDATE SEM WHERE na sexta feira e Adam o removeu do time
adam_gerente.remover_desenvolvedor(joao_dev)

# João ficou pistola e enche a cara de café
joao_dev.beber_cafe(1.6)

print(f'Qde de Gerente de projetos: {GerenteProjeto.numero_empregados}')


