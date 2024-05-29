n = int(input("Insert any  number: "))
total = 1
for i in range(1, n + 1):
    total = total * i
print(f'The factorial is: {total}')