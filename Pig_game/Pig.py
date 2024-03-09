import random
from collections import namedtuple


def add_player(name: str, players):
    players.append(namedtuple('Player', ['name', 'score']))
    players[-1].name = name
    players[-1].user_score = 0


def roll():
    return random.randint(1, 6)


def main():
    # first one who reach to 25 will win
    endpoint = 0
    current_player_index = 0
    players = []

    print('\n-------------{ Welcome to the pig game } -------------\n')
    print('Game description:\n'
          'Each player has a score, and he will roll a dice, and the number he got will be added to his score.\n'
          'The first player whose score >= 25 points will win.\n\n'
          '--( Notice that if your rolled number is (1) your score will be reset to zero. Each player has the option to roll a dice or skip )--\n\n')

    number_of_players = int(input('How many players will participate: '))

    for i in range(number_of_players):
        counter = i + 1
        name = str(input(f'player {counter} name: '))
        add_player(name, players)

    while True:
        print()
        choice = int(input(f'{players[current_player_index].name} enter your choice (0 = skip, 1 = roll a dice): '))

        # player part
        if choice == 1:
            rolling_value = roll()

            if rolling_value == 1:
                print('Unfortunately you got 1, so your score will be zero')
                players[current_player_index].user_score = 0
            else:
                print(f'You got {rolling_value}')
                players[current_player_index].user_score += rolling_value

        # display current score
        print(f'\n{players[current_player_index].name} current score = {players[current_player_index].user_score}')

        endpoint = players[current_player_index].user_score

        if endpoint >= 10:
            print(f'Congratulation!\nThe winner is {players[current_player_index].name}!')
            break

        if current_player_index == number_of_players - 1:
            current_player_index = 0
            continue

        current_player_index += 1


if __name__ == "__main__":
    main()
