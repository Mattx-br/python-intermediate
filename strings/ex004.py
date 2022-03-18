"""

4. Nome na vertical em escada. Modifique o programa anterior para mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

name = input('Nome: ')
for i, j in enumerate(name):
    print(name[:i+1])
