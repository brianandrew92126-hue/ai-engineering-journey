pH = float(input("Enter the pH value: "))
if pH < 0 or pH > 14:
    print("Invalid pH value. pH can only be between 0 and 14.")
elif pH < 7:
    print("The solution is acidic.")
elif pH == 7:
    print("The solution is neutral.")
else:
    print("The solution is basic.")

Hourly_rate = float(input("What hourly rate are you targeting? "))
if Hourly_rate < 0:
    print("Invalid hourly rate. Hourly rate cannot be negative.")
elif Hourly_rate < 20:
    print("This is the entry target.")
elif Hourly_rate < 50:
    print("Developing professional.")
elif Hourly_rate < 100:
    print("High income target.")
else:
    print("Specialist target.")
