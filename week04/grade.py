# this program will read in a student’s percentage mark and print out corresponding the grade
# Author: Hyojin Kim

percentage = int(input ("Enter your percentage: "))
print (f"Your percentage is {percentage}")

if percentage >= 0 and percentage <= 100: 
    if percentage < 40:
        print ("Fail")
    elif percentage < 50: 
        print ("Pass")
    elif percentage < 60:
        print ("Merit 2")
    elif percentage < 70:
        print ("Mergit 1")
    elif percentage >= 70:
        print ("Distinction")
else: 
    print ("Error! Enter the percetage between 0 to 100")
