#List Functions
#1. append(), insert()
nums = [1, 2, 3]
nums.append(4)
nums += [5]
nums.insert(5,6)
print(nums)
print()

#2. List having a sublist
nums = [1,2,3,4]
nums[1] = [nums[1]]  #This turns item 2 into a list
nums[1].append(20)  #This adds the item 20 to the sublist
print(nums)
print()

#3. extend()
nums = [10,9,8,7,6,5]
nums.extend([4,3,2,1])
print(nums)

nums = [10,9,8,7,6,5]
nums.append([4,3,2,1])
print(nums)

nums = [10,9,8,7,6,5]
nums += [4,3,2,1]
print(nums)
print()

#4. len()
print(len(nums))
nums = [1, 2, 3,[1,2,3], 4, 5, 6]
print(len(nums[3]))
print()

#5. insert()
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
print()

#6. remove()
name = ["san","kum",12,24]
name.remove(24)
print("remove method : "+str(name))
print()

#7. index()
letters = ['a','b','c','d']
print("index value : "+str(letters.index('a')))
print()

#8. max()
n = [100,2,3,4,5]
print(max(n))
print()

#9. min()
n = [100,2,3,4,5]
print(min(n))
print()

#10. count()
letters = ['a','b','c','d','a']
print(letters.count('a'))
print()

#11. reverse()
letters = ['a','b','c','d']
print(letters)
letters1 = letters.copy()
letters1.reverse()
print(letters1)
print()
