"""
7. Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""

string = input('digite algo: ')
counter_space = 0
counter_vowel = 0

for char in string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        counter_vowel += 1
    if char == ' ':
        counter_space += 1

print(f'vogais {counter_vowel}')
print(f'espaços em branco {counter_space}')
