# 3. functions
# 3.1. function basics
print("~~~ 3.1. FUNCTION BASICS ~~~")
print(type(len)) # type of a built in function is builtin_function_or_method

import numpy as np
print(type(np.linspace)) # type of an imported function is function

def f1(a,b): # define a function with def; name only alphanumeric + underscores, and starts with a letter like variables
    """
    addition
    input: a, b
    output: a + b
    """ # text can be used for labelling and help with use
    c = a + b
    return c
print(f1(1,2)) # function inputs must all be of the correct types
#print(help(f1)) # help() prints the text inside the function

def f2(e,f):
    g = np.cos(e)**2
    h = (np.sin(f))**2
    return g, h, [g, h]
print(f2(1,5)) # functions can return multiple outputs

def f3():
    print(f"hello ^^")
f3() # even with no input argument, brackets are still required to call a function

def f4(variable = "k"):
    print(f"variable {variable}")
f4() # functions with inputs can be called without an argument when a default input is specified
f4("aaaa") # then, a value can be specified and called as expected

# 3.2. local & global varables
print("~~~ 3.2. LOCAL & GLOBAL VARIABLES ~~~")

def f5(a,b,c):
    out = a + b + c
    print(f"the value of out inside the function is {out}")
    return
out = 1 # an attempt to use a variable defined inside a function outside the function will yield an error
print(f"the value of out outside the function is {out}")
f5(1,2,3) # variables defined inside a function exist in a local system inside the function
print(f"{f5(1,2,3)} inside ≠ {out} outside!")

# 3.3. nested functions
print("~~~ 3.3. NESTED FUNCTIONS ~~~")
def dxyz(x,y,z):
    def dxy(x,y): # define a subfunction within another function
        q = np.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
        return q
    d0 = dxy(x,y)
    d1 = dxy(x,z)
    d2 = dxy(y,z)
    return [d0,d1,d2]
d = dxyz((1,1),(6,4),(2,5)) # calling the parent function necessarily calls the child function 
print(d) # the child does not exist outside its parent environment

# 3.4. lambda functions
print("~~~ 3.4. LAMBDA FUNCTIONS ~~~")
# lambda functions are a more abstract way of defining functions, originating in λ-calculus
# lambda functions are defined by f = lambda arguments : expression
f6 = lambda x, y : x**2 - y**2 # lambda functions can be more convenient for mathematical applications
print(f6(5, 2)) # lambda functions can be called like any other function

print(sorted([(1,2),(2,0),(4,1)], key = lambda x : x[0] + x[1])) # lambda functions can be used inside other functions

# 3.5. function composition
print("~~~ 3.5. FUNCTION COMPOSITION ~~~")
f7 = max # functions can be assigned custom names with variables
print(type(f7)) # type of function-variable is the type of its assignment

def f8(x):
    print(f7(x)+1)
f8([1,7,-8]) # functions can be composed inside other functions