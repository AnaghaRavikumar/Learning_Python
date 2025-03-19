from sysconfig import get_preferred_scheme
from Student import Student
from tkinter.font import names
from Question import Question

import docx

import useful_tools
from math import *


print("Hello  World")

#Draw a shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#Variables and DataType
character_name = "John"
character_age ="35"
print("There was a man named "+character_name+".")
print("He was "+character_age+" years old.")
print("He really liked the name "+character_name+".")
print("But didn't like being  "+character_age+".")

#working with Strings
print("Giraffe Academy")
#To create a new line
print("Giraffe\nAcademy")
#Ti  incl a quotation mark
print("Giraffe\"Academy")
#to just print \
#print("Giraffe\Academy")

phrase   ="Giraffe Academy"
print(phrase)

#concatenation
print(phrase+"is cool")

#use functions with strings
phrase = "Giraffe Academy"
#To convert to uppercase
print(phrase.upper())
#to check if phrase is entirely upper case
print(phrase.isupper())
#Use functions consequently
print(phrase.upper().isupper())
#use  the function to get the length  of the string
print(len(phrase))
#get individual character in the string
print(phrase[0])
#index funtion tells us where exactly the string is
print(phrase.index("Acad"))
#replace functions
print(phrase.replace("Giraffe","Elephant"))


#working with numbers
print(2.0987)
print(-2.0987)
print(3+4.56)
print(3*4)
#order of operations can be specified
print(3*(4+5))
print(10%3)

my_num  = 5
#convert number to string. We can use this when we want to print number along with string
print(str(my_num)+ " is my favourite number")

#absolute value
print(abs(-5))

#power function, we give 2 pieces of info. first arg number and second raised to power of
print(pow(3,3))

#max - returns larger  of the 2 numbers
print(max(2,3))
print(min(4,6))

#round
print(round(4.86))

#Some  other math functions we need to import a library math
#floor rounds the number down
print(floor(3.7))
#ceil rounds the number up
print(ceil(3.7))
#sqrt provides thee sqrt of a numbere
print(sqrt(36))

#getting input from someone
name = input("Enter your name: ")
age = input("Enter your  age: ")
print("Hello "+name+"!")
print("Age  "+age)


#Buliding a Basic calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1+num2
print(result)

#whole numbers/decimal will  create error and break the program
result = int(num1)+int(num2)
print(result)

#use float to be able to use decimal
result = float(num1)+float(num2)
print(result)

#MADLIBS game using python
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun:")
celebrity = input("Enter a celebrity Name: ")
print("Roses are "+color)
print(plural_noun+" are blue")
print("I love "+celebrity)

# List
friends =  ["Kevin","Karen","Jim","Oscar","Toby"]
print(friends[0])
print(friends[-1])
#if we want to grab  karen and everything after that, i.e omit first element in  the list
print(friends[1:])
#To grab elements specified in particular index
print(friends[1:3])
friends[1]= "Mike"
print(friends[1])

# List functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends =  ["Kevin","Karen","Jim","Oscar","Toby"]
#Add  to lists
friends.extend(lucky_numbers)
#Add extra item to the list, append always inserts the item  in the end
friends.append("Penny")
print(friends)
#To add an item to a specific position
friends.insert(1,"Kelly")
print(friends)
#To remove an element
friends.remove("Jim")
print(friends)
#remove last element
friends.pop()
print(friends)
#To find if something is available in the list. If not there it will throw an  error.
print(friends.index("Kevin"))

#to  check  how many times an element shows up in the list
print(friends.count("Jim"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2  = friends.copy()
print(friends2)


#Tuples in python -  Container where you cans tore different values
#Tuples are immutable
coordinates = (4,5)
print(coordinates[0])

#coordinates[1] = 10 -----  This will give a type error as tuple is immutable
#We use tuples when data cannot be changed/ does not change
#I can create a list of  tuples

coordinates = [(4,5), (6,7), (80, 34)]

#functions
def say_hi():
    print("Hello User")

print("TOP")
say_hi()
print("BOTTOM")

#Make functions powerful by giving it some information

def say_hi(name):
    print("Hello "+name)

say_hi("Mike")
say_hi("Steve")

#We can include more than one parameter

def say_hi(name, age):
    print("Hello "+name+", you are "+str(age))

say_hi("Mike", 35)
say_hi("Steve", 70)

#Return statement can  bee used to get information from a function
def cube(num):
    return num*num*num

print(cube(3))

'''
# am at a restaurant
#If I want meat
#I order a steak
#otherwise if I want pasta
#I order a spaghetti & meatballs
#otherwise
#I order a salad.
'''

is_male = False
is_tall = True

if is_male:
    print("You  are a male")
else:
    print("You are not a male")

    #keywords
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are a not a male but are tall")
else:
    print("You are either not male or not tall or both")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 40, 5))

#Building a better calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator")

#DICTIONARIES

monthConversions={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "september",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

#Now we can access these from program -> refer to key and returns the value
print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
#f there is no value
print(monthConversions.get("Lub", "Not a valid key"))

#while loop in python
i = 1
while i<= 10:
    print(i)
    i = i+1

print("Done with loop")

#Building a guessing game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
      out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOOSE!")
else:
 print("You win!")

'''
#for loops
#looping through letters
'''

for letter in "Giraffe Academy":
    print(letter)

#Names in the list
friends = ["Rachel","Joey","Chandler","Phoebe","Monica","Ross"]
for name in friends:
    print(name)

#List of  numbers
for index in range(10):
    print(index)

#range   of numbers
for index in range(3,10):
    print(index)

#to get length of the array
len(friends)
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")

 #Exponent Functions
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3,4))

#2D lists and nested loops
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])
print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)

'''
#Build a Translator
#Giraffe Language
#vowels -> g
#-----------------
#dog -> dgg
#cat -> cgt
'''

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation  = translation + letter
    return translation

print(translate(input("Enter  a phrase: ")))

#COMMENTS
'''
this is a comment
paragraph that can consist of multiple lines 
that need not be executed
'''
# print("Comments are fun")
'''
Error Handling
'''

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

'''
Reading Files using python
'''
employee_file = open("employee.txt","r") #Read information inside the file
# open("employee.txt","w") #Write information  inside the file
# open("employee.txt","a")#cant edit, but you can  add new  data in the file
# open("employee.txt","r+")#allows user to read and write
print(employee_file.readable())#This will tell me if the file is readable
# print(employee_file.read())
print(employee_file.readlines())
employee_file.close()
'''
Writing new files/ appending existing files using python
'''
employee_file = open("employee.txt","a")
employee_file.write("\nKelly - Customer Service")#\n is used to make sure the data is added to a new line
employee_file.close()

#overwrite  the file/ create new file

employee_file = open("employee1.txt","w")
employee_file.write("\nKelly - Customer Service")#\n is used to make sure the data is added to a new line
employee_file.close()

'''
Modules ar python files that I can import into file that 
I am  currently working on 
'''
print(useful_tools.roll_dice(10))
docx.replace() #Python docx

'''
#Classes and Objects
#In python we are dealing with a lot of types of data.
#I can create my own data type in python
'''

student1 = Student("Jim", "Business", 3.1)
student2 = Student("Pam", "Art", 4)

print(student1.name)
print(student2.gpa)
print(student2.on_honor_roll())

#Multipe choice quiz

question_prompts = [
    "What color are apples?\n(a)Red/Green\n(b)Purple\n(c)Orange\n\n"
    "What color are Bananas?\n(a)Teal\n(b)Magenta\n(c)Yellow\n"
    "What color are strawberries\n(a)Yellow\n(b)Red\n(c)Blue\n\n?"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1

    print("You got "+str(score)+'/'+ str(len(questions)) +"correct")

run_test(questions)