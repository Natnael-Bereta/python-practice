a = [1, 4, 6, 9]
b = a[0]
for i in range(len(a)):
    if b > a[i]:
        minimum = a
print(minimum)