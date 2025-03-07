alunos = [
    ("nome", "Raphael", "nota", 8.5),
    ("nome", "Ana", "nota", 10.0),
    ("nome", "Carol", "nota", 5.0),
]
alunos_ordenados = sorted(alunos, key=lambda aluno: aluno["nota"])
print(alunos_ordenados)
