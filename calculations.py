#assignment 2, the making of functions
import math


def checknum(num): 
    #if statement
    if (num < 0):
        return "Number is negative"
    elif(num ==0):
        return "Number is neutral"
    elif (num > 0):
        return "Number is positive"
    else:
        return "Number is not fit in the given condition"

# grading
def grading(value):
    
    if (100 >= value >=90 ): #value >=90    or  value<=100 and value value=<90
        return "Grade is A" 
    elif (90 >= value >=80): #value>=80
        return "Grade is B"
    elif (80>= value >=70): #value>=70
        return "Grade is C"
    elif (70 >= value >=60): #value>=60
        return "Grade is D"
    else:
        return "You have failed"


#fucntion where checking in a list for even or odd numbers
def checkodd(list):
    counteven=0
    countodd=0
    for values in list:
        if (values%2 == 0): #even
            counteven =counteven+1
        else: #odd
            countodd =countodd+1
    #printing the counts    
    print("Even count is: ", counteven)
    print("Odd count is: ", countodd)

def areatri(base, height):
    return (base*height)/2

def areaquad(len,wid):
    return len*wid

def areacir(r):
    #return 3.14*r*r
    return math.pi*r**2
