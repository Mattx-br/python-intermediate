"""
17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba
    o nome
    e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe
    o nome,
    os saltos
    e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

athletes_list = []


def create_athlete(jumps=5):
    athlete = []
    name = input('Digite o nome do atleta: ')
    if not name:
        return 0
    jump_grades = []

    for i in range(jumps):
        jump = float(input("Digite a nota do pulo: "))
        jump_grades.append(jump)

    athlete.extend([name, jump_grades])
    avg_grade = sum(athlete[1]) / len(athlete[1])
    athlete.append(avg_grade)

    return athlete


while True:
    candidate = create_athlete()

    if candidate != 0:
        athletes_list.append(candidate)
        print(f'{candidate[0]} adicionado!\n')

    elif len(athletes_list) == 0:
        print(f'Quantidade de atletas: {len(athletes_list)}')
        print("Programa terminado")
        break
    else:
        print('\n')
        print('=' * 14, 'Relatório', '=' * 15)

        for athlete in athletes_list:
            print(f'Atleta: {athlete[0]}')
            print(f'Saltos: {" - ".join(map(str, athlete[1]))}')
            print(f'Média: {athlete[2]}')

        print('-' * 40)
        print(f'Quantidade de atletas: {len(athletes_list)}')
        break
