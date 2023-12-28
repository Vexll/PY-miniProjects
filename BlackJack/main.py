import random

#                   Our Blackjack House Rules              #
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1. ---> if score > 10 Ace = 1, otherwise A = 11
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_choice = ["yes", "no"]
computer_hand = []
computer_score = 0
user_hand = []
user_score = 0
current_player_index = 0


def hit_card(curr_player_score):
    choice = current_player_choice(curr_player_score)
    if player_turn() == 0:
        user_hand.append(choice)
    else:
        computer_hand.append(choice)


def sum_score(hand_list):
    score = 0
    for i in hand_list:
        score += hand_list[i]
    return score


def player_turn():
    return 1 - current_player_index


def current_player_choice(curr_player_score):
    choice = random.choice(cards)
    if choice == 11 and curr_player_score > 10:
        choice = 1
    return choice
