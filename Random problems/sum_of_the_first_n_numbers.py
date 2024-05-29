try:
    number = int(input("Insert any number: "))
    if number < 0:
        raise ValueError("Input should be a non-negative integer.")
    total = 0
    for i in range(1, number + 1):
        total += i
    print(f'The sum is = {total}')
except:
    print("You can only insert positive integers! yay!")