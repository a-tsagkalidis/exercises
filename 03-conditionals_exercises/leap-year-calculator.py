program_is_on = True

while program_is_on == True:
    year = int(input("\nSelect a year and I'll check if it is a leap year.\nWrite down your selection: "))

    if year % 4 == 0:
        print("Leap year")
    elif year % 200 == 0:
        print("Not a leap year")
    elif year % 400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
