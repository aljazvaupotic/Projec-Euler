#1. month on sunday


#1.1.1900 = MONDAY

#from 1.1.1901 till 31.12.2000

def isLeap(year):
    if(year % 4 == 0):
        return True
    else:
        return False



monthStartDay = [0,0,0,0,0,0,0]


startofMonth = (1+365)%7
year = 1901
month = 1

while (year != 2001) :
    if(isLeap):
        feb = 29
    else:
        feb = 28
    while(month < 13):
        if (month == 2):
            startofMonth = (startofMonth + feb) % 7
        elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            startofMonth = (startofMonth + 31) % 7
        else:
            startofMonth = (startofMonth + 30) % 7
        
        monthStartDay[startofMonth] += 1
        month += 1

    year += 1
    month = 1

print(monthStartDay[0])