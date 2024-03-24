# messing with Files
# Author: Hyojin Kim

# old way
# f = open ('workfile', 'wb+')
# f.write(b'01234')
# f.close()

FILENAME = "data.txt"

with open(FILENAME, 'rt') as f:
    #data = f)
    for data in f:
        #print (data, end="")
        print (data.strip())
        #print (data[:-1])


with open("data2.txt", "wt") as f:
    f.write("how now\n")
    f.write("brwon now")

print ("done")