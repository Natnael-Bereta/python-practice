"""money = 159
lst = []
lst_money = []

while money > 0:
    a = money % 10
    lst.append(a)
    money //= 10

lst_money = lst[::-1]
print(f'You need:\n{lst_money[0]}-"100 birr notes" \n{lst_money[1]}- "10 birr notes" \n{lst_money[2]}- "1 birr notes"')
"""
def min_currency_notes(amount):
    # Available currency notes in descending order
    notes = [100, 50, 10, 5, 1]
    note_counts = {}
    
    # Calculate the number of each type of note needed
    for note in notes:
        if amount >= note:
            note_counts[note] = amount // note
            amount = amount % note
    
    # Print the results
    for note, count in note_counts.items():
        if count == 1:
            print(f"{count} note of {note} birr")
        else:
            print(f"{count} notes of {note} birr")

# Example usage
amount_to_spend = 2
min_currency_notes(amount_to_spend)
