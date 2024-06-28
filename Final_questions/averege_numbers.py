def average_number(*numbers):
    avr = sum(numbers)/len(numbers)
    return avr


flag = True

while flag:
    a = eval(input('Insert to calculate the average: '))
    if a == 'break':
        flag = False
    else:
        print(average_number(a))