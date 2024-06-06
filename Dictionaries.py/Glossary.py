glossary = {"Variable": 'Named box holding data (numbers, text, etc.)',
            "Data type": 'Kind of data a variable can store (numbers, text, True/False, etc.)',
            "Function": ' Reusable code block for specific tasks (takes inputs, returns outputs)',
            "Loop": 'Repeats code until a condition is met (for loops iterate over sequences, while loops repeat based on a condition)',
            "List": 'Ordered collection of items of any data type (access and modify items using indexing)'}
print("Some python terms with their definition.\n")
for term, definition in glossary.items():
    print(f'{term}:\n-{definition}\n')
