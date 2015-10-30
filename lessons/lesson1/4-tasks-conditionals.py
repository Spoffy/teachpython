"""
Tasks
##########

Here are a few tasks to attempt regarding variables!
Each task has instructions above it.

In order to attempt a task, uncomment the code that goes with it and follow the
instructions!
"""

"""
Task 01
##########

Alter all of the following lines of code to print True, instead of False.
"""

print(False or False)

print(True and False)

print(2 > 3)

print("Test" == "Bananarama")

print("Test" == 3)

print("True" and False or False)

a = 1
b = 2
c = "Incorrect"

#This actually errors! See if you can solve it :)
print(a < c and (c > b or b < a))

"""
Task 02
##########

Make the following function return True.
"""

def task_2():
    return 1 == 3
    
print(task_2())


"""
Task 03
##########

Finish the if statement to print only when yourAge + myAge (ourCombinedAge) is greater than to 38

Reminder: An if statement only completes the indented code if the if condition evaluates to true.
Reminder: An if statement follows the syntax: if CONDITION :. eg: 'if 2 + 2 == 4:' 
Example: 2 + 2 == 4 evaluates to true.
Example: 5 > 3 evaluates to true.
Example: 3 >= 3 evaluates to true.
"""

#Uncomment and complete the code below
#myAge = 19
#yourAge = 
#ourCombinedAge =

#if 
#  print(ourCombinedAge)

"""
Task 04
##########

Finish the if/else statement below to check if myString is equal to a string of your choice.
Make sure you set myString equal to a string first!
"""

#Uncomment and complete the code below: 
#myString =

#if
#  print("Your two strings were equal")
#else:
#  print("Your two strings were not equal")


"""
Task 05
##########

#Finish the if/elif/else statement below to evaluate if myInt is divisible by 4, else evaluate if it is divisible by 3.
#Try out myInt for several different values!

#Reminder: We can use the modulo operator to get the remainder. eg: 7 % 3 is equal to 1. (because 2*3 + 1 is equal to 7)

#Hint: If a modulo result is zero, then the left hand operator is wholly divisible by the right hand operator. 
"""

#Uncomment and complete the code below: 
#myInt =

#if
#  print("myInt was divisible by four.")
#elif
#  print("myInt was divisible by three but not four.")
#else:
#  print("myInt was divisible by neither three nor four.")

"""
Task 03
##########

Make the following function print "It was definitely a squirrel!" if
the first parameter is equal to "squirrel", and "Awww" otherwise.

"""

def task_3(text):
    print("squirrel")
    
#This should print "It was definitely a squirrel!"
task_3("squirrel")

#This should print "Awww"
task_3("dog")
