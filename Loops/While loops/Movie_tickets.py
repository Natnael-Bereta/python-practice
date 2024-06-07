
while True:
    user_input = input("How old are you? ")
    if user_input == 'quit':
        print("Exiting the program.")
        break
    try:
        age = int(user_input)
        if age <= 3:
            print("The ticket is free!")
        elif 3 < age <= 12:
            print("$10 for the ticket.")
        elif age < 0:
            print("Age can not be negative!")
        else:
            print("$15 for the ticket.")
    except ValueError:
        print("You can not insert a string except 'quit'!")
