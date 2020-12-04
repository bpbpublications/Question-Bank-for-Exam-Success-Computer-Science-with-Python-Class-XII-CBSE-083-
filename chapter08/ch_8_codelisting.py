# 4. Illustrate how to add rows in a CSV file with an example?
# Ans. 
import CSV
_file =open('F:\\files\\employee1.CSV', mode='w',newline='')

with _file:
    employee_writer = CSV.writer(_file, delimiter=',', quotechar='"')
    employee_writer.writerow(['Vijay Shankar', 'Accounting', 'November'])
    employee_writer.writerow(['Kiran Kumar', 'IT', 'March'])
    
# 5. How to write tuple(s) to the CSV file?
# Ans. Writing tuple to the CSV tuple is simple, tuple(s) can be written to CSV file after converting it to the list.
# For example:
import CSV
_file =open('F:\\files\\employee1.CSV', mode='w',newline='')
employee1 = ('Vijay Shankar', 'Accounting', 'November')
employee2 = ('Kiran Kumar', 'IT', 'March')
with _file:
    _writer = CSV.writer(_file, delimiter=',', quotechar='"')
    _writer.writerow(list(employee1))
    _writer.writerow(list(employee2))
    
# 6. How to write multiple rows to the CSV file?
# Ans. The Writerows() function accepts a list of lists and write all the rows at once.
import CSV
with open('F:\\file\\employee2.CSV', mode='w', newline='') as _file:
_writer = CSV.writer(_file, delimiter='|', quotechar='"')
_writer.writerows(
[
['Vijay Shankar', 'Accounting', 'November'] ,
['Kiran Kumar', 'IT', 'March']
]

# 7. How to write a dictionary to a CSV file?
# Ans. The DictWriter() function is used to write the dictionary to the CSV file. For example:
import CSV
with open('F:\\files\\names.CSV',mode='w',newline='') as _f :
    #Creating header for the file
    fnames = ['first_name', 'last_name']
    writer = CSV.DictWriter(_f, fieldnames=fnames)
    writer.writeheader()
    writer.writerow({'first_name' : 'Khaniya', 'last_name': 'Kumar'})
    writer.writerow({'first_name' : 'Zoya', 'last_name': 'Khan'})
    writer.writerow({'first_name' : 'Julia', 'last_name': 'Roberts'})
    )
    
# 7. How to write multiple dictionaries by using function writerows() to the CSV file?
# Ans. 
import CSV
with open('F:\\files\\students.CSV',mode='w',newline='') as _f :
    fnames =['Id','Name','Course','Location','Block']
    writer = CSV.DictWriter(_f, fieldnames=fnames)
    writer.writeheader()
    writer.writerows([
    {'Id': '0021', 'Name': 'Vijay', 'Course': 'C++', 'Location': 'CV Raman
    Hall', 'Block':'A'},
    {'Id': '0101', 'Name': 'John', 'Course': 'Android', 'Location': 'Vivekanand
    Hall', 'Block': 'C'},
    {'Id': '0102', 'Name': 'Arun', 'Course': 'Python', 'Location': 'Albert
    Eisten Hall', 'Block':'A'},
    {'Id': '0010', 'Name': 'Shaun', 'Course': 'C', 'Location': 'Mahatma Ghandi
    Hall', 'Block': 'B'}])

# 8. How to create a tab separated file?
# Ans. To create the tab separated file, the TAB {‘\t’} is used as a separator. For example:
import CSV
_file =open('F:\\files\\employeetab.CSV', mode='w',newline='')
with _file:
    _writer = CSV.writer(_file, delimiter='\t', quotechar='"')
    _writer.writerow(['Vijay Shankar', 'Accounting', 'November'])
    _writer.writerow(['Kiran Kumar', 'IT', 'March'])
    
# 9. How to read a CSV file?
# Ans. The reader() method of the CSV module is used to fetch all the rows from a CSV file for example
import CSV
_file =open('F:\\files\\employee1.CSV', mode='r')
with _file:
    _reader = CSV.reader(_file)
    for row in _reader:
    # Print each row at a time
    print(row)

# 10. Explain how to read a CSV file with delimiter “|” ?
# Ans. 

import CSV
_file = open("F:\\files\\employee2.CSV","r")

with _file:
    _reader = CSV.reader(_file,delimiter="|")
    for row in _reader:
    # The row variable is a list that represents a row in CSV
        print(row)

# 11. How to read CSV file using function DictReader()?
# Ans. 
with open('F:\\files\\names.CSV',mode='r') as _f :
    dict_reader = CSV.DictReader(_f)
    # iterate over each line as a ordered dictionary
    for row in dict_reader:
        # The row variable is a dictionary
        print(dict(row))

# 12. Explain how to print the file header with an example?
# Ans. 
import CSV
# open file in read mode
with open('F:\\files\\students.CSV', 'r') as read_obj:
    # Pass the file object to DictReader() to get the DictReader object
    CSV_dict_reader = CSV.DictReader(read_obj)
    # Get column names from a CSV file
    column_names = CSV_dict_reader.fieldnames
    print(column_names) 
    
# 13. Explain how to fetch a column using column name from a CSV file?
# Ans. The column name is used to fetch a column from a row. Row is a combination of columns. For example
# row['Id'] is the first field of the row. Below example demonstrate how to fetch a column 
from a CSV file:
with open('F:\\files\\names.CSV',mode='r') as _f :
    dict_reader = CSV.DictReader(_f)
    # Iterate over each line as a ordered dictionary
    for row in dict_reader:
        print(dict(row))
    
# 14. How to read tab separated file?
# Ans. To read the tab separated file the character (“\t” ) is used as delimiter. For example:
_file = open("F:\files\employeetab.CSV","r")
with _file:
    _reader = CSV.reader(_file,delimiter="\t")
for row in _reader:
    print(row)

Long Questions and Answers   
1. Write a program that copy one CSV file to another CSV file?
Ans. 
import CSV
# open file in read mode
_copyfile =open('F:\\files\\studentscopy.CSV',mode='w',newline='')
_file= open('F:\\files\\students.CSV', 'r')
# Pass the file object to DictReader() to get the DictReader object
_dict_reader = CSV.DictReader(_file)

# Get column names from a CSV file
column_names = _dict_reader.fieldnames
writer = CSV.DictWriter(_copyfile, fieldnames= column_names)
writer.writeheader()
for row in _dict_reader:
# Write a row in CSV
    writer.writerow(dict(row))

_file.close()
_copyfile.close()


2. Write a program that deletes a record in the CSV file?
Ans. Steps to delete a record in CSV file:
 Open the source file in the read mode.
 Open another file in write mode and place the row if does not match the criteria.
 Delete the source file.
 Rename the other file to the source file.
import CSV
import os
with open('F:\\files\\studentdata.CSV',mode='w',newline='') as _f :
fnames =['Id','Name','Course','Location','Block']
writer = CSV.DictWriter(_f, fieldnames=fnames)
writer.writeheader()
writer.writerows([
{'Id': '0021', 'Name': 'Vijay', 'Course': 'C++', 'Location': 'CV Raman Hall',
'Block':'A'},
{'Id': '0101', 'Name': 'John', 'Course': 'Android', 'Location': 'Vivekanand Hall',
'Block': 'C'},
{'Id': '0102', 'Name': 'Arun', 'Course': 'Python', 'Location': 'Albert Eisten
Hall', 'Block':'A'},
{'Id': '0010', 'Name': 'Shaun', 'Course': 'C', 'Location': 'Mahatma Ghandi Hall',
'Block': 'B'}
])

memberName = input("Please enter a member's name to be deleted.")
infile = open('F:\\files\\studentdata.CSV' , 'r')
outfile = open('F:\\files\\temp.CSV' , 'w' , newline='')
writer = CSV.writer(outfile)

for row in CSV.reader(infile):
    if memberName not in row:
        writer.writerow(row)
        
infile.close()
outfile.close()
os.remove('F:\\files\\studentdata.CSV')
os.rename('F:\\files\\temp.CSV','F:\\files\\studentdata.CSV')

_file.close()
_copyfile.close()


3. Write a program that calculates the sum of all debit amount from the transaction file?
Ans. 
import CSV
with open('F:\\files\\transactions.CSV',mode='w', newline='')as _file:
    fnames = ['TransactionId','date','debit','credit','remark']
    _writer = CSV.DictWriter(_file,fieldnames=fnames)
    _writer.writerows([
    {'TransactionId':'131234','date':'12/12/2019','debit':'','credit':'1234','remark':'misc
    expense'},
    {'TransactionId':'123457','date':'11/12/2019','debit':'20000','credit':'','remark':'bonus'},
    {'TransactionId':'133458','date':'01/12/2019','debit':'25000','credit':'','remark':'salary'},
    {'TransactionId':'131234','date':'25/11/2019','debit':'','credit':'3000','remark':'Car
    maintenance'},
    {'TransactionId':'123457','date':'11/12/2019','debit':'','credit':'2500','remark':'clothings'},
    {'TransactionId':'133458','date':'01/11/2019','debit':'25000','credit':'2500','remark':'salary'}
    ])
# Read the transactions file
debitamt=[]
with open('F:\\file\\transactions.CSV',mode='r') as _f :
    _reader = CSV.reader(_f)
    # Iterate over each line as a ordered dictionary
    for row in _reader:
    # Row variable is a dictionary that represents a row in CSV
        if(row[2] != ''):
    # Print date and transaction amount
            print(row[1], "\t\t", row[2])
            debitamt.append(float(row[2]))
    
print("Total debited Amount: " ,sum(debitamt))

# 4. Define a function that allows to insert a record in a CSV file using a function.
# Ans. 
import CSV
import os
dberror={"000":"Success",
"ERCode011":"table not exists",
"ERCode012":"Column name mismatch",
"ERCode013":"Column and values mismatch"}
def insertinto(filepath, columns, values):
    if( not isfileexists(filepath) ):
        return "ERCode011"
_record = {}
columnnames=[]
with open(filepath, 'r') as _infile:
    _dictreader = CSV.DictReader(_infile)
    columnnames = _dictreader.fieldnames
#using all() to check subset of list
    if(not all(x in columnnames for x in columns)):
        return "ERCode012"
    if(len(columns) != len(values)):
        return "ERCode013"
# Using zip function to convert lists into dictionary
_record = dict(zip(columns,values))
for element in columnnames:
    if(element not in columns):
    _record[element]=''
    with open(filepath, 'a', newline='') as _infile:
    _dictwriter = CSV.DictWriter(_infile,fieldnames=columnnames)
    _dictwriter.writerow(_record)
    return "000"
    
def isfileexists(filepath):
    if(os.path.exists(filepath)):
        return True
    else:
        return False
#Id,Name,Course,Location,Block
file ='F:\\students.CSV'
cols= ['Id','Name','Course','Location','Block']
vals=['0021','Akash','C++','CV Raman Hall','A']
retcode =insertinto(file,cols,vals)
print(dberror[retcode])
cols= ['Id','Course','Location']
vals=['C++','CV Raman Hall']
retcode =insertinto(file,cols,vals)
print(dberror[retcode])


5. Write a program that allows to select the record(s) from a CSV file
Ans. import csv
import os
dberror={"000":"Success",
"ERCode011":"table not exists",
"ERCode012":"Column name mismatch",
"ERCode013":"Column and values mismatch"}
def select(filepath, columnslist):
    rows=[] #for return the rows selected
    if( not isfileexists(filepath) ):
        return "ERCode011"
collist=[]
colindex=[]
columnnames=[]
with open(filepath, 'r') as _infile:
    _dictreader = csv.DictReader(_infile)
    columnnames = _dictreader.fieldnames
    #using all() to check subset of list
    if(columnslist == "all" or columnslist == "*"):
        for row in _dictreader:
        #convert the orderdict to string
        #convert ordered dictionary to dictionary
        #convert dictionary to list and
#list to string using join
        rows.append(','.join(list(dict(row).values())))
    return rows
    
    invalidcol = 0
    for column in columnslist:
        if (column not in columnnames):
            invalidcol = 1
            break
    
    if(invalidcol == 1):
        return "ERCode012"
        
    for ele in columnslist:
        colindex.append(columnnames.index(ele))
    
    for row in _dictreader:
        r=""
        for idx in colindex:
            r+= str(dict(row)[columnslist[idx]]+",")
            r = r[0:len(r)-1]
            rows.append(r)

    return(rows)
    
def isfileexists(filepath):
    if(os.path.exists(filepath)):
        return True
    else:
        return False
        
#Id,Name,Course,Location,Block
file ='F:\\files\\studentrec.csv'
rows= select( file, ['Id','Name','Course','Location'])
print(rows)
print()
rows= select( file, "all")
print(rows)

