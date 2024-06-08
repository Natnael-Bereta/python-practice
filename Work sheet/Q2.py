word = input("Insert a word to check if it is a palindrome or not. ")
reversed_word = ''
for later in word:
    reversed_word = later + reversed_word
if word == reversed_word:
    print(f'The word {word} is indeed a palindrome!')
else:
    print(f'The word {word} is not a palindrome.')