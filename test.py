def fibonacci(n):
  if n < 0:
    return None
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage
number = 6
for i in range(number):
  print(fibonacci(i))

def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    yield a
    a, b = b, a + b

# Example usage
number = 10
for num in fibonacci(number):
  print(num)

