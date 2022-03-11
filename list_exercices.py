# exercices reference: https://wiki.python.org.br/ExerciciosListas

# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
vetor = []
for i in range(5):
    i = int(input('digite um número:'))
    vetor.append(i)
print(vetor)
'''
# 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
vetor = []
for i in range(10):
    i = int(input(f'digite o {i + 1}º número:'))
    vetor.append(i)
print(vetor[::-1])
'''

# 4. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
vetor =[]
media = 0

for i in range(4):
    nota = int(input(f'Digite a {i + 1}º nota: '))
    vetor.append(nota)
    media += nota


[print(f'Nota: {i}') for i in vetor]
print(f'Média: {media / 4}')
'''

# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.