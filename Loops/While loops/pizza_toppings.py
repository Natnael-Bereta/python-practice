promt = "Enter your pizza toppings.\ntype 'quit' to stop!"
promt += "\n>>"
active = True
while active:
    info = input(promt)
    if info == 'quit':
        active = False
    else:
        print(f'Adding {info} to your pizza!')