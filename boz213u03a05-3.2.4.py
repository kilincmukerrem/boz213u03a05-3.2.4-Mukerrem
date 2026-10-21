secret_number = 777
print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer nımber        |
| and guess what I've            |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Your Guess:"))
             
while (number != secret_number):
    print("WRONG you miserable muggle! \nHA HA HA! You're stuck in my loop!")
    number = int(input("Your Guess:"))


print("How!? Well done, muggle! You are free now.")
