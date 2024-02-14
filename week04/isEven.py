# This program will ask you to enter a number and it will tell you if the number is even or odd.
# Author: Hyojin Kim

userInput = int(input ("enter a number: "))

if (userInput % 2 == 0):
        print (f"{userInput} is evne number")
else: print (f"{userInput} is odd number")


# test booleans

is_alive = True
print (is_alive)

var = (2 != 4)
print (f"var is {var}")

logic = (2 <= 100) and ( 3 >= 100)
print (f"logic is {logic}")


# test if

c = 1
if c == 1:
        print ("I am true")
else: 
        print ("I am false")

print (c)