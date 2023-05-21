continuity = True

while continuity == True:
    print("\nEnter a number and the program can tell if it's an even or an odd number.")
    number = float(input("Place your number here: "))

    if number % 2 > 0:
        print("This is an odd number.\n")
    else:
        print("This is an even number.\n")
        