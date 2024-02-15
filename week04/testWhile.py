# This is my mess to test while loop 
# Author: Hyojin Kim

# counter controlled loop 
count = 0
while (count < 5):
    print ("count is ", count)
    count += 1
print ("At the end, count is ", count)

count = 10
while count >= 0:
    print  ("countdown ", count)
    count -= 1
print ("blast off")


# sentinal controled loop 
val = input ("type something (q to quit): ")
while val != "q":
    print ("Hello")
    val = input ("q t quit: ")

print ("all done")