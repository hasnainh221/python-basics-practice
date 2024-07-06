# variable and datatypes unpacklist
a=1
b=2

# STRING AND NUMARIC DATA TYPES
c="hasnain"
print(a,b,c,"haider")

# STRING NUMARIC AND FLOAT DATA TYPES
x=str(3)
y=int(3)
z=float(3)
print (x,y,z)

# TYPE FUNCTION (CHECK DATA TYPE)
print (type(a))
print (type(b))
print (type(z))

# UNPACKING CONCEPT
fruits = ["apple", "banana", "cherry", "mango"]
x, y, z, a = fruits
print(x,y,z,a)

# COMBINE THE STRING WITH + OPERATOR
l="hasnain "
m="is "
n="good"
print (l+m+n)

# COMPLEX DATA TYPE
k = complex(8, 2)

# BOOLEN DATA TYPE
b = True
print(k)
print(b)

# ADDITION FUCTION
a1 = 9
print(k + a1)

# DATA TYPE CHECK
print("The type of a is ", type(k))
print("The type of b is ", type(b))
print("The type of c is ", type(c))

# SEQUENCE DATA TYPE LIST
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1 )

# SEQUENCE DATA TYPE TUPLE
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

# MAPPED DATA TYPE DICTIONARY
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)

# GLOBAL VARIABLE
# 1ST EXAMPLE
F = "awesome"

def myfunc():
  print("Python is " + F)

myfunc()

# 2ND EXAMPLE
G = "awesome"

def myfunc():
  G = "fantastic"
  print("Python is " + G)

myfunc()

print("Python is " + G)

# 3RD EXAMPLE
def myfunc():
  global E
  E = "fantastic"

myfunc()

print("Python is " + E)

# 4TH EXAMPLE
P = "awesome"

def myfunc():
  global P
  P = "fantastic"

myfunc()

print("Python is " + P)