"""
19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma
quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete
e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados,
o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

"""



print('Enquete: Quem foi o melhor Sistema Operacional?\n')

votes = []

responsive = 0

os_names = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac Os', 'Outro']


def percent(array, element):
    array_length = len(array)
    occurrences = array.count(element)
    return (occurrences / array_length) * 100


print('As possíveis respostas são:')

print('1- Windows Server')
print('2- Unix')
print('3- Linux')
print('4- Netware')
print('5- Mac OS')
print('6- Outro')
print('\n')

while True:

    try:
        os_vote = int(input("Número do Sistema Operacional (0=fim): "))

        if os_vote == 0:
            best = [0, 0, 0]

            # Showing the results
            print('=' * 20)
            print('Resultado da votação')
            print(f'Foram computados {len(votes)} votos')
            print('-' * 51)
            print(f'Sistema Operacional <----> Votos <----> Porcentagem')

            for index, os in enumerate(set(votes)):

                name = os
                count = votes.count(os)
                percent_number = int(percent(votes, os))

                print(f'{os_names[os - 1]}{" " * (32 - len(os_names[os - 1]))}{count}{" " * (17 - len(str(percent_number)))}{percent_number}%')

                # Verifying best player
                best[0] = os if count >= best[1] else best[0]
                best[1] = count if count >= best[1] else best[1]
                best[2] = percent_number if percent_number >= best[2] else best[2]

            print(f'\nO melhor Sistema Operacional foi o número {os_names[best[0] - 1]}, com {best[1]} votos, correspondendo a {best[2]}% do total de votos.')
            break

        elif os_vote > 6:
            print('!!valor inválido!!\n')
        else:
            votes.append(os_vote)

    except ValueError or os_vote > 6:
        print('!!valor inválido!!\n')
