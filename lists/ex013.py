# 13. Faça um programa que receba a temperatura média de cada mês do ano
# e armazene-as em uma lista. Após isto,
# calcule a média anual das temperaturas e mostre todas as temperaturas
# acima da média anual,
# e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

months_name = ['Jan', 'Fev', 'Mar', "Apr", 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Out', 'Nov', ' Dec']
months = len(months_name)
months_temperature = []
anual_avg = 0

# get the temperature of each month
for month in range(months):
    temperature = float(input(f'Digite a temperatura de {months_name[month]}: '))
    months_temperature.append(temperature)
    anual_avg += temperature

anual_avg /= months

# show the temperature of each month
print('Meses com temperatura acima da média anual:')
for i in range(months):
    if months_temperature[i] > anual_avg:
        print(f'{months_name[i]}: {months_temperature[i]}')
