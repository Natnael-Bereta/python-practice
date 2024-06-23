n = int(input("Insert any  number: "))
total = 1
for i in range(2, n + 1):
    total *= i
print(f'The factorial is: {total}')

#To print the above in the form of a string (Do this)
res = ''
for j in range(1, n+1):
    if n == j:
        res += 'j'
    else:
        res += 'j' + '*'
print(res)