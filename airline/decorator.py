def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("hello, world")

hello()

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]



people.sort(key=lambda person:person["house"])

print(people)

import sys
x = int(input("x: "))
y = int(input("y: "))

try:
    result =x / y
except ZeroDivisionError:
    print("Error: Cannot divid by 0.")
    sys.exit(1)
    
print(f"{x}/{y} = {result}")