digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}

input_character = input()
output = ""
for digit in input_character:
    output += digits.get(digit, "!") + " "
print(output)

