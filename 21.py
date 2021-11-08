# sum of divisors array

def divisors (num):
    vsota = 0
    for i in range(1,num):
        if(num%i == 0):
            vsota += i
    return vsota

n = 10000
sumOfDivisors = n*[0]
allTogether = 0
for i in range(n):

    if(sumOfDivisors[i] == -1 ):
        continue
    if(sumOfDivisors[i] == 0):
        sumOfDivisors[i] = divisors(i)
    if (sumOfDivisors[i] == i):
        continue
    else:
        j = sumOfDivisors[i]
        if(j > n):
            continue
        if(sumOfDivisors[j] == 0):
            sumOfDivisors[j] = divisors(j)
        if(i == divisors(j)):
            allTogether += i + j
            sumOfDivisors[i] = -1
            sumOfDivisors[j] = -1
    print(i,j,sumOfDivisors[i],sumOfDivisors[j])

print(allTogether)