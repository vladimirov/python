numbers = [5, 2, 5, 2, 2]
# numbers = [2, 2, 2, 5, 5]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
