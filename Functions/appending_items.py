def add_items(items, item_list=[]):
    item_list.append(items)
    return item_list

flag = True
while flag:
    b = input("Add Items to the list: ")
    a = add_items(b)
    print(a)
    if b == "break":
        flag = False
