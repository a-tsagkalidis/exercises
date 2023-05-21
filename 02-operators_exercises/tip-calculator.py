print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give? 10, 12, or 15 percent?: "))
people = int(input("How many people to split the bill?: "))

tip = tip * 0.01 + 1
bill_with_tip = total_bill * tip
each_person_pay = bill_with_tip / people
#after the variable each_person_pay follows :.2f. That factor gives 2 decimal digits for the value of a floar number.
print(f"Each person sould pay: ${each_person_pay:.2f}")
