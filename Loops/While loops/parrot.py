prompt = "Tell me something and I will repeat it back to you!"
prompt += "\nEnter 'quit' if you want to stop. "
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)
