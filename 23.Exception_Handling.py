#(i)
try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")

#(ii) - An except statement without any exception specified will catch all errors.
try:
    X=6
    y=4
    print(X+Y)
except:
    print("something is wrong")

#(iii) - Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")
   
#(iv)finally
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")
   
#(v)raise
print(1)
raise ValueError
print(2)

#(vi)
try:
  print(1 / 0)
except ZeroDivisionError:
  raise ValueError            #output: zerodivisonerror and valuerror
  
#(vii)
name = "123"
raise NameError("Invalid name!")

#(viii) - In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise
