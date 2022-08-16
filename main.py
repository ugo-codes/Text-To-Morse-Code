import csv

code = []

# open the .csv file containing the english alphabets and their corresponding morse code
with open('./morse.csv') as file:
    morse_code_file = csv.reader(file)
    # read each row in the .csv file and adds it to a dictionary
    morse_code = {row[0]: row[1] for row in morse_code_file}

# asks the user for a text input
text = input("Enter Your Text Here: ")

# loops through the user input and gets the corresponding morse code
for letter in text:
    if letter == ' ':
        code.append(" ")
        continue

    try:
        code.append(morse_code[letter.upper()])
    except KeyError:
        code.append(letter)

# prints out the morse code of the text
print("".join(code))
