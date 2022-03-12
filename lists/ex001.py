#  Exercises reference: https://wiki.python.org.br/ExerciciosListas
# ========================================================================== #

# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []
for i in range(5):
    i = int(input('digite um número:'))
    vetor.append(i)
print(vetor)