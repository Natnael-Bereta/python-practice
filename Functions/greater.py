def get_formated_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

while True:
    print('Insert your name.')
    print("Insert 'q' to stop.")
    f_name = input("First name? ")
    if f_name == 'q':
        break
    l_name = input("Last name? ")
    if l_name == 'q':
        break
    full_name = get_formated_name(first_name=f_name , last_name= l_name)
    print(f'Hellow {full_name}, How are you?')
