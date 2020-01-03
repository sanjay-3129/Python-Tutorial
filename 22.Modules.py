#(i)importing a module
import random
for i in range(10):
	value = random.randint(1,6)	
	print(value)
	
#(i)(a)
import math
print(math.pi)

#(ii) - for specific module object
from math import pi
print(pi)

#(iii) - to import multiple objects
from math import pi,sqrt
print(str(sqrt(4))+" ---- "+str(pi))

#(iv) - to import all objects from a module
from math import *
print(max(10,20))

#(v) - naming the module object with different name
from math import sqrt as square_root
print(square_root(100))

print(help(math))  #it will help to display the full module objects in the shell

#www.python.org - for documentation purpose of every modules
