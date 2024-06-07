sandwich_orders = ['Club sandwich', 'grilled cheese', 'Reuben', 'Turkey sandwich']
finished_sandwiches = []
while sandwich_orders:
    ordered = sandwich_orders.pop()
    print("Making your " + str(ordered) + ".")

    finished_sandwiches.append(sandwich_orders)
print("\n")
for sandwich in finished_sandwiches:
    print("I made your " + str(ordered))
    
#print(finished_sandwiches)
#print(sandwich_orders)