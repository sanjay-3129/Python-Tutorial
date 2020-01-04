'''
The None object is used to represent the absence of a value.
It is similar to null in other programming languages.
Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable.
When entered at the Python console, it is displayed as the empty string.
'''
#(i)
print("Jus printing None:", None)    #None is a null value
print("When comparing two None: "+str(None==None)+"\n")
print("when comparing None with False:", (None==False)) #We notes that None is NoneType while False is BooleanType. So None==False returns False.
print("when comparing None with True:", (None==True))   ##We notes that None is NoneType while True is BooleanType. So None==False returns False.
print("Value of None:", bool(None))
if None:
    print("None got interpreted as True")
else:
    print("None got interpreted as False")

#(ii)
foo = ""
print("What?",foo);print()
'''Note: it says None is an empty value, and other empty values are empty strings("") and 0, not that they are equal.'''

#(iii) The None object is returned by any function that doesn't explicitly return anything else.
def some_func():
  print("Hi!")

var = some_func() #here it prints (Hi!) then the output,
print(var)        #output is None bcs we didnt use "return", to return the value. we are just printing it. so None displays.

#example:
foo = print()
if foo == None:
   print(1)
else:
   print(2)
print()
   
#example
hoo = ''                  #its having some empty string in it.
poo = print('any text')	  #it will display but poo will not have any value
foo = print()             #likewise in the above case, foo has no storage of any value
print(hoo == None)        #check the output
print(poo == None)
print(foo == None)
