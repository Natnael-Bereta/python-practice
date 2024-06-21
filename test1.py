"""def remove_duplicate(input_list):
    no_duplicate = []
    for l in input_list:
        if l not in no_duplicate:
            no_duplicate.append(l)
    return no_duplicate



def remove_duplicate(input_list):
    no_duplicate = []
    seen = set()
    for l in input_list:
        if l not in seen:
            no_duplicate.append(l)
            seen.add(l)
    return no_duplicate"""


def sort_names_by_length(List):
    List.sort(key=len)
    return List


print(sort_names_by_length(['alice', 'bob', 'Natnael']))