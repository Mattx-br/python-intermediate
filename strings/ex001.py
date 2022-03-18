"""
1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

string1 = input('digite algo: ')
string2 = input('digite algo: ')

print(f'Tamanho de "{string1}": {len(string1)}')
print(f'Tamanho de "{string2}": {len(string2)}')
same_length = 'iguais' if len(string1) == len(string2) else 'diferentes'
same_content = 'iguais' if string1 == string2 else 'diferentes'
print(f'As duas strings possuem tamanhos {same_length}')
print(f'As duas strings possuem conteúdos {same_length}')
