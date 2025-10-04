# 4. Branching statements

# 4.1. If-Else statements

def thermostat(temp,idtemp):
    if temp > idtemp + 2:
        s = "cooling"
    elif temp < idtemp - 2:
        s = "heating"
    else:
        s = "off"
    return s

# the general if-elif-else syntax is
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

print(thermostat(24,20))
print(thermostat(14,20))
print(thermostat(19,20))

# branching functions may also be assigned to variables
status = thermostat(16,20)
print(status)

# branching statements can be infinitely nested
def nested(x,y):
    if x > 0:
        if y > 0:
            print("++")
        else:
            print("+-")
    else:
        if y > 0:
            print("-+")
        else:
            print("--")

nested(1,1)
nested(1,-1)
nested(-1,1)
nested(-1,-1)

# logical functions exist to help build branching statements
import numpy as np
print(all([1,1,0])) # all() returns True only if all elements in an array are True
print(any([1,1,0])) # any() returns True if at least one element in an array is True

# 4.2. Ternary operators

# the basic ternary syntax is: variable = expression if condition else expression
isst = False
person = "student" if isst == True else "not student"
print(person)
isst = True
print(person)

# the operator is equivalent to the following piece of code:
# if isst == True:
#     person = "student"
# else:
#     person = "not student"