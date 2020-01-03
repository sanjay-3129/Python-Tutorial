#Functions

#(i) - function without arguments and return method
def func_noarg():
	print("vanakam")

func_noarg()
print()

#(ii) - function with arguments, print and return methods
a = 10
b = 5
def my_func(a,b):  #first we have to define the function and call it or else it will provide an error.
	print("hai")
	c = a+b
	return c       #return method will return the c value to where the function is called and it is assigned to a.
                   #once return is called then it immediately stops being executed. Any code after return will not happen and returns error.
a = my_func(a,b)
print(a)
