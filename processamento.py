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


    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Alunos em recuperação:\n")
        for nome, media in recuperacao:
            arquivo.write(f"{nome}: {media:.2f}\n")

        arquivo.write("\nMelhor aluno:\n")
        arquivo.write(f"{melhor_aluno} com média {calculomedia:.2f}\n")

    return recuperacao, melhor_aluno, calculomedia

