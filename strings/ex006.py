"""
6. Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em 29 de outubro de 1973.
"""

import datetime
import locale

locale.setlocale(locale.LC_TIME, "pt_Br")  # portuguese

birth = input('Digite sua data de nascimento: ')
birth = birth.split('/')

day = datetime.datetime(int(birth[2]), int(birth[1]), int(birth[0]))
month = datetime.datetime(int(birth[2]), int(birth[1]), int(birth[0]))
year = datetime.datetime(int(birth[2]), int(birth[1]), int(birth[0]))


print(f'Você nasceu em {day.strftime("%d")} de {month.strftime("%B")} de {year.strftime("%Y")}.')
