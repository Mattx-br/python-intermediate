# 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []
for i in range(10):
    i = int(input(f'digite o {i + 1}º número:'))
    vetor.append(i)
print(vetor[::-1])
