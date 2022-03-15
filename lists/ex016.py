"""
Utilize uma lista para resolver o problema a seguir.
Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
ou seja, um total de $470.
Escreva um programa (usando um array de contadores)
que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

salary_classes = ['200 299', '300 399', '400 499', '500 599', '600 699', '700 799', '800 899', '900 999', '1000 +']
functionary_per_class = [[index] for index, class_range in enumerate(salary_classes)]
salaries = []
check = True


def get_range(list_of_ranges):
    split_range = list_of_ranges.split(' ')

    range_start = split_range[0]
    range_end = split_range[1]

    return range_start, range_end


def add_salary(brute_sales, commission_percent=0.09, fix_salary=200):
    commission = brute_sales * commission_percent
    final_salary = fix_salary + commission

    return final_salary


def classify_salary(list_of_salaries, classes):
    for index, salary_class in enumerate(classes):

        range_start, range_end = get_range(salary_class)

        for salary_index, salary in enumerate(list_of_salaries):

            if int(range_start) <= salary and range_end == '+':
                functionary_per_class[index].insert(1, salary)

            elif int(range_start) <= salary <= int(range_end):
                functionary_per_class[index].insert(1, salary)

    return functionary_per_class


def show_classification_list(func_per_clas, salary_range):
    for index, salary in enumerate(func_per_clas):

        range_start, range_end = get_range(salary_range[index])

        if len(salary) > 1:

            if int(range_start) <= salary[1] and range_end == '+':
                print(f'Intervalo:      {range_start}+ | Funcionários: {len(salary) - 1}')
            elif int(range_start) <= salary[1] <= int(range_end):
                print(f'Intervalo: {range_start} to {range_end} | Funcionários: {len(salary) - 1}')

        else:
            print(f'Intervalo: {range_start} to {range_end} | Funcionários: {len(salary) - 1}')


print("Para parar a operação, digite um valor menor que zero ou não digite nada e aperte enter")
print('=' * 88)
while check:

    brute_sale = input('Digite o salário do funcionário: ')

    total_salary = add_salary(float(brute_sale)) if brute_sale else 0

    if total_salary <= 200:

        functionary_per_class = classify_salary(salaries, salary_classes)
        show_classification_list(functionary_per_class, salary_classes)
        check = False

    else:
        salaries.append(total_salary)
