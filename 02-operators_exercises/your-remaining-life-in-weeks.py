age = int(input("\nEnter your age in years: "))
months = age * 12
weeks = age * 52
days = age * 365

rem_months = 90*12 - months
rem_weeks = 90*52 - weeks
rem_days = 90*365 - days

print(f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left, if you'll live for 90 years.\n")
