print('Order your T-shirt by providing your size and what to write on it!')
size_input = input('Insert your size: ')
word_input = input('What do you like to be wrote on your T-shit: ')

def t_shirt(size, words):
    print("\nYour T-shirt's size: "+ str(size) + '\nWhat to write on: ' + str(words.title()))

t_shirt(size= size_input, words= word_input)