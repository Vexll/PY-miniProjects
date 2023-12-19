import random
from hangman_resourse import hangman_words
from hangman_resourse import hangman_art


def list_formatting(word):
    temp_list = []
    for _ in range(len(word)):
        temp_list.append("_")
    return temp_list


# random choice part
random_choice = str(random.choice(hangman_words.word_list))
word_length = len(random_choice)
guessing_letters = list_formatting(random_choice)

# introduction part
print("Welcome to the Hangman game")
print("try to fill the blanks with a correct letters")
print("\nword ->   ", end="")
for i in range(word_length):
    print("_", end=" ")
print()  # new line

wrong_attempts = 6  # maximum attempts is 7
while wrong_attempts >= 0:
    letter = input("give a shot: ").lower()
    # handling if the user didn't enter a letter.
    while len(letter) > 1:
        print("please enter a letter not a word")
        letter = input("give a shot: ").lower()

    # checks if letter not in the target word
    if letter not in random_choice:
        print(hangman_art.stages[wrong_attempts])
        wrong_attempts -= 1
        if wrong_attempts == -1:  # checks if the player lose
            print("\nGame Over!\nthe man has been hanged.")
            break

    # displaying the user guessing part
    print("\nword ->   ", end="")
    for i in range(len(random_choice)):
        letter_index = random_choice.find(letter, i, word_length)
        if i == letter_index:
            guessing_letters[i] = letter
        print(guessing_letters[i], end=" ")
    print()  # new line

    # checks if the player win
    if "_" not in guessing_letters:
        print("\nnice work, you win.")
        print("goodbye.")
        break
