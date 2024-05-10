# -----Body Max Index Calculator
weight = input("enter your weight in kg: ")
height = input("enter your height in meters: ")

b_m_i = int(weight) / (float(height) ** 2)

print("your Body Mass Index is : " + str(int(b_m_i)))