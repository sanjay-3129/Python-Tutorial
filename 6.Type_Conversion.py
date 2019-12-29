#Type Conversion
print("2"+"3")

print(int("2")+int("3"))

print(int(2) + 5.0)

print(float("2.0") + 5)

print(str(2)+str(3))

print()
print("5" + "5")	
print((int("5") + int("5")) * 10)
print(int("5") + int("5") * 10)
print(int("5" + "5") * 10 )
print(("5" + "5") * 10 )

print()
print("2" + "2")

print(1 + int('2') + 3 + int('4'))

print(str(5)+ '6'+ str(7))

print ("8" "9")

print("8" + "9")

print("8","9")

print ("4" *5)

print()
print(float(input("Enter a number: ")) + float(input("Enter another number: ")))

#If the input type is not specified, Python treats it as a string:

print((input("Enter a number: ")) + (input("Enter another number: ")))
# user enters 42 and 2
# output: 422

print(float("210" * int(input("Enter a number:" ))))


#example-0
name = 'sanjay'
age = 21
print('%s is my name and %d is my age.' %(name, age))

#example-1
a1 = input()
b1 = input()
print(int(a1)+ int(b1) + 10)

#example-2
a2 = int(input())
b2 = int(input())
print(a2+b2)

#example-3
a3 = chr(int(input())) 
b3 = chr(int(input()))
print(a3+b3)
print(ord(a3)+ord(b3)) #convert char to number
