phone = input("Phone: ")
converter = {"1": "One",
             "2": "Two",
             "3": "Three",
             "4": "Four"}
output = ''
for num in phone:
    output += converter.get(num) + " "
print(output)
