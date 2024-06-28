"""a = int(input("Insert a number to check if it is a palindrome \n >>> "))
b = 0
c = a
while a > 0:
    temp = a % 10
    b = (b*10) + temp
    a //= 10
if c == b:
    print("It is palindrome!")
else:
    print("It is not!")"""

#or

"""n=input ("Enter a number: ")
u= n[::-1]
if n == u:
    print( "Is a palindrome number ")
else:
    print( "Is not a palindrome number")"""

"""a = int(input("Insert a number: "))

b = m = 0 
c = a
res = ""
while a > 0:
    temp = a % 10
    b = (b*10) + temp
    a = a // 10
    m += 1
if len(str(b)) < m:
    res += "0"*(m-len(str(b))) + str(b)
print(res)
"""

