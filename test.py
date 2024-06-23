a = int(input("Insert a number: "))

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


"""a = int(input("Insert a number: "))
print(a)
b = 0 
c = a
while a > 0:
    temp = a % 10
    b = (b*10) + temp
    a = a // 10

if b == c:
    print("Yes it is a palindrome!")
else:
    print("No it is not!")
"""
