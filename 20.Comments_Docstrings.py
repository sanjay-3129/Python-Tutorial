#comments and docstring

# - single line comment
""" multi line comment """

#(i) - Comments are annotations to code used to make it easier to understand. They don't affect how code is run.
x = 365
y = 7
# this is a comment

print(x % y) # find the remainder
# print (x // y)
# another comment

#(ii) - docstring(documentation strings) : designed to explain code, putting a multiline string containing an explanation of the function below the function's first line.
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")
 
shout("spam")    #function calling

# You can access the docstring through the run time using the syntax: funcName.__doc__
print(shout.__doc__)

help(shout) #it will also prints the docstring
