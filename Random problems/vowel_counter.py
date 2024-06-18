words = input("Insert a word to check the number of vowels! \n>> ")
vowels = ['a', 'e', 'i', 'o', 'u']

vowels_in_words = []
for word in words:
    if word in vowels:
        vowels_in_words.append(word)
print(f'Number of vowels in the word: {len(vowels_in_words)}')