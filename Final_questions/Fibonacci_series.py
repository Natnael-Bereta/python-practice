n = 10
fib_series = [0, 1]
for i in range(2, n):
    next_series = fib_series[i - 1] + fib_series[i -2]
    fib_series.append(next_series)

print(fib_series)