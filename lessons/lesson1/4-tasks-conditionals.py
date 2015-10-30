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

Make the following function print "It was definitely a squirrel!" if
the first parameter is equal to "squirrel", and "Awww" otherwise.

"""

def task_3(text):
    print("squirrel")
    
#This should print "It was definitely a squirrel!"
task_3("squirrel")

#This should print "Awww"
task_3("dog")