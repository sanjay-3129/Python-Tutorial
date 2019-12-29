#List
words = ["hai","2",10]
for i in range(0,3):
	print(words[i])
print()

#eg 1	
words = ["Hello", 4, "world", 3]
i = 0
while i < len(words):
    # function str(element) --> read the data type of element like a string
    # function type(element) --> return the element's data type
    print("position: ", str(i), "element: ", words[i], "--> data type:", str(type(words[i])))
    i += 1
print()

#empty list
a = []
print(a)

#Nested List
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])
print(things[2][0])
print()

#String Indexing
str = "Hello world!"
print(str[5],str[6])

words = "I love learning Python using Sololearn!".split()
print(words)
