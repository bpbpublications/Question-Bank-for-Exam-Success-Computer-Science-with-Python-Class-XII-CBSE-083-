# seperators for the date 
seperators='/-'

#list of the date formats
formats=['ddmmyy','ddmmmyy','ddmmyyyy','mmddyy','mmmddyy','mmddyyyy','yyyymmdd']

# This dictionary stores month and their three word abbrevation
threechar_month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',\
7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

# Valid days is a dictionary that contain maximum number of days in a month
validdays={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

# To check of a year is a leap year
# Return value 1 if year is a leap year
# @ Arguments int year

def isleapYear(y):
    if( y % 4 == 0):
        if( (y % 100 == 0) and (y % 400 == 0)):
            return 1
        else:
            return 0
    else:
        return 0

# To check of a date hasis valid or not
# Return val  1 if date is a valid date
# @ Arguments int day, month ,year

def isValidDate(d, m ,y):
    if (m >12):
        return 0
    if(d > 31):
        return 0
    
    #if number days are more than specified day in a month
    if(d > validdays[m]):
        return 0
    if(isleapYear(y) and m ==2 and d > 29):
        return 0
        
    if(not isleapYear(y) and m ==2 and d > 28):
        return 0
    return 1

# Converts the day, month year  as string in date format
# Return string that represents a date based on requested format
# @ Arguments int day, month, year , Seperator  , format  
   
def dateformat(dval, mval,yval, seperator='-',format='ddmmyy'):
    if( not isValidDate(dval,mval,yval)):
        print("Invalid Date")
        return 
    #check if seperator is correct or not
    if( not(  seperator in seperators)  ):
        print("Not a valid  seperators")
        return
    #check if format in format list
    if( not(  format in formats)  ):
        print("Not a valid format ")
        return
    #join the day, month and year
    if(format=='ddmmyy'):
        return  str(dval)+seperator+str(mval)+\
                seperator+str(yval)[-2::] #fetch last 2 characters
    elif(format=='ddmmmyy'):
        return  str(dval)+seperator+str(threechar_month[mval])+\
            seperator+str(yval)[-2::]
    elif(format=='ddmmyyyy'):
        return  str(dval)+seperator+str(mval)+\
                seperator+str(yval)
    elif(format=='mmddyy'):
        return  str(mval)+seperator+\
                str(dval)+seperator+str(yval)[-2::]
    elif(format=='mmmddyy'):
        return  str(threechar_month[mval])+str(dval)+seperator+\
                seperator+str(yval)[-2::]
    elif(format=='mmddyyyy'):
        return  str(mval)+seperator+str(dval)+\
                seperator+str(yval)
    elif(format=='yyyymmdd'):
        return  str(yval)+seperator+str(mval)+\
                seperator+str(dval)
    else:
        return