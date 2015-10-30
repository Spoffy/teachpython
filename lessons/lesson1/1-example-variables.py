"""
Comments
##########

A comment is some text that's ignored when the code is run.
This is a comment, and we'll be using them to provide info and tutorials 
throughout these sessions!

Comments are done either by putting text between three double quotes, or 
putting a hash before it, like so:

# This is a comment
"""

"""
Printing
##########

Printing lets you output text from your program.
Printing is one of simplest and often most useful operations you can do.
You'll see many examples of printing throughout these sessions, providing
useful info when you run this example!
"""

#Printing some text
print("This is how to print some text!")

#Printing multiple bits of text
print("Text part one!", "Text part two!")

"""
Variables
##########

A variable is a named location to store some data.

Metaphor:
    Imagine a set of labelled boxes stacked against a wall.
    Each box is a variable.
    The contents each box is the data stored in each variable.
"""

#You can create a variable like this:
x = 3

#Variables can contain any letter, a number (as long as it doesn't
#start with it) or an underscore.
#The more descriptive the name, the better!
some_variable_1 = 3

#This is not valid
#1_variable = 3

#You can use a variable in lots of places
#Anywhere you can put a value, really!
#For now, let's test it with printing!
print("This is an example of printing a variable:", some_variable_1)

"""
Types
##########
Data comes in lots of different "types".
For example Integers, Floating Point (decimal numbers), Strings.
Roughly, a type tells Python (and you) what that value can do.
"""
"""
Integer numbers:
    These store the value of a whole number (no decimal places).
    They have a highest possible value and a lowest possible value.
    
    WARNING: The following is slightly more advanced. Don't worry if you don't
    understand.
    
    They typically have a highest possible value of 2^32, and a
    lowest possible value of -2^16. 
    This varies from machine-to-machine.
"""
#An integer, assigned to the variable a.
a = 3

#Addition
b = 3 + 2
c = a + b

#Multiplication
d = 2 * 2

#Division
e = 4 / 2

#Remainder (gets the remainder when divided by the other value)
#(Also known as modulo)
f = 5 % 2
#f now has value 1.

#Integers can do more, but this'll do for now!

"""
Floating point numbers (decimals):
    Floating point numbers let you store really big numbers and really small
    ones. 
    
    For example, 9,876,543 or 3.1415926.
    
    Floating point numbers can behave a little bit weirdly (they can lose some
    accuracy), but don't worry about that for now! 
    Python tries to hide this, especially when printing.
"""

#A floating point number
a = 3.5

#Addition
b = 3.5 + 1.5
c = a + b

#Multiplication
c = 4 * 1.5

#Division
d = 3 / 2

"""
Booleans:
    Booleans are a type that can be either True or False.
    They're typically not entered manually, but lots of other things convert
    to booleans.
    
    The most common use cases for these are in "if" statements, which we'll see
    later!
"""

#A boolean
t = True
f = False

#This evaluates to a boolean, even if it isn't obvious at first.
#It's true if 5 is greater than 4, which it is.
x = 5 > 4

"""
Strings:
    Strings are a way of representing text on a computer.
    They consist of a sequence of characters.
    
    Strings are immutable. I.e, they can't change once you've created them!
    Strings are also a type of object. For now, think of that as meaning they
    have functions (actions) which can do things to them. We'll cover that in
    more detail later.
    
    Strings can be added together (concatenated) to make a new string!
"""

#Declaring a string using double quotes "
text = "This is a banana"

#Alternative method of declaring a string. Note the single quotes '
more_text = 'This is also a banana!'

#A third way of declaring a string. Yes, this is the same way as declaring a
#block comment. Python's weird like that.

another_string_method = """ More strings! """

#Adding together, i.e concatenation!
example_adding = "This is a " + "sentence."
added_strings = text + more_text

print("An example of concatenation:", added_strings)

"""
Combining Types
##########

We'll cover types in more detail later, when we cover functions.
However, a few useful things for the time being.

- Most operators (e.g +, -, /, *) don't work on different types. For example, 
  if you try to divide a string and an integer, you'll get an error.
  
- Integers and floats can work together nicely, though rarely this can lead
  to slightly unexpected behaviour. Generally, you'll be doing this a lot.
  
- Types can also explicitly converted to other built-in types (types that are
  a part of Python). 
"""

#This would error
#erroring_thing = "A text" / 3

#Integer added with a float
a = 3 + 2.0

#Most things can't be added to strings straight away...
#This errors
#b = "A" + 3

#However, you can convert using the functions int(), float(), str()
#Don't worry if you don't understand exactly, we'll cover functions soon!
b = "A" + str(3)



