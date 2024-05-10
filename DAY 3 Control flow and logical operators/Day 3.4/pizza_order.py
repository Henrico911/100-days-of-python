print("Welcome to the Python Pizza Deliveries!")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepp_small = 2
pepp_medium = 3
pepp_large = 3

cheese = 1

print("<------MENU------>")
print("==================================")
print(f"Small Pizza: ${small_pizza}")
print(f"Medium Pizza: ${medium_pizza}")
print(f"Large Pizza: ${large_pizza}")
print("\n")
print(f"Pepperoni for small Pizza: + ${pepp_small}")
print(f"Pepperoni for medium Pizza: + ${pepp_medium}")
print(f"Pepperoni for large Pizza: + ${pepp_large}")
print(f"Extra cheese for any size pizza: + ${cheese}")
print("\n")

size = input("What size of pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


if size == "S":
    bill = small_pizza = 15
elif size == "M":
    bill = medium_pizza = 20
elif size == "L":
    bill = large_pizza = 25
else:
    print("Please enter a size")
    
    
if add_pepperoni == "Y":
    if size == "S":
        bill = small_pizza + 2
    else:
        bill = medium_pizza + 3
        bill = large_pizza + 3
        
if extra_cheese == "Y":
    bill = small_pizza + 1
    bill = medium_pizza + 1
    bill = large_pizza + 1
    
print(f"Your final bill is ${bill}")