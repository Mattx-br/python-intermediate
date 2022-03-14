# 9. Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

elements_needed = 10
a = []

for i in range(elements_needed):
    number = int(input("Digite um número: "))
    a.append(number)

# transform each item of 'a' array into squared versions of themselves
time_itself = [item ** 2 for item in a]

sum_squared = 0

# summing each number of time_itself
for number in time_itself:
    sum_squared += number


print(sum_squared)
