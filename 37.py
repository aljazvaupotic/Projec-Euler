#TRUNCT PRIMES

def reverseNumber(n):
    return(int(str(n)[::-1]))

def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

def is_prime(x):
    for i in range(2,x):
        if(x%i == 0 & i != x):
            return False
    return True

def isTrunct(x):
    l = len(str(x))-1
    y = x
    while l > 0:
        if is_prime(x // 10) and is_prime( y% (10**(l))):
            x = x//10
            y = y % (10**l)
            l -= 1
            if(x == 1 or y == 2 or y == 1 ):
                return False

            
        else:
            return False
    return True        

#print(isTrunct(3797))
primes = sieve(1000000)
e = []
#print(primes)

for prime in primes:
    if prime < 20:
        continue
    if isTrunct(prime) :
        if prime not in e:
           print(prime)
           e.append(prime)
           if (len(e) == 11):
               break
print(e)
print(len(e))
print(sum(e))