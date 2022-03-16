"""
18. Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores
para delinear o melhor jogador após cada jogo.

Para isto, faz-se necessário o desenvolvimento de um programa,
que será utilizado pelas telefonistas, para a computação dos votos.
Sua equipe foi contratada para desenvolver este programa.

Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador.

Um número de jogador igual zero, indica que a votação foi encerrada.

Se um número inválido for digitado, o programa deve ignorá-lo,
mostrando uma breve mensagem de aviso, e voltando a pedir outro número.

Após o final da votação, o programa deverá exibir:

a. O total de votos computados;
b. Os números e respectivos votos de todos os jogadores que receberam votos;
c. O percentual de votos de cada um destes jogadores;
d. O número do jogador escolhido como o melhor jogador da partida,
com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos.

O resultado aparece ordenado pelo número do jogador.
O programa deve usar arrays.

O programa deverá executar o cálculo do percentual de cada jogador através de uma função.
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
A função calculará o percentual e retornará o valor calculado.

Abaixo segue uma tela de exemplo.
A disposição das informações deve ser o mais próxima possível ao exemplo.
Os dados são fictícios e podem mudar a cada execução do programa.
Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação
em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.

EXEMPLO DE RESULTADO
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador     Votos               %
9               4               50,0%
10              3               37,5%
11              1               12,5%

O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""

print('Enquete: Quem foi o melhor jogador?\n')

list_players = []
responsive = 14

camisas = [i for i in range(1, 24)]


def percent(array, element):
    array_length = len(array)
    occurrences = array.count(element)
    return (occurrences / array_length) * 100


while True:

    try:
        num_camisa = int(input("Número do jogador (0=fim): "))

        if num_camisa == 0:
            best = [0, 0, 0]

            # Showing the results
            print('=' * 20)
            print('Resultado da votação')
            print(f'Foram computados {len(list_players)} votos')
            print(f'Jogador <----> Votos <----> Porcentagem')

            for jogador in set(list_players):
                # Adjust report's table depending on data
                responsive = 17 if len(str(jogador)) == 2 else 18
                count_player = list_players.count(jogador)
                percent_player = int(percent(list_players, jogador))

                print(f'{jogador}{" " * responsive}{count_player}{" " * 15}{percent_player}%')

                # Verifying best player
                best[0] = jogador if count_player >= best[1] else best[0]
                best[1] = count_player if count_player >= best[1] else best[1]
                best[2] = percent_player if percent_player >= best[2] else best[2]

            print(f'\nO melhor jogador foi o número {best[0]}, com {best[1]} votos, correspondendo a {best[2]}% do total de votos.')
            break

        elif num_camisa > 23:
            print('!!valor inválido!!\n')
        else:
            list_players.append(num_camisa)

    except ValueError or num_camisa > 23:
        print('!!valor inválido!!\n')






