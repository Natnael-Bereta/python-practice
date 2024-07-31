n = int(input("Insert any  number: "))
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(f'The factorial is: {factorial}')

#To print the above in the form of a string (Do this)
res = ''
for j in range(1, n+1):
    if n == j:
        res += 'j'
    else:
        res += 'j' + '*'
print(res)