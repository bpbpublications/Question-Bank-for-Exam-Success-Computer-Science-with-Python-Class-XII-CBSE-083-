Very Short Questions and Answers

#33. Explain how if else works along with an example.
# Find out if a number is even and odd using if and else.
num = int(input("Enter a number"))
if num % 2 == 0:
    print( str(num) + " is an Even number")
else:
    print( str(num) + " is an Odd number")
    
    
#35. Explain how if… elif… else work with an example.
# find out if an number is even, odd or zero using if… elif… else
num = int(input("Enter a number"))
if num == 0:
    print( str(num) + "is Zero not even or odd")
elif num % 2 == 0:
    print( str(num) + " is an Even number")
else:
    print( str(num) + " is an Odd number
    
# 36. Explain how nested if… elif… else work with an example.
# Ans. When if...elif...else or if... else statement is inside another if ... else, if...elif...else statement, this is called
# nested if-else.
# Example:
# Check if number is 0, positive or negative
num = float(input("Enter a number:"))
if (num >= 0):
    if (num == 0):
        print(str(num) +" is Zero")
    else:
        print(str(num) +" positive number")
else:
    print(str(num) +" is a negative number")
    
#38. Write a program that uses while loop to print sum of the following series.
# Program to write the sum of series of 1^2 + 2^2+ 3^2 + n^2
terms = int(input("Enter the number of terms: "))
cnt = 1
sum =0
while( cnt<=terms):
    sum = sum + cnt **2
    print(str(cnt) + " ^ 2 + " ,end=")
    cnt+=1
    
print(' = ',end=' ')
print(sum)

# 42. Find the output of the following Python code.
# Ans. 
for name in['Jayes','Ramya','Taruna','Suraj']:
    print (name)
    if name[0]== 'T':
        break
    else:
        print ('Finished!')
    print ('Got it')

# 43. Find the output of the following Python code.
# Ans. 
for x in[1,2,3,4,5]:
    print(x, end=' ')

# 44. Find the output of the following Python code.
# Ans. 
for i in range(-500,500,100):
    print(i, end=' ')

# 45. Find the output of the following Python code.
# Ans. 
alphabets = ["a", "e", "b", "i", "u", "d"]

for char in alphabets:
    if char not in "aeiou":
        continue
    print(char, end=' ')

# 46. Write code that traverses a string.
# Ans. For loop allows iterating the string:
string = "narayan"
for char in string:
    print(char, end = " ")

# 49. Write a program that reverse the string.
# Ans. Method #1
string = "check"
revstring = string[::-1]
print(revstring)

Method #2
string ="check"
revstring =""
for char in string:
    revstring = char + revstring
print(revstring)

# 64. How to reverse a list?
# Ans. The reverse() method allows to reverse a list. For example,
#reverses a list
_list = [1,2,3,4,5]
_list.reverse()
print(_list)

# 65. How to sort a list?
# Ans. The sort() method is used to sort the elements of a list.
# Example:
_list = [5,4,3,2,1]
_list.sort()
print(_list)

#Sort list in reverse order
_list = [1,2,3,4,5]
_list.sort(reverse=True)
print(_list)

# 66. How to make a copy of a list?
# Ans. The copy() methods returns a copy of a list.
_list =[1,2,3,4]
_listcopy = _list.copy()
print(_listcopy)

# 67. How to find a number of elements in a list?
# Ans. 
The len() method returns the number of elements in the list.
_list = [1,2,3,46,7,8,90]
len(_list)

# 68. How to find the element with maximum value from a list?
# Ans. The max() method returns the element with maximum value.
_list = [1,2,3,46,7,8,90]
print(max(_list))

# How to find the element with minimum value from a list?
# Ans. The min() method returns the elements with minimum value.
_list = [1,2,3,46,7,8,90]
print(min(_list))

# 70. How to create an empty tuple?
# Ans. An empty tuple can be created by using tuple() method for example
_tuple = tuple()
print(_tuple)

# 71. How to create a tuple from an existing sequence?
# Ans. The tuple() method is used to create tuple by using a sequence as shown below:.
_tuple = tuple([1,2,3,4,5])
print(_tuple)

# How to find the element with minimum value from a list?
# Ans. The min() method returns the elements with minimum value.
_list = [1,2,3,46,7,8,90]
print(min(_list))

# 70. How to create an empty tuple?
# Ans. An empty tuple can be created by using tuple() method for example
_tuple = tuple()
print(_tuple)

# 71. How to create a tuple from an existing sequence?
# Ans. The tuple() method is used to create tuple by using a sequence as shown below:.
_tuple = tuple([1,2,3,4,5])
print(_tuple)

# 74. How to join two tuples?
# Ans. To join two tuples + operator is used.
# Example:
_tuple1 = (1,2,3)
_tuple2 = (4,5,6)
_tuple = _tuple1 + _tuple2
print(_tuple)

# 75. How to retrieve elements from a tuple?
# Ans. 
_tuple = (1,2,3,4,5,6)
for item in _tuple:
    print(item, end=',' )

# 76. How to find the index of an element that exists in a tuple?
# Ans. 
_tuple =(1,2,3,4,5)
_tuple.index(4)

# 77. How to find the occurrence of an element that exists in a tuple?
# Ans.
 _tuple =(1,2,3,4,5,2,3,2,4,2,5,6,2)
_tuple.count(2)

# 81. How to unpack a tuple?
# Ans. Tuple unpacking involves extracting values back from tuple into variables. Example,
_tuple = 1,2,3,4
a,b,c,d = _tuple
print(a,b,c,d)

#82. How to find number of elements in a tuple?
#Ans. 
_tuple = (1,2,3,46,7,8,90)
len(_tuple)

#83. How to find the element that has maximum value in a tuple?
#Ans. Method max() returns the elements that has maximum value in a tuple. Example:
_tuple = (1,2,3,46,7,8,90)
print(max(_tuple))

# 84. How to find the element that has minimum value in a tuple?
# Ans. Method min() returns the elements that has minimum value in a tuple. Example:
_tuple = (1,2,3,46,7,8,90)
print(min(_tuple))

# 89. How to traverse a dictionary?
# Ans. 
_dict = {'Afghanistan':'Kabul' ,'India':'New Delhi',
'UK':'London','USA':'Washington DC'}
for item in _dict.items():
    print(item)

# 90. How to create an empty dictionary?
# Ans.
_dict ={}
print(_dict)

# 91. How to add an item to a dictionary?
# Ans. 
_dict = {}
_dict['Afghanistan']='Kabul'
_dict['India']='New Delhi'
print(_dict)

# 92. How to get all the items of a dictionary?
# Ans. _dict = {'Afghanistan':'Kabul' ,'India':'New Delhi'}
# The function items() return a new view of the dictionary’s items (key, value). The items() can be used to
retrieve items(key-value pair).
for item in _dict.items():
print(item)

# 93. How to retrieve all the keys from a dictionary?
# Ans. keys() method is used to retrieve all the keys from the dictionary.
_dict = {'Afghanistan':'Kabul' ,'India':'New Delhi',
'UK':'London','USA':'Washington DC'}
for key in _dict.keys():
    print(key)
    
# 94. How to get all the values from a dictionary?
# Ans. values() method is used to retrieve all the values from a dictionary.
_dict = {'Afghanistan':'Kabul' ,'India':'New Delhi',
'UK':'London','USA':'Washington DC'}
for value in _dict.values():
    print(value)

# 95. How to display key and value from a dictionary?
# Ans. To display key and value from a dictionary:
_dict = {'Afghanistan':'Kabul' ,'India':'New Delhi',
'UK':'London','USA':'Washington DC'}
for key in _dict.keys():
    print(key , _dict.get(key))

#98. How to change the value of a key?
#Ans. 
_dict = {'Australia':'Sydney'}
_dict['Australia'] ='Canbera'
print(_dict)

# 99. How to clear all the items from the dictionary?
# Ans. The clear() method is used to remove all the items from the dictionary.
_dict = {'Afghanistan':'Kabul' ,'India':'New Delhi',
'UK':'London','USA':'Washington DC'}
_dict.clear()
print(_dict())

# 100. How to remove an item from a dictionary?
# Ans. pop(key[,d]) removes an item and returns its value. d is return if key is not found.
_dict = {'Afghanistan':'Kabul' ,'India':'New Delhi',
'UK':'London','USA':'Washington DC'}
print( _dict.pop('Afghanistan'))

_dict = {'Afghanistan':'Kabul' ,'India':'New Delhi',
'UK':'London','USA':'Washington DC'}
print(_dict.popitem())

# 96. How to retrieve the value of a key?
# Ans. The get() method is used to retrieve the value if key is passed as an argument.
# get(key[,d]) returns the value of the key. If key doesn’t exists, it returns (default is None).

_dict = {'Afghanistan':'Kabul' ,'India':'New Delhi',
'UK':'London','USA':'Washington DC'}
print(_dict.get('India'))

# 97. How to remove/delete an item from a dictionary?
# Ans. 
_dict = {'Afghanistan':'Kabul' ,'India':'New Delhi',
'UK':'London','USA':'Washington DC'}
del _dict['Afghanistan']
print(_dict)

# 102. How to merge two dictionaries?
# Ans. We can use update ([dict]) method to merge two dictionary; it will overwrite the existing keys.
_dict1 ={1:'a',2:'e'}
_dict2 ={3:'i',4:'o',5:'u'}
_dict = _dict1.update(_dict2)
print(_dict)

# 103. How to create a copy of a dictionary?
# Ans. The copy method is used to copy a dictionary, as shown below:
_dict ={1:'a',2:'e',3:'i',4:'o',5:'u'}
_dictcopy = _dict.copy()
print( dictcopy )

Programming Questions and Answers

1. Write a program to check if a year is a leap year or not.
Ans. 
year = int(input("Enter a year: "))
if (year % 4) == 0):
#If year is divisible by 100 it must be divisible by 400 as well
    if (year % 100 and year % 400 ) == 0:
        print( str(year) +" is a leap year")
    else:
        print( str(year) +" is not a leap year")
else:
    print(str(year) +" is not a leap year")

# 2. Find the output of the following programs.
# Ans. a) 
for i in [1,2,3,4,5,6,7,8,9,10]:
print(i, end ="\t")

b)
string = "Python is fun"
#split() functions split a string into
words words = string.split(" ")
for word in words:
    print(word)

c) 
for i in range(1,11):
        for j in range(1,6):
            print(i * j, end="\t")
        print("\n")
        
        
# 3. Write a program to add natural numbers up to n terms using while loop and for loop.
# Ans. # sum = 1+2+3+...+n using while

num = int(input("Enter numbers of terms:"))
# initialize sum and the counter

sum = 0
i = 1

while i <= num:
    sum = sum + i
    # increment counter
    i = i+1
    
# print the sum
print("The sum is", sum)

# sum = 1+2+3+...+n using for loop
num = int(input("Enter numbers of terms:"))
# initialize sum
sum = 0
for i in range(1, num+1):
    sum = sum + i
# print the sum
print("The sum is", sum)

# 4. Write a program that counts the number of digits and letters in a string.
# Ans. string = "room no 420"
digits=letters=0
for char in string:
    if char.isdigit():
        digits=digits+1
    elif char.isalpha():
        letters=letters+1
    else:
        pass
        
print("Number of Letters", letters)
print("Number of Digits", digits)

# 5. Write a program that converts a list of words to a string.
# Ans. Example 1:
_list=['P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'f', 'u', 'n', '!']
string = ""

for char in _list:
    string += char
print(string)

Example 2:
_list =['Python', 'is', 'fun!']
#using join to convert list to string
string = " ".join(_list)
print(string)

# 6. Write a program that counts the frequency of each letter in a string.
# Ans. 
string ="google.com"
#dictionary to store letter and its frequency
string="google.com"
freq = {}
for char in string:
    if char in freq:
# if a letter exists in the add the frequency of letter
    freq[char] += 1
# if a letter does exist frequency of letter is one else:
    else:
    freq[char] = 1

#print letter and its frequency
for key, value in freq.items():
    print(key , value)

