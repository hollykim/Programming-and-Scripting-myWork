# messing with functions
# resource: https://docs.python.org/3/library/functions.html
# author: Hoyjin Kim


def adding (a, b):
    c = a + b
    return print (c) 

adding (1,2)

x = lambda a : a * 100
print (x (2))

y, z = (3, 5)
print (y, z)
print (y, z , sep="") # No space between y and z
print (y, z , end="") # No new line between line 16 and 17. No new line for the next code
print (f"{y} & {z}")
print ("{} + {}".format(y,z))

def cube (number):
    print (number)
    return (number * 2)

ans = cube (77)
print (f"we got {ans}")