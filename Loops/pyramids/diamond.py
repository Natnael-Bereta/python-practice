n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end= '')
    for k in range(i):
        print('* ', end='')
    print()

for p in range(n-1, 0, -1):
    for s in range(n-p):
        print(" ", end='')
    for y in range(p):
        print("* ", end='')
    print()
"""    print(' '* (n-i), end=' ')
    print("* " * (i))
for k in range(n-1, 0, -1):
    print(' ' * ((n-1)-2), end=' ')
    print("* " * (n-2))"""