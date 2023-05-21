weight = int(input("\nPlace your weight in kg: "))
height = float(input("Place your height in m: "))

bmi = round(weight/(height**2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}. You're considered underweight.\n")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}. You have a normal weight.\n")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}. You're considered slightly overweight.\n")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}. You're considered obese.\n")
else:
    print(f"Your BMI is {bmi}. You're considered clinically obese.\n")
    