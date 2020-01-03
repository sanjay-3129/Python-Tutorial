"""
Functions can be assigned and reassigned to variables and later referenced by those names.
"""
#(i)
def multiply(a,b):
	return a*b
opr = multiply
print(opr(5,6))

#(ii)
def multiply(a,b):
	return a*b
opr = multiply(5,6)
print(opr)

#(iii) - functions can also be used as arguments of other functions
def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))
