letters = str(input("Insert a word: "))
vowels = ['a', 'e','i', 'o', 'u']
exist = []
for letter in letters:
    for vowel in vowels:
        if letter == vowel:
            exist.append(letter)
print(f"You have used {len(exist)} vowels")