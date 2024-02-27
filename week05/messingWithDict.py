# messing with dictionaries
# Author: Hyojin Kim

car = {
    "make" : "ford",
    "model" : "modeo",
    "year" : 2020,
    "owner" : {
        "name" : "Hyojin",
        "driver-number" : 1234
        }
}

print(car)
print (car["owner"])
print (car["owner"].get("name"))
print (type(car["owner"].get("name")))


# loop

for key in car:
    print(key, "has value", car[key])


for key, value in car.items():
    print(key, "has value", value)