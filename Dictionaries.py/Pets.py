pets = [Max := {'Owner name': 'Natty',
                  'Animal type': 'Dog'},
        Milo := {'Owner name': 'Beki',
                  'Animal type': 'Cat'},
        Sunny := {'Owner name': 'Lemi',
                  'Animal type': 'Bird'}]
for pet in pets:
    for key, value in pet.items():
        print(f'{key}: {value}')

#Check out how you can print the names of the pets inside the list!!