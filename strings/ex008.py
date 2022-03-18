"""
8. Palíndromo.
Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa.
Por exemplo: OSSO e OVO são palíndromos.
Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
Faça um programa que leia uma sequência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""

print('Palindrome checker\n')

string = input("Digite uma frase: ")

string = string.split()
string = ''.join(string)

is_palindrome = True if string[::-1].lower() == string.lower() else False

print(is_palindrome)