age = int(input("What is your age? "))
if 0 <= age <= 2:
    print("You are a Baby!")
elif 2 <= age <= 4:
    print("You are a Toddler!")
elif 4 <= age <= 13:
    print("You are a Kid!")
elif 13 <= age <= 20:
    print("You are a Teenager!")
elif 20 <= age <= 65:
    print("You are an Adult!")
elif age > 65:
    print("You are an Elder!")
elif age < 0:
    print("Age can not be negative!")
