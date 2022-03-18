"""
3. Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
"""

name = input('Nome: ')

for i, char in enumerate(name):
    print(name[i])
