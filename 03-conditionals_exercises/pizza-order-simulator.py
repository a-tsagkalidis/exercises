from random import randint

delivery_time = randint(20, 60)
bill = 0

print("\nWelcome to Python Pizza Deliveries!")

user_size = input("What size of a pizza do you want? [Small $15 / Medium $20 / Large $25]: ").lower()
if user_size == "s" or user_size == "small":
    bill += 15
    size = "small"
elif user_size == "m" or user_size == "medium":
    bill += 20
    size = "medium"
elif user_size == "l" or user_size == "large":
    bill += 25
    size = "large"

user_pepperoni = input("Do you want pepperoni on your pizza? [Yes/No]: ").lower()
if user_pepperoni == "y" or user_pepperoni == "yes" and bill == 15:
    bill += 2
    print("That's an extra $2")
elif user_pepperoni == "y" or user_pepperoni == "yes" and bill >= 20:
    bill += 3
    print("That's an extra $3")

user_cheese = input("Do you want some extra cheese on you pizza for a +1$ [Yes/No]: ").lower()
if (user_cheese == "y" or user_cheese == "yes") and (user_pepperoni == "y" or user_pepperoni == "yes"):
    bill += 1
    print(f"\nYou have ordered a {size} pizza with pepperoni and extra cheese.")
    confirm = input("Confirm your order [Yes/No]: ").lower()
    if confirm == "y" or confirm == "yes":
        print(f"Your final bill is: ${bill}.\n")
elif user_cheese == "y" or user_cheese == "yes":
    bill += 1
    print(f"\nYou have ordered a {size} pizza with extra cheese.")
    confirm = input("Confirm your order [Yes/No]: ").lower()
    if confirm == "y" or confirm == "yes":
        print(f"Your final bill is: ${bill}.\n")
elif user_pepperoni == "y" or user_pepperoni == "yes":
    print(f"\nYou have ordered a {size} pizza with pepperoni.")
    confirm = input("Confirm your order [Yes/No]: ").lower()
    if confirm == "y" or confirm == "yes":
        print(f"Your final bill is: ${bill}.\n")
else:
    print(f"\nYou have ordered a {size} pizza.")
    confirm = input("Confirm your order [Yes/No]: ").lower()
    if confirm == "y" or confirm == "yes":
        print(f"Your final bill is: ${bill}.\n")

if delivery_time < 31:
    print(f"Your pizza will be delivered in about {delivery_time} minutes. Thank you for your order!")
elif delivery_time >= 31:
    print(f"Your order will be delivered in about {delivery_time} minutes due to many orders. Thank you for your understanding.")
