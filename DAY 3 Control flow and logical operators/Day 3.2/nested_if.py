print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can hide the rollercoaster")
    age = int(input("What is your age: "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age <= 25:
        print("You are old enough to pay $12. Idiot")
    else:
        print("You are too old for the rollercoaster, motherf**ker")
else:
    print("Sorry, you have to grow taller before you can ride.")
    print("Thank you")
    