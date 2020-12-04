Short Questions and Answers
# 1. How to create a module? Explain it with an example.
# Ans. A module is a file which is saved as .py extension. It can contain functions, variable, and class. Let’s create a module that implements stack and its functions as shown below and save this file as DSstack.py module:

stack =[]
def push(val):
    stack.append(val)
    
def pop():
    if(len(stack) == 0):
        print("Stack Empty")
        return None
else:
    return stack.pop()

def peek():
    if(len(stack) == 0):
       print("Stack Empty")
        return None
    else:
        return stack[len(stack)-1]

Long Questions and Answers
3. Explain how the module is created and used with an example.
Ans. Modules are created by saving a file under the extension .py. For example, this is a module DSstack.py:
stack =[]
def push(val):
    stack.append(val)
def pop():
    if(len(stack) == 0):
        print("Stack Empty")
        return None
    else:
        return stack.pop()
        
def peek():
    if(len(stack) == 0):
        print("Stack Empty")
        return None
    else:
    return stack[len(stack)-1]
    
#Create the file that evaluates postfix expression:
#import DSstack
from DSstack import *
expression = []
while True:
    item=input("Enter a character")
    if (item==''):
        break
    expression.append(item)
    
#Adding items to stack one by one
print(expression) #Print expression

#loop for checking each character one by one
for i in range(len(expression)):
    if(expression[i].isdigit()==True):
        #if character is digit push it to stack
        push((int(expression[i])))
            
    elif(expression[i]=='*'):
        operand1=pop()
        operand2=pop()
        res = operand2 * operand1
        push(res)
        
    elif(expression[i]=='+'):
        operand1=pop()
        operand2=pop()
        res = operand2 + operand1
        push(res)
        
    elif(expression[i]=='-'):
        operand1=pop()
        operand2=pop()
        res = operand2 - operand1
        push(res)
            
    elif(expression[i]=='/'):
        operand1=pop()
        operand2=pop()
        res=operand2/operand1
        stack.push(res)
            
print('Postfix expression is',stack[0])