string = input("Insert a word: ")
if len(string) <= 2:
    print(string + string)
else:
    initial_2 = string[:2]
    final_2 = string[-2:]
    print(initial_2 + final_2)
