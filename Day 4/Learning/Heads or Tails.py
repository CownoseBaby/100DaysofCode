# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

print("Welcome to the Heads and Tails")

random_side = random.randint(1, 2)

if random_side == 1:
    print("Heads")
else:
    print("Tails")
