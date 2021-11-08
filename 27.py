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

primes1000 = sieve(1000)
primes = primes1000[:]
largest = 0

for b in range(1,1001):
    for a in range(1,1001):
        i = 0
        while True:
            quad = (i ** 2) + (a * i) + b
            if quad not in primes:
                if is_prime(quad):
                    #print(quad,is_prime(quad))
                    primes.append(quad)
                else:
                    if i-1 >= largest:
                        largest = i - 1
                        axb = a*b
                        amax = a
                        bmax = b
                        apos = True
                        #print(largest,i)
                        break
                    else:
                        break
            i += 1
        i = 0
        while True:
            quad = (i ** 2) - (a * i) + b
            if quad not in primes:
                if is_prime(quad) and quad > 0:
                    primes.append(quad)
                else:
                    if i-1 >= largest:
                        largest = i - 1
                        axb = a*b
                        amax = a
                        bmax = b
                        apos = False
                        #print(largest,i)
                        break
                    else:
                        break
                    
            i += 1

print(axb)
print(amax, bmax, apos)
        