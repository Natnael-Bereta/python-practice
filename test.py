a = int(input("Insert a number: "))
b = 0 
c = a
while a > 0:
    temp = a % 10
    b = (b*10) + temp
    a = a // 10
if c == b:
    print("Yes, it is a palindrome!")
else:
    print("It is not!")


#Home work
"""reverse string = 'Hello'  
and  array = ["bb", ]"""