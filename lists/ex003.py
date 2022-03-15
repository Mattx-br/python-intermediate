# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

vetor =[]
media = 0

for i in range(4):
    nota = int(input(f'Digite a {i + 1}º nota: '))
    vetor.append(nota)
    media += nota


[print(f'Nota: {i}') for i in vetor]
print(f'Média: {media / 4}')
