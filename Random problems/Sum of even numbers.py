number = int(input("Insert a number: "))
sum_of_even_numbers = 0
for even in  range(2, number + 1,2):
    sum_of_even_numbers += even
print(f'The sum is: {sum_of_even_numbers}')
