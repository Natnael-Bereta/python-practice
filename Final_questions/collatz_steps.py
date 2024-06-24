def count_collatz_steps(n):
    h = 0 #how much does the while loop run
    while n > 1:
        h += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
    
    return h


print(count_collatz_steps(6))