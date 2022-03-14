# 10. Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

elements_needed = 10

first = []
second = []
third = []

for i in range(elements_needed):
    number_for_first = input("Digite um número para o array 'first': ")
    number_for_second = input("Digite um número para o array 'second': ")
    third.extend([number_for_first, number_for_second])

print(third)
