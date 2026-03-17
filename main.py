from processamento import sistema

alunos = [
    ("Isabella", [9, 7]),
    ("Thiago", [3, 8]),
    ("Guilherme", [10, 9]),
    ("Lucas", [9, 9])
]

recuperacao, melhor_aluno, calculomedia = sistema(alunos)

print("Aluno em Recuperação:")
for nome, media in recuperacao:
    print(nome, media)

print("Melhor aluno:")
print(melhor_aluno, calculomedia)