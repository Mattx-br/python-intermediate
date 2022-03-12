# 7. Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma,
# a multiplicação
# e os números.

vetor = []
soma = 0
multiplicacao = 1
for i in range(5):
    number = int(input('Digite um número inteiro: '))
    vetor.append(number)
    soma += number
    multiplicacao *= number

print(f'soma: {soma} \nmultiplicação: {multiplicacao}')
print(vetor)
