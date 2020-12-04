#Python program that tests the date format module (Test.py):
import dateformat
print(dateformat.dateformat(12,12,2001))
# Output:
# 12-12-01
print(dateformat.dateformat(12,12,2001,'/'))
# Output:
# 12/12/01
#Print date with separator '/' in various formats
print(dateformat.dateformat(12,12,2001,'/','ddmmyy'))
print(dateformat.dateformat(12,12,2001,'/','ddmmmyy'))
print(dateformat.dateformat(12,12,2001,'/','ddmmyyyy'))
print(dateformat.dateformat(12,12,2001,'/','mmddyy'))
print(dateformat.dateformat(12,12,2001,'/','mmmddyy'))
print(dateformat.dateformat(12,12,2001,'/','mmddyyyy'))
# Output:
# 12/12/01
# 12/Dec/01
# 12/12/2001
# 12/Dec/01
# Dec/12/01
# Dec/12/2001
#Print date with separator '–'in various formats
print(dateformat.dateformat(12,12,2001,'-'))
print(dateformat.dateformat(12,12,2001,'-','ddmmyy')) 
print(dateformat.dateformat(12,12,2001,'-','ddmmmyy'))
print(dateformat.dateformat(12,12,2001,'-','ddmmyyyy'))
print(dateformat.dateformat(12,12,2001,'-','mmddyy'))
print(dateformat.dateformat(12,12,2001,'-','mmmddyy'))
print(dateformat.dateformat(12,12,2001,'-','mmddyyyy'))
print(dateformat.dateformat(12,12,2001,'/','yyyymmdd'))
# Output:
# 12-12-01
# 12-dec-01
# 12-Dec-2001
# 12-12-01
# Dec-12-01
# Dec-12-01
# 12-12-2001
# 2001/12/12
#invalid Date format
print(dateformat.dateformat(12,12,2001,'/','yyymmdd'))
# Output:
# Not a valid format None
#invalid separator
print(dateformat.dateformat(12,12,2001,'//'))
# Output:
# Not a valid separators
# None
#invalid date month of April cannot have 31 days
print(dateformat.dateformat(31,4,2001,'-'))
# Output:
# Invalid Date
# None
#invalid date month > 12
print(dateformat.dateformat(12,13,2001,'-'))
# Output:
# Invalid Date
# None
#valid date in a leap year
print(dateformat.dateformat(29,2,2020,'-'))
# Output:
# 29-2-20
print(dateformat.dateformat(32,4,2020,'-'))
# Output:
# Invalid Date
# None