string = input("Insert a word: ")
list_of_strings = []
for laters in string:
    new = list_of_strings.append(laters)
    initial_2 = new[:2]
    final_2_laters = new[-3:]
    if len(string) <= 2:
        print(string + string)
    else:
        print(initial_2 + final_2_laters)