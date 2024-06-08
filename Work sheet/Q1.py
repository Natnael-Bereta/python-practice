#cse = { "name" : ['Seid', 'Chala', 'Abenezer', 'Abel', 'Kebede','Mohammed'],
       
 #      "Sell": [10000,2000, 4000, 20000, 8000, 5000],
  #     "Percent":[0.05] , 
   #     "Fixed_salary" :[5000],
    #   }
#salary = fixed_salary
#for salary in cse:
 #   print(cse["Abel"])

cse = { 'Seid': [10000, 0.05, 5000], 
       'Chala': [2000, 0.05, 5000],
       'Abenezer': [4000, 0.05, 5000],
       'Abel': [20000, 0.05, 5000],
       'Kebede': [8000, 0.05, 5000],
       'Mohammed': [5000, 0.05, 5000]
       }

for info in cse.values():
    sell, percent, fixed_salary = info
    salary = fixed_salary + (sell * percent)
    info.append(salary)

print(f'Name    Total salry')

for name, value in cse.items():
    print(f'{name}    {value[-1]}')
    
