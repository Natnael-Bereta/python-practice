Input = [23,4,-6,23,-9,21,3,-45,-8]
positive = []
negative = []
for number in Input:
    if number > 0:
        positive.append(number)
    else:
        negative.append(number)

print(f'Positive {positive} \nNegative {negative}')