numbers = [1, 9, 3, 7]
max_value = numbers[0]

for number in numbers:
    if max_value < number:
        max_value = number #remember this
print(max_value)