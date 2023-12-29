import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    print("dsfsdfhsdfjhsdkhfsdkhfksdhfsd")
    print("dsfsdfhsdfjhsdkhfsdkhfksdhfsd")
    print("dsfsdfhsdfjhsdkhfsdkhfksdhfsd")

    x = int(input("(1/2): "))
    if x == 1:
        print("clearing...")
        clear_screen()
