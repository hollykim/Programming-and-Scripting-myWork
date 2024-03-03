# more messing with functions & flexible arguments
# author: Hyojin Kim

print (1,2,3, sep="", end="\t")
print ("Hi")

# unnamed args
def fun1 (*args):
        print(type(args))
        print (args)
        for val in args:
                print(val)

fun1 ("a", "b", "c")

# keyword arguments
def fun2(**kwargs):
        print (type(kwargs))
        print (kwargs)
        #for val in args:
        #       print (val1)

fun2 (name = "Joe", age = 30, gender = "Male")

# sample program that return average and sum of input.

def ave(*values):
        number_of_values = len (values)
        sum = 0
        for value in values: 
                sum += value
        avergae = sum / number_of_values
        return avergae , sum 

av1, sum_of_numbers = ave(1,2,3,4,5,6)
print (f"avg is {av1} and sum is {sum_of_numbers}")

