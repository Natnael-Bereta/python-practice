active = True
print("Insert words and I will tell you which one is the longest.")
print("Type 'e' for enough!")

list_of_words = []

while active:
    words = input(">> ")
    if words == 'e':
        break
    list_of_words.append(words)

    longest_word = ''
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)
print(list_of_words)



