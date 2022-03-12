# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
even = []
odd = []
for i in range(20):
    value = int(input(('Digite um número: ')))
    vetor.append(value)
    if value % 2 != 0:
        even.append(value)
    else:
        odd.append(value)

print(vetor)
print(even)
print(odd)
