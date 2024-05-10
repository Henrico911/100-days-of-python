print("Welcome to the Love Calculator")

name1 = input("What is your name?\t")
name2 = input("What is their name?\t")

combined_name = name1 + name2
lower_case_combined_name = combined_name.lower()

t= lower_case_combined_name.count("t")
r= lower_case_combined_name.count("r")
u= lower_case_combined_name.count("u")
e= lower_case_combined_name.count("e")
true = t + r + u + e

l= lower_case_combined_name.count("l")
o= lower_case_combined_name.count("o")
v= lower_case_combined_name.count("v")
e= lower_case_combined_name.count("e")
love = l + o + v + e

love_score = str(int(true)) + str(int(love))



if (int(love_score) < 10) or (int(love_score) > 90):
    print(f"Your love score is {int(love_score)}, you go together like coke and mentos")
elif (int(love_score) >= 40) and (int(love_score) <= 50):
    print(f"Your love score is {int(love_score)}, you are alright together")
else:
    print(f"Your love score is {str(int(love_score))}")

# print(love_score)