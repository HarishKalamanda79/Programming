# if and else statement's

'''
if condition:
    statement
else:
    statement
'''

if True:
    print("I am if Statement")
else:                               # in this code if statement will be false it will print else statement otherwise print's if statement
    print("I am else statement")    

'''
if condition:
    statement
elif condition:
    statement
else:
    statement
'''
# if, elif & else
if True:
    print("I am if statement") # if condition will true it print's if statement
elif True:# if, if and elif both conditions are True it print's if statement
    print("I am elif statement")# elif condition will true it will print elif statement
else: # if, if and elif bothe conditions are false it will print's else statement
    print("I am else statement")
    
#if, elif, else & nested if.

if True:
    print("Outer if Statement")
    if True:
        print("nested if statement")
    else:
        print("inner else statement")
else:
    print("Outer else statement")

#sample code 👇🏻
# Student Progress Checker

marks = 72

# Using if-elif-else to evaluate performance
if marks >= 90 and marks <= 100:
    print("Excellent! You got an A+ grade.")
elif marks >= 80 and marks <= 100:
    print("Very Good! You got an A grade.")
elif marks >= 70 and marks <= 100:
    print("Good job! You got a B grade.")
elif marks >= 60 and marks <= 100:
    print("Fair. You got a C grade.")
elif marks >= 50 and marks <= 100:
    print("Needs Improvement. You got a D grade.")
else:
    print("Fail. You need to work harder.")
    print("Don't give up! You can do better next time.")

#nested if sample code

# Input student marks and attendance
marks = 71
attendance = 64

# Main if-elif-else block for marks
if marks >= 90:
    print("Grade: A+")

    # Nested if to check attendance
    if attendance >= 90:
        print("Excellent academic performance with great attendance!")
    else:
        print("Good marks, but improve your attendance.")
        
elif marks >= 75:
    print("Grade: A")

    if attendance >= 80:
        print("Well done! Keep it up.")
    else:
        print("You scored well, but work on attending classes regularly.")

elif marks >= 60:
    print("Grade: B")

    if attendance >= 70:
        print("Average performance, but decent attendance.")
    else:
        print("Try to improve both marks and attendance.")

elif marks >= 40:
    print("Grade: C")

    if attendance >= 60:
        print("You're passing, but both marks and attendance need improvement.")
    else:
        print("You're at risk. Focus more on studies and attendance.")

else:
    print("Grade: F - Fail")
    
    if attendance < 50:
        print("Poor performance and very low attendance.")
    else:
        print("You're failing academically. Work harder!")



