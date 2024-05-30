numbers = [23, 45, 3, 36, 23, 44, 23, 3]
no_duplicate = []
seen = set()
for number in numbers:
    if number not in seen:
        seen.add(number)
        no_duplicate.append(number)
print(no_duplicate)
#OR INSTEAD
for number in numbers:
    if number not in no_duplicate:
        no_duplicate.append(number)
print(no_duplicate)