# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACE_HOLDER = "[name]"


with open("Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.read().split("\n")  # convert it to list

with open("input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()  # read the letter content

# create the letter for specific person
for i in range(len(names)):
    ready_letter = letter_content.replace(PLACE_HOLDER, names[i])
    completed_letter = open(f"Output/ReadyToSend/letter_for_{names[i]}", "w")
    completed_letter.write(ready_letter)
    completed_letter.close()

