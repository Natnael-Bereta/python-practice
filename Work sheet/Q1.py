#cse = { "name" : ['Seid', 'Chala', 'Abenezer', 'Abel', 'Kebede','Mohammed'],
       
 #      "Sell": [10000,2000, 4000, 20000, 8000, 5000],
  #     "Percent":[0.05] , 
   #     "Fixed_salary" :[5000],
    #   }
#salary = fixed_salary
#for salary in cse:
 #   print(cse["Abel"])

cse = { 'Seid': [1000, 0.05, 5000], 
       'Chala': [2000, 0.05, 5000],
       'Abenezer': [4000, 0.05, 5000],
       'Abel': [20000, 0.05, 5000],
       'Kebede': [8000, 0.05, 5000],
       'Mohammed': [5000, 0.05, 5000]
       }
fixed_salary = cse.items()
sell = cse.items()
percent = cse.items()
salary = fixed_salary + (sell * percent)