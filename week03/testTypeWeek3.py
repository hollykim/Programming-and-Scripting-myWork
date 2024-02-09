# meessing with variable types
# aythor: Hyojin Kim

answer = 12
print (f"answer is {answer}")
print (answer)
#print ("The answer is " + answer)
print ("The answer is " + str(answer))
print (f"type of answer is {type(answer)}") #print type 


i = 3
fl = 3.5
isa = True
memo = "Hello there"
lots = []

print('variable {} is of type:{} and value:{}'.format('i', type(i), i))
print('variable {} is of type:{} and value:{}'.format('fl', type(fl), fl))
print('variable {} is of type:{} and value:{}'.format('is', type(isa), isa))
print('variable {} is of type:{} and value:{}'.format('memo', type(memo), memo))
print('variable {} is of type:{} and value:{}'.format('lots', type(lots), lots))

# sub.py
# x = int(input ("Enther the frist number: "))
# y = int(input ("Enther the second number: "))
# z = x - y
# print (f"{x} - {y} = {z}")

# print ("{} minus {} is {}".format(x,y,z))


# div.py
x1 = int(input ("Enther the frist number: "))
y1 = int(input ("Enther the second number: "))
z1 = x1//y1
remainder = x1 % y1
print ("{} divided by {} is {} and remainder is {}".format(x1,y1,z1,remainder))

#program that prints a random number between 1 to 10

import random
number = random.randint(1,10)
print("here is a random number {}".format(number))
