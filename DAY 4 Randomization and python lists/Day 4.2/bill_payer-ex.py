# import random

# name_string = input("Give me evrybody's name, separated by a comma: ")
# names = name_string.split(", ")

# random_name = random.choice(names)

# print(names)
# print(f"{random_name} is going to buy the meal today")

#--------the above code worked-------------------#



import random

name_string = input("Give me evrybody's name, separated by a comma: ")
names = name_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items -1)
bill_payer = names[random_choice]

print(f"{bill_payer} is going to pay for the meal today")