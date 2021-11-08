def isPrime(x):
    for i in range(2,x):
        if(x%i == 0 & i != x):
            return False
    return True

def turn(num):
    numLen = len(str(num))-1
    ld = num % 10
    num = num //10
    ld *=  10**numLen
    
    return num+ld

def hasEven(num):
    while num > 0:
        if ((num%10)%2 == 0):
            return True
        num //= 10
    return False

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros
MAX = 10 ** 6
listOfPrimes = zerolistmaker(MAX+1)
listOfPrimes[2] = 1
listOfPrimes[3] = 1
listOfPrimes[5] = 1
listOfPrimes[7] = 1
sum = 4 #osnovni 2,3,5,7
print(hasEven(1111))

for i in range(10,MAX+1):
    listStevilke = []
    check = not hasEven(i)
    print(i, check)
    howMany = len(str(i))-1
    if(check == True):
        while check and howMany >= 0:
            if(listOfPrimes[i] == 2):
                check = False
            elif(listOfPrimes[i] == 1):
                i = turn(i)
            elif(isPrime(i) == True):
                listOfPrimes[i] = 1
                listStevilke.append(i)
                i = turn(i)
            else:
                check = False
            howMany -= 1
    if (check == True):
        for stevilka in listStevilke:
            listOfPrimes[stevilka] == 2
        sum += len(listStevilke)
        print(listStevilke)
    

print(sum)
print()
