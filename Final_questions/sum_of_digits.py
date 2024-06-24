def add_number(n):
    sum_ = 0
    while n > 0:
        temp = n % 10
        sum_ += temp
        n = n // 10
    return sum_


print(add_number(123)) 