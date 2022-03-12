# 6. Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

alunos = []
media_alunos = []

for i in range(2):  # this first for serves for the 10 students
    media = 0
    for j in range(4):  # this one for their grades
        nota = float(input(f'Digite a {j + 1}ª nota do {i + 1}º aluno: '))
        media += nota

    media /= 4
    media_alunos.append(media)


def greater_seven(n):
    if n >= 7:
        return True
    else:
        return False


print(f'Alunos com média maior ou igual a 7: {len(list(filter(greater_seven, media_alunos)))}')
