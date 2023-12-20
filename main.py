def prime_checker(number: int):
    if (number % 2 == 0) or (number % 3 == 0) or (number % 5 == 0) or (number % 7 == 0) or (number % 11 == 0):
        return False
    return True


def prime_checker_loop(number: int):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print("@".isalnum())