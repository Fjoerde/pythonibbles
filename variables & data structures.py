# 2. variables and data structures
# 2.1. variable assignment
print("~~~ 2.1. VARIABLE ASSIGNMENT ~~~") # print() outputs text

x = 1
y = x + 1
print(x,y)

print(type(x)) # type() outputs the data type of a given variable
print(type(y)) # type of an integer is int

# 2.2. string data structure
print("~~~ 2.2. STRING DATA STRUCTURE ~~~")

h = "hello world"
print(h)

s = "string"
print(s)
print(type(s))
len(s) # len() gives the length of a string

empty = ""
print(type(empty)) # type of empty string is still a string
print(len(empty)) # length of empty string is zero

print(s[1]) # strings can be decomposed as vectors of characters, and indices start from 0
print(s[0:3],h[6:]) # range of characters with :, not inclusive for endpoints!
print(h[0:9:2]) # add step on the end
print(h[::2]) # retrieve every other character
print(h[6:-2]) # slice substrings from the end of the string with -, where -1 in the end point is the last character, etc.

print("..." + h) # concatenate strings directly with +

print(h.upper()) # uppercase, lowercase with .lower() works the same
print(h.replace("world","london")) # .replace() replaces parts of the strings with others

uni = "imperial"
dept = "physics"
country = "the uk"
print("%s has the best %s department in %s"%(uni, dept, country)) # pre-format a string with some variables
print(f"{uni} has the best {dept} department in {country}") # new pre-formatting since python 3.6
print(f"thus two squared is {2*2}.") # formatted string without needing to convert the data type even

# 2.3. list data structure
print("~~~ 2.3. LIST DATA STRUCTURE ~~~")

l1 = [1, 2, 3] # list created with []
print(l1)
l2 = ["a", "b", "c"]
l3 = l1 + l2 # concatenate lists with + irrespective of element type
print(l3)
l4 = [l1, l2] # lists can hold other lists
print(l4)

print(l1[0] + l1[2]) # use indices starting from zero to retrieve list elements
print(l4[0][1]) # use multiple sets of brackets for nested list elements
print(l3[:3], l3[-1]) # indices function as expected like with strings for ranges and final elements

print(len(l1), len(l4), len(l4[0])) # len() returns length of the list

l1.append(4) # .append() adds an element to the end of a list
l1.insert(2, "i") # .insert() adds an element inside a list and shifts the following ones to the right
l1.remove(3) # .remove() removes an element from a list
del l1[0] # del does the same as remove
print(l1)

l5 = []
print(len(l5)) # empty list has length zero
l5.append(5)
check = 5 in l5 # in is a boolean operation checking whether an element is in a list
print(type(check)) # type of the output of in is bool

lh = list(h) # list() turns a string or other sequenced items into a list of characters
print(lh)

# 2.4. tuple data structure
print("~~~ 2.4. TUPLE DATA STRUCTURE ~~~")

t1 = (1, 2, 3, 2) # tuple created with () is essentially an immutable list
print(t1)
print(t1.count(2)) # .count() counts the occurrence of a given element

a, b, c, d = t1 # assignment for tuples works when both sides of = have the same number of elements
print(a, b, c, d) 
t2 = 4, 3, 2, 3 # tuples don't specifically need () but better to have them
print(t2)

t3 = (("a", 1), ("b", 2), ("c", 3)) # tuples typically contain heterogeneous collections, where items have different types
print(t3)

# 2.5. set data structure
print("~~~ 2.5. SET DATA STRUCTURE ~~~")

s1 = {1, 1, 2, 3, 4, 3, 6, 5, 2, 5, 5, 6, 6, 5} # set created with {} is 
print(s1)

sh = set(lh) # set() forms a set of the unique elements of a list or a tuple
print(sh)

s2 = {4, 5, 5, 6, 5, 6, 7, 8, 8, 9}
print(s1.union(s2)) # .union() functions as mathematical union
print(s1.intersection(s2)) # .intersection() functions as mathematical intersection
s3 = {2, 2, 3,}
print(s3.issubset(s1)) # .issubset() checks for whether a set is a subset of another set
print(s3.issubset(s2))

# 2.6. dictionary data structure
print("~~~ 2.6. DICTIONARY DATA STRUCTURE ~~~")

d1 = {"a":1, "b":2, "c":3} # dictionary formed with {} is a set of key:value pairs
print(d1["a"]) # retrieve value for a given key using the key as an index

print(d1.keys()) # .keys() returns all keys for the dictionary
print(d1.values()) # .values() returns all values for the dictionary

d2 = {"imperial":"uk", "ethz":"switzerland", "hku":"hong kong", "ubc":"canada"}
print(list(d2)) # list() on a dictionary returns a list of all keys for the dictionary

print("imperial" in d2) # in and not in can be used to check whether keys are in the dictionary
print("tsinghua" not in d2)

d2["tsinghua"] = "china" # append an element to a dictionary by using the key as an index and assigning it a value
print(d2) # output the dictionary as key:value pairs

d3 = dict([("uk", "europe"), ("japan", "asia"), ("canada", "north america"), ("nigeria", "africa")]) # dict([]) forms a dictionary from a list of tuples
print(d3)

# 2.7. numpy arrays
print("~~~ 2.7. NUMPY ARRAYS ~~~")

import numpy as np # when using the numpy package, always import it at the start of the programme, and call it np by convention
# package management is a pain, so if you have trouble see if you are using the correct environment or interpreter; the book recommends miniconda
X = np.array([1, 4, 3]) # create a vector or other array from a list with np.array()
Y = np.array([[1, 4, 3], [9, 2, 7]]) # create matrices as a list of rows
print(X) # vectors are printed as rows
print(Y) # arrays are printed with each new row on a new line

print(X.shape, Y.shape) # .shape gives the number of rows and columns in the array as (r, c)
# for vectors like X, .shape gives the dimension n of the vector as (n,)
print(X.size, Y.size) # .size gives the number of elements in the array

A = np.arange(1, 2000, 1) # .arange() defines a vector of a numerical range with a startpoint, exclusive endpoint, and step (defaults to 1 if unspecified)
B = np.linspace(0, 100, 41) # .linspace() defines a vector range between a startpoint, inclusive endpoint, and exact number of elements
print(A)
print(B)

print(X[1], Y[1,0]) # use indices as [i] for vectors and [i,j] for matrices
print(Y[1,:], Y[:,1]) # retrieve specific rows and columns using : as the index
print(Y[:,[0,2]]) # retrieve several columns or rows at once using lists of indices

C = np.zeros((3,5)) # .zeros() generates an array of zeroes
D = np.empty((4,4)) # .empty() generates an array of random very small but nonzero values hence can be faster
E = np.ones((5,3)) # .ones() generates an array of ones
print(C)
print(D)
print(E)

F = Y*5-2 # arithmetic operators apply to values individually
G = (Y**2)/4+9 # using ** to square a matrix squares the values, not the matrix
print(G)

H = np.array([[3,8],[5,2]])
I = np.array([[1,2],[3,4]])
print(H+I,"\n",H-I) # matrix addition and subtraction are elementwise
print(H*I) # multiplying matrices with * computes a hadamard (elementwise) product
print(np.multiply(H,I)) # .multiply() also computes a hadamard (elementwise) product
HI = np.matmul(H,I) # .matmul() computes a matrix product
print(HI)
print(H@I) # @ also computes a matrix product

J = np.array([1, 2, 3])
K = np.array([4, 5, 6])
JK = np.dot(J,K) # .dot() outputs the dot (inner) product of vectors
print(JK)
print(np.dot(H,I)) # .dot() with two non-vector matrices outputs a matrix product like .matmul(), but .matmul() is often preferred

L = HI.T # .T forms the transpose of the matrix
print(L)

print(H>I) # compare elements of two arrays
M = np.array([1, 6, 7, 2, 3])
N = np.array([6, 5, 3, 8, 9])
O = M[M>3] # filter elements that fit a given constraint
P = N[N>M] # form arrays by comparing elementwise between matrices
print(O)
print(P)