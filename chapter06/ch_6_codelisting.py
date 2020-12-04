Short Questions and Answers

# 2. Explain how to write to a binary file with an example.
# Ans. 
filepath = "F:\\files\\quotes.dat"
mode = "wb"
string="Successful and unsuccessful people do not vary greatly\
in their abilities. They vary in their desires to reach their potential \
- John Maxwell"
bytestream = bytearray(string,'ascii')
with open(filepath,mode) as _wfile:
    _wfile.write(bytestream)
print("Data is written to the filepath")

#Alternative we can write code as:
_wfile = open(filepath,mode)
_wfile.write(bytestream)
_wfile.close()

# 3. Explain how to read a binary file with an example.
# Ans. 
filepath = "F:\\files\\quotes.dat"
mode="rb"
data=""
with open(filepath,mode) as _wfile:
    data = _wfile.read()
    
print(data.decode('ascii'))
#The decode() method is used to convert the string into the ascii format.


# 5. Illustrate with the help of an example, how to write and read a list of integers?
# Ans. Example: Write a list of integers to a binary file

f=open("F:\\files\\list.dat","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.close()

#The list() function converts the byte array to list.
f=open("F:\\files\\list.dat","rb")
#Convert byte array to list
num= list(f.read())
print (num)
f.close()

# 6. Illustrate with the help of example how to write and read tuple of integers.
# Ans. Example: Write to a Binary File
f=open("F:\\files\\tuple.dat","wb")
num=(5, 10, 15, 20, 25)
arr=bytearray(num)
f.write(arr)
f.close()
#The tuple() function converts the bytearray to list

f=open("F:\\files\\tuple.dat" ,"rb")
#Convert byte array to list
num= tuple(f.read())
print (num)

# 7. Illustrate how to append content at the end of the binary file?
# Ans. To append content at the end of binary file, open file in append mode and add the content as demonstrate in the below example.
# Example: Write to a Binary File
f=open("F:\\files\\append.dat","wb")
string="Live as if you were to die tomorrow.\nLearn as if you were to live forever.\n"
f.write(bytearray(string,'ascii'))
f.close()
#Append to the binary file

f=open("F:\\files\\append.dat","ab")
newstring="-Mahatma Gandhi"
f.write(bytearray(newstring,'ascii'))
f.close()

#Example: Reading a Binary File
f=open("F:\\files\\append.dat","rb")
string=f.read()
print (string.decode('ascii'))
f.close()

# 8. Find the size of the below file.
# The text in the file is:
# Live as if you were to die tomorrow.
# Learn as if you were to live forever.
# —Mahatma Gandhi
# Ans. 
_file = open("F\\files\\quotes.dat","rb")
_file.read()
print("The total number of characters in file " , _file.tell())

Long Questions and Answers
# 1. Write a function that replace a word in a binary file.
# Below is the code that creates a binary file and replaces a word in it:

with open('F:\\files\\file.dat', 'wb') as file:
    # Write byte arrays to file
    file.write(b"This is mumbai\n")
    file.write(b"This is delhi\n")
    file.write(b"This is jaipur\n")

#Ans. # Function to update the content of binary file
RecordFound = 0
def update_binfile(word, newword):
    # store each word after reading from the file
    string = b""
    # Flag variable to check if the record is found or not
    
    # Open the file in read and binary mode
    with open('F:\\files\\file.dat', 'rb+') as file:
        filepointer = 0
    # Reading file character by character
        string = file.read(1)
        data_infile = string
        # Iterate loop until end of file
        while data_infile:
            data_infile = file.read(1)
        #print(data_infile)
        # Checking if the space or new line is reached
            if data_infile == b" " or data_infile== b"\n":
                if string == word:
                # Moving the file pointer to the read last word
                    file.seek(filepointer)
                # Updating the content of the file
                    file.write(newword)
                    RecordFound = 1
                    break
                else:
                    # store the current position of the file pointer
                    filepointer = file.tell()
                    data_infile = string = file.read(1)
            else:
            # Storing character until end of space or line
                string += data_infile
                continue
        
if RecordFound == 1:
    print("Record is updated")
else:
     print("Record not found")
     
word = input("Enter the word to be replaced: ").encode()
newword = input("\nEnter the new word: ").encode()
update_binfile(word, newword)

# 2. Write a function that search a word in a binary file.
# Ans. Below is the code that creates a file
with open('F:\\files\\file.dat', 'wb') as file:
    # Write byte arrays to file
    file.write(b" This is mumbai\n")
    file.write(b" This is delhi\n")
    file.write(b" This is jaipur\n")

# Flag variable to check if the record is found or not
RecordFound = 0
  
def Search_binfile(searchword):
    # store each word after reading
    # from the file
    string = b""

    # Open the file in read and binary mode
    with open('F:\\files\\file.dat', 'rb+') as file:
    # Reading file character by character
    string = file.read(1)
    data_infile = string
    # Iterate loop until end of file
    while data_infile:
        data_infile = file.read(1)
    # Checking if the space or new line is reached
        if data_infile == b" " or data_infile == b"\n":
            if string == searchword:
                RecordFound = 1
                break
            else:
                data_infile = string = file.read(1)
        else:
        # Storing character until end of space or line
            string += data_infile
            continue

if RecordFound == 1:
    print("Record Found")
else:
    print("Record not found")
searchword = input("\nEnter the word to be searched: ").encode()
Search_binfile(searchword)


# 3. Illustrate the use of functions seek() and tell() with the help of an example.
# Ans. The below code demonstrate the use of the seek() and tell():
# string = b"Your time is limited, so don't waste it living someone else's life.\nDon't be trapped by dogma\n- which is living with the results of other people's thinking.\n- Steve Jobs"
_file = open("check.txt","wb")
_file.write(string)
_file.close()
_file = open("check.txt","rb")
print("Name of the File : ",_file.name)
str=_file.read(10)
print("Position of file pointer after reading 10 characters ")
pos= _file.tell()
print("Current Position : ",pos)
#offset form the beginning of the file
pos = _file.seek(0,0)
print("Setting Pointer back to Top")
print("The current position is ", pos)
_file.seek(156,0)
print(_file.read().decode("ascii"))
_file.close()
print("The current position is ", _file.tell())
#offset form the current position of the file
_file.seek(1,1) BPB Publications

print(_file.read().decode("ascii"))
_file.close()
