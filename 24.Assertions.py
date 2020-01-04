#check the 3 sections one by one using the comments. we cant compile the 3 types at a time bcs after giving an exception the program exits.

"""
An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
An expression is tested, and if the result comes up false, an exception is raised.
Assertions are carried out through use of the assert statement.
Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.
"""

#(i)
'''
print(1)
assert (2 + 2 == 4), "error spooted"
print(2)
assert 1 + 1 == 3
print(3)
'''

#(ii)
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))

#(iii) - assert inside the try except block
'''
try:
    temp = -10
    assert (temp >= 0), "Colder than absolute zero!"
except AssertionError:
    print ("Error Bypassed")
'''
