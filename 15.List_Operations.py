#List Operations
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)
print()

#b = a -> this doesn't copy list a into variable b, but treats b as a pointer (synonym) for a
a = ['x' , 'y']
b = a
b[0] = 'z'
print(b) #output: ['z' , 'y'] no surprise
print(a) #!!!output!!!: ['z' , 'y']
print()

#copy() method.
a = ['a','b']
b = a.copy()
b[1] = 'c'
print(a)
print(b)
print()

#added and multiplied  as strings
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)
print()

#Difference btw List and Split
s ='i love humanity'
a =list(s)
print (a)
#output : ['i', ' ', 'l', 'o', 'v', 'e', ' ', 'h', 'u', 'm', 'a', 'n', 'i', 't', 'y']

s ='i love humanity'.split()
print (s)
#output : ['i', 'love', 'humanity']
print()

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
print()

print("hello" in "hello world")
print()

nums = [1, [4,5], 2, 3]
print(4 in nums)
print(5 in nums)
print([4,5] in nums)
print(4 in nums[1])
