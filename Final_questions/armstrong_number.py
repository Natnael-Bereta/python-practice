a = int(input("Insert any number to check if it is an armstrong \n >>> "))
original_number = a
number_of_digit = 0

while a > 0:
    number_of_digit += 1
    a = a // 10


armstrong_number = 0

while a > 0:
    temp = a % 10
    armstrong_number = armstrong_number + (temp ** number_of_digit)
    a = a // 10

if armstrong_number == original_number:
    print("Yes it is an armstrong number!")
else:
    print("It is not!")