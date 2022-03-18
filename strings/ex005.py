"""
5. Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""

name = input('Nome: ')

for i, j in enumerate(name):
    print(name)
    name = name[::].replace(name[-1], '')
