def sort_names_by_length(List):
    List.sort(key=len)
    return List


print(sort_names_by_length(['alice', 'bob', 'Natnael']))