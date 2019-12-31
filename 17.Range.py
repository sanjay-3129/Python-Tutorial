#(i)range -creates sequential list of numbers
a = list(range(10))
print(a)

b = tuple(range(10))
print(b)

#another method for reversing the list or tuple
for a in reversed(range(10)):
	print (a)
"""
b = int(range(10))
print(b)
"""      


#(ii) - two arguments
c = list(range(0,10))
print(c)
c_rev = list(range(10,0))  #with two arguments we cannot reverse so it will give empty list
print(c_rev)  # output: []



#(iii) - three arguments
#ascending
d = list(range(0,10,2))   #  range(beginning_value, ending value, increment counter)
print(d)

#decesending
d_rev = list(range(10,0,-2))
print(d_rev)

#operators in 3rd argument
numbers = list(range(5, 20, 4//2))
print(numbers)

#when the first argument is higher and second is lower, the 3rd argument must be negative like this:

numbers = list(range(5, -5, -2))
print(numbers)

