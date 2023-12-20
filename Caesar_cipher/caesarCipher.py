from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alphabet_length = len(alphabet)


# encrypt and decrypt process
# 1. search for the letter index in alphabet list
# 2. shifting step
# 3. add the letter in variable


def encrypt(plain_word: str, shift: int):
    cipher_word = ""
    for i in range(len(plain_word)):
        if plain_word[i] == " ":
            cipher_word += " "
        elif plain_word[i].isdigit() or (not plain_word[i].isalnum()):
            cipher_word += plain_word[i]
        else:
            letter_index = (alphabet.index(plain_word[i]) + shift) % alphabet_length
            cipher_word += alphabet[letter_index]
    return cipher_word


def decrypt(cipher_word: str, shift: int):
    origin_word = ""
    for i in range(len(cipher_word)):
        if cipher_word[i] == " ":
            origin_word += " "
        elif cipher_word[i].isdigit() or (not cipher_word[i].isalnum()):
            origin_word += cipher_word[i]
        else:
            letter_index = abs(alphabet.index(cipher_word[i]) - shift) % alphabet_length
            origin_word += alphabet[letter_index]
    return origin_word


print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(encrypt(text, shift))
    elif direction == "decode":
        print(decrypt(text, shift))
    else:
        print("invalid input!")

    choice = input("do you have another word? (yes/no): ").lower()
    if choice == "no":
        print("goodbye...")
        break
