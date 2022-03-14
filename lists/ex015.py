# 15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

quit_loop = True
grades = []
sum_values = 0
over_avg = 0
under_7 = 0

while quit_loop:

    value = float(input('Digite a nota: '))

    if value == -1:

        break
    else:
        grades.append(value)
        sum_values += value


# show the quantity of inputted values
print(f'Quantidade de valores lidos: {len(grades)}')

# show each value one aside each other
[print(f'{value} ', end='') for value in grades]

print('')

# show each value one above other in a reverse way
[print(f'{value}') for value in grades[::-1]]

print('A soma dos valores: ', sum_values)

avg_values = sum_values / len(grades)
print('A média dos valores: ', avg_values)

# Checking every grade to see if it is bigger or lower than the average
for grade in grades:
    if grade > avg_values:
        over_avg += 1
    elif grade < 7:
        under_7 += 1
    else:
        pass

print("Quantidade de valores acima da média calculada: ", over_avg)
print("Quantidade de valores abaixo de 7: ", under_7)

print('Obrigado por usar o programa!!!')
