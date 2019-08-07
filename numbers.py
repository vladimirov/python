numbers = [3, 6, 24, 8, 4, 10, 10]
numbers = list(dict.fromkeys(numbers))
print(numbers)

numbers = [3, 6, 24, 8, 4, 10, 10]
uniques_numbers = []
for number in numbers:
    if number not in uniques_numbers:
        uniques_numbers.append(number)
print(uniques_numbers)

