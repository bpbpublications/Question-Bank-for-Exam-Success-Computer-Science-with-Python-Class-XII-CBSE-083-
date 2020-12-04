Long Questions and Answers
4. Write a program that searches an item in a list.
Ans. #program linear search
def linearsearch( lst, element):
	for index in range(len(lst)):
		if( lst[index] == element ):
			return index+1
	#if element not found return -1
	return -1
	
l = [ 23, 56, 45, 67, 89, 5 , 9, 39, 99]
location = linearsearch(l, 9)
if(location > 0):
print("The element found at location " + str(location))
else:
print("Element not found !!!")


# 5. Write a program that performs the binary search.
# Ans. # Program for recursive binary search and returns the index
# if a search key present otherwise -1
def binSearch(_list, lowrange, upprange, searchkey):
    # Check base case
    if upprange >= lowrange:
        mid = 1+(upprange - lowrange)//2
        # Checks if an element is present in the middle
        if _list[mid] == searchkey:
            return mid
        # If element is smaller than mid, it may present in upper sublist
        elif _list[mid] > searchkey:
            return binSearch(_list, lowrange, mid-1, searchkey)
        # search in upper sublist
        else:
            return binSearch(_list, mid + 1, upprange, searchkey)
    else:
        # Element is not present in the list
        return -1
        
_list = [2, 3, 5, 7,10, 40 ]
searchkey = 10
# Function call
result = binSearch(_list, 0, len(_list)-1, searchkey)
if (result != -1):
    print ("Element is present at index % d" % result )
else:
    print ("Element is not present in list')
    
    
# 9. Explain how are items deleted from the list in python?
# Ans. The below code demonstrates to remove an element from the list: Consider an example,To delete the element 4 from the list:
_list = [1,4,6,7,8,0,9]
_list[:1] + _list[2:]
[1, 6, 7, 8, 0, 9]
#To delete an element from a list:
def del_listItem(_list, element):
    found = False
    for index in range(len(_list)):
        if( _list[index] == element ):
            found = True
            del _list[index]
            break
    return found
    
l = [1,4,6,7,8,0,9]
element = 4
#checks if an element is deleted
isdeleted = del_listItem(l, element)
if(isdeleted == True):
    print (str(element) + " is deleted ")
else:
    print (str(element) + " not found in list ")
print(l)

# 10. How to insert an element into a sorted list?
# Ans. The Insort() method of the Bisect module allows placing an element in the sorted list as shown in below code:
import bisect
def insert_sortlist(_list, num):
bisect.insort(_list, num)
return _list
_list = [1, 2, 4]
num = 3
print(insert_sortlist(_list, num))

14. How pop() method is implemented?
Ans. stack =[]
def pop():
return stack.pop()
15. Implement a pop() method that checks if the list is empty?
Ans. stack =[]
def pop():
#if stack is empty returns none
if(stack == []):
return None
else:
return stack.pop()
# 16. Write a program that implements the stack.
# Ans. #implements stack.py (module)
stack =[]
def push(val):
    # add element to the end of stack (top)
    stack.append(val)
    
def pop():
    #if stack is empty returns none
    if(stack == []):
        return None
    else:
        return stack.pop()

#Implementing the stack in stackaap.py
Stackapp.py
import stack
stack.push(10)
stack.push(20)
print(stack.pop())
print(stack.pop())

17. How is the peek method implemented?
Ans. Peek method returns the element without popping (deleting) it:
def peek():
    if ( stack == []):
        return None
    else:
    #return last element
        return stack[len(stack)-1]

# 18. Explain the use of the stack with an example.
# Ans. To explain the use of the stack, consider an example where we can use the stack to convert a decimal number into a binary equivalent (a string representation). To convert a decimal number to a binary
# number, the number is divided until it is greater than 1. It keeps the remainder and arranges the remainder in reverse order. Here, the remainder is stored in the stack because the binary number is in the reverse order of the remainder.

stack =[]
def dec_binary(num):
    if num > 1:
        dec_binary(num//2)
        stack.append(str(num % 2))
        
num = 10
dec_binary(num)
#convert stack to string and print binary string
print("The binary of ", str(num) , " is ", ''.join(stack))

# 20. Write a program that evaluates a postfix expression.
# Ans. 
exp="2 3 + "
resultstk=[]
res=0
for i in range(len(exp)):
    if(exp[i].isdigit()==True):
        resultstk.append(int(exp[i]))
    elif(exp[i]=='*'):
        operand1=resultstk.pop()
        operand2 =resultstk.pop()
        res = operand2 * operand1
        resultstk.append(res)
    elif(exp[i]=='+'):
        operand1=resultstk.pop()
        operand2=resultstk.pop()
        res = operand2 + operand1
        resultstk.append(res)
    elif(exp[i]=='-'):
        operand1=resultstk.pop()
        operand2=resultstk.pop()
        res = operand2 - operand1
        resultstk.append(res)
    elif(exp[i]=='/'):
        operand1=resultstk.pop()
        operand2=resultstk.pop()
        res=operand2/operand1
        resultstk.append(res)
        
print('The result is',resultstk[0])


#24. Write a program that implements the queue.
# Ans. 
queue =[]
def enqueue(val):
    # add element to the end of stack (rear)
    queue.append(val)
def dequeue():
    #if stack is empty returns none
    if(queue == []):
        return None
    else:
        return queue.pop(0)
        
def printqueue():
    if ( queue == []):
        print ("Queue Empty...")
        return
    else:
        for element in queue:
        print(element, end=", ")
    print()

import queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Printing list")
queue.printqueue()
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

