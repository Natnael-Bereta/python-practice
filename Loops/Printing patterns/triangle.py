"""n = 5
for i in range(1, n+1):
    print('*' * i, end)"""

#OR

n = 5
for i in range(1, n+1): #row
    for j in range(1, i+1): #column
        print("*", end =" ") #The end=" " argument ensures that the next print statement does not move to a new line but continues on the same line.
    print() #This prints a newline character, moving the cursor to the next line after the inner loop completes. This ensures that each row of asterisks is printed on a new line.