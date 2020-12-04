Long Questions and Answers
# 3. How to write text for a file, explain it with an example.
# Ans. Here’s is the text we want to write to file.
# Dream it. Wish it. Do it.
# Success doesn’t just find you. You have to go out and get it.
# Push yourself, because no one else is going to do it for you.
# Let’s see an example of writing content to a file:
#open a file in write mode
_file = open('f:\\examples\\quotes.txt', 'w')
_file.write('Dream it. Wish it. Do it.\n')
_file.write('Success doesn't just find you. You have to go out and get it.\n')
_file.write('Push yourself, because no one else is going to do it for you.')
_file.close()

#Let’s see another example on how to write using the writelines() method:
_file = open('f:\\examples\\quotesall.txt', 'w')
_file.writelines ('Dream it. Wish it. Do it.\nSuccess doesn't just find you. You have to go out and get it.\nPush yourself because no one else is going to do it for you.')
_file.close()

#Let’s see another example
_file = open('f:\\examples\\quotesalllines.txt','w')
textlist= ['Dream it. Wish it. Do it.\n' \
'Success doesn't just find you. You have to go out and get it.\n' \
'Push yourself, because no one else is going to do it for you.']
for line in textlist:
#use print method to use the print line.
    print (line , file= _file)
_file.close()

#Let’s see one more example on how to read content in the file using a with keyword:
textlist= ['Dream it. Wish it. Do it.\n' \
'Success doesn't just find you. You have to go out and get it.\n' \
'Push yourself, because no one else is going to do it for you.']
with open('f:\\examples\\quotesalllines1.txt','w') as _file:
for line in textlist:
print ( line , file= _file )

# 5. How to read the content of a file line by line and print it?
# Ans. Let’s see an example:
_file = open('f:\\examples\\quotes.txt','r')
# read the line
line = _file.readline()
# keep reading one line at a time, until file is empty
while line:
    print(line,end='')
# use realine() to read next line
    line = _file.readline()
_file.close()

#Let’s see an another example:
_file = open('f:\\examples\\quotes.txt','r')
while True:
    # read line
    line = _file.readline()
    print(line,end='')
    # check if a line is not empty
    if not line:
        break
_file.close()

#Let’s see an example to use readlines and iterators to print line by line:
_file = open('f:\\examples\\quotes.txt','r')
# return list of lines
filecontent = _file.readlines()
#iterate list to print line by line
for line in filecontent:
    print(line,end='')
_file.close()

# 6. Write a program that counts the number of words in a file.
# Ans. 
wordcount = 0
_file = open("f:\\examples\\quotes.txt", 'r')
wordcount = 0
_lines = _file.readlines()
for line in _lines:
#split the line into list of words
    words = line.split()
#count the number or word in line
    wordcount += len(words)

print("The number of words in file:")
print(wordcount)

#Let’s see another example:
_file = open("f:\\examples\\quotes.txt", 'r')
#read the entire text and split it into words
text = _file.read().split()
print("The number of words are "+ str(len(text)))

# 7. Write a program that counts the number of characters in a text file.
# Ans. 
chcount = 0
_file = open("f:\\examples\\quotes.txt", 'r')
ch =_file.read(1)
if ch:
    chcount+=1
while True:
    if not ch:
        break
    else:
        chcount+=1
        
    ch =_file.read(1)
    

print("The number of characters in file:")
print(chcount)
_file.close()

# 8. Write a program that counts the number of vowels in a text file.
# Ans. 
vowelcount = 0
_file = open("f:\\examples\\quotes.txt", 'r')
ch =_file.read(1)
while True:
    if not ch:
        break
    else:
        if( ch in 'aeiouAEIOU' ):
            vowelcount+=1
    ch =_file.read(1)
    
print("The number of Vowels in file:")
print(vowelcount)


# 9. Write a program that counts the number of word ‘it’ in a file.
# Ans. 
_file = open("f:\\examples\\quotes.txt", 'r')'
searchword = input("Enter the word to be searched: " )
#split the text into list of words and count the
# occurrence of the search word using count() method
text =_file.read().split()
print("The word " + searchword +" found "+ str(text.count(searchword)) +" times.")

# 10. Write a program that searches a word and replaces it with another word in a text file.
# Ans. Let’s find and replace it with It:
_file = open("f:\\examples\\quotes.txt", 'r')
text =_file.read()
#read the content
searchword = input("Enter the word to be searched: ")
replaceword = input("Enter the word to be replaced: ")
#replaced the word
text = text.replace(searchword, replaceword)
_file.close()
#write the updated text
_file = open("f:\\examples\\quotesreplaced.txt", 'w')
_file.write(text)
_file.close()
# Read again after changes and print it
print("File after update")
_file = open("f:\\examples\\quotes.txt", 'r')
text =_file.read()
print(text, end='')
_file.close()
print("End of update")

# 11. Write a program that finds and prints the longest line in the file.
# Ans. Let’s assume we have the following content in quotes.txt file:
# Dream it. Wish it. Do it.
# Success doesn't just find you. You have to go out and get it.
# Push yourself, because no one else is going to do it for you.

_file = open("f:\\examples\\quotes.txt", 'r')
text = _file.readlines()
largestline =''
for line in text:
    if( len(line) > len(largestline)):
        largestline = line

print("The largest line is")
print(largestline)

# 12. Write a program that finds and prints the longest word in the file.
# Ans. 
_file = open("f:\\examples\\quotes.txt", 'r')
wordlist = _file.read().split()
largestword=''
for word in wordlist:
    if( len(word) > len(largestword) ):
        largestword = word
        
print(''The largest word is '')
print(largestword)

# 13. Write a program that copies the content from one text file to another file.
# Ans. Let’s consider the following as input file:
# Dream it. Wish it. Do it.
# Success doesn't just find you. You have to go out and get it.
# Push yourself, because no one else is going to do it for you.

_file = open("f:\\examples\\quotes.txt", 'r')
text = _file.read()
_file.close()
_filecopy = open("f:\\examples\\quotescopy.txt", 'w')
_filecopy.write(text)
_filecopy.close()

# 14. Write a program that copies the content from one text file to another file excluding the word ‘it’.
# Ans. 
_file = open("f:\\examples\\quotes.txt", 'r')
lines = _file.readlines()
_file.close()
_file = open("f:\\examples\\quotes.txt", 'r')
_filecopy = open("f:\\examples\\quotesreplaced.txt", 'w')

for line in lines:
    if ( 'it' in line ):
    #replace 'it' with ''
    line= line.replace('it', '')
    _filecopy.write(line)

_file.close()
_filecopy.close()

# 15. What is the output of the following code?
# Ans. The file AlbertEinstein.txt has the following text:
# "Intellectuals solve problems, geniuses prevent them, weak people revenge. Strong people forgive. Intelligent people ignore. Most people say that it is the intellect which makes a great scientist. They are wrong: it is character"
_file = open("f:\\examples\\AlbertEinstein.txt", 'r')
text = _file.readline().split()
print(text[0])
_file.close()

# 17. Write a program to display all the lines along with line numbers.
# Ans. 
import os
import sys
_file = open("f:\\examples\\quotes.txt", 'r')
count=0
for line in lines:
    count+=1
    print(count ,":", line, file=sys.stdout)

_file.close()

# 18. Write a program that prints the last two lines form a file.
# Ans. 
_file = open("f:\\examples\\quotes.txt", 'r')
lines = _file.readlines()
print("Printing last two lines")
print(lines[-2],end='')
print(lines[-1], end='')

# 19. Write a program that searches a name that exists in a .csv file as shown below.
# Ans. The file users.csv has first name, last name, password, email address, phone number, user id,
# It has the following rows:
# Narayan,Sharma,1234,narayan@test.com,91-999-999-9999,101
# Mukesh,Verma,1235,mukesh@test.com,91-999-999-9998,101
# Ramesh,Kumar,3478,ramesh@test.com,91-999-999-9997,101
# Vikram,Sethi,4532,vikram@test.com,91-999-999-9996,101
# Savita,Mahajan,2343,savita@test.com,91-999-999-9995,101
# Let’s write a program to find a name in the file:

_file = open("f:\\examples\\users.csv", 'r')
name = input("\n Enter name to be searched")
lines = _file.readlines()
_file.close()
match =False

for line in lines:
    if name in line:
        match = True
        break
        
if(match):
    print(name + " Name found in file")
else:
    print(name + " Name is not found in file")

_file.close()

20. Write a program to delete a record from a file.
Let’s see the code to delete a record from a file:
_file = open("f:\\examples\\users.csv", 'r')
_temp = open("f:\\examples\\temp.csv", 'w')
name = input("\n Enter name to be deleted: ")
lines = _file.readlines()
_file.close()
match =False
for line in lines:
    if name in line:
        pass
    else:
        _temp.write(line)
_temp.close()

#remove
os.remove("f:\\examples\\users.csv")
os.rename("f:\\examples\\temp.csv","f:\\examples\\users.csv")

# 21. Write a program that copies a line that contains the word “Athletics” from the file sportdata.
# txt and copy it to the file called Atheletics.txt
# Ans. Here’s the data stored in file sportsdata.txt:
# Vikas Jain Badminton national 34 51
# Manish Verma Athletics international 10 18
# Dinesh Agarwal TennisTable national 20 13
# Anil Jain Athletics international 50 6
# Mohan Prakash Athletics national 34 51
# Manish Dev Athletics national 68 51
# Varun Yadav TableTennis national 22 32
#Let see the program to perform the same:

_file = open("f:\\examples\\Sportsdata.txt", 'r')
_temp = open("f:\\examples\\Atheletics.txt", 'w')
lines = _file.readlines()
_file.close()
for line in lines:
        if 'Atheletics' in line:
            _temp.write(line)
_temp.close()
