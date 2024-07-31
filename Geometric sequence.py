def isGeometric(number_lst):
    if len(number_lst) < 2:
        return False
    first_ratio = number_lst[0]/number_lst[1]

    for i in range(1, len(number_lst)-1):
        current_ratio = number_lst[i]/number_lst[i+1]
    
    if current_ratio != first_ratio:
        return False
    return True
    

inpt = input(("Insert a list of numbers separated by comma to check weather it's Geometric sequence or not:  "))
string_list = inpt.split(",")
number_list = [int(num.strip()) for num in string_list]
print(isGeometric(number_list))