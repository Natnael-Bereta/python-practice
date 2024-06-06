pets = [{"Owner name": "Natty",
         "Animal type": "Dog"},
        {"Owner name": "Beki",
         "Animal type": "Cat"},
        {"Owner name": "Lemi",
         "Animal type": "Bird"}]

for pet in pets:
  # Access 'Animal type' directly to print pet name
  print(f"Pet: {pet['Animal type']}")
  # Alternatively, use loop to iterate through all key-value pairs
  # for key, value in pet.items():
  #   print(f"{key}: {value}")
