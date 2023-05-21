print("\nWelcome to the Love Calculator!")
your_name = input("What's your name?\n").lower()
their_name = input("What's their name?\n").lower()

t = your_name.count("t") + their_name.count("t")
r = your_name.count("r") + their_name.count("r")
u = your_name.count("u") + their_name.count("u")
e = your_name.count("e") + their_name.count("e")

l = your_name.count("l") + their_name.count("l")
o = your_name.count("o") + their_name.count("o")
v = your_name.count("v") + their_name.count("v")

true_score = str(t + r + u + e)
love_score = str(l + o + v + e)

total_score = int(true_score + love_score)

if total_score < 10 or total_score > 90:
    print(f"\nYour score is {total_score}, you go together like coke and mentos.\n")
elif total_score > 40 and total_score < 50:
    print(f"\nYour score is {total_score}, you're alright together.\n")
else:
    print(f"\nYour score is {total_score}.\n")
