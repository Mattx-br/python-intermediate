"""
Credits:
https://www.youtube.com/watch?v=8ext9G7xspg
"""

import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Nice, congrats. You accepted the number {random_number}')


# in this case, you choose the number, x is only the maximum
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_computer = random.randint(low, high)
        else:
            guess_computer = low  # could also be high, because low = high
        feedback = input(f'Is {guess_computer}? too high (H), low (L) or correct (C)? ').lower()

        if feedback == 'h':
            high = guess_computer - 1
        if feedback == 'l':
            low = guess_computer + 1

    print(f'Yeah! I\'ve guessed your number {guess_computer} correctly!!!')


if __name__ == '__main__':
    computer_guess(150)
