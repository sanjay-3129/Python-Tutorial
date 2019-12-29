#python numbers
a,b,c = 1,2,"san"
del b
b = 200
print (a)
print (b)
print (c)

# BUT NOTICE THE DIFFERENCE BELOW - Reassigning in order to change the values of that particulat variable:

a, b = 0, 1
a, b = b, a + b
print(a)
print(b)

#!/usr/bin/python   #single line comment
#podaaaa

import sys; x = 'foo'; sys.stdout.write(x + '\n') #multiple stmts on single line

a = "true"
true = "true"
if (a==true):
    print ("true")
else:
    print ("false")
''' haiii              #multi line comment
machiiii ok'''

if a=="ttrue":
    print ("hai")
elif a==true:
    print ("vankam")
else:
    print ("podaaa")

