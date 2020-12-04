Very Short Questions and Answers
# 14. Write a recursive function for calculating factorial of a number.
# Ans. 
def _fact(num):
# Base case: 1! = 1
    if num == 1:
    return 1
# Recursive case: num! = num * (num-1)!
    else:
        return num * _fact(num-1)

Short Questions and Answers

# 1. Write a python function that returns the sum of all the elements of the list using recursion.
# Ans. Find the sum of the all the elements of the list using recursion function:
lst = [1,2,3,4,5,6,7,8]

#Base case: If list is empty sum is zero
#Recursive case: Sum of 1st element + sum of rest of the elements
def sum_list(lst):
    #base case
    if(len(lst)==0):
        return 0
    else:
    #recursive case sum + first element+ sum of the remaining list
    return lst[0] + sum_list(lst[1:])

print(sum_list(lst))

# 2. Write a function that prints the multiplication of digits of a number using recursion.
# Ans. Multiplication of digits by using the recursion function:
def multiply_digits(num):
    #base case if all digits are exhausted number become zero returns 1
    if (num == 0):
        return 1
    else:
    #recursive case last digit * rest of the digits
    return num%10 * multiply_digits(num//10)
    
print(multiply_digits(1357))

# 4. Write a Python function to calculate the GCD of two numbers.
# Ans. 
def fngcd(num1, num2):
    if(num2 == 0):
        return num1
    else:
        return fngcd(num2, num1 % num2)

# 5. Write a function that recursively calculates the sum of below series.
# 12 + 22 + 32 + 42 + 52 + …
# Ans. 
def sqrseries(n):
    if( n == 1 ):
        return 1
    else:
        return n * n + sqrseries(n-1)
        
print(sqrseries(10))

Long Questions and Answers
# 1. Write a function that recursively reverses a string. Explain how a recursive solution works.
# Ans. Solution 1:
def rev_str_rec(string):
    #base case if length is 0 return the string
    if(len(string)==0):
        return string
     else:
    #recursive case add last character to string in front of the string
        return string[-1] + rev_str_rec(string[:-1])
        
print(rev_str_rec("narayan"))   
        
Solution 2:
def rev_recursive(string):
    #base case
    if len(string) == 0:
        return string
    else:
    #recursive case add first character to the last of the string
        return rev_recursive(string[1:]) + string[0]
    
a = "narayan"
print(rev_recursive(a))



