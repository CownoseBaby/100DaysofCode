# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Len prints # of items starting at 0: Items in list is 4
num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person_buying = names [random_choice]

print(person_buying + " is buying the meal today!")

# random.randint(0, x)