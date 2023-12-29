import random
import art
import os

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
computer_hand = None
user_hand = None


def get_card(score, player):
    choice = player_choice(score)
    if player == "user":
        user_hand.append(choice)
    elif player == "computer":
        if computer_choice():
            computer_hand.append(choice)


def computer_choice():
    choices = ["yes", "no"]
    computer_score = player_score(computer_hand)
    if computer_score < 21:
        if random.choices == "yes":
            return True
    return False


def player_score(hand_list=None):
    score = 0
    if hand_list is not None:
        for i in range(len(hand_list)):
            score += hand_list[i]
    return score


def player_choice(score=0):
    choice = random.choice(cards)
    if choice == 11 and score > 10:  # Ace 'A' condition
        choice = 1
    return choice


def endgame_screen():
    print(f"Your final hand: {user_hand}, final score: {player_score(user_hand)}")
    print(f"Computer final hand: {computer_hand}, final score: {player_score(computer_hand)}")
    check_win(player_score(computer_hand), player_score(user_hand))


def check_win(computer_score, user_score):
    if user_score > 21:
        print("You went over. You lose!")
    if computer_score == user_score:
        print("Draw")
        return
    if computer_score > user_score:
        print("You lose!")
        return
    print("You win!")


def menu_game():
    while True:
        option = input("Do you want to play a game of Blackjack? 'y' or 'n': ").lower()
        if option == "n":
            return False
        elif option != "y":
            print("invalid input!")
        else:
            clear_screen()
            print(art.logo)
            return True


def hand_preparation():
    for i in range(2):
        choice = player_choice(player_score(user_hand))
        user_hand.append(choice)
        choice = player_choice(player_score(computer_hand))
        computer_hand.append(choice)


def display():
    print(f"\tYour cards: {user_hand}, current score: {player_score(user_hand)}")
    print(f"\tComputer's first card: {computer_hand[0]}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game():
    while True:
        display()
        draw_card_option = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_card_option == 'y':
            get_card(player_score(user_hand), "user")
            get_card(player_score(computer_hand), "computer")
            continue
        else:
            get_card(player_score(computer_hand), "computer")
            endgame_screen()
            break


while True:
    user_hand = []
    computer_hand = []
    flag = menu_game()
    if not flag:
        break
    hand_preparation()
    play_game()
