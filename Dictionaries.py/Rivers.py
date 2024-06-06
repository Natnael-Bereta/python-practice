river_name = {'Nile': 'Egypt',
              'Awash': 'Ethiopia',
              'Amazon': 'South America',
              'Missisipi river' : 'North America'}
for river, country in river_name.items():
    print(f'The {river} runs through {country}!')
print("\nThe rivers are: ")
for river in river_name.keys():
    print(river)
print("\nThe countries are: ")
for country in river_name.values():
    print(country)