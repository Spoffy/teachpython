"""
Boolean Logic
##########

Boolean logic, put simply, means ways of combining the values of True and False.

Python has many built in operators to comparing values and combining booleans.
We'll briefly cover these below, so we can go onto the awesomeness of conditionals!

http://learnpythonthehardway.org/book/ex27.html
https://docs.python.org/3/library/stdtypes.html
"""

#Just to recap, the simplest forms of booleans are like so
true = True
false = False

#Note how True and False are case sensitive!

#The first operator to cover is equality. This is true if two variables
#(or literals, such as 3.0, or "Text") are equal in value.
#Note, the operator is TWO equal signs. 
#One equals sign is assignment to a variable. Two is a check for equality.

#This is True
3 == 3
"Text" == "Text"

#This is False
3 == 2
"Text" == "Banana"

#There's also the opposite of equality.... inequality! The not equal operator 
#works the same as equality, but is False is they're equal, and True if they're
#not equal. The exact opposite!

#These are now False
3 != 3 
"Text" != "Text"

#These are now all True!
3 != 2
"Text" != "Banana"

#Let's look at some operators for mainly working with numbers! Huzzah, numbers!
#Firstly, greater than and its opposite, less than.
#They check if one number is greater than another or, equivalently, less than
#another number!

#Greater than in action
#These are all True!
3 > 2 
1.2 > 1.1

#Equivalently, these are all False
2 > 3
1.1 > 1.2

#Less than works exactly the same, but the operator is the other way around!
#These are now all True!
2 < 3
1.1 < 1.2

#And these are now all False!
3 < 2
1.2 < 1.1

#The way to remember these is simple:
"""The mouth of the crocodile is always towards the bigger number if it's True"""
#or
"""The bigger end of the operator is towards the bigger number"""

#However, these operators are known as "strictly less than", and vice versa.
#As in, these are False
2 < 2
2 > 2

#But there's a solution! Two operators called "Greater than or equal to" and,
#of course, "Less than or equal to"
#These are now True! Huzzah!
2 <= 2 
2 >= 2

#The final important operator is "not". It's really simple but really, really
#useful. It just flips the result of whatever it's in front of!
#I.e False becomes True, True becomes False!

#Here's a few examples
#These ALL evaluate to True
not 2 == 3
not 2 > 3
not 5 < 2
not 2 <= 2

#Everything here can also be applied to variables!
true = True
false = False

#False
true == false

#True
true == (not false) #Brackets needed... explained later.
not (true == false)

#Finally, there's two special magical operators that only work on values of True
#and False. These are extremely important for combining the above things into
#Something more useful. They're called "and" and "or"!
#This reference is really useful if you're uncertain how these work:
# http://learnpythonthehardway.org/book/ex27.html

#"and" is True whenever the things on either side of it are True!
#Otherwise, it's False.
#These are all True
True and True
1 == 1 and 2 == 2
1 == 1 and 2 < 3
False and False
1 == 1 and not 2 == 3

#These are all False
True and False
False and True
1 == 1 and 2 == 3
1 <= 2 and 3 <= 2
1 == 1 and not 2 == 2

#The "or" operator is similar to "and", in that it only works on True and False.
#Logical "Or" is True whenever the thing on its left OR the thing on the right
#are True. It's False only if the thing on the left and the thing on the right
#are both False.

#This is all True!
True or False
False or True
True or True
1 == 1 or False
False or 2 < 3
2 < 3 or 2 > 3 #Left one is True, right one is False

#This is all False
False or False
2 > 3 or 3 > 4
False or 2 == 3

#You can also combine "and" and "or" with... anything else.
#To make sure things are worked out in the right order, you can wrap things
#In brackets. Anything in brackets is calculated first, like in maths!
#Try and follow the following examples

#These are all True
(False or True) and True
True and True and True and (True or False)
False or (False or (False or (False or True)))
1 == 1 and (2 == 2 or 2 > 3)

#These are all False
(False and True) or False
False or False or False or False or False and True

#Etc. It's confusing, sometimes you have to spent quite a while thinking about
#how to do logic like this! After a while, it'll be almost second nature :)

"""
Conditionals
##########

Conditional statements are a way of choosing bits of code to run.

How they work: A statement (be it a variable, a function call or an operator) is
used as a condition to decide to which way to go. If the statement is equal to
anything but "False" or "None" then the condition is true.

Again, examples!
"""

#This is the most basic conditional.
#Notice how the layout is similar to a function. The code to be run is
#indented once so it's inside the conditional.
if True:
    print("Hello world!")

#Note, how this next print statement DOESN'T run
if False:
    print("This will never be seen!")
    
#You can put... well, pretty much anything we've seen above into these!
if 1 < 2:
    print("1 is less than 2!")
    
if 2 == 2:
    print("2 is equal to 2! Who knew?!")

if 3 < 2:
    print("But 3 isn't less than 2. So we'll never see this :(")

if 2 == 2 and False:
    print("One side of the and is False. We'll never see this! Curses!")
    
if not True:
    print("Not displayed, because it's not True!")

#It goes on like this... hell, we can have some functions!
if len("This text is 32 characters long!") == 32:
    print("Wow, it actually is 32 characters long!")
    
#You can also have an "else" block. This executes if the condition is False.
#I.e, If the first block doesn't run, the else block does.

if False:
    print("This won't display as the condition is False.")
else:
    print("This will, because it's after an else!")