"""
Functions
##########

Functions are typically introduced a bit later, but they'll be useful for
understanding some of the things we'll cover next.

Functions are blocks of code that can be reused. They contain a series
of statements (such as x = y, or print(3)) that are executed whenever it is run.

Running a function is called "calling" it.

Functions can also have data (variables) given to them to use in their code.
These are called parameters.

Functions can return a value. This effectively means that the place where the
function is called is equal to that value.

This is all quite confusing.
Lets have some examples to make all this clearer.
"""

#list is a function built into Python.
#list returns a new empty list.
#The syntax for calling (executing) a function, is to type its name, followed
#by a pair of brackets.

list()

#Let's see the value returned by list()

print("Value of list:", list())

#As you can see, you can stick a call to a function anywhere it would make sense 
#to put a variable.

#Let's try having a few functions of our own!
#Here's a simple one that just prints "Hello from function one!" when it's called

def function_one():
    print("Hello from function one!")
    
#Important points here:
#
# 1. Functions start with "def some_name():" some_name can be pretty much any
#    word. It's convention to make it all lower case, with an underscore between
#    words
#
# 2. The body of the function (the code you want to run each time) is indented
#    by a single tab. This is how Python knows what's in the function.
#
    
#And let's call it...

function_one()

"""
Functions with Parameters
##########
"""

#Defining these is very similar to a normal function.
def some_function_with_parameters(param_one):
    print(param_one)
    
#Let's disect this a little.
#So, the first line is very similar to before. Except we have param_one between
#the brackets. This is the name of our first parameter. 
#We can now use that as you would any other variable inside the function!
#In this case, we print it!
#Neat, eh?

#We call functions with parameters like this
some_function_with_parameters("Hey, this is the first parameter!")

#Again, we can put in anything we like into that first parameter! Whatever we
#put in will end up assigned to param_one.

#We can even have multiple parameters!
def some_function_with_multiple_parameters(param_one, param_two, param_three):
    print("Param one:", param_one)
    print("Param two:", param_two)
    print("Param three:", param_three)

#You can see each of the parameters is seperated by a comma!
#You might be able to guess how the function is called!

some_function_with_multiple_parameters("One", "Two", 3)

#Finally, returning things!
def some_function_with_return_value():
    return 3
    
#This looks very similar to the first one, but with that line "return 3"
#"return" stops executing the function and assigns the function the value
#at the point it was called. Let's see an example!

print("My function returns:", some_function_with_return_value())

#This can work anywhere a variable can, as before:

x = some_function_with_return_value()