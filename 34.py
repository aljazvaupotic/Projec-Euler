def factorial(n):
    if n == 1 or n == 0: return 1
    return n*factorial(n-1)
def numToList(num):
    return list(map(int,str(num)))

array = [0]*10
for i in range(0,10):
    array[i] = factorial(i)

y = []
for x in range(3,2540161):
    s = numToList(x)
    t = 0
    for number in s:
        t += array[number]
    if t == x:
        y.append(x)


print(y)
print(sum(y))