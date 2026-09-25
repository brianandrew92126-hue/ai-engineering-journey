password = " "
while password != "chemistry123":
    password = input("Enter password: ")
    if password != "chemistry123":
        print("Incorrect password. Please try again.")
    else:
        print("Access granted.")
#challenge 1
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")


#challenge 2
while True:
    try:
        pH = float(input("Enter the pH value: "))
    except ValueError:
        print("Invalid input. Please enter a number for pH.")
        continue
    if pH < 0 or pH > 14:
        print(f"Invalid pH value. pH can only be between 0 and 14.")
    elif pH < 7:
        print("The solution is acidic.")
    elif pH > 7:
        print("The solution is basic.")
    else:
        print("The solution is neutral.")
    while True:
        answer = input("Do you want to test another pH value? (yes/no): ").strip().lower()
        if answer == "yes":
            break
        elif answer == "no":
            print("program ended.")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            


