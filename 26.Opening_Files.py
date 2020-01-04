#(i) - opening a file with read mode
myFile = open("D:\\Python\\Test_File.txt",'r')
data = myFile.read()
print(data)
myFile.close()      #close() - Once a file has been opened and used, you should close it.

#(ii)binary read mode
img = "C:\\Users\\ksanj\\OneDrive\\Pictures\\quotes\\hardwork.jpg"
a = open(img,'rb')       #this will read the image and gives their binary value as an output
d = a.read()
print(d)
a.close()

"""
Why bother closing your files?

At the OS level, processes have a limit on the number of open files, so if you write a program that will run a long time and possibly open many files you need to be careful.

It's a good habit to close your files.
"""

