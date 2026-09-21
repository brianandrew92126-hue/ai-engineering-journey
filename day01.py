name = input("What is your name? ")
mass = float(input("Enter mass of solute in grams: "))
volume = float(input("Enter solution volume in litres: "))

concentration = mass / volume

print(f"Hello {name}")
print(f"The concentration is {concentration} g/L")