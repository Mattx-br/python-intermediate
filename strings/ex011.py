"""
11. Jogo de Forca. Desenvolva um jogo da forca.
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!

"""

string = "cenoura"
separated = list(string)
letters_discovered = ['_' for i in range(0, len(separated))]

error_counter = 0
accept_counter = 0

while True:
    char = input('\nDigite uma letra: ')

    print('\nA palavra é: ', end='')
    for index, letter in enumerate(separated):
        if char == separated[index]:
            letters_discovered[index] = char
            accept_counter += 1

        print(f'{letters_discovered[index]} ', end='')

    if string.find(char) == -1:
        error_counter += 1
        print(f"\nErrou pela {error_counter}º vez. Tente novamente")

    if accept_counter == len(separated):
        print("\nAcertou!!!")
        break

    elif error_counter >= 6:
        print('Perdeu!!!')
        break
