expression = input("Input any expression: ")
try:
    evaluation = eval(expression)
    print(f'The answer is: {evaluation}')
except ZeroDivisionError:
    print("You can't divide by zero!")