"""
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em
reconhecimento ao bom resultado alcançado durante o ano que passou.
Para isto contratou você para desenvolver a aplicação que servirá
como uma projeção de quanto será gasto com o pagamento deste abono.

Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os
representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

a. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
b. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo,
recebem este valor mínimo;

Agora, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa,
descontos, impostos ou outras particularidades.

Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários.
Um valor de salário igual a 0 (zero) encerra a digitação.

Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador,
conforme a regra definida acima.

Ao final, o programa deverá apresentar:
    O salário de cada funcionário, com o valor do abono;
    O número total de funcionários processados;
    O valor total a ser gasto com o pagamento do abono;
    O número de funcionário que receberá o valor mínimo de 100 reais;
    O maior valor pago como abono;

A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.
Os valores podem mudar a cada execução do programa.


Projeção de Gastos com Abono
============================

Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0

Salário    - Abono
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""

salary_list = []


def get_abono(brute_value, percent, minimum=100.0):
    result = brute_value * percent if (brute_value * percent) >= minimum else minimum
    return result


while True:
    try:
        salary = float(input("Salário: "))

        if salary != 0:
            salary_list.append(salary)

        # With the program finished, will execute this part
        else:
            count_salaries = len(salary_list)
            total_salaries = sum(salary_list)
            abono = []
            print("\nRelatório")
            print('-' * 20)
            print(f'Salário <----> Abono')

            for index, salary in enumerate(salary_list):
                abono.append(get_abono(salary, 0.2))
                print(f'R$ {salary}{" " * (12 - len(str(salary)))}R$ {abono[index]}')

            print(f"\nForam processados {count_salaries} colaboradores")
            print(f'Total gasto com abonos: R$ {sum(abono)}')
            print(f'Valor mínimo pago a {abono.count(100)} colaboradores')
            print(f'Maior valor de abono pago: R$ {sorted(abono)[-1]}')

            break

    except ValueError:
        print('!!!Valor inválido!!!')
