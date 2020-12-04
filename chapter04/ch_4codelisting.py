Programming Questions and Answers

# 5. Write a program that counts the frequency of each character in a string.
# Ans. 
string="google.com"
dict = {}
keys = dict.keys()

for ch in string:
    if ch in keys:
        dict[ch] += 1
    else:
        dict[ch] = 1
        
print(dict)    

# 6. Write a program that counts the frequency of each word in a string.
# Ans. 
string= "the quick brown fox jumps over the lazy dog."
wordcounts = {}
# split a sentence into words
words = string.split()
for word in words:
# if word already in dictionary add its frequency
    if word in wordcounts:
        wordcounts[word] += 1
    else:
        wordcounts[word] = 1
            print( wordcounts)


# 7. Write a program that reverses each word of a string.
# Ans. 
string = "This is string"
# reversed() function returns reverse the string
string = reversed(string)
string =''.join(string)
print(string)


# 8. Write a program that counts the number of vowels in a given text.
# Ans.
vowels = "aeiouAEIOU"
vowelcount=0
string="the quick brown fox jumps over the lazy dog."
for ch in string:
    if(ch in vowels):
        vowelcount+=1
        
print(" The vowel count is " , vowelcount)

# 9. Write a program to remove spaces from a given string.
# Ans. 
string =" This is a string "
string = string.replace(' ','')
print(" The string without spaces")
print(string)

# 10. Write a program that computes the sum of digits in a string.
# Ans. 
string="1234abcd56"
sum_digit = 0
for ch in string:
    if ch.isdigit() == True:
        digit = int(ch)
        sum_digit+= digit

print("The sum is ", sum_digit)

# 11. Write a program that counts lowercase, uppercase, other characters, and numeric values in a given string.
# Ans. 
string="Addressis123@pin110010"
upper_cnt, lower_cnt, number_cnt, other_cnt = 0, 0, 0, 0
for ch in string:
    if ch.isupper():
        upper_cnt += 1
    elif ch.islower():
        lower_cnt += 1
    elif ch.isdigit():
        number_cnt += 1
    else:
        other_cnt += 1
        
print('\nUpper case characters: ',upper_cnt)
print('Lower case characters: ',lower_cnt)
print('Digit characters: ',number_cnt)
print('Other characters: ',other_cnt)

#Method 2:
#Check if characters are same from right and left side of the string
li= -1
palindrome=True
for i in range(len(string)//2):
    if(string[i]== string[li]):
        li-=1
    else:
        palindrome =False
        break
        
print(string +" is palindrome: "+ str(palindrome))

# 12. Write a program that checks if a string is a Palindrome.
# Ans. #Method 1: if string and its reverse are same, it is palindrome
string="nitin"
palindrome=True
if( string == string[::-1]):
    print("Palindrome")
else:
    print("Not a palindrome")
    
    