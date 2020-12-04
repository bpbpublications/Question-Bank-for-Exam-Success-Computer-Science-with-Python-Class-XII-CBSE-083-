Short Questions and Answers
# 5. Illustrate how to pickle and unpickle an integer with an example?
# Ans. 
import pickle
data = 1
with open(F:\\files\\intdata.dat', 'wb') as _file:
    pickle.dump(data, _file)
    
#Read the value

with open(F:\\files\\intdata.dat', 'rb') as _file:
    _dataretrieve =pickle.load(_file )
print(_dataretrieve)

# 6. Illustrate how to pickle and unpickle a float with an example?
# Ans. 
data = 1.0
with open(F:\\files\\floatdata.dat', 'wb') as _file:
    pickle.dump(data, _file)
    
#Unpicking the float data
with open(F:\\files\\floatdata.dat', 'rb') as _file:
    _dataretrieve =pickle.load(_file )
print(_dataretrieve)

# 7. Illustrate how to pickle and unpickle a tuple with an example?
# Ans. 
tuple = (1,2,3,4)
with open(F:\\files\\tupledata.dat', 'wb') as _file:
    pickle.dump(tuple, _file)
    
#unpickling the tuple
with open(F:\\files\\tupledata.dat', 'rb') as _file:
    _dataretrieve =pickle.load(_file )
print(_dataretrieve)

# 8. Illustrate how to pickle and unpickle list with an example?
# Ans. 
list = [10,20,30,40]
with open(F:\\files\\listdata.dat', 'wb') as _file:
    pickle.dump(list, _file)
#Unpickling the list
with open(F:\\files\\listdata.dat', 'rb') as _file:
    _dataretrieve =pickle.load(_file )
print(_dataretrieve)

# 9. Illustrate how to pickle and unpickle dictionary with an example?
# Ans. 
dictionary = {1:'a',2:'b',3:'c'}
with open(F:\\files\\dictionarydata.dat', 'wb') as _file:
    pickle.dump(dictionary,_file)
    
# Unpickling the dictionary
with open(F:\\files\\dictionarydata.dat', 'rb') as _file:
    _dataretrieve = pickle.load(_file )
    
print(_dataretrieve)


# 10. Illustrate how to pickle and unpickle a string with an example?
# Ans. 
string ="this is test string"
with open(F:\\files\\stringdata.dat', 'wb') as _file:
    pickle.dump(string,_file)
    
# Unpickling the string
with open(F:\\files\\stringdata.dat', 'rb') as _file:
    _dataretrieve =pickle.load(_file )
print(_dataretrieve)

1. Illustrate how to pickle and unpickle multiple records with an example?
Ans. 
import pickle
# database
employeedb = {}
def storeData():
    # initializing data to be stored in db
    employee1 = {'name' : 'Sankar Mahadev','desigantion' : \
    'SE-II', 'pay-bracket' : 'C'}
    employee2 = {'name' : 'Vishnu Pathak', 'desigantion' : '\
    Architect-I', 'pay-bracket' : 'E'}
    employee3 = {'name' : 'Ganesh Shankar','desigantion' : '\
    Evangalist', 'pay-bracket' : 'D'}
    employeedb['20111234'] = employee1
    employeedb['20112345'] = employee2
    employeedb['20122356'] = employee3
    
    dbfile = open(F:\\files\\employee.dbf', 'ab')
    pickle.dump(employeedb, dbfile)
    dbfile.close()

def loadData():

    # for loading open file in binary mode
    dbfile = open(F:\\files\\employee.dbf', 'rb')
    empdb = pickle.load(dbfile)
    for keys in empdb:
        print(keys, '=>', empdb[keys])
    print()
    dbfile.close()
    
storeData()
loadData()
