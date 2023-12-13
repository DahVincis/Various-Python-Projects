# Import the Pet class from pet.py
from pet import Pet

# Open the text file and read the data
with open('petdata.txt') as file:
    lines = file.readlines()

# Create a list of Pet objects
pets = []
for line in lines:
    data = line.strip().split(',')
    if len(data) < 3:
        print(f"Skipping line: {line}")
    else:
        pet = Pet(data[0], data[1], data[2])
        pets.append(pet)

# Output the content of the Pet objects
for pet in pets:
    print(pet)

# Find owners with snake and insect family type pets
snakeOwn = set()
insectOwn = set()
for pet in pets:
    if pet.get_family_type() == 'snake':
        snakeOwn.add(pet.get_owner())
    elif pet.get_family_type() == 'insect':
        insectOwn.add(pet.get_owner())

# Output the names of owners with snake and insect family type pets
print("Owners with snake family type pets:")
for own in snakeOwn:
    print(own)

print("Owners with insect family type pets:")
for own in insectOwn:
    print(own)