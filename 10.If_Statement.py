#if statement - indention is important that is the blank space after the if statement
a = 10
b = 20
if(a<b): print("one")

if(a<b):print("two")

if(a<b):
	print("three")
	c = a+b
	d = a/b
	print(c)
	print(d)
	if(a==10):
		print("vanakam")
	
print(c+d)

#nested if
num = int(input("enter something but number: "))
if num > 5:
   print("Bigger than 5")
   if num <=47:
      print("Between 5 and 47")

#test
num = 7
if num > 3:
   print("3")
   if num < 5:     #this one fails so it doesnt goes to next if statement
      print("5")
      if num ==7:
         print("7")
