weight = int(input("Insert weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() =="K" :
    converted = weight // 0.45
    print("Weight in Lbs is: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs is : " + str(converted))