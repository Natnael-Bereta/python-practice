b = 2
def calc():
    for a in range(1,20,4):
       if a%b == 0:
         print(a*a)
       else:
          print(a*b)
calc()
    