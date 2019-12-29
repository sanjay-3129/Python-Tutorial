#boolean logic - and, or, not
a = str(input("Are you a girl or a boy ?\n"))
b = int(input("How old are you ?\n"))
if (a == "girl" and b >= 18) :
  print("Hello beautiful\n")
else :
  print("Goodbye !!\n")
  
print()

#or

a = int(input())
b = int(input())
if(a==1 or b==2):
	print("yes")
else:
	print("No")

print()

#not
a = int(input())
b = int(input())
if(not a==b):
	print("yes")
else:
	print("No")
