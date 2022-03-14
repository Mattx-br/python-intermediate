# 11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

elements_needed = 10
first = []
second = []
extra = []
third = []

for i in range(elements_needed):
    number_for_first = input("Digite um número para o array 'first': ")
    number_for_second = input("Digite um número para o array 'second': ")
    number_for_extra = input("Digite um número para o array 'extra': ")
    third.extend([number_for_first, number_for_second, number_for_extra])

print(third)
