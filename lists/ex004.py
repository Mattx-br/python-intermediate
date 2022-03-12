# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = []
consoante = []
for i in range(10):
    char = input('Digite uma letra: ')
    vetor.append(char)
    if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
        consoante.append(char)

print(vetor)
print(consoante)
