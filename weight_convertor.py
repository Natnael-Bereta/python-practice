weight = int(input("What is your weight? "))
unit = input("In Kg or in lb? ").capitalize()
weight_Kg = weight * 0.45
weight_Lb = weight/0.45
if unit == 'Kg':
    print(f'Your weight in lb = {weight_Lb}')
elif unit == 'Lb':
    print(f'Your weight in Kg = {weight_Kg}')
else:
    print("Invalid input.")
