def sistema(alunos):
    recuperacao = []
    melhor_aluno = ""
    calculomedia = 0

    for nome, notas in alunos:

        if notas == []:
            continue

        soma = 0
        for n in notas:
            soma = soma + n

        media = soma / len(notas)

        if media < 7:
            recuperacao.append((nome, media))

        if media > calculomedia:
            calculomedia = media
            melhor_aluno = nome

    return recuperacao, melhor_aluno, calculomedia