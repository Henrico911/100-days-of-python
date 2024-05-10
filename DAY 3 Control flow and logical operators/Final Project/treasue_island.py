print("Welcome To Treasure Island")
print("Your mission is to find the treasure")

choice1 = input("You are at a cross road, Where do you want go? Type <left> or <right>: ").lower()

if choice1 == "left":
    choice2 = input("You come to a lake. There's an island in the middle of the lake. Type <wait> to wait for a boat. Type <swim> to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with three (3) doors. One RED, one YELLOW and one BLUE. Which colour do you choose?: ").lower()
        if choice3 == "red":
            print("Its a room full of fire. Game over")
        elif choice3 == "yellow":
            print("-----YOU - FOUND - THE - TREASURE. YOU - WIN!-----")
        elif choice3 == "blue":
            print("You entered a room full of beasts. Game over")
        else:
            print("You chose a room that doesn't exist. Game over")
    else:
        print("You got attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game Over.")
