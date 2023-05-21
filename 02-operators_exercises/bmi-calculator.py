weight = int(input("\nPlease enter your weight in kg: "))
height = float(input("Please enter your height in m: "))

bmi = weight / (height**2)

print(f"Your BMI equals to {round(bmi)}\n")
