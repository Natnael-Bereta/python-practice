"""i = 1 
while i <= 10:
    print(i)
    i += 1

for i in range(1,11, 2):
    print(i)"""

"""i = 0
while i <= 20:
    if i % 2 == 0:
         i += 2
         print(i)
    else:
        i += 1
        print(i)"""
#1
i = 0 
while i <= 5:
    if i == 4:
        continue
    print(i)
    i += 1

#2
i = 0 
while i <= 5:
    if i == 4:
        continue
    i += 1
    print(i)
    i =+ 1

#3
i = 0 
while i <= 5:
    if i == 4:
        i += 1
        continue
    print(i)
    i += 1

#4
i = 0 
while i <= 5:
    if i == 4:
        i += 1
        continue
    print(i)
    i =+ 1
    print(i)
    i += 1

#5
i = 0 
while i <= 5:
    if i == 4:
        print(i)
        continue
    print(i)
    i =+ 1

#6
i = 0 
while i <= 5:
    if i == 4:
        print(i)
        i += 1
        continue
    print(i)

#7
i = 0 
while i <= 5:
    if i == 4:
        print(i)
        i += 1
        continue
    print(i)
    i += 1