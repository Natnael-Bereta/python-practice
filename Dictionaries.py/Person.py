#personal information about a person
#info = {"first name": "Natnael",
 #       "last name" : 'Tegegne',
  #      "age": 20,
   #     "city": "Addis Ababa"}
#print(f'First name: {info["first name"]}\nLast name: {info["last name"]}\nAge: {info["age"]}\nCity: {info["city"]}')

info = [ user1 := {"first name": "Natnael",
        "last name" : 'Tegegne',
        "age": 20,
        "city": "Addis Ababa"},
        user2 := {"first name": "Digo",
        "last name" : 'Degaga',
        "age": 40,
        "city": "Minesota"}]
for user in info:
    for key, value in user.items():
        print(f'{key}: {value}')