n = int(input("Insert the first number: "))
m = int(input("Insert the second number: "))
for i in range(1, m + 1):
    k = n * i
    print(f'{n} x {i} = {k}')