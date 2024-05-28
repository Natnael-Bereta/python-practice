try:
    number = int(input("How many numbers?"))
    total_sum = 0
    for n in range(number):
        num = float(input("Insert the numbers: "))
        total_sum += num
    avr = total_sum/ number
    print("The average is:" , avr)
except:
    print("You can only insert integer!")

