from tkinter import *
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    pass_length = random.randint(8, 32)
    password = ''
    is_pass_valid = False
    while not is_pass_valid:
        for i in range(pass_length):
            password += random.choice(digits)
        is_pass_valid = is_password_valid(password)
    if not pass_entry.get() == '':
        pass_entry.delete(0, END)
    pass_entry.insert(END, password)


def is_password_valid(password: str) -> bool:
    special_characters = set('!@#$%^&*()')
    lowercase_letters = set('abcdefghijklmnopqrstuvwxyz')
    uppercase_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXY')

    has_special_char = False
    has_lowercase_char = False
    has_digit = False
    has_uppercase_char = False
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special_char = True
        elif char in lowercase_letters:
            has_lowercase_char = True
        elif char in uppercase_letters:
            has_uppercase_char = True

        # Exit early if all conditions are met
        if has_digit and has_special_char and has_lowercase_char and has_uppercase_char:
            return True
    return has_uppercase_char and has_digit and has_special_char and has_lowercase_char

    # ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # website | email/username | password
    website = website_entry.get()
    email = email_usr_entry.get()
    password = pass_entry.get()
    account_format = f'{website} | {email} | {password}\n'
    with open('passwords.txt', 'a') as pass_file:
        pass_file.write(account_format)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('MyPass')
window.config(padx=60, pady=20)

# canvas
canvas = Canvas(width=200, height=189, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 95, image=logo_img)
canvas.grid(column=1, row=0, padx=10, pady=10)

# website label
website_label = Label(text='Website:', font=('Arial', 11))
website_label.grid(column=0, row=1, padx=10, pady=10)

# website entry
website_entry = Entry(width=60)
website_entry.grid(column=1, row=1, padx=10, pady=10)

# Email/username label
email_usr_label = Label(text='Email/Username:', font=('Arial', 11))
email_usr_label.grid(column=0, row=2, padx=10, pady=10)

# Email/username entry
email_usr_entry = Entry(width=60)
email_usr_entry.grid(column=1, row=2, padx=10, pady=10)

# Password label
pass_label = Label(text='Password:', font=('Arial', 11))
pass_label.grid(column=0, row=3, padx=10, pady=10)

# Frame
frame = Frame(window)
frame.grid(column=1, row=3, padx=5, pady=5)

# Password entry
pass_entry = Entry(frame, width=30)
pass_entry.grid(column=1, row=3, padx=5, pady=5)

# generate Password
gen_button = Button(frame, text='Generate Password', command=password_generator)
gen_button.grid(column=2, row=3, padx=10, pady=10)

# submit button
submit_button = Button(text='Add', width=50, command=save_password)
submit_button.grid(column=1, row=4)

window.mainloop()
