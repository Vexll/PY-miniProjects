import random, os, art
from game_data import data


def comparison(a_account: dict, b_account: dict):
    return a_account['follower_count'] >= b_account['follower_count']


def get_greater_follower_account(a_account: dict, b_account: dict):
    if comparison(a_account, b_account):
        return a_account
    else:
        return b_account


def user_guess(a_account: dict, b_account: dict):
    # take the user guess and return if it's true or false
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a':
            return comparison(a_account, b_account)
        elif guess == 'b':
            return comparison(b_account, a_account)
        print("invalid input!")


def display(a_account: dict, b_account: dict, user_score):
    print(art.logo)
    if user_score != 0:
        print(f"You're right! Current score: {user_score}")
    print(f"Compare A: {a_account['name']}, {a_account['description']}, {a_account['country']}.")
    print(art.vs)
    print(f"Compare B: {b_account['name']}, {b_account['description']}, {b_account['country']}.")


def play_game():
    # here the user start playing, whenever he loses the function return his score
    score = 0
    a_account, b_account = setup_accounts()
    while True:
        clear_screen()
        correct_acc = get_greater_follower_account(a_account, b_account)
        display(a_account, b_account, score)
        user_result = user_guess(a_account, b_account)
        if user_result:
            score = increase_score(score)
            a_account, b_account = update_accounts(correct_acc)
            continue
        return score


def end_game_message(user_score: int):
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {user_score}")


def update_accounts(correct_acc: dict):
    new_second_acc = random.choice(data)
    data.remove(new_second_acc)
    return correct_acc, new_second_acc


def increase_score(score: int):
    return score + 1


def setup_accounts():
    # return two dict randomly from data list and remove them.
    a_account = random.choice(data)
    data.remove(a_account)
    b_account = random.choice(data)
    data.remove(b_account)
    return a_account, b_account


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    user_score = play_game()
    end_game_message(user_score)


if __name__ == "__main__":
    main()
