#if_else statements
a = 10
b = 15
if a+b==25:
	print("true")
else:
	print("false")

print()

#nested if_else
num = 7
if num == 5:
  print("Number is 5")
else: 
  if num == 11:
    print("Number is 11")
  else:
    if num == 7:
      print("Number is 7")
    else: 
      print("Number isn't 5, 11 or 7")

#elif stmts
num = 7
if num == 5:
   print("Number is 5")
elif num == 11:
   print("Number is 11")
elif num == 7:
   print("Number is 7")
else:
   print("Number isn't 5, 11 or 7")
