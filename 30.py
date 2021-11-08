def sumOfFifth(n):
    numlist = list(map(int,str(n)))
    for x in range(0,len(numlist)):
        numlist[x] = numlist[x] ** 5
    return sum(numlist)


max = 9 ** 5 * 6
good = 0
ok = []
for i in range(2,max+1):
    tmp = sumOfFifth(i)
    if i == tmp:
       ok.append(i)
       good += i
print(good)
print(ok)