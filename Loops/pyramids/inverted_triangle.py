n = 5
for i in range(n, 0, -1): # i runs from n=5 to 1(included) by decreasing order of value -1
    for j in range(i, 0, -1):
        print('*', end=' ')
    print()