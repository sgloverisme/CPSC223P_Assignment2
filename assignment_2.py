#sarah glover
#8/31/2022
#taking user input, making loops conditional statements i/o 
#the "main" file

from collections import defaultdict
import numbers
from calculation import* #importing the calculation.py to use functions


# username = input("Enter Username:")  #taking in an user input, string
# print("username is: " + username) #printing the user input 

# age=int(input("Enter your age:"))   #taking in an int user input 
# print("My age is: ", age) #printing an int input, use the COMMA, do not concantinate

#printing functions
print(checknum(4))
print(grading(70))


list = [12,34,21,53,23]
print(checkodd(list))

#print(range(10))
#print(list(range(10)))
#print(list(range(20,40)))
#print(list(range(6,24,4))) #6 is the starting, 24 is the end point, 4 is the increment

#printing a list of values using a for loop and using range()
numbers= [20,30,40,50,60,70,80,90]

for val in range(len(numbers)):
    print(numbers[val])

lang=["python", "java","c","c++"] 
for a in range(len(lang)):
    print(lang[a].upper()) #upper() makes all the string upper case


c=0 #counter
while c <10:
    c +=3
    print("python while loop")


for string in "Python loops":
    if string == "o" or string =="p" or string == "t": #removes these letters
        continue
    print("Current letter: " , string)

evenodd=[1,2,3,4,5,6,7,8,9,0] 
for i in range(len(evenodd)):
    evenodd.append(evenodd[i]+2) #adding 2 to each value 
print(evenodd) #printing the original and the new values of evenodd

#creating the records of the students in the list 
#creating functions in calculation.py, passing arugement name of student
#make f loop where if the student is in the given list. if equal, break and return the name. if not equal, continue.

record = {'python':90, 'java':95, 'c':50, 'c++':20}
subject_name_1= 'python'
subject_name_2='ruby'

def sub(subjectname):
    for subject in record:
        if subject ==subjectname:
            return record[subject]
        break
    else:
             return "subject is 404"

print("subject is: ", sub(subject_name_1))
print("subject is: ", sub(subject_name_2))

#nums=[2,7,11,15], target =9 , output [0,1]
#nums=[3,2,4], target=6, output[1,2]

# number=defaultdict(int)
# number['one']=1
# number['two']=2
# print(number['two'])

# nums=[2,7,11,15] #other list is [3,2,4]
# target=9 #other target is 6

#  #putting in a list and int 
# def twonum(nums: list[int], target: int):
#     number=defaultdict(int)

#     for i, n, in enumerate(nums):
#         if target - n in number: #target 
#             return [i, number[target-n]]
#         number[n] =i 


# print("output is", twonum(nums,target))
# result =enumerate([1,2,3])
# print(result)
# print(list[result])

#pass statement used in for loop 

sequence = {"python", "java", "statement"}
for value in sequence:
    if value == "java":
        pass 
    else: 
        print("havent reached to java: ", value)


stri = "hello student"
stri2 = "good morning"

print(stri)
print(stri[3]) #getting a char from stri
#print(stri2)

# stri3 = """triple quotes for the name of the 
#         class of python of strings 
#         in california state university"""

# print(stri3)

print(areatri(2,3))
print(areaquad(2,4))
print(areacir(4))

a= [1,2,3,5,6]
#deleting an element from list by their index
del a[0] 
print(a)

tuple_1=("python", "java", "c++") 
# print(tuple_1[0])
# #printing the last element of a list
# print("element at -1 index", tuple_1[-1]) 

    # try:
    #     del tuple_1[1]
    #     print(tuple_1)
    # except Exception as e: 
    #     print(e)

#repitition of tuples
# tuple_1 = tuple_1 * 3 
# print(tuple_1)

#abs()
# a = -20
# print("absolute value: ", abs(a))

# k=[1,2,3,4]
# k1=[0, False] 
# print(all(k)) #returns true 
# print(all(k1)) #retuns false


# y=bin(20)
# print(y) #obBINARYNUMBER

test1=[]
print(test1, "is", bool(test1))

string = "wuz up"
array=bytes(string, "utf-8")
print(array)

print(callable(8)) #callable() checking is smg can be called