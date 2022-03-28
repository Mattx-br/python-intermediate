import random


def play():
    user = input('Rock (R), Paper (P) or scissors (S)? ').lower()
    computer = random.choice(['r', 'p', 's'])

    print(f'Computer choice was "{computer}"')
    if user == computer:
        return 'Tie'

    if is_win(user, computer):
        return 'You won!!!'

    return 'You lost!'
    # r > s, s > p, p > r


# return true if player wins
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())