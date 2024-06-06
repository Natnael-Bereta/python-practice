name_number = {'Natty': [23, 43, 53],
               'Beki': [42, 34],
               'Kiya': [32, 49],
               'Lemi': [57, 50],
               'Umeran': [49],
               'Sifen': [38, 90, 53]}
#print(f'Natty: {name_number["Natty"]} \nBeki: {name_number["Beki"]} \nKiya: {name_number["Kiya"]} \nLemi: {name_number["Lemi"]}')
#for name, number in name_number.items():
 #   print(f'{name}: {number}')

for name, number in name_number.items():
    print(f'\n{name}:')
    for num in number:
        print(f'{num}')
#well dona my G!