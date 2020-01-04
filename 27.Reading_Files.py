#(i)reading the file and printing all its content
myFile = open("D:\\Python\\Test_File.txt",'r')
data = myFile.read()
print(data)
myFile.close()
print()

#(ii)reading file with arguments
data = open("D:\\Python\\Test_File.txt",'r')
print(data.read(10));print()
print(data.read(40));print()  # it continues from where it Left off
print(data.read(0));print()   #it will print nothing but a empty space
print(data.read(-1));print()  #read(-1) - will read the remaining values from already read file.
data.close()

#(iii)(a)reading each line in a file and outputs into "list"
file = open("D:\\Python\\Test_File.txt", "r")
print(file.readlines())
file.close()
print()

'''
Q: how the below script knows that we are iterating over lines? 
A: Python automatically reads files by lines. It reads text by characters.
So if we were to say text = file.read() first and then put text in the for loop instead, it would go by character, which is what you'll often want to do
As the file is in the for loop, however, Python reads it line by line.
'''

#(iii)(b) - see the difference well
#ex1 - reading by line
try:
    file = open("D:\\Python\\Test_File.txt", "r")
    for line in file:
        print(line)
finally:
    file.close()

#ex2 - reading by char
try: 
    file = open("D:\\Python\\Test_File.txt", "r")
    txt = file.read()
    for char in txt:
        print(char)
finally:
    file.close()
