def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

num = factorial(100)

print(sum((map(int,str(num)))))