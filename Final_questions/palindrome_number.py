a = int(input("Insert a number to check if it is a palindrome \n >>> "))
b = 0
c = a
while a > 0:
    temp = a % 10
    b = (b*10) + temp
    a //= 10
if c == b:
    print("It is palindrome!")
else:
    print("It is not!")
