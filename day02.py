name=input("What is your name? ")
age=int(input("How old are you? "))
mass=float(input("What is your mass in kilograms? "))
height=float(input("What is your height in meters? "))
student_answer=input("Are you a student? (yes/no) ")
student=student_answer.lower()=="yes"
bmi=mass/height**2
print(f"Hello {name}")
print(f"You are {age} years old")
print(f"Your mass is {mass}kg")
print(f"Your height is {height}m")
print(f"You are a student: {student}")
print(f"Your BMI is {bmi:.2f}")
print(type(name))
print(type(age))
print(type(mass))
print(type(height))
print(type(student))
print(type(bmi))
rate=float(input("What is your hourly rate in dollars?"))
hours=float(input("How many hours do you work per day?"))
days=float(input("How many days do you work per week?"))
daily_income=rate*hours
weekly_income=daily_income*days
estimated_monthly_income=weekly_income*4.33
print(f"Your hourly rate is ${rate:.2f}")
print(f"Your daily income is ${daily_income:.2f}")
print(f"Your weekly income is ${weekly_income:.2f}")
print(f"Your estimated monthly income is ${estimated_monthly_income:.2f}")
