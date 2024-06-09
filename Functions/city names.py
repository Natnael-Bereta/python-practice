def city_country(city, country):
    full_name = f'"{city}, {country}"'
    return full_name
while True:
    print("Insert the name of the city and countr.")
    print("Insert 'q' to quit.")
    city = input("City name? ")
    if city == 'q':
        print("You quitted the program.")
        break
    country = input("Country name? ")
    if country == 'q':
        print("You quitted the program.")
        break
    full_name = city_country(city=city , country= country)
    print(full_name)