Very Short Questions and Answers

# 7. Write a function that calculates the volume of a cube. Input parameter side and unit as a default parameter. The volume of a cube is side * side * side.
# Ans. 
import math

def cube_volume (side , unit="inches"):
    return str(side**3 ) + " " + unit
    
side =float(input("Enter the length of the side"))
print(cube_volume(side,'cms'))
side =float(input("Enter the length of the side"))
print(cube_volume(side))

# 8. Write a function that prints even numbers from the list.
# Ans. 
slist= [1, 12, 3, 4, 15, 6, 7, 18, 9, 8]
def print_even (list):
    for i in range( 0,len(list)):
        if ( list[i] % 2 == 0 ):
            print(list[i], end=", ")

print_even(slist)

# 9. Write a function that prints odd numbers from the list?
# Ans. 
slist= [1, 12, 3, 4, 15, 6, 7, 18, 9, 8]
def print_odd (list):
    for i in range( 0,len(list)):
        if ( list[i] % 2 != 0 ):
            print(list[i], end=", ")
            
print_odd(slist)

# 11. How to retrieve the docstring?
Ans. 
def my_function():
    """The function's docstring"""
    
# A docstring can be retrieved in two ways:
# a. Using doc attribute __doc__ for example
my_function.__doc__

# b. Using the help function
help(my_function)


#12. Write a function to calculate the area of a triangle.
#Ans. Arguments are base and height of a triangle. The formula used is: Area = 1/2*base*height
def triangle_area( base, height):
area = .5 * base * height
return area
height = int(input("Enter height: "))
base = int(input("Enter base: "))
print("The area of the triangle is: ")
print(triangle_area(height,base))
Output:
13. Write a function to calculate the area of a circle.
Ans. Parameter are radius and return value is area of a circle. The formula used is: area = 22/7 * r **2
def circle_area( radius):
area = 22/7*(radius **2)
return area
rad = float(input("Enter radius: "))
print(circle_area(rad))

# 14. What is the return value of the following function?
def sumthree(x, y, z):
    print("The sum is: " + str (x + y + z) )
    
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))

retval= sumthree(num1, num2, num3)
print("The return value is ")
print(retval)

# 15. Find the output of the following function.
def sumthree(a, b, c):
    return a + b + c
    print("The sum is: ")
    print(a + b + c)
    
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))

print("The sum of " + str(num1) + " + " + str(num2) + " + " + str(num3) + " is
:",end= " ")
sumthree(num1,num2,num3)

# 16. Find the output of the following program.
num = 10
def golocalscope():
    num = 50
    return num

print(num)
print(golocalscope())
print(num)

# 17. Find the output of the following program.
# Ans. 
num = 10
def golocalscope():
    global num
    num =50
    
print(num)
print(golocalscope() )
print(num)

# 23. Write a recursive function to add the first ‘n’ terms of the series: 1+ 1/2 - 1/3+1/4
# Ans.
total = 1.0
term =-1
x= 2

def sum_series(n):
    #using global variable to retain value between multiple function calls
    global total
    global term
    global x
    if n == 1:
        return total
    else:
        # Change the sign
        term = term * -1
        total= total +( ( 1 / x ) * term )
        x+=1
    return sum_series(n-1)
    
print(sum_series(5))
print(sum_series(10))
print(sum_series(20))
print(sum_series(50))

# 24. Write a function that multiply all its numbers in a list.
# Ans. 
def mul_list(lst):
    mul=1
    for element in lst:
    mul*=element
    return mul
    
lst = [ 2,4,6,10]
print(mul_list(lst) )
print(mul_list([1,2,3,4,5]))
print(mul_list(range(1,10)))

#39. Explain the default argument and its utility.
# Ans. Function header with default parameters allows skipping of passing the arguments while calling the
# function. For example:
def welcome(name , title="Mr." , msg= "Welcome aboard!!!"):
    print (msg , "" ,title , "" ,name)
welcome("Ramesh Kumar")
welcome("Savita Khanna ","Mrs.")

# 40. Can function return multiple values? If yes, how?
# Ans. Function can return multiple values as shown in below code:
def SQR( num1, num2):
    _t = num1 * num1, num2 * num2
    return _t
    
print( SQR(5,10))

Long question and Answer

1. Write a Python function that accepts a string and returns the number of characters in
uppercase and lowercase.
Ans. Let’s create a dictionary to store the count of upper case and lower case characters in the dictionary:
_dict = {"UC":0, "LC":0}
def char_count(string):
for char in string:
if char.isupper():
#increment the count of upper case
_dict["UC"]+=1
# increment the count of lower case
elif char.islower():
_dict["LC"]+=1
# pass if character is not upper and lower case
else:
pass
char_count("My name is Bond!!! James Bond")
print("The number of upper case character(s): " + str(_dict.get("UC")))
print("The number of lower case character(s): " + str(_dict.get("LC")))

# 2. Write a function to check whether a number is perfect or not.
# Ans. In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors. Equivalently, a perfect number is a number that is half the sum of all positive divisors (including itself). For example, 6 is perfect number, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: (l +2 + 3 + 6)/2 = 6.The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. Other perfect numbers are 496 and 8128.
# Let’s write a function to find if a number is perfect or not:6
def perfect_number (num):
    sum = 0
    for i in range (1, num):
    if num % i == 0:
        sum += i
        
    return sum == num
        
num = int(input("Enter a number: "))
if( perfect_number(num) == True ):
    print("The "+ str( num ) + " is a perfect number ")
else:
    print("The "+ str( num ) + " is not a perfect number ")
    
# 4. Write a function that converts one currency to another currency or vice versa.
# Ans. In the following code, _dict contains the conversion rate. Let’s see in detail:
_dict={"USD-INR":68.86,"INR-USD":.015, "GBP-INR":85.26,"INR-GBP":0.0117241}
def curr_converter(amt, fromcurr='INR', tocurr='USD' ):
#create key for conversion
    key = fromcurr + "-" + tocurr
    if( key in _dict.keys()):
        return amt * _dict.get(key)
#converting USD to IR
print("Converting from 1 USD to IR")
print(curr_converter(1,"USD","INR"))
print("Converting from 1 INR to USD")
print(curr_converter(1,"INR","USD"))
print("Converting from 1 IR to GBP")
print("Converting from 100 INR to USD")
print(curr_converter(100))
print(curr_converter(1,"INR","GBP"))

# 5. Write a function to compute the factorial of a number (a non-negative integer).
# Ans. The function accepts a number and returns its factorial.
def fact(num):
    if(num < 0):
        print("Error ! no factorial value for negative number")
    elif(num == 0):
        return 0
    else:
        f=1
        while(num > 0):
            f*=num
            num-=1
    return f
    
print(fact(5))
print(fact(0))
print(fact(-2))

#6. Find the output of the following code.
def printline(newline, char='*', len = 20):
for i in range(len):
print(char, end='')
if(newline):
print()
printline(True)
printline(True, char ='-'))
printline( True, char='-', len =40)
printline(False, char = '='))
Ans. Output:
********************
--------------------
----------------------------------------
====================

Programming Questions and Answer
# 1. Write a program that accepts a sequence of words as input and prints the words after sorting them in alphabetical order.
# Ans. 
string = 'my name is antony'
#splits sentence into words
words = string.split(' ')
#sort the list of the words
words.sort()
#join the words into a string
print(' '.join(words))

# 2. Write a function that accepts a number and prints the Fibonacci series upto the number given.
# Ans. #function that print Fibonacci series
def Fibonacci(num):
    # Simultaneous assignment
    f1,f2=0,1
    print(f1, f2, end=' ')
    while f2<num:
    #simultaneous assignment f1 = f2 and f2 = f1+f2
        f1,f2 = f2,f1+f2
    
fibonacci(100)
print(f1, end=",")

# 3. Write a function that prints the sum of the following series.
# series x + x ^2 / 2! + x ^3 / 3!+. n
# Ans. 
import math
def series(x, terms):
    sum=0
    i=1
    while i < terms:
        sum = sum + math.pow(x,i) / math.factorial(i)
        i+=1
    return sum
    
print(series(2,10))

# 4. Write a program that returns the longest word from a list of words.
# Ans. 
def longestword( _list ):
    largest=""
    for word in _list:
        if( len(word) > len(largest)):
        largest = word
    return largest
    
#covert the string into list
lst= "this is a program to find the longest word in the sentence".split(" ")
print(longestword(lst))

# 5. Write a function that converts a list of characters into a string.
# Ans. 
def list_to_str(_list):
    return string = ''.join(_list)

lst = ['p', 'y', 't', 'h','o','n']
print(list_to_str(lst))

# 6. Write a function to get the frequency of each element in a list.
Ans. 
def element_freq(_list):
    # To store elements and their occurrence
    _freq={}
    for ele in _list:
        if(ele in _freq):
    # if element exists in dictionary
    # add the frequency of an element
            _freq[ele] += 1
        else:
            _freq[ele] = 1
    return _freq
    
print(element_freq([1,2,4,5,6,1,2,8,3,10,5]))

# 7. Write a program to unpack a tuple in several variables.
# Ans. #creating a tuple
_tuple = 1, 2, 3
print(_tuple)
Output:
(1,2,3)
num1, num2, num3 = _tuple
#unpack a tuple in variables
print(num1 + num2 + num3)

# 8. Write a function to convert a tuple to a string.
# Ans. 
def tuple_to_str(_tuple):
    # to convert tuple in list first and
    #use join to convert into string
    string =" ".join(list(_tuple))
    return (string)
    
print(tuple_to_str( ('p', 'y ', 't ', 'h ', 'o ', 'n ') ))

# 9. Write a program to add an item in a tuple at the beginning, end, or a given location.
# Ans. The tuple is immutable and cannot be altered. To add the new tuple, the ‘+’ operator is used; it returns a newly created tuple. Below example demonstrates to add the element in the tuple:
def additem(_tuple,ele,loc=0):
    # Add the element at the beginning of the tuple
    if (loc == 0):
            _tuple = (ele,) + _tuple
    # Add the element at the end of the tuple
    elif(loc == len(_tuple)):
        _tuple = _tuple + (ele,)
    else:
    # Add the element at the specified location
        _tuple = _tuple[:loc] + (ele,) + _tuple[loc:]
    return _tuple

print(additem((1,2,3,4,5,6),7,0))
print(additem((1,2,3,4,5,6),7,len((1,2,3,4,5,6)))
print(additem((1,2,3,4,5,6),7,3))
