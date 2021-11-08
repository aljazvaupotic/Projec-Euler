""" We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists? """


def isPandi(num):
    p = [1]*(len(str(num))+1)
    p[0] = 0
    word = list(map(int,(str(num))))
    #print(p)
    #print(sum(p))
    if 0 in word:
        return False
    else:
        for stevka in word:
            if stevka > len(word):
                return False
            if p[stevka] == 1:
                p[stevka] = 0
    #print(sum(p),num)
    return (sum(p) == 0)


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
		if is_prime[i] == True and isPandi(i):
			prime.append(i)
	return prime



save = 0
primes = sieve(987654321)


print (primes(len(primes)-1))