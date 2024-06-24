def remove_duplicate(input_list):
    no_duplicate = []
    for l in input_list:
        if l not in no_duplicate:
            no_duplicate.append(l)
    return no_duplicate



