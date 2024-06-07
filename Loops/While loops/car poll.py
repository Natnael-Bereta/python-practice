responses = {}
poll_active = True

while poll_active:
    name = input("What is your name? ")
    car = input("What car do you want to ride? ")

    responses[name] = car
    repeat =input("\nDo you want other person to take the poll (yes/no)? ")
    if repeat == 'no':
        poll_active = False
        print("\n---Poll result---")
        for key, value in responses.items():
            print(f'{key} wants to drive {value}.')