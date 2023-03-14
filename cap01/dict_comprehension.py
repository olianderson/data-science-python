# Dicionário de alunos e notas 
dict_alunos = {"Anderson": 56, "Claudio": 45, "Cayo": 43}

dict_alunos_estado = {k: ("Aprovado" if v >= 45 else "Reprovado") for (k, v) in dict_alunos.items()}
print(dict_alunos_estado)