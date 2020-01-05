#When a file is opened in write mode, the file's existing content is deleted.
file = open("newfile.txt",'w')      #if there is no file then a new file will be created. Check your current directory where you saved ur python file.
msg = input(); print()              
abd = file.write(msg)
print(abd)      #printing of write method will return the no. of bytes written to a file, if successful.
file.close()

file = open("newfile.txt",'r')
txt = file.read()
print(txt)      #prints the content that is present inside the file.
file.close()
print()

'''
It is good practice to avoid wasting resources by making sure that 
files are always closed after they have been used. One way of doing this is to use try and finally.
'''
#opening the file using try finally is a good practice
try:
   f = open("file.txt")
   print(f.read())
except FileNotFoundError:
	print("no such file or directory")
finally:
	try:
	   f.close()
	except:
		print("cant close file")
print()
		
#The file is automatically closed at the end of the with statement, even if exceptions occur within it.
with open("newfile.txt") as f:
   print(f.read())
print()

#example
try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)
